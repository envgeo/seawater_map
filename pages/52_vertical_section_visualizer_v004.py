import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
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
    
    # 観測地点のドット
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

# --- 地図描画関数 (一直線の測線付き) ---
def create_station_map(df_plot, x_axis_option):
    # 背景地図のベース作成 (観測点のプロット)
    fig = px.scatter_mapbox(
        df_plot, 
        lat="Latitude_degN", 
        lon="Longitude_degE",
        hover_name="Station" if "Station" in df_plot.columns else None,
        zoom=3,
        height=500
    )
    
    if not df_plot.empty:
        # X軸の選択肢に基づいてソートし、最初と最後の点を特定
        # 緯度・経度・距離のいずれであっても「端の2点」を結ぶ
        line_data = df_plot.sort_values(x_axis_option)
        start_pt = line_data.iloc[0]
        end_pt = line_data.iloc[-1]
        
        # 測線を「一直線」として追加
        fig.add_trace(go.Scattermapbox(
            mode="lines",
            lon=[start_pt["Longitude_degE"], end_pt["Longitude_degE"]],
            lat=[start_pt["Latitude_degN"], end_pt["Latitude_degN"]],
            line=dict(width=4, color="red"),
            name="Transect Line",
            hoverinfo="skip"
        ))
        
        # 起点 (断面図の左端 0km/西端/南端) を星印で強調
        fig.add_trace(go.Scattermapbox(
            mode="markers",
            lon=[start_pt["Longitude_degE"]],
            lat=[start_pt["Latitude_degN"]],
            marker=dict(size=18, color="yellow", symbol="star"),
            name="Origin / Start"
        ))

    fig.update_layout(
        mapbox_style="open-street-map",
        margin={"r":0,"t":0,"l":0,"b":0},
        showlegend=True
    )
    return fig

def main():
    # --- カスタムCSS ---
    st.markdown("""
        <style>
        div[data-baseweb="select"] > div:first-child {
            max-height: 100px;
            overflow-y: auto;
        }
        </style>
    """, unsafe_allow_html=True)

    st.sidebar.title("Section Control Panel")
    
    ref_data_source = st.sidebar.radio("Select Data Source:", envgeo_utils.DATA_SOURCES)

    try:
        df = envgeo_utils.load_isotope_data(ref_data_source)
    except Exception as e:
        st.error(f"Data loading error: {e}")
        return

    st.sidebar.markdown("---")
    
    # --- フィルタリング ---
    with st.sidebar.expander("🔍 Dataset Filters", expanded=False):
        if 'reference' in df.columns:
            ref_list = sorted(df['reference'].dropna().unique().tolist())
            selected_refs = st.multiselect("Filter by Reference", ref_list, default=ref_list)
        else:
            selected_refs = None

        if 'Transect' in df.columns:
            transect_list = sorted(df['Transect'].dropna().unique().tolist())
            selected_transects = st.multiselect("Filter by Transect", transect_list, default=transect_list)
        else:
            selected_transects = None

        if 'Year' in df.columns:
            min_y, max_y = int(df['Year'].min()), int(df['Year'].max())
            sld_year = st.sidebar.slider("Year Range", min_y, max_y, (min_y, max_y))
            df = df[df['Year'].between(sld_year[0], sld_year[1]) | df['Year'].isna()]

        if 'Month' in df.columns:
            month_list = sorted([int(m) for m in df['Month'].dropna().unique()])
            selected_months = st.multiselect("Filter by Month", month_list, default=month_list)
            df = df[df['Month'].isin(selected_months) | df['Month'].isna()]

    # パラメータ選択
    target_col = st.sidebar.radio("Target Parameter", ["d18O", "Salinity", "Temperature_degC", "dD"])

    # 断面図の設定
    st.sidebar.markdown("---")
    with st.sidebar.expander("🎨 Plot Appearance", expanded=True):
        x_axis_option = st.selectbox("X-axis for Section", ["Longitude_degE", "Latitude_degN", "Distance_km"])
        
        # 距離計算
        if x_axis_option == "Distance_km":
            df = df.sort_values("Longitude_degE")
            if not df.empty:
                base_lat, base_lon = df.iloc[0]['Latitude_degN'], df.iloc[0]['Longitude_degE']
                df['Distance_km'] = np.sqrt(
                    ((df['Latitude_degN']-base_lat)*111.1)**2 + 
                    ((df['Longitude_degE']-base_lon)*111.1*np.cos(np.radians(base_lat)))**2
                )

        valid_data = df[df[target_col].notna()]
        def_z_min = float(valid_data[target_col].min()) if not valid_data.empty else 0.0
        def_z_max = float(valid_data[target_col].max()) if not valid_data.empty else 1.0
        z_min, z_max = st.slider(f"{target_col} Scale", -10.0, 50.0, (def_z_min, def_z_max))
        grid_res = st.select_slider("Grid Resolution", options=[50, 100, 200, 300], value=100)
        smoothness = st.slider("Smoothing (Sigma)", 0.0, 5.0, 2.5, 0.5)

    # プロット用データの準備
    df_plot = df.dropna(subset=[x_axis_option, 'Depth_m', target_col, 'Latitude_degN', 'Longitude_degE'])

    # --- メイン表示 ---
    st.title("Vertical Section Visualizer")
    st.info(f"Showing {len(df_plot)} points after filtering.")

    if len(df_plot) > 5:
        xi = np.linspace(df_plot[x_axis_option].min(), df_plot[x_axis_option].max(), grid_res)
        yi = np.linspace(df_plot['Depth_m'].min(), df_plot['Depth_m'].max(), grid_res)
        X, Y = np.meshgrid(xi, yi)

        try:
            Z = griddata((df_plot[x_axis_option], df_plot['Depth_m']), df_plot[target_col], (X, Y), method='cubic')
            Z_lin = griddata((df_plot[x_axis_option], df_plot['Depth_m']), df_plot[target_col], (X, Y), method='linear')
            Z = np.where(np.isnan(Z), Z_lin, Z)
            
            if smoothness > 0:
                Z = gaussian_filter(Z, sigma=smoothness)
            
            tab1, tab2 = st.tabs(["🎨 Color Contour", "📈 Line Contour"])
            with tab1:
                st.plotly_chart(create_section_plot(Z, xi, yi, df_plot, x_axis_option, target_col, z_min, z_max, "color"), use_container_width=True)
            with tab2:
                st.plotly_chart(create_section_plot(Z, xi, yi, df_plot, x_axis_option, target_col, z_min, z_max, "line"), use_container_width=True)
                
        except Exception as e:
            st.error(f"Interpolation failed: {e}")
    else:
        st.warning("Insufficient data points for interpolation.")

    st.markdown("---")
    st.subheader("Station Map & Straight Transect Line")
    if not df_plot.empty:
        # st.map の代わりに、一直線を描画可能なカスタム関数を使用
        st.plotly_chart(create_station_map(df_plot, x_axis_option), use_container_width=True)

    with st.expander("Show Filtered Data Table", expanded=False):
        st.dataframe(df_plot.astype(str), use_container_width=True)

if __name__ == "__main__":
    main()