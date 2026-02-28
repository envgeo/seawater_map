import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from scipy.interpolate import griddata
from scipy.ndimage import gaussian_filter
import envgeo_utils

# --- 断面図作成用関数 ---
def create_section_plot(Z, xi, yi, df_points, x_col, target_col, z_min, z_max, plot_type="color"):
    fig = go.Figure()
    if plot_type == "color":
        fig.add_trace(go.Contour(
            z=Z, x=xi, y=yi, colorscale='Portland',
            zmin=z_min, zmax=z_max,
            colorbar=dict(title=target_col, orientation='h', y=-0.25, tickformat=".2f"),
            contours=dict(showlabels=True, coloring='heatmap', start=z_min, end=z_max),
            line_width=0, connectgaps=True
        ))
    else:
        fig.add_trace(go.Contour(
            z=Z, x=xi, y=yi,
            zmin=z_min, zmax=z_max,
            showscale=True,
            colorbar=dict(title=target_col, orientation='h', y=-0.25),
            contours=dict(
                coloring='none', 
                showlabels=True,
                labelfont=dict(size=12, color='black'),
                start=z_min,
                end=z_max
            ),
            connectgaps=True
        ))
    
    # 観測地点のドットを断面図上に重ねる
    fig.add_trace(go.Scatter(
        x=df_points[x_col], y=df_points['Depth_m'],
        mode='markers',
        marker=dict(size=6, color='black', opacity=0.6),
        name='Stations',
        hoverinfo='skip'
    ))

    fig.update_layout(
        xaxis_title=x_col,
        yaxis_title="Depth (m)",
        yaxis=dict(autorange='reversed'),
        height=600,
        margin=dict(l=50, r=50, b=100, t=50)
    )
    return fig

def main():
    # --- 1. サイドバーの設定 ---
    st.sidebar.title("Section Control Panel")
    
    # データソース選択
    ref_data_source = st.sidebar.radio("Select Data Source:", envgeo_utils.DATA_SOURCES)

    # データのロード
    try:
        df = envgeo_utils.load_isotope_data(ref_data_source)
    except Exception as e:
        st.error(f"Data loading error: {e}")
        return

    # --- 2. フィルタリングセクション ---
    st.sidebar.markdown("---")
    
    with st.sidebar.expander("🔍 Dataset Filters", expanded=True):
        # Transect フィルタ
        if 'Transect' in df.columns:
            transect_list = sorted(df['Transect'].dropna().unique().tolist())
            selected_transects = st.multiselect("Filter by Transect", transect_list, default=transect_list)
        else:
            selected_transects = None

        # Year フィルタ
        if 'Year' in df.columns:
            min_y = int(df['Year'].min()) if not df['Year'].dropna().empty else 1960
            max_y = int(df['Year'].max()) if not df['Year'].dropna().empty else 2028
            sld_year_min, sld_year_max = st.slider("Year Range", min_y, max_y, (min_y, max_y))
        else:
            sld_year_min, sld_year_max = 1960, 2028

        # Month フィルタと短縮表示ロジック
        if 'Month' in df.columns:
            all_months = sorted([int(m) for m in df['Month'].dropna().unique()])
            selected_months = st.multiselect("Filter by Month", all_months, default=all_months)
            
            # --- 短縮表示ロジック ---
            if len(selected_months) == 12 or (len(selected_months) == len(all_months) and len(all_months) > 0):
                month_display = "All"
            elif len(selected_months) == 0:
                month_display = "None"
            else:
                sorted_m = sorted(list(set(selected_months)))
                ranges = []
                if sorted_m:
                    start = sorted_m[0]
                    for i in range(len(sorted_m)):
                        if i + 1 == len(sorted_m) or sorted_m[i+1] != sorted_m[i] + 1:
                            end = sorted_m[i]
                            ranges.append(f"{start}-{end}" if start != end else str(start))
                            if i + 1 < len(sorted_m): start = sorted_m[i+1]
                month_display = ", ".join(ranges)
            st.markdown(f"Selected: :green[MONTH]: [{month_display}]")
        else:
            selected_months = None

    # パラメータ選択
    target_col = st.sidebar.radio("Target Parameter", ["d18O", "Salinity", "Temperature_degC", "dD"])

    # 断面図の設定
    st.sidebar.markdown("---")
    x_axis_option = st.sidebar.selectbox("X-axis for Section", ["Longitude_degE", "Latitude_degN", "Distance_km"])
    
    # --- フィルタの適用 ---
    df_f = df.copy()
    if selected_transects:
        df_f = df_f[df_f['Transect'].isin(selected_transects)]
    if 'Year' in df_f.columns:
        df_f = df_f[df_f['Year'].between(sld_year_min, sld_year_max)]
    if selected_months:
        df_f = df_f[df_f['Month'].isin(selected_months)]

    # --- Distance_km の計算ロジック (KeyError対策) ---
    if x_axis_option == "Distance_km" and "Distance_km" not in df_f.columns:
        if not df_f.empty:
            # 緯度・経度から簡易距離(km)を計算（最初の地点を0とする）
            df_f = df_f.sort_values(['Latitude_degN', 'Longitude_degE'])
            base_lat = df_f.iloc[0]['Latitude_degN']
            base_lon = df_f.iloc[0]['Longitude_degE']
            # 1度あたりの距離を約111kmとして計算
            df_f['Distance_km'] = np.sqrt(
                ((df_f['Latitude_degN'] - base_lat) * 111.1)**2 + 
                ((df_f['Longitude_degE'] - base_lon) * 111.1 * np.cos(np.radians(base_lat)))**2
            )
        else:
            df_f['Distance_km'] = []

    # プロット用データの準備 (ここで x_axis_option が確実に存在するようにした)
    df_plot = df_f.dropna(subset=[x_axis_option, 'Depth_m', target_col, 'Latitude_degN', 'Longitude_degE'])

    # スケール設定
    valid_data = df_plot[df_plot[target_col].notna()]
    def_z_min = float(valid_data[target_col].min()) if not valid_data.empty else 0.0
    def_z_max = float(valid_data[target_col].max()) if not valid_data.empty else 1.0
    z_min, z_max = st.sidebar.slider(f"{target_col} Scale", -10.0, 50.0, (def_z_min, def_z_max))

    grid_res = 100
    smoothness = st.sidebar.slider("Smoothing (Sigma)", 0.0, 5.0, 2.5, 0.5)

    # --- 3. メイン画面の表示 ---
    st.title("Vertical Section Visualizer")
    st.info(f"Showing {len(df_plot)} points after filtering.")

    if len(df_plot) > 5:
        xi = np.linspace(df_plot[x_axis_option].min(), df_plot[x_axis_option].max(), grid_res)
        yi = np.linspace(df_plot['Depth_m'].min(), df_plot['Depth_m'].max(), grid_res)
        X, Y = np.meshgrid(xi, yi)

        try:
            # 補間処理
            Z = griddata((df_plot[x_axis_option], df_plot['Depth_m']), df_plot[target_col], (X, Y), method='cubic')
            Z_lin = griddata((df_plot[x_axis_option], df_plot['Depth_m']), df_plot[target_col], (X, Y), method='linear')
            Z = np.where(np.isnan(Z), Z_lin, Z)
            
            if smoothness > 0:
                Z = gaussian_filter(Z, sigma=smoothness)
            
            tab1, tab2 = st.tabs(["🎨 Color Contour", "📈 Line Contour"])
            with tab1:
                fig_color = create_section_plot(Z, xi, yi, df_plot, x_axis_option, target_col, z_min, z_max, plot_type="color")
                st.plotly_chart(fig_color, use_container_width=True)
            with tab2:
                fig_line = create_section_plot(Z, xi, yi, df_plot, x_axis_option, target_col, z_min, z_max, plot_type="line")
                st.plotly_chart(fig_line, use_container_width=True)
                
        except Exception as e:
            st.error(f"Interpolation failed: {e}")
    else:
        st.warning("Insufficient data points for interpolation. Please adjust filters.")

    st.markdown("---")
    st.subheader("Station Map")
    if not df_plot.empty:
        # 地図表示用の列名を変換
        map_data = df_plot[['Latitude_degN', 'Longitude_degE']].rename(
            columns={'Latitude_degN': 'latitude', 'Longitude_degE': 'longitude'}
        )
        st.map(map_data, use_container_width=True)

    with st.expander("Show Filtered Data Table (CSV)", expanded=False):
        st.dataframe(df_plot.astype(str), use_container_width=True)

if __name__ == "__main__":
    main()