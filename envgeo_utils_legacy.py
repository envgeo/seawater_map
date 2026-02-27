import pandas as pd
import streamlit as st
# import plotly.graph_objects as go


##############################################################################
# --- 1. メインデータの読み込み ---
# Cache isotope data for rapid access (Japan/Global)
##############################################################################
@st.cache_data
def load_isotope_data(ref_data, sheet_num=1): # デフォルトを1に設定
    """
    ref_data に基づいて適切なファイルを読み込み、DataFrameを返す関数。キャッシュされるため、一度読み込めば2回目以降は一瞬で終わります。
    Loads the appropriate file based on ref_data and returns a DataFrame. Subsequent calls are near-instant due to caching.
    """
    """
    sheet_num を引数に追加することで、呼び出し側でシートを選択可能にします。
    """
    # 1. データソースによってファイル名を指定
    # 1. Select filename based on data source
    if ref_data == "Kodama et al. (2024) only":
        excel_file = 'dataset/d18O_20230513-1_NA2_2021add.xlsx'
        # sheet_num = 1
    elif ref_data == "Kodama et al. (2024) with other reports":
        excel_file = 'dataset/d18O_20240927_ref_YSKH.xlsx'
        # sheet_num = 1
    elif ref_data == "with NASA_database":
        excel_file = 'dataset/d18O_NASA_all_data_Python_20250123.xlsx'
        # sheet_num = 1 # もしNASAデータのシート名が異なる場合はここを調整
    else:
        return pd.DataFrame() # 該当なしの場合は空のDFを返す

    # 2. データの読み込み（Excel読み込みが重いためここがキャッシュの肝です）
    # 2. Load data (Caching is essential here as Excel reading is resource-intensive)
    
    
    #エラーを排除しない場合
    # try:
    #     df = pd.read_excel(excel_file, sheet_name=sheet_num)
    #     return df
    # except Exception as e:
    #     st.error(f"ファイルの読み込みに失敗しました: {excel_file} - {e}")
    #     return pd.DataFrame()
    
    
    # 2. データの読み込みとクリーニング
    # エラーを排除する場合
    try:
            df = pd.read_excel(excel_file, sheet_name=sheet_num)
            
            # --- ここから追加 ---
            before_count = len(df)
            
            # # 数値に変換（NASAエラー対策,  'str' and 'float'）
            # 文字列が混じっていても強制的に数値にする（errors='coerce'）
            for col in ['d18O', 'dD', 'Longitude', 'Latitude']:
                if col in df.columns:
                    df[col] = pd.to_numeric(df[col], errors='coerce')
                    
            df.attrs['removed'] = before_count - len(df.dropna(subset=['d18O'])) # 消えた数をメモ
            
            # 不備がある行（d18Oや経緯度がNaNになった行）を除去
            # cols_to_check = [c for c in ['d18O', 'Longitude', 'Latitude'] if c in df.columns]
            # df = df.dropna(subset=cols_to_check).copy()
            
            # 属性に除外数を保存
            df.attrs['removed_count'] = before_count - len(df)
            df.attrs['total_count'] = before_count
            
            
            # StationやDate列に型が混在するとクラウドでエラーが出るため、文字列に統一
            for col in ['Station', 'Date', 'Cruise']:
                if col in df.columns:
                    df[col] = df[col].astype(str)
            
                    return df
        
        
    except Exception as e:
        st.error(f"読み込み失敗: {e}")
        return pd.DataFrame()
        







##############################################################################
#--- 2. 海岸線データの読み込み ---，JAPANかGLOBALか
##############################################################################
@st.cache_data
def load_coastline_data(ref_data):
    """
    ref_data に基づいて適切な海岸線ファイルを読み込み、座標リストを返す。
    """
    # 1. 場合分けの設定
    if ref_data == "with NASA_database":
        coastline_excel = 'coastline/world_coastline_coordinates_50m.xlsx'
    else:
        # Kodama et al. の場合はどちらも日本近海
        # coastline_excel = 'coastline/japan_coast_line.xlsx'
        coastline_excel = 'coastline/world_coastline_coordinates_50m.xlsx'
        
    
    # 2. 読み込み処理
    try:
        df_coast = pd.read_excel(coastline_excel)
        return df_coast['Longitude'].tolist(), df_coast['Latitude'].tolist()
    except Exception as e:
        st.error(f"海岸線ファイルの読み込みに失敗しました: {coastline_excel} - {e}")
        return [], []
    




##############################################################################
#--- 3. レイアウトの一括適用 ---，JAPANかGLOBALか
##############################################################################

def apply_common_layout(fig, ref_data, z_min, z_max, x_range=None, y_range=None):
    """全てのPlotlyグラフに共通の見た目と、データに応じた視点切り替えを一括適用する"""
    is_nasa = (ref_data == "with NASA_database")
    
    # --- 1. 表示モードに応じた視点とアスペクト比の切り替え ---
    if is_nasa:
        # 【NASA用】太平洋側から日本を見下ろす（高高度）
        camera_setting = dict(
            eye=dict(x=1.2, y=-0.8, z=2.2), # zを大きくして上空から
            center=dict(x=0, y=0, z=-0.1)
        )
        target_aspectratio = dict(x=2, y=1, z=0.5)
    else:
        # 【日本近海用】日本上空（少し南西寄り）から見下ろす
        camera_setting = dict(
            eye=dict(x=-0.8, y=-0.8, z=2.2), # 絶対値を小さくすると直下に近い角度になります
            center=dict(x=0, y=0, z=-0.1)
        )
        target_aspectratio = dict(x=1, y=1, z=1)

    # --- 2. シーン設定の組み立て ---
    scene_dict = dict(
        aspectmode='manual',
        aspectratio=target_aspectratio,
        zaxis=dict(range=[z_min, z_max]),
        xaxis_title='Longitude E',
        yaxis_title='Latitude N',
        zaxis_title='Water Depth',
        camera=camera_setting
    )
    
    # 軸範囲の適用（日本近海などで範囲指定がある場合）
    if x_range:
        scene_dict['xaxis'] = dict(range=x_range)
    if y_range:
        scene_dict['yaxis'] = dict(range=y_range)
        
    # --- 3. レイアウトの更新 ---
    fig.update_layout(
        scene=scene_dict,
        width=700,
        height=600,
        margin=dict(r=20, l=10, b=10, t=10)
    )
    
    return fig





##############################################################################
#--- 4. 水深に関連するキーワード（'Depth_m' など）の場合に、カスタムカラースケール選択 ---
##############################################################################


def get_custom_colorscale(selected_item):
    """
    選択項目に応じてカスタムカラースケールを返す。
    Depthの場合は浅い層の変化を強調する。
    """
    # 1. 通常時（Depth以外）のスケール
    standard_scale = [
        'darkblue', 'blue', 'lightblue', 'lightgreen', 
        'green', 'yellow', 'orange', 'red'
    ]

    # 2. Depth時：浅い方の変化を大きくする設定
    # 数値(0.0~1.0)を指定することで、色の配分を調整できます。
    # ここでは、0.0(浅い)〜0.3(中層)の間で激しく変化させ、0.3以降(深い)を青系で固定します。
    depth_keywords = ['Depth_m', 'Water Depth', 'depth']
    
    if selected_item in depth_keywords:
        # データが負の値（表層が0、底層が-500など）の場合のスケール
        # 0.0 はスケール内の最小値（最も深い負の値）、1.0 は最大値（0m付近）を指す
        depth_scale = [
            [0.0, 'darkblue'],   # 最深部（例：-500m）
            [0.5, 'blue'],       # 中層
            [0.7, 'lightblue'],  # ここから表層に向かって急激に変化
            [0.85, 'lightgreen'],
            [0.9, 'yellow'],
            [0.95, 'orange'],
            [0.99, 'pink'],         # 最表層（0m付近）
            [1.0, 'red']         # 最表層（0m付近）
        ]
        return depth_scale
    
    return standard_scale


##############################################################################
#--- 5. 地図スタイルの設定 ---
##############################################################################


def apply_map_style(fig, map_mode):
    """
    PlotlyのFigureオブジェクトと選択されたモードを受け取り、
    背景タイルを適用して返す共通関数。
    """
    
    fig.update_layout(mapbox_style="carto-positron")

    if map_mode == "Standard":
        fig.update_layout(mapbox_style="carto-positron")
        
    elif map_mode == "Satellite":
        fig.update_layout(
            mapbox_style="white-bg",
            mapbox_layers=[{
                "below": 'traces',
                "sourcetype": "raster",
                "source": ["https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"],
                "sourceattribution": "USGS"
            }]
        )
        
    elif map_mode == "Bathymetry (Sea)":
        fig.update_layout(
            mapbox_style="white-bg",
            mapbox_layers=[{
                "below": 'traces',
                "sourcetype": "raster",
                "source": ["https://services.arcgisonline.com/arcgis/rest/services/Ocean/World_Ocean_Base/MapServer/tile/{z}/{y}/{x}"],
                "sourceattribution": "Esri, GEBCO"
            }]
        )
        
    elif map_mode == "Contour (GSI)":
        # 国土地理院タイル：拡大しても消えず、詳細になる
        fig.update_layout(
            mapbox_style="white-bg",
            mapbox_layers=[{
                "below": 'traces',
                "sourcetype": "raster",
                "source": ["https://cyberjapandata.gsi.go.jp/xyz/std/{z}/{x}/{y}.png"],
                "sourceattribution": "国土地理院 (GSI)"
            }]
        )
    
    # 共通のレイアウト設定
    fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))
    
    return fig




##############################################################################
#--- 6. キャッシュクリア ---
##############################################################################
def clear_app_cache():
    st.cache_data.clear()
