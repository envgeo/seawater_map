#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 17:15:03 2023
@author: Toyoho Ishimura @Kuoto-U
2026/02/10 update 
"""

# このバージョンは補完計算しすぎなので，調整が必要


# --- バージョン管理の設定 ---
version = "2.10" #2026/02/23
fig_title = "envgeo-seawater-database"  # 2026/02/12
# fig_title = r"SEAWATER $\delta^{18}$O MAP WEB (b02)"  # 2026/02/12



import cartopy
import streamlit as st
import pandas as pd
import numpy as np
import cartopy.crs as ccrs
# import matplotlib.ticker as mticker
import matplotlib.pyplot as plt
import envgeo_utils  # 作った設定ファイルを読み込む
# 以下はコンターマップ用
from scipy.interpolate import griddata
import cartopy.feature as cfeature  # 陸地塗りつぶし用

from mpl_toolkits.axes_grid1 import make_axes_locatable




import io





print(f"-------32_map_d18O_zoom_select_({version})--------")

# datetimeモジュールを使った現在の日付と時刻の取得
import datetime
dt = datetime.datetime.today()  # ローカルな現在の日付と時刻を取得
print(dt)  # 2021-10-29 15:58:08.356501



############ページタイトル設定############

# st.set_page_config(
#     page_title="d18O mapping",
#     # page_icon="🗾",
#     layout="wide"
#     )







# 現状では使わないここから
@st.cache_data
def get_filtered_data(ref_data, selected_cruises, salinity_range, depth_range):
    # データの読み込み
    df = envgeo_utils.load_isotope_data(ref_data)
    if df.empty:
        return df
    
    # ここでフィルタリングを一括で行う
    df = df[df['Cruise'].isin(selected_cruises)]
    df = df[(df['Salinity'] >= salinity_range[0]) & (df['Salinity'] <= salinity_range[1])]
    df = df[(df['Depth_m'] >= depth_range[0]) & (df['Depth_m'] <= depth_range[1])]
    
    return df
# 現状では使わないここまで



def main():
    
        
    # タイトル
    st.header(f'δ18O mapping({version})')
  
    # リロードボタン
    st.button('Reload')





    # データソースの変数、envgeo_utilsから読み出す
    data_source_JAPAN_SEA = envgeo_utils.data_source_JAPAN_SEA
    data_source_AROUND_JAPAN = envgeo_utils.data_source_AROUND_JAPAN
    data_source_GLOBAL = envgeo_utils.data_source_GLOBAL
    

    # データソース選択
    ref_data = st.radio("data source (see home>about):", (data_source_JAPAN_SEA, data_source_AROUND_JAPAN, data_source_GLOBAL), horizontal=True, args=[1, 0])


    # plot_all_data = st.radio("Plot all data on the background as red:", ("YES", "NO"), horizontal=True, args=[1, 0])



    # 選択したデータセットの文献表示
    
    if ref_data == data_source_JAPAN_SEA:
        st.write(envgeo_utils.refs_JAPAN_SEA)
        
    elif ref_data == data_source_AROUND_JAPAN:
        # st.text('including data from previous reports')
        st.write(envgeo_utils.refs_AROUND_JAPAN)

        
    elif ref_data == data_source_GLOBAL:
        st.write(envgeo_utils.refs_GLOBAL)
        
    else:
        st.warning("data source error")



    #データソースによって選ぶファイルを変える
    # if ref_data == data_source_JAPAN_SEA:
    #     excel_file = 'd18O_20230513-1_NA2_2021add.xlsx'

    # elif ref_data == data_source_AROUND_JAPAN:
    #     excel_file = 'd18O_20240927_ref_YSKH.xlsx'
        
    # else:
    #     excel_file = 'd18O_NASA_all_data_Python_20250123.xlsx'
        
        
    # sheet_num = 1
    
    # df1 = pd.read_excel(excel_file, sheet_name=sheet_num)
    
    
    # envgeo_utilsからデータフレーム読み込み
    df1 = envgeo_utils.load_isotope_data(ref_data)
    



######  scalebarで制御してsubmitする場合 ################

    with st.sidebar.form("parameter", clear_on_submit=False):
        
        
        
        # #################文献選択ここから###########################################
        
        
        # # st.subheader('data source:')
        
        # # ref_data = st.radio("data source (see home>about):", (data_source_JAPAN_SEA, data_source_AROUND_JAPAN), horizontal=True, args=[1, 0])
        
        # if ref_data == data_source_JAPAN_SEA:
        #     ############論文データ追加用の設定############
        #     #　足りなくなれば追加で，
        #     Transect001 = 'Pacific'
        #     Transect002 = 'Pacific_west'
        #     Transect003 = 'Noto'
        #     Transect004 = 'Toyama'
        #     Transect005 = 'SI'
        #     Transect006 = 'Yamato'
        #     Transect007 = 'Shimane&Tottori'
        #     Transect008 = 'NA2'
        #     Transect009 = 'Tsushima'							  
        #     Transect010 = 'nECS'						  
        #     Transect011 = 'CK'						  
        #     Transect012 = 'ECS2021'							  
        #     Transect013 = 'sECS'					  
        #     Transect014 = 'Nansei'
        #     # Transect015 = ''
        #     # Transect016 = ''
        #     # Transect017 = ''
        #     # Transect018 = ''
        #     # Transect019 = ''
        #     # Transect020 = 'ここの新規項目を入力'
        #     # Transect021 = 'ここの新規項目を入力'
        #     # Transect022 = 'ここの新規項目を入力'
        #     # Transect023 = 'ここの新規項目を入力'
        #     # Transect024 = 'ここの新規項目を入力'
        #     # Transect025 = 'ここの新規項目を入力'
        #     # Transect026 = 'ここの新規項目を入力'
        #     # Transect027 = 'ここの新規項目を入力'
        #     # Transect028 = 'ここの新規項目を入力'
        #     # Transect029 = 'ここの新規項目を入力'
        #     # Transect030 = 'ここの新規項目を入力'
        # elif ref_data == data_source_AROUND_JAPAN:
        #     ############論文データ追加用の設定############
        #     #　足りなくなれば追加で，
        #     Transect001 = 'Pacific'
        #     Transect002 = 'Pacific_west'
        #     Transect003 = 'Noto'
        #     Transect004 = 'Toyama'
        #     Transect005 = 'SI'
        #     Transect006 = 'Yamato'
        #     Transect007 = 'Shimane&Tottori'
        #     Transect008 = 'NA2'
        #     Transect009 = 'Tsushima'							  
        #     Transect010 = 'nECS'						  
        #     Transect011 = 'CK'						  
        #     Transect012 = 'ECS2021'							  
        #     Transect013 = 'sECS'					  
        #     Transect014 = 'Nansei'
        #     # Transect015 = 'KUWANO'
        #     Transect016 = 'Yamamoto_2001'
        #     Transect017 = 'Sakamoto_2019'
        #     Transect018 = 'Kodaira_2016'
        #     Transect019 = 'Horikawa_2023'
        #     # Transect020 = 'ここの新規項目を入力'
        #     # Transect021 = 'ここの新規項目を入力'
        #     # Transect022 = 'ここの新規項目を入力'
        #     # Transect023 = 'ここの新規項目を入力'
        #     # Transect024 = 'ここの新規項目を入力'
        #     # Transect025 = 'ここの新規項目を入力'
        #     # Transect026 = 'ここの新規項目を入力'
        #     # Transect027 = 'ここの新規項目を入力'
        #     # Transect028 = 'ここの新規項目を入力'
        #     # Transect029 = 'ここの新規項目を入力'
        #     # Transect030 = 'ここの新規項目を入力'
        
        
        # else:
        #     Transect000 = 'NASA_database'
        #     Transect001 = 'Pacific'
        #     Transect002 = 'Pacific_west'
        #     Transect003 = 'Noto'
        #     Transect004 = 'Toyama'
        #     Transect005 = 'SI'
        #     Transect006 = 'Yamato'
        #     Transect007 = 'Shimane&Tottori'
        #     Transect008 = 'NA2'
        #     Transect009 = 'Tsushima'							  
        #     Transect010 = 'nECS'						  
        #     Transect011 = 'CK'						  
        #     Transect012 = 'ECS2021'							  
        #     Transect013 = 'sECS'					  
        #     Transect014 = 'Nansei'
        #     # Transect015 = 'KUWANO'
        #     Transect016 = 'Yamamoto_2001'
        #     Transect017 = 'Sakamoto_2019'
        #     Transect018 = 'Kodaira_2016'
        #     Transect019 = 'Horikawa_2023'
        #     # Transect020 = 'ここの新規項目を入力'
        #     # Transect021 = 'ここの新規項目を入力'
        #     # Transect022 = 'ここの新規項目を入力'
        #     # Transect023 = 'ここの新規項目を入力'
        #     # Transect024 = 'ここの新規項目を入力'
        #     # Transect025 = 'ここの新規項目を入力'
        #     # Transect026 = 'ここの新規項目を入力'
        #     # Transect027 = 'ここの新規項目を入力'
        #     # Transect028 = 'ここの新規項目を入力'
        #     # Transect029 = 'ここの新規項目を入力'
        #     # Transect030 = 'ここの新規項目を入力'
        
        # #################文献選択ここまで###########################################
        
        st.header('select parameters ➡ submit')
        
##############################################################################
# サイドバーここから
##############################################################################

        
        
        st.form_submit_button(":red[submit]")

        ###このセットでsubmitボタン豚津に出来る
        # st.form_submit_button(":red[submit (TOP)]")
        # submitted = st.form_submit_button(":red[submit (BOTTOM)]")
        
        
        #　一つだけの時は以下
        # submitted = st.form_submit_button(":red[submit]")
        
        
        
        st.subheader(':blue[--- for data range ---]') 
        
        
        
        #年の範囲       # サブレベルヘッダ
        # st.sidebar.subheader('年の範囲')
        
        sld_year_min, sld_year_max = st.slider(label='Year selected',
                                    min_value=1960,
                                    max_value=2028,
                                    value=(1960,2028),
                                    )
        # st.sidebar.write(f'Selected: {sld_year_min} ~ {sld_year_max}')
        
        #月の範囲       # サブレベルヘッダ
        # st.sidebar.subheader('月の範囲')
        
        
        # --- 月　スライダー版（これを書き換え） ---
        # sld_month_min, sld_month_max = st.slider(label='Month selected',
        #                             min_value=1,
        #                             max_value=12,
        #                             value=(1, 12),
        #                             )
        # # st.sidebar.write(f'Selected: {sld_month_min} ~ {sld_month_max}')
        

        # --- 月　multiselect版 ---
        selected_months = st.multiselect(
            label='Month selected',
            options=list(range(1, 13)),  # 1〜12の選択肢
            default=list(range(1, 13))   # 初期状態は全選択
        )
        
        
        #経度longitudeの範囲   
        # st.sidebar.subheader('経度の範囲')
        sld_lon_min, sld_lon_max = st.slider(label='Longitude selected',
                                    min_value=-180,
                                    max_value=180,
                                    value=(-180, 180),
                                    )
        # st.sidebar.write(f'Selected: {sld_lon_min} ~ {sld_lon_max}')
        
        
        #緯度の範囲   
        # st.sidebar.subheader('緯度の範囲')
        sld_lat_min, sld_lat_max = st.slider(label='Latitude selected',
                                    min_value=-90,
                                    max_value=90,
                                    value=(-90, 90),
                                    )
        # st.sidebar.write(f'Selected: {sld_lat_min} ~ {sld_lat_max}')
        
        
        #水深の範囲   
        # st.sidebar.subheader('水深の範囲')
        sld_depth_min, sld_depth_max = st.slider(label='Water depth selected',
                                    min_value=0,
                                    max_value=9000,
                                    value=(0, 9000),
                                    )
        # st.sidebar.write(f'Selected: {sld_depth_min} ~ {sld_depth_max}')
        
        #塩分の範囲   
        # st.sidebar.subheader('塩分の範囲')
        sld_sal_min, sld_sal_max = st.slider(label='Salinity selected',
                                    min_value=-1,
                                    max_value=40,
                                    value=(-1, 40),
                                    )
        # st.sidebar.write(f'Selected: {sld_sal_min} ~ {sld_sal_max}')
        
        
        #水温の範囲   
        # st.sidebar.subheader('水温の範囲')
        sld_temp_min, sld_temp_max = st.slider(label='Temperature selected',
                                    min_value=-3,
                                    max_value=35,
                                    value=(-3, 33),
                                    )
        # st.sidebar.write(f'Selected: {sld_temp_min} ~ {sld_temp_max}')
            
           
           
        # st.sidebar.subheader('航海区の範囲')dfから要素抽出
        # 例：列名が "RockType" の場合
        Transect_list = df1["Transect"].dropna().unique().tolist()
        print(Transect_list,"AAA")
        
        selected_cruise = st.multiselect('Choose cruise area', Transect_list,default=Transect_list)
        

        # st.sidebar.subheader('航海区の範囲')手動で指定する場合
        # if ref_data == data_source_JAPAN_SEA:
        #     selected_cruise = st.multiselect('Choose cruise area',
        #                                 [
        #                                    Transect001,
        #                                    Transect002,
        #                                    Transect003,
        #                                    Transect004,
        #                                    Transect005,
        #                                    Transect006,
        #                                    Transect007,
        #                                    Transect008,
        #                                    Transect009,
        #                                    Transect010,
        #                                    Transect011,
        #                                    Transect012,
        #                                    Transect013,
        #                                    Transect014,
        #                                  ],
        #                                default=(
        #                                    Transect001,
        #                                    Transect002,
        #                                    Transect003,
        #                                    Transect004,
        #                                    Transect005,
        #                                    Transect006,
        #                                    Transect007,
        #                                    Transect008,
        #                                    Transect009,
        #                                    Transect010,
        #                                    Transect011,
        #                                    Transect012,
        #                                    Transect013,
        #                                    Transect014,
        #                                            ))

        # elif ref_data == data_source_AROUND_JAPAN:
        #         selected_cruise = st.multiselect('Choose cruise area',
        #                                     [
        #                                        Transect001,
        #                                        Transect002,
        #                                        Transect003,
        #                                        Transect004,
        #                                        Transect005,
        #                                        Transect006,
        #                                        Transect007,
        #                                        Transect008,
        #                                        Transect009,
        #                                        Transect010,
        #                                        Transect011,
        #                                        Transect012,
        #                                        Transect013,
        #                                        Transect014,
        #                                         # Transect015,
        #                                         Transect016,
        #                                         Transect017,
        #                                         Transect018,
        #                                         Transect019,
        #                                        # Transect020,
        #                                        # Transect021,
        #                                        # Transect022,
        #                                        # Transect023,
        #                                        # Transect024,
        #                                        # Transect025,
        #                                        # Transect026,
        #                                        # Transect027,
        #                                        # Transect028,
        #                                        # Transect029,
        #                                        # Transect030,
        #                                      ],
        #                                    default=(
        #                                        Transect001,
        #                                        Transect002,
        #                                        Transect003,
        #                                        Transect004,
        #                                        Transect005,
        #                                        Transect006,
        #                                        Transect007,
        #                                        Transect008,
        #                                        Transect009,
        #                                        Transect010,
        #                                        Transect011,
        #                                        Transect012,
        #                                        Transect013,
        #                                        Transect014,
        #                                         # Transect015,
        #                                         Transect016,
        #                                         Transect017,
        #                                         Transect018,
        #                                         Transect019,
        #                                        # Transect020,
        #                                        # Transect021,
        #                                        # Transect022,
        #                                        # Transect023,
        #                                        # Transect024,
        #                                        # Transect025,
        #                                        # Transect026,
        #                                        # Transect027,
        #                                        # Transect028,
        #                                        # Transect029,
        #                                        # Transect030,
        #                                                ))
        # else:
        #     selected_cruise = st.multiselect('Choose cruise area',
        #                                     [
        #                                         Transect000,
        #                                        Transect001,
        #                                        Transect002,
        #                                        Transect003,
        #                                        Transect004,
        #                                        Transect005,
        #                                        Transect006,
        #                                        Transect007,
        #                                        Transect008,
        #                                        Transect009,
        #                                        Transect010,
        #                                        Transect011,
        #                                        Transect012,
        #                                        Transect013,
        #                                        Transect014,
        #                                         # Transect015,
        #                                         Transect016,
        #                                         Transect017,
        #                                         Transect018,
        #                                         Transect019,
        #                                        # Transect020,
        #                                        # Transect021,
        #                                        # Transect022,
        #                                        # Transect023,
        #                                        # Transect024,
        #                                        # Transect025,
        #                                        # Transect026,
        #                                        # Transect027,
        #                                        # Transect028,
        #                                        # Transect029,
        #                                        # Transect030,
        #                                      ],
        #                                    default=(
        #                                        Transect000,
        #                                        Transect001,
        #                                        Transect002,
        #                                        Transect003,
        #                                        Transect004,
        #                                        Transect005,
        #                                        Transect006,
        #                                        Transect007,
        #                                        Transect008,
        #                                        Transect009,
        #                                        Transect010,
        #                                        Transect011,
        #                                        Transect012,
        #                                        Transect013,
        #                                        Transect014,
        #                                         # Transect015,
        #                                         Transect016,
        #                                         Transect017,
        #                                         Transect018,
        #                                         Transect019,
        #                                        # Transect020,
        #                                        # Transect021,
        #                                        # Transect022,
        #                                        # Transect023,
        #                                        # Transect024,
        #                                        # Transect025,
        #                                        # Transect026,
        #                                        # Transect027,
        #                                        # Transect028,
        #                                        # Transect029,
        #                                        # Transect030,
        #                                                ))

        
        # # st.write(f'Selected: {selected_cruise}')
        
        
        
        st.write('Cruise Area (2015-2021) in Kodama et al.(2024)')
        st.image("data/sites_20230515.gif") 
        
    
        # #スペース入れる
        # st.subheader(':blue[  ]')
        # st.subheader(':blue[  ]')
        st.subheader(':blue[--- for fig scale only ---]')
        
    
        
    
        
        if ref_data == data_source_JAPAN_SEA:

            #地図の描画範囲（拡大）
            # # 120-0.001, 145+0.001, 20-0.001, 45+0.001
            
            # # st.sidebar.subheader('地図の経度の範囲（拡大）')
            map_lon_min, map_lon_max = st.slider(label='Map Longitude ',
                                        min_value=120-0.001,
                                        max_value=145+0.001,
                                        value=(120-0.001, 145+0.001),
                                        )
            # # st.sidebar.write(f'Selected: {map_lon_min} ~ {map_lon_max}')
            
            # # st.sidebar.subheader('地図の緯度の範囲（拡大）')
            map_lat_min, map_lat_max = st.slider(label='Map Latitude ',
                                        min_value=20-0.001,
                                        max_value=45+0.001,
                                        value=(20-0.001, 45+0.001),
                                        )
            # # st.sidebar.write(f'Selected: {map_lat_min} ~ {map_lat_max}')
        elif ref_data == data_source_AROUND_JAPAN:
            #地図の描画範囲（拡大）
            # # 120-0.001, 145+0.001, 20-0.001, 45+0.001
            
            # # st.sidebar.subheader('地図の経度の範囲（拡大）')
            map_lon_min, map_lon_max = st.slider(label='Map Longitude ',
                                        min_value=-180-0.001,
                                        max_value=180+0.001,
                                        value=(120-0.001, 180+0.001),
                                        )
            # # st.sidebar.write(f'Selected: {map_lon_min} ~ {map_lon_max}')
            
            # # st.sidebar.subheader('地図の緯度の範囲（拡大）')
            map_lat_min, map_lat_max = st.slider(label='Map Latitude ',
                                        min_value=-70-0.001,
                                        max_value=55+0.001,
                                        value=(0-0.001, 55+0.001),
                                        )
            # # st.sidebar.write(f'Selected: {map_lat_min} ~ {map_lat_max}')
            
            
            # st.sidebar.subheader('描画水深の範囲')
            # fig_depth_min, fig_depth_max = st.slider(label='Water depth selected',
            #                             min_value=0,
            #                             max_value=1000,
            #                             value=(0, 500),
            #                             )
            # st.sidebar.write(f'Selected: {fig_depth_min} ~ {fig_depth_max}')
            
            
        
        else:
            #地図の描画範囲（拡大）
            # # 120-0.001, 145+0.001, 20-0.001, 45+0.001
            
            # # st.sidebar.subheader('地図の経度の範囲（拡大）')
            map_lon_min, map_lon_max = st.slider(label='Map Longitude',
                                        min_value=-180-0.001,
                                        max_value=180+0.001,
                                        value=(-180-0.001, 180+0.001),
                                        )
            # # st.sidebar.write(f'Selected: {map_lon_min} ~ {map_lon_max}')
            
            # # st.sidebar.subheader('地図の緯度の範囲（拡大）')
            map_lat_min, map_lat_max = st.slider(label='Map Latitude',
                                        min_value=-70-0.001,
                                        max_value=55+0.001,
                                        value=(-90-0.001, 90+0.001),
                                        )
            # # st.sidebar.write(f'Selected: {map_lat_min} ~ {map_lat_max}')
            
            
            # st.sidebar.subheader('描画水深の範囲')
            # fig_depth_min, fig_depth_max = st.slider(label='Water depth selected',
            #                             min_value=0,
            #                             max_value=1000,
            #                             value=(0, 500),
            #                             )
                # st.sidebar.write(f'Selected: {fig_depth_min} ~ {fig_depth_max}')
                
                
                
                
                
                
        # 図のd18Oの範囲    2026/02/19追加
        # サイドバーにカラーバー調整用のスライダーを設置
        # st.write("### Colorbar Scale")   
        if ref_data == data_source_JAPAN_SEA:
            sld_d18O_min, sld_d18O_max = st.slider(label='d18O range for colorbar',
                                        min_value=-20.0,
                                        max_value=5.0,
                                        value=(-1.5, 1.0),
                                           )
            
        elif ref_data == data_source_AROUND_JAPAN:
                sld_d18O_min, sld_d18O_max = st.slider(label='d18O range for colorbar',
                                            min_value=-20.0,
                                            max_value=5.0,
                                            value=(-1.5, 1.0),
                                               )
        else:

                sld_d18O_min, sld_d18O_max = st.slider(label='d18O range for colorbar',
                                            min_value=-20.0,
                                            max_value=5.0,
                                            value=(-5.0, 2.0),
                                               )
            
        
        submitted = st.form_submit_button(":red[submit!]")

##############################################################################
# サイドバーここまで
##############################################################################



    
    
    
    
    
    # df1 = df1[(df1['Depth_m'] == 'xxx') 
    #             # |(df1['Depth_m'] <= 10) & (df1['Depth_m'] >= 0)
    #             # |(df1['Depth_m'] <= 200) & (df1['Depth_m'] > 10)
    #             # |(df1['Depth_m'] <= 500) & (df1['Depth_m'] > 200)
    #             # |(df1['Depth_m'] <= 1000) & (df1['Depth_m'] > 500)
                
    #             |(df1['Depth_m'] <= sld_depth_max) & (df1['Depth_m'] >= sld_depth_min )#調整用
    #             | df1.isnull().all(axis=1)]      
      
    
    
    # #streamlitのマルチ選択用  ヘッダ付近に配置
    # erea_list = list(df1['Transect'].unique())
    # selected_erea = st.sidebar.multiselect('航海区分を選択(Notoは日本海沿岸部)', default=[
    #                   'CK',
    #                   # 'Nansei',
    #                   # 'nECS',
    #                   # 'Noto',
    #                   # 'Pacific',
    #                   # 'Pacific_west',
    #                   # 'sECS',
    #                   # 'Shimane&Tottori',
    #                   # 'SI',
    #                   # 'Toyama',
    #                   # 'Tsushima',
    #                   # 'Yamato',
    #                   # 'NA2'
    #                   # 'ECS2021'
    #                   ])
    
    df1 = df1[(df1['Transect'].isin(selected_cruise))
               | df1.isnull().all(axis=1)]
    # #streamlitのマルチ選択用
    
    
      
    
    
    # #描画する緯度経度を指定 
    df1 = df1[(df1['Longitude_degE'] == 'xxx') 
                # |(df1['Longitude_degE'] <= 145) & (df1['Longitude_degE'] >= 140)    
                # |(df1['Longitude_degE'] <= 140) & (df1['Longitude_degE'] >= 135)         
                # |(df1['Longitude_degE'] <= 135) & (df1['Longitude_degE'] >= 130)
                # |(df1['Longitude_degE'] <= 130) & (df1['Longitude_degE'] >= 125)
                # |(df1['Longitude_degE'] <= 125) & (df1['Longitude_degE'] >= 120)
                # |(df1['Longitude_degE'] <= 120) & (df1['Longitude_degE'] >= 115)
                
                |(df1['Longitude_degE'] <= sld_lon_max) & (df1['Longitude_degE'] >= sld_lon_min) #調整用
                | df1.isnull().all(axis=1)]      
      
    
    df1 = df1[(df1['Latitude_degN'] == 'xxx')
                # |(df1['Latitude_degN'] <= 45) & (df1['Latitude_degN'] >= 40)          
                # |(df1['Latitude_degN'] <= 40) & (df1['Latitude_degN'] >= 35)
                # |(df1['Latitude_degN'] <= 35) & (df1['Latitude_degN'] >= 30)
                # |(df1['Latitude_degN'] <= 30) & (df1['Latitude_degN'] >= 25)
                # |(df1['Latitude_degN'] <= 25) & (df1['Latitude_degN'] >= 20)
                
                |(df1['Latitude_degN'] <= sld_lat_max) & (df1['Latitude_degN'] >= sld_lat_min) #調整用
                | df1.isnull().all(axis=1)]      
      
              
    # --- 月 (スライダー用) ---
    # df1 = df1[(df1['Month'] == 'xxx')
                
    #             |(df1['Month'] <= sld_month_max) & (df1['Month'] >= sld_month_min)
    #             | df1.isnull().all(axis=1)]
      
    # --- 月 (multiselect用) ---
    if selected_months:
        # isin で選ばれた月を抽出
        # | (または)
        # df1.isnull().all(axis=1) で全ての列が空の行（挿入した空白行）を抽出
        df1 = df1[df1['Month'].isin(selected_months) | df1.isnull().all(axis=1)]
    else:
        # 月が一つも選ばれていない場合でも、空白行だけは残す
        df1 = df1[df1.isnull().all(axis=1)]         
      
    
    
    df1 = df1[(df1['Salinity'] == 'xxx')
              # |(df1['Salinity'] >= 0) & (df1['Salinity'] <= 38)
              
                |(df1['Salinity'] >= sld_sal_min) & (df1['Salinity'] <= sld_sal_max)
              | df1.isnull().all(axis=1)]      
    
    
    df1 = df1[(df1['Depth_m'] == 'xxx') 
                # |(df1['Depth_m'] <= 10) & (df1['Depth_m'] >= 0)
                # |(df1['Depth_m'] <= 200) & (df1['Depth_m'] > 10)
                # |(df1['Depth_m'] <= 500) & (df1['Depth_m'] > 200)
                # |(df1['Depth_m'] <= 1000) & (df1['Depth_m'] > 500)
                
                |(df1['Depth_m'] <= sld_depth_max) & (df1['Depth_m'] >= sld_depth_min )#調整用
                | df1.isnull().all(axis=1)]      
                   
    
        
    df1 = df1[(df1['Temperature_degC'] == 'xxx') 
                
                |(df1['Temperature_degC'] <= sld_temp_max) & (df1['Temperature_degC'] >= sld_temp_min )#調整用
                | df1.isnull().all(axis=1)]      
                   
    
    #描画する年範囲を指定
    df1 = df1[(df1['Year'] <= sld_year_max) & (df1['Year'] >= sld_year_min) | df1.isnull().all(axis=1)] 
    
    #描画する月範囲を指定 and指定
    # df1 = df1[(df1['Month'] >= 5) & (df1['Month'] <= 10)] 
    #描画する月範囲を指定 or指定
    # df1 = df1[(df1['Month'] >= 11) | (df1['Month'] <= 4)] 
    #描画する月範囲を指定
    # df1 = df1[(df1['Transect'] == "Noto") & (df1['Transect'] == "Noto")] 
    #描画するPI指定
    # df1 = df1[(df1['PI'] == "Kodama") | (df1['PI'] == "Kitajima")] 
    
    
    
    
    #選んだパラメーター表示
    # st.write('YEAR:'+str(sld_year_min)+'-'+str(sld_year_max)+', ' 
    #           +'MONTH:'+str(sld_month_min)+'-'+str(sld_month_max)+', '
    #           +'Longitude:'+str(sld_lon_min)+'-'+str(sld_lon_max)+', '
    #           +'Latitude:'+str(sld_lat_min)+'-'+str(sld_lat_max)+', '
    #           +'Water_depth:'+str(sld_depth_min)+'-'+str(sld_depth_max)+', '
    #           +'Salinity:'+str(sld_sal_min)+'-'+str(sld_sal_max))
    # st.write('Area(Cruise)',selected_cruise)
    # selected_cruise_indicate =str(list(selected_cruise[:]))
    # st.write('Selected Area (Cruise)', selected_cruise_indicate)
    # print('Area(Cruise)', list(selected_cruise[:]))
    #テキストの色変更
    # st.write(""":red['test']""")




    
    #df1が空になっているかどうかを確認する
    df_empty = df1.empty

    # st.write(df_empty)
    data_found_num = str(len(df1["d18O"]))

    
    # バリデーション処理
    if df_empty == 1:  #データが無かったとき
        st.warning('no data found')
        # 条件を満たないときは処理を停止する
        st.stop()
    elif df_empty == 0: #データがあったとき
        st.write(data_found_num,'data found')


    # #平均値と標準偏差
    # col1, col2, col3, col4 = st.columns(4)

    # with col2:
    #     average = np.mean(df1['d18O'])
    #     average = round(average,3)
    #     st.write('d18O _ave:', average)

    # with col3:
    #     stdev = np.std(df1['d18O'])
    #     stdev = round(stdev,3)
    #     st.write('stdev: ±', stdev)  
        
    
    # col1, col2, col3, col4 = st.columns(4)

    # with col2:
    #     average = np.mean(df1['Salinity'])
    #     average = round(average,2)
    #     st.write('Sal_ave:', average)

    # with col3:
    #     stdev = np.std(df1['Salinity'])
    #     stdev = round(stdev,2)
    #     st.write('stdev ±:', stdev)  
        
    # col1, col2, col3, col4 = st.columns(4)

    # with col2:
    #     average = np.mean(df1['Temperature_degC'])
    #     average = round(average,2)
    #     st.write('Temp_ave:', average)

    # with col3:
    #     stdev = np.std(df1['Temperature_degC'])
    #     stdev = round(stdev,2)
    #     st.write('stdev ±:', stdev)  
        
    
    
    
    
    
##################################選択データ表示　2024/10/07###################################################################################################################

    
    
        selected_row = "Transect"
    
        #列の要素を表示
        d_select_add2 = df1[selected_row].value_counts().to_dict()
        d_select_add2_sum = df1[selected_row].count().sum()
        print('要素と出現数:', d_select_add2)
        print('要素と出現数:', d_select_add2_sum)
        print('---------------')
                            
##################################選択データ表示　2024/10/07###################################################################################################################

        # with表記 (推奨)
        with st.expander("selected data", expanded=False):
    
        #選んだパラメーター表示
        
        
        # 月がスライダーの場合
            # st.write(':green[YEAR]:'+str(sld_year_min)+'-'+str(sld_year_max)+', '
            #           +':green[MONTH]:'+str(sld_month_min)+'-'+str(sld_month_max)+', '
            #           +':green[Longitude]:'+str(sld_lon_min)+'-'+str(sld_lon_max)+', '
            #           +':green[Latitude]:'+str(sld_lat_min)+'-'+str(sld_lat_max)+', '
            #           +':green[Water_depth]:'+str(sld_depth_min)+'-'+str(sld_depth_max)+', '
            #           +':green[Salinity]:'+str(sld_sal_min)+'-'+str(sld_sal_max))
            
        # 月がマルチセレクトの場合　　リストを文字列に変換（例: [1, 2] -> "1, 2"）
            month_display = ", ".join(map(str, sorted(selected_months))) if selected_months else "None"
        
            st.write(':green[YEAR]:' + str(sld_year_min) + '-' + str(sld_year_max) + ', '
                     + ':green[MONTH]:' + '[' + month_display + ']' + ', '
                     + ':green[Longitude]:' + str(sld_lon_min) + '-' + str(sld_lon_max) + ', '
                     + ':green[Latitude]:' + str(sld_lat_min) + '-' + str(sld_lat_max) + ', '
                     + ':green[Water_depth]:' + str(sld_depth_min) + '-' + str(sld_depth_max) + ', '
                     + ':green[Salinity]:' + str(sld_sal_min) + '-' + str(sld_sal_max))
                
                
            
            # st.write('Area(Cruise)',selected_cruise)
            selected_cruise_indicate =str(list(selected_cruise[:]))
            st.write(':green[Selected Data (Cruise, papers)]', selected_cruise_indicate)
        
            st.write(':green[Selected Data (detail)]',d_select_add2)
            
            
            st.write(':green[Average values]')
                                    
            #平均値と標準偏差
            col1, col2, col3, col4 = st.columns(4)
        
            with col2:
                average = np.mean(df1['d18O'])
                average = round(average,3)
                st.write('d18O _ave:', average)
        
            with col3:
                stdev = np.std(df1['d18O'])
                stdev = round(stdev,3)
                st.write('stdev: ±', stdev)  
                
            
            col1, col2, col3, col4 = st.columns(4)
        
            with col2:
                average = np.mean(df1['Salinity'])
                average = round(average,2)
                st.write('Sal_ave:', average)
        
            with col3:
                stdev = np.std(df1['Salinity'])
                stdev = round(stdev,2)
                st.write('stdev ±:', stdev)  
                
            col1, col2, col3, col4 = st.columns(4)
        
            with col2:
                average = np.mean(df1['Temperature_degC'])
                average = round(average,2)
                st.write('Temp_ave:', average)
        
            with col3:
                stdev = np.std(df1['Temperature_degC'])
                stdev = round(stdev,2)
                st.write('stdev ±:', stdev)  
                
        
##################################選択データ表示　2024/10/07###################################################################################################################

    








    #  ここから図の設定と描画



    ###############################################################################################
    ############################################################################################### 
    ###############################################################################################
    ###############################################################################################
    # st.write(":red[d18O map (select parameters)]")
    st.markdown("##### :red[--- The map area can be adjusted using the [fig scale] setting---]")

    # st.markdown("# AAA")
    # st.title("AAA")
    # st.markdown("## BBB")
    # st.header("BBB")
    # st.markdown("### CCC")
    # st.subheader("CCC")
    # st.markdown("#### DDD")
    # st.markdown("##### EEE")
    # st.markdown("###### FFF")
    # st.markdown("GGG")

    

    
    ###############################################################################################
    ############################################################################################### 
    ###############################################################################################
    ###############################################################################################
    
#     #日本地図描画
    
#     # fig = plt.figure(figsize=(8, 6), facecolor="white", dpi=150,tight_layout=False)
#     fig = plt.figure(figsize=(12, 8),facecolor="white", dpi=150,tight_layout=False)
    
    
#     # ax = fig.add_subplot(111, projection=ccrs.Mercator(central_longitude=140.0), facecolor="white")
#     ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    
#     # ax.set_global()
#     # ax.coastlines()
#     ax.coastlines(resolution='50m')
    
#     # ax.set_extent([120-0.01, 145+0.01, 20-0.01, 45+0.01]) #この行を入れるとStreamlitでおかしくなる
#     # ax.set_extent([120-0.001, 145+0.001, 20-0.001, 45+0.001], crs=ccrs.PlateCarree())
    
#     # ax.set_xlim([120-0.01, 145+0.01])
#     # ax.set_ylim([20-0.01, 45+0.01])
    

    
#     #############川とを描画したいとき#############
#     # import cartopy.feature as cfeature
#     # ax.add_feature(cfeature.NaturalEarthFeature ('physical', 'land', '10m', facecolor='darkgrey'))
#     # ax.add_feature(cfeature.NaturalEarthFeature\
#     #           ('physical', 'rivers_lake_centerlines', '10m', facecolor='none',edgecolor='dodgerblue'))
#     #############川ここまで#############
    
#     # #############いろいろ描画したいとき#############
#     # import cartopy.feature as cfeature
#     # ax.add_feature(cfeature.LAND)
#     # ax.add_feature(cfeature.OCEAN)
#     # ax.add_feature(cfeature.COASTLINE)
#     # ax.add_feature(cfeature.BORDERS, linestyle=":")
#     # ax.add_feature(cfeature.LAKES)
#     # ax.add_feature(cfeature.RIVERS)
#     # #############いろおろここまで#############
    
#     ax.set_xlim([map_lon_min, map_lon_max])
#     ax.set_ylim([map_lat_min, map_lat_max])
    
#     # """図のフォント設定、サイズも"""
#     ##### ベースのフォントとフォントサイズの指定
#     # plt.rcParams['font.family'] = 'Arial'
#     plt.rcParams["font.size"] = 15
    
    
    
    
    
#     gl = ax.gridlines(draw_labels=True)
    
    
    
#     ####################################################################################################################################################
    
#     # # コンターマップにする場合は以下をアクティブにする
    
#     # # --- ここから書き換え ---
    
#     # # 1. 補完用のグリッド座標を作成
#     # # 地図の表示範囲（map_lon_minなど）を200x200の網目にする
#     # grid_x, grid_y = np.meshgrid(
#     #     np.linspace(map_lon_min, map_lon_max, 200),
#     #     np.linspace(map_lat_min, map_lat_max, 200)
#     # )

#     # # 2. データの補完計算
#     # # 観測地点の座標とd18Oの値 から、グリッド上の値を推定
#     # grid_z = griddata(
#     #     (df1["Longitude_degE"], df1["Latitude_degN"]), 
#     #     df1['d18O'], 
#     #     (grid_x, grid_y), 
#     #     method='linear' # 観測密度が低い場合は 'linear' が安定します
#     # )

#     # # 3. 等値線図 (contourf) の描画
#     # # vmin, vmax は既存の設定 に合わせます
#     # levels = np.linspace(-1.5, 1.0, 26)
#     # ax_cmap = ax.contourf(
#     #     grid_x, grid_y, grid_z, 
#     #     levels=levels, 
#     #     cmap='jet', 
#     #     extend='both', 
#     #     transform=ccrs.PlateCarree(),
#     #     alpha=0.8
#     # )

#     # # (オプション) 実際の観測地点を小さな黒点で重ねる（データの出所がわかって便利です）
#     # ax.scatter(df1["Longitude_degE"], df1["Latitude_degN"], c='black', s=2, alpha=0.3, transform=ccrs.PlateCarree())
    
#     # # --- ここまで書き換え ---
    
#     ####################################################################################################################################################
    
    
    
    
    
#     ####################################################################################################################################################
    
#     #緯度経度と水深とTransectで制限
#     # df1 = df
    
    
    
    
    
    
    
#     # # print(df.dtypes)
    
#     # #描画
#     # ax_cmap = ax.scatter(df1["Longitude_degE"], df1["Latitude_degN"], c=df1['d18O'],cmap='jet', s=10, alpha=0.7, vmin=-1.5, vmax=1, transform=ccrs.PlateCarree())
    
    
#     # #カラーバーの位置調整
#     # from mpl_toolkits.axes_grid1.inset_locator import inset_axes
#     # axins1 = inset_axes(ax,
#     #                    width="50%",  # width = 10% of parent_bbox width
#     #                    height="2%",  # height : 50%
#     #                    loc='lower right',
#     #                    bbox_to_anchor=(-0.02, 0.1, 1, -0.7),
#     #                    bbox_transform=ax.transAxes,
#     #                    )
    
    
#     # fig.colorbar(ax_cmap, shrink=0.65, cax=axins1,orientation='horizontal',label=r"$\delta^{18}$O"+' (VSMOW)')
    
#     # # ax.set_title('title', fontsize=20)
#     # # ax.set_title(selected_area, fontsize=20) #Transectでソートした場合
    
#     # st.pyplot(fig)
    
    
    
#     ax_cmap = ax.scatter(df1["Longitude_degE"], df1["Latitude_degN"], c=df1['d18O'],cmap='jet', s=10, alpha=0.7, vmin=sld_d18O_min, vmax=sld_d18O_max, transform=ccrs.PlateCarree())
    
    

    
# # =============================================================================
# #     2023/07/22ここから不具合　修正
# # =============================================================================

    
#     # カラーバーの位置調整
#     # from mpl_toolkits.axes_grid1.inset_locator import inset_axes
#     # axins1 = inset_axes(ax,
#     #                     width="50%",  # width = 10% of parent_bbox width
#     #                     height="2%",  # height : 50%
#     #                     loc='lower right',
#     #                     bbox_to_anchor=(-0.02, 0.1, 1, -0.7),
#     #                     bbox_transform=ax.transAxes,
#     #                     )
#     # fig.colorbar(ax_cmap, shrink=0.65, cax=axins1,orientation='horizontal',label=r"$\delta^{18}$O"+' (VSMOW)')
    
    
    
#     # cax = fig.add_axes((0.47, 0.19, 0.25, 0.015))
    
#     # fig.colorbar(ax_cmap, shrink=0.2, orientation='horizontal',label=r"$\delta^{18}$O"+' (VSMOW)',cax=cax)
    
    
#     # --- 修正後のカラーバー配置 ---
#     from mpl_toolkits.axes_grid1 import make_axes_locatable
    
#     # カラーバーを配置するための軸（cax）を、メインの軸（ax）に紐づけて作成
#     divider = make_axes_locatable(ax)
#     # size="3%" はカラーバーの太さ、pad=0.5 は図からの距離
#     # axes_class に plt.Axes を指定するのが Cartopy と共存させるコツです
#     cax = divider.append_axes("bottom", size="3%", pad=0.6, axes_class=plt.Axes)
    
#     # カラーバーの描画
#     fig.colorbar(
#         ax_cmap, 
#         cax=cax, 
#         orientation='horizontal', 
#         label=r"$\delta^{18}$O (VSMOW)"
#     )
#     # --- 修正ここまで ---
    
    
    

# # =============================================================================
# # 　2023/07/22ここまで不具合 修正
# # =============================================================================
    
#     # ax.set_title('title', fontsize=20)
#     # ax.set_title(selected_area, fontsize=20) #Transectでソートした場合
    
    
#     #全体のタイトル名　　手入力
#     main_title = fig_title
#     sub_title = 'Lon:'+str(sld_lon_min)+'-'+str(sld_lon_max)+', Lat:'+str(sld_lat_min)+'-'+str(sld_lat_max)+', Y:'+str(sld_year_min)+'-'+str(sld_year_max)+', M:'+str(sld_month_min)+'-'+str(sld_month_max)+', S:'+str(sld_sal_min)+'-'+str(sld_sal_max)+', D:'+str(sld_depth_min)+'-'+str(sld_depth_max)+'m'
#     sub_title2 = ''
    
#     title_head = str(main_title+'\n'+sub_title+'\n'+sub_title2)
#     title_head2 = title_head.replace('_', ' ') #図のタイトル表示用
#     fig.suptitle(title_head2,fontsize=15)
        

    
#     # import io
#     # fn = sub_tite
#     # img = io.BytesIO()
#     # plt.savefig(img, format='png')
     
#     # btn = st.download_button(
#     #    label="Download image",
#     #    data=img,
#     #    file_name=fn,
#     #    mime="image/png")
    
    
    

    
#     #######################画像を保存するためのボタン作成########################
#     sub_title2 = sub_title
#     sub_title2 = sub_title2.replace(':', '') #pdf書き出し用
#     # sub_title2 = sub_title2.replace('>', '') #pdf書き出し用
#     # sub_title2 = sub_title2.replace('<', '') #pdf書き出し用
#     sub_title2 = sub_title2.replace(',', '_') #pdf書き出し用
#     sub_title2 = sub_title2.replace(' ', '') #pdf書き出し用
#     sub_tite = str('Fig_d18O_map'+'_'+sub_title2+".png")


    
#     #画像を保存，以下の方法だとローカルにも保存されてしまう
#     # fn = sub_tite
#     # # plt.savefig(fn)

#     # with open(fn, "rb") as img:
#     #     btn = st.download_button(
#     #         label="Download image",
#     #         data=img,
#     #         file_name=fn,
#     #         mime="image/png"
#     #     )

#     #Save to memory first. の場合は，ローカルに保存されないので安心
#     import io
#     fn = sub_tite
#     img = io.BytesIO()
#     plt.savefig(img, format='png')
     
#     btn = st.download_button(
#        label="Download image",
#        data=img,
#        file_name=fn,
#        mime="image/png"
#        )
    
    
#     st.pyplot(fig)

    
    







    ###############################################################################################
    ############################################################################################### 
    ###############################################################################################
    ###############################################################################################
    #全体のタイトル名　　手入力
    # main_title = 'DEPTH PROFILE (V02)'
    main_title = fig_title
    
    # --- 月 (スライダー用) ---  
    # sub_title = 'Lon:'+str(sld_lon_min)+'-'+str(sld_lon_max)+', Lat:'+str(sld_lat_min)+'-'+str(sld_lat_max)+', Y:'+str(sld_year_min)+'-'+str(sld_year_max)+', M:'+str(sld_month_min)+'-'+str(sld_month_max)+', S:'+str(sld_sal_min)+'-'+str(sld_sal_max)+', D:'+str(sld_depth_min)+'-'+str(sld_depth_max)+'m'
    # --- 月 (multiselect用) ---
    # 月の表示用テキストを作成（選択されたリストをカンマ区切りにする）
    month_text = ", ".join(map(str, sorted(selected_months))) if selected_months else "None"
    
    
    ### もし「月が多すぎてサブタイトルが長くなる」のが嫌な場合
  # 月の表示ロジック
    if len(selected_months) == 12:
        month_display = "All"
    elif len(selected_months) == 0:
        month_display = "None"
    else:
        # 標準機能だけで「1-3」のように短縮するロジック
        sorted_m = sorted(list(set(selected_months)))
        ranges = []
        if sorted_m:
            start = sorted_m[0]
            for i in range(len(sorted_m)):
                # 次の要素が連続していない、または最後の要素の場合に書き出し
                if i + 1 == len(sorted_m) or sorted_m[i+1] != sorted_m[i] + 1:
                    end = sorted_m[i]
                    ranges.append(f"{start}-{end}" if start != end else str(start))
                    if i + 1 < len(sorted_m):
                        start = sorted_m[i+1]
        month_display = ", ".join(ranges)
        
        

    sub_title = f"Lon:{sld_lon_min}-{sld_lon_max}, Lat:{sld_lat_min}-{sld_lat_max}, Y:{sld_year_min}-{sld_year_max}, M:{month_display}, S:{sld_sal_min}-{sld_sal_max}, D:{sld_depth_min}-{sld_depth_max}m"

    # sub_title = (
    #     f"Lon:{sld_lon_min}-{sld_lon_max}, Lat:{sld_lat_min}-{sld_lat_max}, "
    #     f"Y:{sld_year_min}-{sld_year_max}, M:[{month_text}], "
    #     f"S:{sld_sal_min}-{sld_sal_max}, D:{sld_depth_min}-{sld_depth_max}m"
    # )
    main_title2 = sub_title
    
    
    
    
    sub_title2 = ''
    
    title_head = str(main_title+'\n'+sub_title+'\n'+sub_title2)
    title_head2 = title_head.replace('_', ' ') #図のタイトル表示用

    # ファイルのタイトルを自動設定
    sub_title2 = sub_title
    sub_title2 = sub_title2.replace(':', '') #pdf書き出し用
    # sub_title2 = sub_title2.replace('>', '') #pdf書き出し用
    # sub_title2 = sub_title2.replace('<', '') #pdf書き出し用
    sub_title2 = sub_title2.replace(',', '_') #pdf書き出し用
    sub_title2 = sub_title2.replace(' ', '') #pdf書き出し用
    sub_tite = str('Fig_d18O_map'+'_'+sub_title2+".png")

    ###############################################################################################
    ############################################################################################### 
    ###############################################################################################
    ###############################################################################################


    # ==========================================================
    # Map Center Selection
    # ==========================================================
    center_option = st.radio(
        ":blue[Map Center:]",
        ("Atlantic (0°)", "Pacific (180°)"),
        horizontal=True
    )
    
    lon_center = 0 if "Atlantic" in center_option else 180
    
    def wrap_lon(lon, center):
        return (lon - center + 180) % 360 - 180 + center
    
    plt.rcParams["font.size"] = 15

    # ==========================================================
    # Scatter Map
    # ==========================================================
    fig = plt.figure(figsize=(12, 8), facecolor="white", dpi=150)
    
    ax = fig.add_subplot(
        1, 1, 1,
        projection=ccrs.PlateCarree(central_longitude=lon_center)
    )
    
    # print("map_lon_min:", map_lon_min)
    # print("map_lon_max:", map_lon_max)
    # print("map_lat_min:", map_lat_min)
    # print("map_lat_max:", map_lat_max)
    map_lon_min = max(-180, map_lon_min)
    map_lon_max = min( 180, map_lon_max)
    map_lat_min = max( -90, map_lat_min)
    map_lat_max = min(  90, map_lat_max)
    
    ax.set_extent(
        [map_lon_min, map_lon_max, map_lat_min, map_lat_max],
        crs=ccrs.PlateCarree()
    )
    
    ax.coastlines(resolution="50m", zorder=3)
    ax.add_feature(cfeature.LAND,
                   facecolor="white",
                   edgecolor="black",
                   linewidth=0.5,
                   zorder=2)
    
    ax.gridlines(draw_labels=True, zorder=4)
    
    lon_wrapped = wrap_lon(df1["Longitude_degE"].values, lon_center)
    
    ax_scatter = ax.scatter(
        lon_wrapped,
        df1["Latitude_degN"],
        c=df1["d18O"],
        cmap="jet",
        s=10,
        alpha=0.7,
        vmin=sld_d18O_min,
        vmax=sld_d18O_max,
        transform=ccrs.PlateCarree(),
        zorder=1
    )
    
    # PNG保存（Scatter）
    img_scatter = io.BytesIO()
    fig.savefig(img_scatter, format="png", dpi=300, bbox_inches="tight")
    img_scatter.seek(0)
    
    # ==========================================================
    # 補間（周期拡張オプション付き）
    # ==========================================================
    
    use_cyclic = st.checkbox(
        "Enable cyclic interpolation (dateline connection)",
        value=False
    )
    
    lon_original = df1["Longitude_degE"].values
    lat_vals     = df1["Latitude_degN"].values
    val          = df1["d18O"].values
    
    # ==========================================================
    # ★ データ拡張（必要なときだけ）
    # ==========================================================
    
    if use_cyclic and lon_center == 180:
        lon_ext = np.concatenate([lon_original,
                                  lon_original - 360,
                                  lon_original + 360])
        lat_ext = np.concatenate([lat_vals, lat_vals, lat_vals])
        val_ext = np.concatenate([val, val, val])
    else:
        lon_ext = lon_original
        lat_ext = lat_vals
        val_ext = val
    
    # ---- グリッド ----
    grid_lon = np.linspace(-180, 180, 360)
    grid_lat = np.linspace(map_lat_min, map_lat_max, 250)
    
    X, Y = np.meshgrid(grid_lon, grid_lat)
    
    # ---- 補間 ----
    Z = griddata(
        (lon_ext, lat_ext),
        val_ext,
        (X, Y),
        method="linear"
    )
    
    Z = np.ma.masked_invalid(Z)
    
    # ==========================================================
    # ★ cyclic point（これも必要なときだけ）
    # ==========================================================
    
    if use_cyclic and lon_center == 180:
        from cartopy.util import add_cyclic_point
        Z_plot, lon_plot = add_cyclic_point(Z, coord=grid_lon)
    else:
        Z_plot = Z
        lon_plot = grid_lon
        
    # ==========================================================
    # Contour Map Figure 作成
    # ==========================================================
    fig_contour = plt.figure(figsize=(12, 8), facecolor="white", dpi=150)
    
    ax2 = fig_contour.add_subplot(
        1, 1, 1,
        projection=ccrs.PlateCarree(central_longitude=lon_center)
    )
    
    # extent
    ax2.set_extent(
        [map_lon_min, map_lon_max, map_lat_min, map_lat_max],
        crs=ccrs.PlateCarree()
        )   
    # ==========================================================
    # 描画
    # ==========================================================
    
    levels = np.linspace(sld_d18O_min, sld_d18O_max, 51)
    
    ax_cntr = ax2.contourf(
        lon_plot,
        grid_lat,
        Z_plot,
        levels=levels,
        cmap="jet",
        extend="both",
        transform=ccrs.PlateCarree(),
        alpha=0.85,
        zorder=1
    )
    
    ax2.add_feature(
        cfeature.LAND,
        facecolor="white",
        edgecolor="black",
        linewidth=0.5,
        zorder=2
    )
    
    ax2.coastlines(resolution="50m", zorder=3)
    ax2.gridlines(draw_labels=True, zorder=4)
    
    # ---- 観測点（表示用はwrap）----
    lon_wrapped = wrap_lon(lon_original, lon_center)
    
    ax2.scatter(
        lon_wrapped,
        lat_vals,
        c="black",
        s=2,
        alpha=0.3,
        transform=ccrs.PlateCarree(),
        zorder=5
    )
    
    # ---- カラーバー（Cartopy安全版）----
    cbar = fig_contour.colorbar(
        ax_cntr,
        ax=ax2,
        orientation="horizontal",
        pad=0.05,
        fraction=0.05
    )
    cbar.set_label(r"$\delta^{18}$O (VSMOW)")
    
    # ---- PNG保存 ----
    img_contour = io.BytesIO()
    fig_contour.savefig(img_contour, format="png", dpi=300, bbox_inches="tight")
    img_contour.seek(0)
        
    # ==========================================================
    # 表示切替
    # ==========================================================
    map_type = st.radio(
        ":blue[Map Type:]",
        ("Scatter Map", "Contour Map"),
        horizontal=True
    )
    
    if map_type == "Scatter Map":
        st.download_button(
            "Download Scatter Map",
            img_scatter,
            f"Fig_d18O_scatter_{sub_title2}_center{lon_center}.png",
            "image/png"
        )
        st.pyplot(fig)
    
    else:
        st.download_button(
            "Download Contour Map",
            img_contour,
            f"Fig_d18O_contour_{sub_title2}_center{lon_center}.png",
            "image/png"
        )
        st.pyplot(fig_contour)


    ###############################################################################################
    ############################################################################################### 
    ###############################################################################################
    ###############################################################################################
    
    # # --- 図の共通設定とライブラリの追加 ---
    # from mpl_toolkits.axes_grid1 import make_axes_locatable
    # from scipy.interpolate import griddata
    # import cartopy.feature as cfeature
    # import io

    # # フォントサイズの一致
    # plt.rcParams["font.size"] = 15

    # # =============================================================================
    # # 図1：散布図（既存のプロットマップ）
    # # =============================================================================
    # st.write(":blue[--- Scatter Plot Map ---]")
    # fig = plt.figure(figsize=(12, 8), facecolor="white", dpi=150, tight_layout=False)
    # ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    
    # ax.set_xlim([map_lon_min, map_lon_max])
    # ax.set_ylim([map_lat_min, map_lat_max])
    
    # # 陸地の白抜きと海岸線
    # ax.add_feature(cfeature.LAND, facecolor='white', edgecolor='black', linewidth=0.5, zorder=2)
    # ax.coastlines(resolution='50m', zorder=3)
    # ax.gridlines(draw_labels=True, zorder=4)

    # # 散布図の描画
    # ax_cmap = ax.scatter(df1["Longitude_degE"], df1["Latitude_degN"], 
    #                      c=df1['d18O'], cmap='jet', s=10, alpha=0.7, 
    #                      vmin=sld_d18O_min, vmax=sld_d18O_max, transform=ccrs.PlateCarree(), zorder=1)

    # # カラーバーを自動的に図の下に配置
    # divider = make_axes_locatable(ax)
    # cax = divider.append_axes("bottom", size="5%", pad=0.5, axes_class=plt.Axes)
    # fig.colorbar(ax_cmap, cax=cax, orientation='horizontal', label=r"$\delta^{18}$O (VSMOW)")

    # # タイトル設定
    # main_title = r'SEAWATER $\delta^{18}$O MAP WEB (Scatter)'
    # sub_title = f'Lon:{sld_lon_min}-{sld_lon_max}, Lat:{sld_lat_min}-{sld_lat_max}, Y:{sld_year_min}-{sld_year_max}, D:{sld_depth_min}-{sld_depth_max}m'
    # title_head2 = main_title + '\n' + sub_title
    # fig.suptitle(title_head2, fontsize=15)

    # # 保存用バイナリ
    # fn_scatter = f"Fig_d18O_scatter_{sub_title2}.png"
    # img_scatter = io.BytesIO()
    # fig.savefig(img_scatter, format='png')
    # st.download_button(label="Download Scatter Map Image", data=img_scatter, file_name=fn_scatter, mime="image/png")
    
    # st.pyplot(fig)


    # # =============================================================================
    # # 図2：詳細コンターマップ（高解像度・滑らか補完）
    # # =============================================================================
    # st.write("---")
    # st.write(":blue[--- Detailed Interpolated Contour Map ---]")
    
    # fig_contour = plt.figure(figsize=(12, 8), facecolor="white", dpi=150, tight_layout=False)
    # ax2 = fig_contour.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    
    # ax2.set_xlim([map_lon_min, map_lon_max])
    # ax2.set_ylim([map_lat_min, map_lat_max])

    # # 1. 高詳細な補完計算
    # # グリッド解像度を 500x500 に向上
    # grid_lon = np.linspace(map_lon_min, map_lon_max, 500)
    # grid_lat = np.linspace(map_lat_min, map_lat_max, 500)
    # X, Y = np.meshgrid(grid_lon, grid_lat)
    
    # # method='cubic' を使用して、点間を滑らかな曲線で補完
    # Z = griddata(
    #     (df1["Longitude_degE"], df1["Latitude_degN"]), 
    #     df1['d18O'], 
    #     (X, Y), 
    #     method='linear'
    # )

    # # 2. 等値線図 (contourf) の描画 (zorder=1)
    # # 階調を 51段階に増やして滑らかに
    # # levels = np.linspace(-1.5, 1.0, 51)
    # levels = np.linspace(sld_d18O_min, sld_d18O_max, 51)
    # ax_cntr = ax2.contourf(X, Y, Z, levels=levels, cmap='jet', extend='both', 
    #                        transform=ccrs.PlateCarree(), alpha=0.8, zorder=1)
    
    # # 補助的な境界線 (contour) を追加して詳細さを強調
    # # line_levels = np.linspace(-1.5, 1.0, 51)
    # line_levels = np.linspace(sld_d18O_min, sld_d18O_max, 51)
    # ax2.contour(X, Y, Z, levels=line_levels, colors='black', linewidths=0.2, 
    #             alpha=0.4, transform=ccrs.PlateCarree(), zorder=1)

    # # 3. 陸地の白抜き (zorder=2)
    # ax2.add_feature(cfeature.LAND, facecolor='white', edgecolor='black', linewidth=0.5, zorder=2)

    # # 4. 海岸線とグリッド (zorder=3, 4)
    # ax2.coastlines(resolution='50m', zorder=3)
    # ax2.gridlines(draw_labels=True, zorder=4)

    # # 5. 実際の観測地点を点として薄く重ねる (zorder=5)
    # ax2.scatter(df1["Longitude_degE"], df1["Latitude_degN"], c='black', s=2, alpha=0.3, transform=ccrs.PlateCarree(), zorder=5)

    # # 6. カラーバーの自動配置
    # divider2 = make_axes_locatable(ax2)
    # cax2 = divider2.append_axes("bottom", size="5%", pad=0.5, axes_class=plt.Axes)
    # fig_contour.colorbar(ax_cntr, cax=cax2, orientation='horizontal', label=r"$\delta^{18}$O (VSMOW)")

    # # タイトル設定（Scatter を Interpolated に置換）
    # title_contour = title_head2.replace('(Scatter)', '(Detailed Interpolated)')
    # fig_contour.suptitle(title_contour, fontsize=15)

    # # 保存用バイナリ
    # fn_contour = f"Fig_d18O_contour_{sub_title2}.png"
    # img_contour = io.BytesIO()
    # fig_contour.savefig(img_contour, format='png')
    # st.download_button(label="Download Contour Map Image", data=img_contour, file_name=fn_contour, mime="image/png")

    # st.pyplot(fig_contour)
    
    # # --- 以下、既存の Plotly や DataFrame 表示へ続く ---



    ###############################################################################################
    ############################################################################################### 
    ###############################################################################################
    ###############################################################################################





    ###############################################################################################
    ############################################################################################### 
    ###############################################################################################
    ###############################################################################################



  
    
    # ##########採取地点のmap　拡大可能##################
    
    # df1['lat'] = df1['Latitude_degN']
    # df1['lon'] = df1 ['Longitude_degE']
    
    # # df = pd.DataFrame(
    # #     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    # #     columns=['lat', 'lon'])
    
    # st.map(df1)


    ##########採取地点のmap　その２　拡大可能##################
    
    ###############################################################################################
    ############################################################################################### 
    ###############################################################################################
    ###############################################################################################

    import plotly.express as px

    fig = px.scatter_mapbox(df1, lat="Latitude_degN", lon="Longitude_degE", zoom=3,
                            # color='Month',
                            hover_data=["d18O",'dD',"Salinity",'Temperature_degC','Date','Cruise','Station','Depth_m', 'reference'],
                            opacity=0.4,
                            )
    
    
    
    
    # # fig.update_layout(mapbox_style="open-street-map")
    # fig.update_layout(mapbox_style="carto-positron")
    # fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    


    # # 地図を表示    
    # # ID重複を割けるために，Keyを追加。　修正後（一意のキーを追加）　
    # # マウスホイールでのズームが強制的に有効
    # st.plotly_chart(
    #     fig, 
    #     use_container_width=True, # クラウドではTrueの方が見やすいです
    #     key="3d_visualizer_map_d18O",
    #     config={'scrollZoom': True, 'displayModeBar': True} # ズームを有効化
    # )
    

    ###############################################################################################
    ###############################################################################################
    ###############################################################################################
    ###############################################################################################


    # 選択されたデータの地点プロット
    # --- 採取地点の地図表示 (Auto-Zoom & 幅広設定) ---
    st.divider()
    st.subheader('Location Map (Auto-Zoom)')

    import math

    # 1. 地図背景の選択
    map_mode = st.radio(
        "Map Style:", 
        ["Standard", "Satellite", "Bathymetry (Sea)", "Contour (GSI)"], 
        horizontal=True,
        key="map_style_31_auto"
    )

 # 2. データの範囲から中心座標とズームレベルを計算
    lat_min, lat_max = df1["Latitude_degN"].min(), df1["Latitude_degN"].max()
    lon_min, lon_max = df1["Longitude_degE"].min(), df1["Longitude_degE"].max()

    # 初期値（日本）の設定
    default_lat, default_lon, default_zoom = 36.0, 138.0, 4.0

    # --- 判定と計算を一本化 ---
    if pd.isna(lat_min) or pd.isna(lon_min):
        # 【抽出前】データがない場合は日本を中心に固定
        center_lat, center_lon, auto_zoom = default_lat, default_lon, default_zoom
    else:
        # 【抽出後】データがある場合
        center_lat = (lat_min + lat_max) / 2
        center_lon = (lon_min + lon_max) / 2
        
        lat_diff = max(lat_max - lat_min, 0.1)
        lon_diff = max(lon_max - lon_min, 0.1)
        
        # 03番準拠のピクセル計算
        map_width_px, map_height_px = 1200, 700
        zoom_lon = math.log2((map_width_px * 360) / (lon_diff * 256))
        zoom_lat = math.log2((map_height_px * 180) / (lat_diff * 256))
        
        # 東西に広範囲な場合に全プロットを収めるため、マージンを少し多めに引く (-1.8)
        # この 1.5 を 1.8 や 2.0 にすると、さらに一歩「引いた」視点になります。
        auto_zoom = min(zoom_lon, zoom_lat) - 2.0
        auto_zoom = max(1, min(15, auto_zoom))

        # もしデータが世界規模（100度以上）に広がっているなら、日本中心の引きの絵にする
        if lon_diff > 100:
              center_lat, center_lon, auto_zoom = default_lat, default_lon, 1.5
    
    
    
    
    # 03番と同じピクセル基準の計算
    map_width_px = 1200  # ここを大きく設定することで、計算上のズームを最適化します
    map_height_px = 700
    zoom_lon = math.log2((map_width_px * 360) / (lon_diff * 256))
    zoom_lat = math.log2((map_height_px * 180) / (lat_diff * 256))
    
    auto_zoom = min(zoom_lon, zoom_lat) - 1.5
    auto_zoom = max(1, min(15, auto_zoom))

    # 3. 地図の作成 (px.scatter_mapbox内ではwidthを指定しない)
    c_scale_d18o = envgeo_utils.get_custom_colorscale("d18O")

    fig_map = px.scatter_mapbox(
        df1, 
        lat="Latitude_degN", 
        lon="Longitude_degE",
        color="d18O", 
        color_continuous_scale=c_scale_d18o,
        #############################ポップアップ情報ここから##########################
        hover_data={
            "Latitude_degN": True,  # 名前を表示
            "Longitude_degE": True,  # 値を表示
            "d18O": True, 
            "dD": True, 
            "Salinity": True, 
            "Temperature_degC": True, 
            "Year": True, 
            "Month": True, 
            "Day": True, 
            "Cruise": True, 
            "Station": True,
            "Depth_m": True,
            "reference": True,  # カテゴリを表示
            # "x": False,  # X座標はツールチップから除外
            # "y": False  # Y座標はツールチップから除外
        },
        #############################ポップアップ情報ここまで##########################
        opacity=0.6,
        height=500  # 高さはここで固定
    )

    # 4. 背景スタイルの適用
    fig_map = envgeo_utils.apply_map_style(fig_map, map_mode)
    
    

    

    # 5. レイアウト設定 (ここが幅を広げる決め手)
    fig_map.update_layout(
        mapbox=dict(
            center=dict(lat=center_lat, lon=center_lon),
            zoom=auto_zoom
        ),
        margin=dict(l=0, r=0, t=0, b=0),
        # widthを指定せず autosize を True にすることで、コンテナいっぱいに広がる
        autosize=True, 
        coloraxis_colorbar=dict(
            title="δ18O (‰)",
            x=1.0,           # カラーバーを右端に寄せる
            xanchor='right'
        )
    )

    # 6. 表示 (use_container_width=True を確実に使う)
    # ID重複を割けるために，Keyを追加。　修正後（一意のキーを追加）　
    # マウスホイールでのズームが強制的に有効
    st.plotly_chart(
        fig_map, 
        use_container_width=True, # クラウドではTrueの方が見やすいです
        key="d18O_map",
        config={'scrollZoom': True, 'displayModeBar': True} # ズームを有効化
    )






    ###############################################################################################
    ###############################################################################################
    ###############################################################################################
    ###############################################################################################

    ##選ばれたデータを表示
    # 例：特定の列だけを選択して新しいデータフレームを作成
    
    # with表記 (推奨)
    # with st.expander("selected dataset (CSV)", expanded=False):
                
    #     df1_table = df1[['reference','Cruise', 'Station', 'Date', 'Longitude_degE', 'Latitude_degN', 'Depth_m', 'Temperature_degC', 'Salinity', 'd18O', 'dD']]

    #     st.dataframe(df1_table)    
        
    with st.expander("selected dataset (CSV)", expanded=False):
        df1_table = df1[['reference','Cruise', 'Station', 'Date', 'Longitude_degE', 'Latitude_degN', 'Depth_m', 'Temperature_degC', 'Salinity', 'd18O', 'dD']].copy()        
        # 【重要】表示直前に全列を文字列化（これでArrowエラーは100%消えます）
        df1_table = df1_table.astype(str) 
        
        # 最新の width='stretch' を使用
        st.dataframe(df1_table, use_container_width=True)
    
    ###############################################################################################
    ###############################################################################################
    ###############################################################################################
    ###############################################################################################
    
    ###############################################################################################
    ############################################################################################### 
    ###############################################################################################
    ###############################################################################################

if __name__ == '__main__':
    main()
    
    
