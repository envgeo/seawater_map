#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 17:15:03 2023
@author: Toyoho Ishimura @Kuoto-U
2026/02/10 update 
"""

#2026/02/25現在，excelとenvgeo_utilsが専用のになってる。
#エクセルは入れ替えても問題なしなので，全部といつしても良いかも
#さらにsheet1に全て統一可能，行挿入スクリプトを使えばOK

# --- バージョン管理の設定 ---
version = "2.08d" #2026/02/21
fig_title = "envgeo-seawater-database"  # 2026/02/12
    
    


import streamlit as st
import pandas as pd
import numpy as np
import envgeo_utils  # 作った設定ファイルを読み込む

print((f"--------17_depth_d18O_Temperature_({version})--------"))
# datetimeモジュールを使った現在の日付と時刻の取得
import datetime
dt = datetime.datetime.today()  # ローカルな現在の日付と時刻を取得
print(dt)  # 2021-10-29 15:58:08.356501


    
    
    
import matplotlib.pyplot as plt
# import pandas as pd
# import datetime
# import matplotlib.dates as dates
from matplotlib.ticker import FormatStrFormatter
# from matplotlib.ticker import MultipleLocator
# import matplotlib.ticker as ticker
# import cartopy.crs as ccrs
# import seaborn as sns
# from sklearn.metrics import mean_squared_error
# from sklearn.metrics import r2_score









def main():
    
    # タイトル
    st.header(f'Depth profile ({version})')
    
    # リロードボタン
    st.button('Reload')
    
    
    
    
    
    #################ソース選択・要素選択###########################################
    
    ##############################################################################
    # --- 1. データソースのラジオボタン ---   
    ##############################################################################


    # データソースの変数、envgeo_utilsから読み出す
    data_source_JAPAN_SEA = envgeo_utils.data_source_JAPAN_SEA
    data_source_AROUND_JAPAN = envgeo_utils.data_source_AROUND_JAPAN
    data_source_GLOBAL = envgeo_utils.data_source_GLOBAL
   

    # データソース選択
    # ref_data = st.radio("data source (see home>about):", (data_source_JAPAN_SEA, data_source_AROUND_JAPAN), horizontal=True, args=[1, 0])

   
    # データソース選択 NASA入り
    ref_data = st.radio("data source (see home>about):", (data_source_JAPAN_SEA, data_source_AROUND_JAPAN, data_source_GLOBAL), horizontal=True, args=[1, 0])


    ##############################################################################
    # --- 2. 文献の表示　---　　 
    ##############################################################################


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
        
        

    ##############################################################################
    # --- 3. プロットの選択　---　　 
    ##############################################################################



    col1, col2 = st.columns([1,1])
    with col1:
        plot_all_data = st.radio("Plot all data on the background as gray line:", ("YES", "NO"), horizontal=True, args=[1, 0])
    
    with col2:
        plot_element = st.radio("Target Parameter:", ("d18O(VSMOW)", "Temperature (°C)", "Salinity"), horizontal=True, args=[1, 0])

    

        
    if plot_element == "d18O(VSMOW)":
        #水深-d18Oの時
        X_data = "d18O"
        Y_data = "Depth_m"
        
        
        # """XYの表示用のラベルを指定"""
        X_label = r"$\delta^{18}$O"
        Y_label = "water depth (m)"
        
        
        # """XYの表示用のラベルのスケールを指定"""
        iso_scale_X = "(VSMOW)"
        iso_scale_Y = ""
     
        #水深-d18Oの時
        # lim_min_X = -1.4
        # lim_max_X = 0.6
        
        # 海域別の初期値設定
        if ref_data == data_source_GLOBAL:
            fig_x_min, fig_x_max = -20.0, 4.0  # GLOBALは幅を広く
        elif ref_data == data_source_JAPAN_SEA:
            fig_x_min, fig_x_max = -1.4, 0.6  # 日本海はズーム
        else:
            fig_x_min, fig_x_max = -1.4, 0.6  # Around JAPAN(標準)

     
    elif plot_element == "Temperature (°C)":
        #水深-水温の時
        X_data = "Temperature_degC"
        Y_data = "Depth_m"
        
        # """XYの表示用のラベルを指定"""
        X_label = "Temperature(°C)"
        Y_label = "water depth (m)"
        
        # """XYの表示用のラベルのスケールを指定"""
        iso_scale_X = ""
        iso_scale_Y = ""
        
    	# #水深-d18Oの時
        # lim_min_X = -2
        # lim_max_X = 30
        
        # 海域別の初期値設定
        if ref_data == data_source_GLOBAL:
            fig_x_min, fig_x_max = -3, 35  # GLOBALは幅を広く
        elif ref_data == data_source_JAPAN_SEA:
            fig_x_min, fig_x_max = -2, 30  # 日本海はズーム
        else:
            fig_x_min, fig_x_max = -2, 30  # Around JAPAN(標準)

        
    elif plot_element == "Salinity":
        #水深-塩分の時
        X_data = "Salinity"
        Y_data = "Depth_m"
        
        # """XYの表示用のラベルを指定"""
        X_label = "Salinity"
        Y_label = "water depth (m)"
        
        # """XYの表示用のラベルのスケールを指定"""
        iso_scale_X = ""
        iso_scale_Y = ""
        
    	# #水深-d18Oの時
        # lim_min_X = 28
        # lim_max_X = 36
        
        # 海域別の初期値設定
        if ref_data == data_source_GLOBAL:
            fig_x_min, fig_x_max = 0, 40  # GLOBALは幅を広く
        elif ref_data == data_source_JAPAN_SEA:
            fig_x_min, fig_x_max = 28, 36  # 日本海はズーム
        else:
            fig_x_min, fig_x_max = 28, 36  # Around JAPAN(標準)
    
    else:()





    
######  scalebarで制御してsubmitする場合 ################

    with st.sidebar.form("parameter", clear_on_submit=False):
        
        st.header('select parameters ➡ submit')
        
        
        
        
        #################文献選択ここから###########################################
        
        
        # st.subheader('data source:')
        
        # ref_data = st.radio("data source (see home>about):", (data_source_JAPAN_SEA, data_source_AROUND_JAPAN), horizontal=True, args=[1, 0])
        
        if ref_data == data_source_JAPAN_SEA:
            ############論文データ追加用の設定############
            #　足りなくなれば追加で，
            Transect001 = 'Pacific'
            Transect002 = 'Pacific_west'
            Transect003 = 'Noto'
            Transect004 = 'Toyama'
            Transect005 = 'SI'
            Transect006 = 'Yamato'
            Transect007 = 'Shimane&Tottori'
            Transect008 = 'NA2'
            Transect009 = 'Tsushima'							  
            Transect010 = 'nECS'						  
            Transect011 = 'CK'						  
            Transect012 = 'ECS2021'							  
            Transect013 = 'sECS'					  
            Transect014 = 'Nansei'
            # Transect015 = ''
            # Transect016 = ''
            # Transect017 = ''
            # Transect018 = ''
            # Transect019 = ''
            # Transect020 = 'ここの新規項目を入力'
            # Transect021 = 'ここの新規項目を入力'
            # Transect022 = 'ここの新規項目を入力'
            # Transect023 = 'ここの新規項目を入力'
            # Transect024 = 'ここの新規項目を入力'
            # Transect025 = 'ここの新規項目を入力'
            # Transect026 = 'ここの新規項目を入力'
            # Transect027 = 'ここの新規項目を入力'
            # Transect028 = 'ここの新規項目を入力'
            # Transect029 = 'ここの新規項目を入力'
            # Transect030 = 'ここの新規項目を入力'
        elif ref_data == data_source_AROUND_JAPAN:
            ############論文データ追加用の設定############
            #　足りなくなれば追加で，
            Transect001 = 'Pacific'
            Transect002 = 'Pacific_west'
            Transect003 = 'Noto'
            Transect004 = 'Toyama'
            Transect005 = 'SI'
            Transect006 = 'Yamato'
            Transect007 = 'Shimane&Tottori'
            Transect008 = 'NA2'
            Transect009 = 'Tsushima'							  
            Transect010 = 'nECS'						  
            Transect011 = 'CK'						  
            Transect012 = 'ECS2021'							  
            Transect013 = 'sECS'					  
            Transect014 = 'Nansei'
            # Transect015 = 'KUWANO'
            Transect016 = 'Yamamoto_2001'
            Transect017 = 'Sakamoto_2019'
            Transect018 = 'Kodaira_2016'
            Transect019 = 'Horikawa_2023'
            # Transect020 = 'ここの新規項目を入力'
            # Transect021 = 'ここの新規項目を入力'
            # Transect022 = 'ここの新規項目を入力'
            # Transect023 = 'ここの新規項目を入力'
            # Transect024 = 'ここの新規項目を入力'
            # Transect025 = 'ここの新規項目を入力'
            # Transect026 = 'ここの新規項目を入力'
            # Transect027 = 'ここの新規項目を入力'
            # Transect028 = 'ここの新規項目を入力'
            # Transect029 = 'ここの新規項目を入力'
            # Transect030 = 'ここの新規項目を入力'
        
        
        else:
            Transect000 = 'NASA_database'
            Transect001 = 'Pacific'
            Transect002 = 'Pacific_west'
            Transect003 = 'Noto'
            Transect004 = 'Toyama'
            Transect005 = 'SI'
            Transect006 = 'Yamato'
            Transect007 = 'Shimane&Tottori'
            Transect008 = 'NA2'
            Transect009 = 'Tsushima'							  
            Transect010 = 'nECS'						  
            Transect011 = 'CK'						  
            Transect012 = 'ECS2021'							  
            Transect013 = 'sECS'					  
            Transect014 = 'Nansei'
            # Transect015 = 'KUWANO'
            Transect016 = 'Yamamoto_2001'
            Transect017 = 'Sakamoto_2019'
            Transect018 = 'Kodaira_2016'
            Transect019 = 'Horikawa_2023'
            # Transect020 = 'ここの新規項目を入力'
            # Transect021 = 'ここの新規項目を入力'
            # Transect022 = 'ここの新規項目を入力'
            # Transect023 = 'ここの新規項目を入力'
            # Transect024 = 'ここの新規項目を入力'
            # Transect025 = 'ここの新規項目を入力'
            # Transect026 = 'ここの新規項目を入力'
            # Transect027 = 'ここの新規項目を入力'
            # Transect028 = 'ここの新規項目を入力'
            # Transect029 = 'ここの新規項目を入力'
            # Transect030 = 'ここの新規項目を入力'
        
        #################文献選択ここまで###########################################
        
        
        
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
        
        
        
    
    
        
    
        # country=st.sidebar.text_input('国を入力', 'Japan')
        # year=st.sidebar.number_input('年(1952~5年おき)',1952,2007,1952,step=5)
    
    
        #スペース入れる
    
    
        #年の範囲       # サブレベルヘッダ
        # st.sidebar.subheader('年の範囲')
        
        sld_year_min, sld_year_max = st.slider(label='Year selected',
                                    min_value=1960,
                                    max_value=2028,
                                    value=(1960, 2028),
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
                                    min_value=0,
                                    max_value=40,
                                    value=(0, 40),
                                    )
        # st.sidebar.write(f'Selected: {sld_sal_min} ~ {sld_sal_max}')
        
            
           
        # st.sidebar.subheader('航海区の範囲')
        if ref_data == data_source_JAPAN_SEA:
            selected_cruise = st.multiselect('Choose cruise area',
                                        [
                                           Transect001,
                                           Transect002,
                                           Transect003,
                                           Transect004,
                                           Transect005,
                                           Transect006,
                                           Transect007,
                                           Transect008,
                                           Transect009,
                                           Transect010,
                                           Transect011,
                                           Transect012,
                                           Transect013,
                                           Transect014,
                                         ],
                                       default=(
                                           Transect001,
                                           Transect002,
                                           Transect003,
                                           Transect004,
                                           Transect005,
                                           Transect006,
                                           Transect007,
                                           Transect008,
                                           Transect009,
                                           Transect010,
                                           Transect011,
                                           Transect012,
                                           Transect013,
                                           Transect014,
                                                   ))

        elif ref_data == data_source_AROUND_JAPAN:
                selected_cruise = st.multiselect('Choose cruise area',
                                            [
                                               Transect001,
                                               Transect002,
                                               Transect003,
                                               Transect004,
                                               Transect005,
                                               Transect006,
                                               Transect007,
                                               Transect008,
                                               Transect009,
                                               Transect010,
                                               Transect011,
                                               Transect012,
                                               Transect013,
                                               Transect014,
                                                # Transect015,
                                                Transect016,
                                                Transect017,
                                                Transect018,
                                                Transect019,
                                               # Transect020,
                                               # Transect021,
                                               # Transect022,
                                               # Transect023,
                                               # Transect024,
                                               # Transect025,
                                               # Transect026,
                                               # Transect027,
                                               # Transect028,
                                               # Transect029,
                                               # Transect030,
                                             ],
                                           default=(
                                               Transect001,
                                               Transect002,
                                               Transect003,
                                               Transect004,
                                               Transect005,
                                               Transect006,
                                               Transect007,
                                               Transect008,
                                               Transect009,
                                               Transect010,
                                               Transect011,
                                               Transect012,
                                               Transect013,
                                               Transect014,
                                                # Transect015,
                                                Transect016,
                                                Transect017,
                                                Transect018,
                                                Transect019,
                                               # Transect020,
                                               # Transect021,
                                               # Transect022,
                                               # Transect023,
                                               # Transect024,
                                               # Transect025,
                                               # Transect026,
                                               # Transect027,
                                               # Transect028,
                                               # Transect029,
                                               # Transect030,
                                                       ))
        else:
            selected_cruise = st.multiselect('Choose cruise area',
                                            [
                                                Transect000,
                                               Transect001,
                                               Transect002,
                                               Transect003,
                                               Transect004,
                                               Transect005,
                                               Transect006,
                                               Transect007,
                                               Transect008,
                                               Transect009,
                                               Transect010,
                                               Transect011,
                                               Transect012,
                                               Transect013,
                                               Transect014,
                                                # Transect015,
                                                Transect016,
                                                Transect017,
                                                Transect018,
                                                Transect019,
                                               # Transect020,
                                               # Transect021,
                                               # Transect022,
                                               # Transect023,
                                               # Transect024,
                                               # Transect025,
                                               # Transect026,
                                               # Transect027,
                                               # Transect028,
                                               # Transect029,
                                               # Transect030,
                                             ],
                                           default=(
                                               Transect000,
                                               Transect001,
                                               Transect002,
                                               Transect003,
                                               Transect004,
                                               Transect005,
                                               Transect006,
                                               Transect007,
                                               Transect008,
                                               Transect009,
                                               Transect010,
                                               Transect011,
                                               Transect012,
                                               Transect013,
                                               Transect014,
                                                # Transect015,
                                                Transect016,
                                                Transect017,
                                                Transect018,
                                                Transect019,
                                               # Transect020,
                                               # Transect021,
                                               # Transect022,
                                               # Transect023,
                                               # Transect024,
                                               # Transect025,
                                               # Transect026,
                                               # Transect027,
                                               # Transect028,
                                               # Transect029,
                                               # Transect030,
                                                       ))

        
        # st.write(f'Selected: {selected_cruise}')
        
        
        
        st.write('Cruise Area (2015-2021) in Kodama et al.(2024)')
        st.image("data/sites_20230515.gif") 
        
        
        
        
        
        
        #######################################################################
        #######################################################################   
        ###  図の調整　サイドバー
        #######################################################################        
        #######################################################################       
        
        #スペース入れる
        # st.subheader(':blue[  ]')
        # st.subheader(':blue[  ]')
        st.subheader(':blue[--- for fig scale only ---]')
        
        
        # #地図の描画範囲（拡大）
        # # 120-0.001, 145+0.001, 20-0.001, 45+0.001
        
        # # st.sidebar.subheader('地図の経度の範囲（拡大）')
        # map_lon_min, map_lon_max = st.sidebar.slider(label='Map Longitude selected',
        #                             min_value=120-0.001,
        #                             max_value=145+0.001,
        #                             value=(120-0.001, 145+0.001),
        #                             )
        # # st.sidebar.write(f'Selected: {map_lon_min} ~ {map_lon_max}')
        
        # # st.sidebar.subheader('地図の緯度の範囲（拡大）')
        # map_lat_min, map_lat_max = st.sidebar.slider(label='Map　Latitude selected',
        #                             min_value=20-0.001,
        #                             max_value=45+0.001,
        #                             value=(20-0.001, 45+0.001),
        #                             )
        # # st.sidebar.write(f'Selected: {map_lat_min} ~ {map_lat_max}')
        
        
        
        
        
        # st.sidebar.subheader('描画水深の範囲')
        if ref_data == data_source_JAPAN_SEA:
            fig_depth_min, fig_depth_max = st.slider(label='Depth scale',
                                        min_value=0,
                                        max_value=1000,
                                        value=(0, 500),
                                        )
            # st.sidebar.write(f'Selected: {fig_depth_min} ~ {fig_depth_max}')
            
        elif ref_data == data_source_AROUND_JAPAN:
            fig_depth_min, fig_depth_max = st.slider(label='Depth scale',
                                        min_value=0,
                                        max_value=3500,
                                        value=(0, 2000),
                                        )
            # st.sidebar.write(f'Selected: {fig_depth_min} ~ {fig_depth_max}')
            
        else:
            fig_depth_min, fig_depth_max = st.slider(label='Depth scale',
                                        min_value=0,
                                        max_value=9000,
                                        value=(0, 2000),
                                        )
            # st.sidebar.write(f'Selected: {fig_depth_min} ~ {fig_depth_max}')
            
        
        
        
        
        ###  作業中
        # st.sidebar.subheader('X軸の描画範囲の範囲')
        if ref_data == data_source_JAPAN_SEA:
            lim_min_X, lim_max_X = st.slider(label=f'Axis Scale for {plot_element}',
                                        min_value=-fig_x_min,
                                        max_value=fig_x_max,
                                        value=(fig_x_min, fig_x_max),
                                        )
            # st.sidebar.write(f'Selected: {fig_depth_min} ~ {fig_depth_max}')
            
        elif ref_data == data_source_AROUND_JAPAN:
            lim_min_X, lim_max_X = st.slider(label=f'Axis Scale for {plot_element}',
                                        min_value=fig_x_min,
                                        max_value=fig_x_max,
                                        value=(fig_x_min, fig_x_max),
                                        )
            # st.sidebar.write(f'Selected: {fig_depth_min} ~ {fig_depth_max}')
            
        else:
            lim_min_X, lim_max_X = st.slider(label=f'Axis Scale for {plot_element}',
                                        min_value=-fig_x_min,
                                        max_value=fig_x_max,
                                        value=(fig_x_min, fig_x_max),
                                        )
            # st.sidebar.write(f'Selected: {fig_depth_min} ~ {fig_depth_max}')
      
            
            
        ###  作業中  



            

        #図のサイズXY
        # st.sidebar.subheader('図のサイズ')
        sld_fig_size_min_X, sld_fig_size_max_Y = st.slider(label='Fig size (X vs Y)',
                                    min_value=1,
                                    max_value=40,
                                    value=(8, 12),
                                    )
        # st.sidebar.write(f'Selected: {sld_fig_size_min_X} ~ {sld_fig_size_max_Y}')
        


        #フォントサイズ
        # st.sidebar.subheader('図のサイズ')
        sld_font_size_min_S, sld_font_size_max_L = st.slider(label='Font size (scale vs label)',
                                    min_value=4,
                                    max_value=40,
                                    value=(16, 20),
                                    )
        # st.sidebar.write(f'Selected: {sld_fig_size_min_X} ~ {sld_fig_size_max_Y}')
                    
                    
        #メモリ間隔
        # st.sidebar.subheader('図のサイズ')
        tick_interval_min_X, tick_interval_max_Y = st.slider(label='Tick interval (X vs Y)',
                                    min_value=4,
                                    max_value=40,
                                    value=(11, 11),
                                    )
        # st.sidebar.write(f'Selected: {sld_fig_size_min_X} ~ {sld_fig_size_max_Y}')           
                    
                    
                    
        
        
        
                            
        submitted = st.form_submit_button(":red[submit!]")

##############################################################################
# サイドバーここまで
##############################################################################
                    
                    
                    
                    
                    
                    
                    
                    
                    ####################################################################################################################################################
    
    

                    
                    
                    ####################################################################################################################################################
                    

        
    # fig = plt.figure(figsize = (8, 12),dpi=150)
    fig = plt.figure(figsize = (sld_fig_size_min_X, sld_fig_size_max_Y),dpi=150)
    
    fig.subplots_adjust(wspace=0.3, hspace=0.3)
    
    
    #PDFに書き出すかどうか
    # PDF_export_SUB = 1
    
    
    
    #データソースによって選ぶファイルを変える
    # if ref_data == data_source_JAPAN_SEA:
    #     excel_file = 'd18O_20230513-1_NA2_2021add.xlsx'
    # else:
    #     excel_file = 'd18O_20240927_ref_YSKH.xlsx'
    
    
    # sheet_num = 2
    
    # df = pd.read_excel(excel_file, sheet_name=sheet_num)
    # df_original = envgeo_utils.load_isotope_data(ref_data, sheet_num=1)
    df_original = envgeo_utils.load_isotope_data(ref_data, sheet_num=2)  #ここがメインのシート選択　
    
    
    # """図のフォント設定、サイズも"""
    ##### ベースのフォントとフォントサイズの指定
    # plt.rcParams['font.family'] = 'Arial'
    plt.rcParams["font.size"] = 16
    
    
    
    
    
    # """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    # """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    

    

    
    # """選択描画範囲の設定用"""
    def data_limit():
    
            # sheet_num = 1
            # df1 = pd.read_excel(excel_file, sheet_name=sheet_num)
            df1 = df_original
            
            # df1 = df_fig_ALL
        
            #緯度経度と水深とTransectで制限
            # df1 = df_fig_add
            
            df1 = df1[(df1['Depth_m'] == 'xxx') 
                        
                        |(df1['Depth_m'] <= sld_depth_max) & (df1['Depth_m'] >= sld_depth_min )#調整用
                        | df1.isnull().all(axis=1)]      
              
            
            
            
                                
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
        
        
        
            # 2026/02/22以前の        
            # df1 = df1[(df1['Transect'].isin(selected_cruise))
            #            | df1.isnull().all(axis=1)]
            # #streamlitのマルチ選択用
            
            
        
            # 修正　2026/02/23
            df1 = df1[df1['Transect'].isin(selected_cruise) | df1['Transect'].isna()].copy()
                # なぜこれで青色の線のスキマが復活するのか
                # 元のデータ (df):
                # 　　「データA」→「データA」→「空白行」→「データA」
                # これまでの抽出 (df1):
                #　　 reference が「データA」のものだけを抽出した結果、「空白行」が条件に合わず消されてしまい、「データA」同士が隣り合って線が繋がってしまった
                # 新しい抽出:
                #　　| df['reference'].isna() （または reference が空であること）という条件を加えることで、「データA」の間にあった「空白行」も一緒に df1 にコピーされるようになる

                
               
    
            # if ref_data == data_source_JAPAN_SEA:
            #     df1 = df1[ (df1['Transect'] == 0) 
            #                 | (df1['Transect'] == Transect001) 
            #                 | (df1['Transect'] == Transect002)
            #                 | (df1['Transect'] == Transect003)
            #                 | (df1['Transect'] == Transect004)
            #                 | (df1['Transect'] == Transect005)
            #                 | (df1['Transect'] == Transect006)
            #                 | (df1['Transect'] == Transect007)
            #                 | (df1['Transect'] == Transect008)
            #                 | (df1['Transect'] == Transect009)
            #                 | (df1['Transect'] == Transect010)
            #                 | (df1['Transect'] == Transect011)
            #                 | (df1['Transect'] == Transect012)
            #                 | (df1['Transect'] == Transect013)
            #                 | (df1['Transect'] == Transect014)
            #                 | df1.isnull().all(axis=1)]      
            # else:
            #     df1 = df1[ (df1['Transect'] == 0) 
            #                 | (df1['Transect'] == Transect001) 
            #                 | (df1['Transect'] == Transect002)
            #                 | (df1['Transect'] == Transect003)
            #                 | (df1['Transect'] == Transect004)
            #                 | (df1['Transect'] == Transect005)
            #                 | (df1['Transect'] == Transect006)
            #                 | (df1['Transect'] == Transect007)
            #                 | (df1['Transect'] == Transect008)
            #                 | (df1['Transect'] == Transect009)
            #                 | (df1['Transect'] == Transect010)
            #                 | (df1['Transect'] == Transect011)
            #                 | (df1['Transect'] == Transect012)
            #                 | (df1['Transect'] == Transect013)
            #                 | (df1['Transect'] == Transect014)
            #                 # | (df1['Transect'] == Transect015)
            #                 | (df1['Transect'] == Transect016)
            #                 | (df1['Transect'] == Transect017)
            #                 | (df1['Transect'] == Transect018)
            #                 | (df1['Transect'] == Transect019)
            #                 # | (df1['Transect'] == Transect020)
            #                 # | (df1['Transect'] == Transect021)
            #                 # | (df1['Transect'] == Transect022)
            #                 # | (df1['Transect'] == Transect023)
            #                 # | (df1['Transect'] == Transect024)
            #                 # | (df1['Transect'] == Transect025)
            #                 # | (df1['Transect'] == Transect026)
            #                 # | (df1['Transect'] == Transect027)
            #                 # | (df1['Transect'] == Transect028)
            #                 # | (df1['Transect'] == Transect029)
            #                 # | (df1['Transect'] == Transect030)
            #                 | df1.isnull().all(axis=1)]      



            # #描画する緯度経度を指定 
            df1 = df1[(df1['Longitude_degE'] == 'xxx') 
                        
                        |(df1['Longitude_degE'] <= sld_lon_max) & (df1['Longitude_degE'] >= sld_lon_min) #調整用
                        | df1.isnull().all(axis=1)]      
              

            df1 = df1[(df1['Latitude_degN'] == 'xxx')
                        
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
                      
                        |(df1['Salinity'] >= sld_sal_min) & (df1['Salinity'] <= sld_sal_max)
                      | df1.isnull().all(axis=1)]      
            
            #描画する年範囲を指定
            df1 = df1[(df1['Year'] <= sld_year_max) & (df1['Year'] >= sld_year_min) | df1.isnull().all(axis=1)] 

            
            return df1
    
    
    
    
        
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
    
    
    # sub_title = 'Area B (N:25-130,E:135-140,D:>10m)'
    # sub_title = '(N:25-130,E:135-140,D:>10m)'
    sub_title2 = ''
    
    # title_head = 'seawater_data_(Sea_of_Japan) \n selected_area'
    title_head = str(main_title+'\n'+sub_title+'\n'+sub_title2)
    
    title_head2 = title_head.replace('_', ' ') #図のタイトル表示用
    # title_head_pdf = title_head.replace('\n', ' ') #pdf書き出し用
    fig.suptitle(title_head2,fontsize=20)
    
    
    #範囲をタイトルに入れる


    
    
    # """センタ奇病が範囲のlabel，手入力"""
    # sheet_names_add2 = "Area B (N:25-130,E:135-140,D:>10m)"
    
    # sheet_names_add2 = 'selected'
    # sheet_names_add2 =  'N:25-130,E:135-140,D:>10m'
    
    
    
    #追加でさらに特定のクルーズのみplotする場合1
    selected_add3 = 2
    selected_row2 = 'Cruise'
    selected_value = 'YK1606'
    # selected_value = 'xxx'
    
    # """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    # """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    # """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    # """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    # """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    # """top right """
    # """水深"""
    
    
    
    #####################################
    ######    EXCEL SHEET select    #####
    #####################################
    
    # """EXCELブックのシート選択、シートごとの描画色も"""
    #シート２はdepthプロファイルのみ抽出したシート
    sheet_num = [2]  #ここ必要ない，過去に複数のエクセルシート読み込んだなごり
    
    
    ######　プロットの色選択，sheet_numの順番に対応 10以上の数がある場合には色を追加 ######
    color = ["red","lime","blue","green","darkcyan","cyan","orange","yellow","fuchsia","violet","greenyellow"]
    
    # color = ["blue","blue","blue","blue","blue","blue","blue","blue","blue","blue","blue"]
    
    
    ############################################
    ######      font size line etc..       #####
    ############################################
    
    # """凡例（legend）を入れるかどうか"""
    legend = 1 #1以外だと凡例無し
    
    
    # """図のサイズと解像度"""
    # fig_size = [4,9] #図のサイズ
    # fig_dpi = 150 #図の解像度
    
    # """線の太さとマーカーのサイズ"""
    ##### 線の太さとマーカーのサイズと種類
    # lw_select = 2 #プロットラインの太さ
    # marker_select = '.' #プロットマーカーの種類，種類はweb参照
    # ms_select = 15 #プロットマーカーのサイズ
    
    #軸のメモリの長さ
    ax_length = 5
    
    #ラインとプロットの透明度
    # fig_alpha = 0.85 #不透明度、1は透過なし,0.1-1の間の数
    
    
    
    
    ########################################
    ######    SUB FIG: d13C vs d18O    #####
    ########################################
    
    
    # """XYの列を指定 エクセルシートから"""
    
    #水深-d18Oの時
    # X_data = "d18O"
    # Y_data = "Depth_m"
    
    
    
    # """XYの表示用のラベルを指定"""
    
    # X_label = r"$\delta^{18}$O"
    # Y_label = "water depth (m)"
    
    
    
    # """XYの表示用のラベルのスケールを指定"""
    
    # iso_scale_X = "(VSMOW)"
    # iso_scale_Y = ""
    
    
    
    # """作図用,色とマーカーとサイズやタイトルも"""
    
    sheet_num_XY = sheet_num #ここは変更しない
    ###### 別途，X_Yのプロットをするかどうか,色を一括にするか ######
    #する場合は1,しない場合は2
    X_Y = 1
    
    #メインプロットの設定
    X_Y_C = "gray" #色の設定
    X_Y_M = " " #現時点で色は変更設定なしマーカーの種類
    X_Y_S = 1
    
    
    #全体の回帰直線を書く場合「１」　書かない場合には「２」
    # reg_line_write = 2
    
    
    
    
    
    # 追加で強調プロットをする場合は,d13C_d18O_addを「1」しない場合は「2」　シートナンバー選択、
    X_Y_add = 1
    sheet_num_add = sheet_num
    
    
    
    # 条件抽出する場合「1」しない場合は「2」　
    fig_add_sort = 1
    selected_row = "Transect"
    
    # selected_area = 'CK'
    # selected_area = 'Nansei'
    # selected_area = 'nECS'
    # selected_area = 'Noto'
    # selected_area = 'Pacific'
    # selected_area = 'Pacific_west'
    # selected_area = 'sECS'
    # selected_area = 'Shimane&Tottori'
    # selected_area = 'SI'
    # selected_area = 'Toyama'
    # selected_area = 'Tsushima'
    # selected_area = 'Yamato'
    # selected_area = 'NA2'
    # selected_area = 'ECS2021'
    
    
    
    
    #タイトル
    fig_title_X_Y= X_label + " - "+ Y_label + "" #d13C_d18O書き出し専用
    
    #プロットの透明度
    alpha_all = 0.4 #メインプロット
    alpha_selected = 1 #強調プロット
    
    #強調プロットの色の指定
    # X_Y_C_add =  "blue" #単色にしたい場合
    X_Y_C_add_each = 1 #シート毎に塗り分けたい場合は「１」　そうでなければ「２」
    
    #個別に近似直線を引く場合「１」，引かない場合はそれ以外の数字
    # reg_line_add_write = 2
    
    
    
    #############################################
    ######      data range for SUB FIG      #####
    #############################################
    
    
    # #水深-d18Oの時
    # lim_min_X = -1.4
    # lim_max_X = 0.6
    lim_min_Y = fig_depth_max
    # lim_min_Y = 1000
    lim_max_Y = fig_depth_min
    

    
    # """------------------ここから先はさわらない！----------------------"""
    # """以下の設定は基本的に変更しない"""
    
    
    #もとのエクセルファイルのシートリストを表示
    # print()
    # sheet_all = pd.read_excel(excel_file, sheet_name=None)
    # print("選択したExcelのSheetリスト:",list(sheet_all.keys()))
    
    
    
    
    
    
    # """ここからdepth"""
    if X_Y == 1:
        # sheet_num_XY = [3,4,5,6,7,8]
        
        print('-------------SUB_FIG   d13C vs d18O-------------')
        
        # ax = plt.subplot(323)
        # fig = plt.figure()
        # grid = plt.GridSpec(3,2, wspace=0.76, hspace=0.45)
        grid = plt.GridSpec(1,1, )
        ax = fig.add_subplot(grid[0, 0])
        
        # ax.set_xlabel(X_label + iso_scale_X, fontsize=20)
        # ax.set_ylabel(Y_label + iso_scale_Y, fontsize=20)  #LateX形式で特殊文字
        
        ax.set_xlabel(X_label + iso_scale_X, fontsize=sld_font_size_max_L)
        ax.set_ylabel(Y_label + iso_scale_Y, fontsize=sld_font_size_max_L)  #LateX形式で特殊文字
    
        
        # input_sheet_name = pd.ExcelFile(excel_file).sheet_names
        # for sheet_num in sheet_num:    
        #     print("読み込まれたSheet:", [sheet_num], input_sheet_name[sheet_num])
        
        for sheet_num_XY in sheet_num_XY:
            # df_fig_ALL = pd.read_excel(excel_file, sheet_name=input_sheet_name[sheet_num_XY])
    
     #Excelファイルの読み込み
            # df_fig_ALL = pd.read_excel(excel_file, sheet_name=sheet_num_XY)
            df_fig_ALL = df_original
            
            # 特定の列に特定の変数を持つ行と空白行を残す
            # df_fig_ALL = df_fig_ALL[(df_fig_ALL[selected_row] == () | df_fig_ALL.isnull().all(axis=1)]
            # plt.plot(df_fig_ALL[X_data], df_fig_ALL[Y_data],c=X_Y_C, marker=X_Y_M, lw=0.5, alpha=alpha_all, label='ALL')
            
            if plot_all_data == "YES":
                plt.plot(df_fig_ALL[X_data], df_fig_ALL[Y_data],c=X_Y_C, marker=X_Y_M, lw=0.5, alpha=alpha_all, label='ALL')
            else:()
            
            
            #列の要素を表示
            # d_select = df_fiｇ_add[selected_row].value_counts().to_dict()
            # print('要素と出現数:', d_select)
            # print('---------------')
    
    
            plt.legend(fontsize = 16) # 凡例の数字のフォントサイズを設定
    
    
            ax.set_xlim(lim_min_X, lim_max_X) 
            ax.set_ylim(lim_min_Y, lim_max_Y) 
            # plt.tick_params(labelsize=16)
            plt.tick_params(labelsize=sld_font_size_min_S)
            # ax.set_xticks(np.linspace(lim_min_X, lim_max_X,11))
            # ax.set_yticks(np.linspace(lim_min_Y, lim_max_Y, 11))
            ax.set_xticks(np.linspace(lim_min_X, lim_max_X,tick_interval_min_X))
            ax.set_yticks(np.linspace(lim_min_Y, lim_max_Y, tick_interval_max_Y))
            
            
            

            
            if plot_element == "d18O(VSMOW)":
                ax.xaxis.set_major_formatter(FormatStrFormatter("%+.1f"))
                ax.yaxis.set_major_formatter(FormatStrFormatter("%.f"))

             
            elif plot_element == "Temperature (°C)":
                ax.xaxis.set_major_formatter(FormatStrFormatter("%.f"))
                ax.yaxis.set_major_formatter(FormatStrFormatter("%.f"))

                lim_max_X = 30

                
            elif plot_element == "Salinity":
                ax.xaxis.set_major_formatter(FormatStrFormatter("%.1f"))
                ax.yaxis.set_major_formatter(FormatStrFormatter("%.f"))

            
            else:()

                
    
            ax.tick_params(length=ax_length)
            # ax.annotate("point A", xy = (-7, 0), size = 15,
            #             color = "red", arrowprops = dict())
    
        # plt.title(fig_title_X_Y, fontsize=16) #
        plt.legend(fontsize = 20) # 凡例の数字のフォントサイズを設定
        
    
        
        #追加で強調プロットをする場合
        if X_Y_add == 1:
            # sheet_num_add = [1]
            # sheet_num_add = [2,3]
            for sheet_num_add in sheet_num_add:    
        
                if X_Y_C_add_each == 1:
                    
                    # plt.title(fig_title_X_Y+'_with_selected', fontsize=20) #
                    
                    X_Y_C_add  =  color[sheet_num_add] #メインFigと同じくシート毎に分けたい場合
                    
           
                    
                    df1 = data_limit()
                    df_fig_add = df1
                    
                    
                        
    
                    
                       
                    #########月ごとに色分けする場合######################
                    lw_add = 0.6 #線の太さ
                    # 描画する月範囲を指定 and指定
                    df13 = df1[(df1['Month'] >= 1) & (df1['Month'] <= 3)
                              | df_fiｇ_add.isnull().all(axis=1)]  
                    plt.plot(df13[X_data], df13[Y_data],c='blue', marker=X_Y_M, lw=lw_add, alpha=alpha_selected, label='1-3')
                    
                    # 描画する月範囲を指定 and指定
                    df46 = df1[(df1['Month'] >= 4) & (df1['Month'] <= 6)
                              | df_fiｇ_add.isnull().all(axis=1)]  
                    plt.plot(df46[X_data], df46[Y_data],c='green', marker=X_Y_M, lw=lw_add, alpha=alpha_selected, label='4-6')
                    
                    # 描画する月範囲を指定 and指定
                    df79 = df1[(df1['Month'] >= 7) & (df1['Month'] <= 9)
                              | df_fiｇ_add.isnull().all(axis=1)]  
                    plt.plot(df79[X_data], df79[Y_data],c='orange', marker=X_Y_M, lw=lw_add, alpha=alpha_selected, label='7-9')
                    # 描画する月範囲を指定 and指定
                    df1012 = df1[(df1['Month'] >= 10) & (df1['Month'] <= 12)
                              | df_fiｇ_add.isnull().all(axis=1)]  
                    plt.plot(df1012[X_data], df1012[Y_data],c='purple', marker=X_Y_M, lw=lw_add, alpha=alpha_selected, label='10-12')
                    
                    
                    # 特定の列に特定の変数を持つ行と空白行を残す
                    # df_fiｇ_add = df_fiｇ_add[(df_fiｇ_add[selected_row] == selected_area) | df_fiｇ_add.isnull().all(axis=1)]
                    # df_fiｇ_add = df_fiｇ_add[(df_fiｇ_add[selected_row] == selected_area) | df_fiｇ_add.isnull().all(axis=1)]
                    
                    
                    
                    
                    
                    #########全部plotする場合######################    
                    
                    #列の要素を表示
                    d_select = df_fiｇ_add[selected_row].value_counts().to_dict()
                    print('要素と出現数:', d_select)
                    print('---------------')
    
        
                    plt.legend(fontsize = sld_font_size_min_S) # 凡例の数字のフォントサイズを設定
    
                    
                    
                    #############################
                    if selected_add3 == 1:
    
                        #個別に色を変えてもう一つプロット
                        # Excelファイルの読み込み
                        # df_fiｇ_add = pd.read_excel(excel_file, sheet_name=sheet_num_add)
                        df_fiｇ_add = df_original
                        selected_row2 = selected_row2
                        selected_value = selected_value
                        
                        # 特定の列に特定の変数を持つ行と空白行を残す
                        df_fiｇ_add = df_fiｇ_add[(df_fiｇ_add[selected_row2] == selected_value) | df_fiｇ_add.isnull().all(axis=1)]
                        plt.plot(df_fiｇ_add[X_data], df_fiｇ_add[Y_data],c='red', marker=X_Y_M, lw=2, alpha=alpha_selected, label=selected_value)
                        plt.legend(fontsize = 16) # 凡例の数字のフォントサイズを設定
                        
                    else:()
                      
                    #############################
                    
                    
                    
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

            
                else:() 
                
        else:()
    else:()
    

     
    ###############################################################################################
    ############################################################################################### 
    ###############################################################################################
    ###############################################################################################
    # st.write(":red[d18O map (select parameters)]")
    st.markdown("##### :red[--- The fig-size can be adjusted using the [fig scale] setting---]")

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
                
                    
    
    #######################画像を保存するためのボタン作成########################
    sub_title2 = sub_title
    sub_title2 = sub_title2.replace(':', '') #pdf書き出し用
    # sub_title2 = sub_title2.replace('>', '') #pdf書き出し用
    # sub_title2 = sub_title2.replace('<', '') #pdf書き出し用
    sub_title2 = sub_title2.replace(',', '_') #pdf書き出し用
    sub_title2 = sub_title2.replace(' ', '') #pdf書き出し用
    sub_tite = str('Fig_depth'+'_'+sub_title2+".png")


    
    #画像を保存，以下の方法だとローカルにも保存されてしまう
    # fn = sub_tite
    # # plt.savefig(fn)

    # with open(fn, "rb") as img:
    #     btn = st.download_button(
    #         label="Download image",
    #         data=img,
    #         file_name=fn,
    #         mime="image/png"
    #     )

    #Save to memory first. の場合は，ローカルに保存されないので安心
    import io
    fn = sub_tite
    img = io.BytesIO()
    plt.savefig(img, format='png')
     
    btn = st.download_button(
       label="Download image",
       data=img,
       file_name=fn,
       mime="image/png"
       )
    
    
    
    
# show plots
# fig.tight_layout()
# fig.show()

       
            
    
    # st.subheader('Area Chart')
    # st.area_chart(df_fig_ALL)
    
    # Matplotlib の Figure を指定して可視化する
    st.pyplot(fig)
    
    
    ###############################################################################################
    ###############################################################################################
    ###############################################################################################
    ###############################################################################################
    
    # ##########採取地点のmap　拡大可能##################
    # df1 = data_limit()
    # df1['lat'] = df1['Latitude_degN']
    # df1['lon'] = df1['Longitude_degE']
    
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
        key="depth_profile",
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
        # 1. 必要な列をコピー
        df1_table = df1[['reference','Cruise', 'Station', 'Date', 'Longitude_degE', 'Latitude_degN', 'Depth_m', 'Temperature_degC', 'Salinity', 'd18O', 'dD']].copy()        
        # --- [追加] 空白行（すべての列が欠損値の行）を削除 ---
        df1_table = df1_table.dropna(how='all')
        # 【重要】表示直前に全列を文字列化（これでArrowエラーは100%消えます）
        df1_table = df1_table.astype(str) 
        
        # 3. テーブルを表示
        # 最新の width='stretch' を使用すべきか？
        st.dataframe(df1_table, use_container_width=True)
    
    ###############################################################################################
    ###############################################################################################
    ###############################################################################################
    ###############################################################################################


if __name__ == '__main__':
    main()
    
    

