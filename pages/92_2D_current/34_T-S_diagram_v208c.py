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
    # --- サイドバーの設定 ---
    st.sidebar.title("Section Control Panel")
    
    # 1. データソース選択
    ref_data = st.sidebar.radio("Select Data Source:", envgeo_utils.DATA_SOURCES)

    # 2. データのロード
    try:
        df = envgeo_utils.load_isotope_data(ref_data)
    except Exception as e:
        st.error(f"Data loading error: {e}")
        return

    # (A) 測線フィルタ
    if 'Transect' in df.columns:
        transect_options = sorted([str(x) for x in df['Transect'].dropna().unique() if str(x).strip() != ""])
        selected_transects = st.sidebar.multiselect(
            "Select Transects", 
            transect_options, 
            default=transect_options
        )
        df_f = df[df['Transect'].astype(str).isin(selected_transects)] if selected_transects else df.copy()
    else:
        st.sidebar.warning("'Transect' column not found in this dataset.")
        df_f = df.copy()

    # (B) データフィルタリング
    st.sidebar.subheader("Data Filtering")
    params = [p for p in ["d18O", "Salinity", "Temperature_degC", "dD"] if p in df.columns]
    if not params:
        st.error("No target parameters found in the dataset.")
        return
    target_col = st.sidebar.radio("Target Parameter", params)
    
    min_y = int(df['Year'].min()) if 'Year' in df.columns and not df['Year'].dropna().empty else 1960
    max_y = int(df['Year'].max()) if 'Year' in df.columns and not df['Year'].dropna().empty else 2028
    sld_year_min, sld_year_max = st.sidebar.slider("Year Range", min_y, max_y, (min_y, max_y))
    
    max_d = int(df['Depth_m'].max()) if 'Depth_m' in df.columns and not df['Depth_m'].dropna().empty else 9000
    sld_depth_min, sld_depth_max = st.sidebar.slider("Depth Range (m)", 0, max_d, (0, max_d))
    
    st.sidebar.markdown("---")
    st.sidebar.subheader("Map Settings")
    map_mode = st.sidebar.selectbox("Map Style", ["light", "dark", "satellite", "outdoors", "streets"], index=2)

    st.sidebar.markdown("---")
    st.sidebar.subheader("Section Plot Settings")
    x_axis_option = st.sidebar.selectbox("X-axis for Section", ["Longitude_degE", "Latitude_degN", "Distance_km"])
    
    valid_data = df_f[df_f[target_col].notna()]
    def_z_min = float(valid_data[target_col].min()) if not valid_data.empty else 0.0
    def_z_max = float(valid_data[target_col].max()) if not valid_data.empty else 1.0
    z_min, z_max = st.sidebar.slider(f"{target_col} Scale Range", -10.0, 50.0, (def_z_min, def_z_max))

    grid_res = st.sidebar.select_slider("Grid Resolution", options=[50, 100, 200, 300], value=100)
    smoothness = st.sidebar.slider("Smoothing (Sigma)", 0.0, 5.0, 2.0, 0.5)

    df_final = df_f[
        (df_f['Year'].between(sld_year_min, sld_year_max)) &
        (df_f['Depth_m'].between(sld_depth_min, sld_depth_max))
    ].copy()

    df_plot = df_final.dropna(subset=[x_axis_option, 'Depth_m', target_col, 'Latitude_degN', 'Longitude_degE'])

    # --- メイン画面表示 ---
    st.title("Vertical Section Visualizer")

    # (1) 地図表示
    st.subheader("Station Map (Scroll to Zoom)")
    if not df_plot.empty:
        hover_config = {
            "Latitude_degN": True,
            "Longitude_degE": True,
            "Year": True,
            "Month": True,
            "Cruise": True,
            "Station": True,
            "Depth_m": ":.1f",
        }
        for c in ["d18O", "dD", "Salinity", "Temperature_degC", "reference", "Reference"]:
            if c in df_plot.columns:
                hover_config[c] = True

        # 1. マップ作成
        fig_map = px.scatter_mapbox(
            df_plot, 
            lat="Latitude_degN", lon="Longitude_degE",
            color=target_col,
            color_continuous_scale="Portland",
            range_color=[z_min, z_max],
            hover_data=hover_config,
            opacity=0.8, height=600
        )
        
        # 2. スタイルの適用
        fig_map = envgeo_utils.apply_map_style(fig_map, map_mode)
        
        # 3. 中心点と初期ズームの計算
        center_lat = df_plot['Latitude_degN'].mean()
        center_lon = df_plot['Longitude_degE'].mean()

        # 4. レイアウト設定 (上手くいっているコードの構造を厳密に反映)
        fig_map.update_layout(
            mapbox=dict(
                center=dict(lat=center_lat, lon=center_lon),
                zoom=2.5,
                # マウスホイール操作をMapboxレベルで許可
                scrollzoom=True 
            ),
            margin=dict(l=0, r=0, t=0, b=0),
            autosize=True,
            # 操作モードを'zoom'に固定
            dragmode="zoom",
            # パラメータ変更時もカメラ位置を保持
            uirevision="constant", 
            coloraxis_colorbar=dict(
                title=f"{target_col}",
                x=1.0,
                xanchor='right'
            )
        )
        
        # 5. 表示 (configオプションを明示的に指定)
        st.plotly_chart(
            fig_map, 
            use_container_width=True, 
            key="TS_plot", 
            config={
                'scrollZoom': True, 
                'displayModeBar': True,
                'modeBarButtonsToAdd': ['drawline', 'drawopenpath', 'drawclosedpath', 'drawcircle', 'drawrect', 'eraselayer'],
                'responsive': True
            }
        )
    else:
        st.warning("No data found for the selected filters.")

    st.markdown("---")

    # (2) 断面図表示
    st.subheader(f"Vertical Section: {target_col}")
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
            
            tab1, tab2 = st.tabs(["Color Contour", "Line Contour"])
            with tab1:
                fig_color = create_section_plot(Z, xi, yi, df_plot, x_axis_option, target_col, z_min, z_max, plot_type="color")
                st.plotly_chart(fig_color, use_container_width=True)
            with tab2:
                fig_line = create_section_plot(Z, xi, yi, df_plot, x_axis_option, target_col, z_min, z_max, plot_type="line")
                st.plotly_chart(fig_line, use_container_width=True)
        except Exception as e:
            st.error(f"Interpolation calculation failed: {e}")
    else:
        st.info("Insufficient data points for a section plot. Please adjust the filters.")

    # (3) データテーブル表示
    with st.expander("Show Selected Data Table (CSV)", expanded=False):
        st.dataframe(df_plot.astype(str), use_container_width=True)

if __name__ == "__main__":
    main()