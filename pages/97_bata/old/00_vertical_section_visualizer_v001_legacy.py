import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from scipy.interpolate import griddata
from scipy.ndimage import gaussian_filter
import envgeo_utils_legacy

# --- ページ設定の衝突回避 ---
# st.set_page_config(page_title="Vertical Section", layout="wide")

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
                end=z_max,
                size=(z_max - z_min) / 10 if z_max != z_min else 0.1
            ),
            line=dict(width=1.5, color='black'),
            connectgaps=True
        ))

    fig.add_trace(go.Scatter(
        x=df_points[x_col], y=df_points['Depth_m'],
        mode='markers', marker=dict(color='gray', size=4, opacity=0.5),
        name="Station", text=df_points['Station'], showlegend=False
    ))

    fig.update_layout(
        xaxis_title=x_col, yaxis_title="Depth (m)", 
        height=700, margin=dict(b=150), plot_bgcolor='white'
    )
    fig.update_yaxes(autorange='reversed', gridcolor='lightgray', showgrid=True)
    fig.update_xaxes(gridcolor='lightgray', showgrid=True)
    return fig

def main():
    st.subheader('Comprehensive Vertical Section Visualizer (v2.26)')

    # --- 1. データ読み込み ---
    ref_data_choice = st.sidebar.radio("Data group:", ("Kodama et al. (2024) only", "All reports"), index=0)
    ref_arg = "Kodama et al. (2024) only" if "only" in ref_data_choice else None

    try:
        df = envgeo_utils_legacy.load_isotope_data(ref_arg)
        
        # 【エラー対策】列名を強制的に文字列に変換してから空白除去
        df.columns = [str(col).strip() for col in df.columns]
        
        # カラム名の揺れ（大文字・小文字）を補正
        df = df.rename(columns={col: col.capitalize() for col in df.columns if str(col).lower() == 'transect'})
        df = df.rename(columns={col: col.capitalize() for col in df.columns if str(col).lower() == 'cruise'})
        df = df.rename(columns={col: col.capitalize() for col in df.columns if str(col).lower() == 'year'})
        
    except Exception as e:
        st.error(f"読み込みエラー: {e}")
        return

    # --- 2. 抽出条件 ---
    st.sidebar.markdown("### 2. 抽出条件")
    
    # (A) 測線フィルタ
    if 'Transect' in df.columns:
        transect_list = sorted([str(x) for x in df['Transect'].dropna().unique() if str(x).strip() != ""])
        selected_transects = st.sidebar.multiselect("測線を選択", transect_list, default=[transect_list[0]] if transect_list else [])
        df_f = df[df['Transect'].astype(str).isin(selected_transects)] if selected_transects else df.copy()
    else:
        st.error("'Transect'列が見つかりません。")
        return

    # (B) 年(Year)フィルタ
    if 'Year' in df_f.columns:
        # 数値と文字列が混在しても大丈夫なように処理
        year_values = df_f['Year'].dropna().unique()
        year_list = sorted([int(float(y)) for y in year_values if str(y).replace('.','',1).isdigit()])
        selected_years = st.sidebar.multiselect("年(Year)を選択", year_list, default=year_list)
        df_f = df_f[df_f['Year'].astype(float).isin(selected_years)] if selected_years else df_f

    # (C) 航海(Cruise)フィルタ
    if 'Cruise' in df_f.columns:
        cruise_list = sorted([str(x) for x in df_f['Cruise'].dropna().unique() if str(x).strip() != ""])
        selected_cruises = st.sidebar.multiselect("航海(Cruise)を選択", cruise_list, default=cruise_list)
        df_f = df_f[df_f['Cruise'].astype(str).isin(selected_cruises)] if selected_cruises else df_f

    # (D) 空間スライダー
    try:
        lons = (float(df_f['Longitude_degE'].min()), float(df_f['Longitude_degE'].max()))
        sel_lon = st.sidebar.slider("経度範囲", lons[0], lons[1], lons, step=0.01)
        lats = (float(df_f['Latitude_degN'].min()), float(df_f['Latitude_degN'].max()))
        sel_lat = st.sidebar.slider("緯度範囲", lats[0], lats[1], lats, step=0.01)

        df_final = df_f[
            (df_f['Longitude_degE'] >= sel_lon[0]) & (df_f['Longitude_degE'] <= sel_lon[1]) &
            (df_f['Latitude_degN'] >= sel_lat[0]) & (df_f['Latitude_degN'] <= sel_lat[1])
        ]
    except:
        df_final = df_f

    # --- 3. 解析設定 ---
    st.sidebar.markdown("---")
    available_cols = [c for c in ['d18O', 'Salinity', 'Temperature_degC'] if c in df.columns]
    target_col = st.sidebar.selectbox("表示項目", available_cols)
    
    # データが空の場合のガード
    if df_final.empty:
        st.warning("条件に一致するデータがありません。")
        return

    data_min, data_max = float(df_final[target_col].min()), float(df_final[target_col].max())
    z_min = st.sidebar.number_input("Scale Min", value=data_min, step=0.1)
    z_max = st.sidebar.number_input("Scale Max", value=data_max, step=0.1)

    x_axis_option = st.sidebar.radio("断面図の横軸", ['Longitude_degE', 'Latitude_degN'])
    grid_res = st.sidebar.select_slider("グリッド解像度", options=[50, 100, 200, 300], value=100)
    smoothness = st.sidebar.slider("平滑化 (Smoothing)", 0.0, 5.0, 2.5, 0.5)

    df_plot = df_final.dropna(subset=[x_axis_option, 'Depth_m', target_col])

    # --- 4. 計算と表示 ---
    xi = np.linspace(df_plot[x_axis_option].min(), df_plot[x_axis_option].max(), grid_res)
    yi = np.linspace(df_plot['Depth_m'].min(), df_plot['Depth_m'].max(), grid_res)
    X, Y = np.meshgrid(xi, yi)

    try:
        Z = griddata((df_plot[x_axis_option], df_plot['Depth_m']), df_plot[target_col], (X, Y), method='cubic')
        Z_lin = griddata((df_plot[x_axis_option], df_plot['Depth_m']), df_plot[target_col], (X, Y), method='linear')
        Z = np.where(np.isnan(Z), Z_lin, Z)
        if smoothness > 0: Z = gaussian_filter(Z, sigma=smoothness)
    except:
        st.error("補間計算に失敗しました。")
        return

    st.map(df_plot[['Latitude_degN', 'Longitude_degE']].rename(columns={'Latitude_degN':'lat', 'Longitude_degE':'lon'}))
    
    tab1, tab2 = st.tabs(["🎨 Color Contour", "📈 Contour Lines Only"])
    with tab1:
        fig_color = create_section_plot(Z, xi, yi, df_plot, x_axis_option, target_col, z_min, z_max, plot_type="color")
        st.plotly_chart(fig_color, use_container_width=True)
    with tab2:
        fig_line = create_section_plot(Z, xi, yi, df_plot, x_axis_option, target_col, z_min, z_max, plot_type="line")
        st.plotly_chart(fig_line, use_container_width=True)

if __name__ == '__main__':
    main()
