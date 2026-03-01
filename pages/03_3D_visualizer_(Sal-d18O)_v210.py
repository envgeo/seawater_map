
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 16:00:21 2023


@author: Toyoho Ishimura @Kuoto-U

2026/02/10 update 
"""


# --- バージョン管理の設定 ---
version = "2.10" #2026/02/23



import streamlit as st
# from streamlit_folium import folium_static
# import folium
# import pandas as pd
import numpy as np
import plotly.express as px
# import plotly.graph_objects as go
# import plotly.express as px
import envgeo_utils  # 作った設定ファイルを読み込む
from streamlit_plotly_events import plotly_events
import math



print(f"--------03_3D_visualizer_({version})--------")
# datetimeモジュールを使った現在の日付と時刻の取得
import datetime
dt = datetime.datetime.today()  # ローカルな現在の日付と時刻を取得
print(dt)  # 2021-10-29 15:58:08.356501





############ページタイトル設定############

# st.set_page_config(
#     page_title="d18O mapping",
#     page_icon="🗾",
#     # layout="wide"
#     )




############メイン設定############


def main():
    
    # 注意書き
    st.header(f'3D visualizer ({version})')
    

    ############################################################
    # リロードボタン
    st.button('Reload')
    
    




    # データソースの変数、envgeo_utilsから読み出す
    data_source_JAPAN_SEA = envgeo_utils.data_source_JAPAN_SEA
    data_source_AROUND_JAPAN = envgeo_utils.data_source_AROUND_JAPAN
    data_source_GLOBAL = envgeo_utils.data_source_GLOBAL
    

    # データソース選択
    ref_data = st.radio("data source (see home>about):", (data_source_JAPAN_SEA, data_source_AROUND_JAPAN, data_source_GLOBAL), horizontal=True, args=[1, 0])

    
    # データソース選択 old
    # ref_data = st.radio("data source (see home>about):", (data_source_JAPAN_SEA, data_source_AROUND_JAPAN, data_source_GLOBAL), horizontal=True, args=[1, 0])



    #Excel読み込み
    # sheet_num = 1
    # df1 = pd.read_excel(excel_file, sheet_name=sheet_num)
    df1 = envgeo_utils.load_isotope_data(ref_data)
    
    

    
######  scalebarで制御してsubmitする場合 ################

    with st.sidebar.form("parameter", clear_on_submit=False):
        
        st.header('select parameters >>> submit')
        

                
            
        
        #################論文選択ここから###########################################


        # ref_data = st.radio("data source (see home>about):", (data_source_JAPAN_SEA, data_source_AROUND_JAPAN), horizontal=True, args=[1, 0])



        #################全データプロット選択ここから###########################################

        # st.subheader('data source:')
        
        # plot_all_data = st.radio("Plot all data on the background as red:", ("YES", "NO"), horizontal=True, args=[1, 0])
        
        # if plot_all_data == "YES":()

        # else:()
        
        #################全データプロット選択ここまで###########################################
        
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
        
        
        # elif ref_data == data_source_GLOBAL:
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
        
        # else:()
        
        # #################文献選択ここまで###########################################
        
        
        
        
        
        
        
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
                                    min_value=-1,
                                    max_value=40,
                                    value=(-1, 40),
                                    )
        # st.sidebar.write(f'Selected: {sld_sal_min} ~ {sld_sal_max}')
        
            
        
        
        
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
        # elif ref_data == data_source_GLOBAL:
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
        # else:()
        
        # # st.write(f'Selected: {selected_cruise}')
        
        
        
        st.write('Cruise Area (2015-2021) in Kodama et al.(2024)')
        st.image("data/sites_20230515.gif") 
        
        

        
                                    
        submitted = st.form_submit_button(":red[submit!]")

##############################################################################
# サイドバーここまで
##############################################################################

        # キャッシュのクリア　サイドバーの一番下などに配置
        # st.sidebar.markdown("---") # 区切り線
        if st.sidebar.button("🔄 clear cache"):
            envgeo_utils.clear_app_cache()
            # st.sidebar.success("キャッシュをクリアしました！再読み込みします...")
            st.rerun() # アプリを再実行して最新のExcelを読み込ませる
        


    
    # 注意書き
    
    

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
        
        
    
    # if ref_data == data_source_JAPAN_SEA:
    #     st.write(':blue[data source:]  Kodama et al. (2024)')
        
    # elif ref_data == data_source_AROUND_JAPAN:
    #     # st.text('including data from previous reports')
    #     st.write(':blue[data source:] Kodama et al. (2024), Yamamoto et al. (2001), Sakamoto et al. (2019), Kodaira et al. (2016), Horikawa et al. (2023).')

        
    # elif ref_data == data_source_GLOBAL:
    #     # st.text('including data from previous reports')

    #     st.write(':blue[data source:] Kodama et al. (2024), Yamamoto et al. (2001), Sakamoto et al. (2019), Kodaira et al. (2016), Horikawa et al. (2023).')
    #     st.write(':blue[with:] NASA_database (Jan.23, 2025)]https://data.giss.nasa.gov/cgi-bin/o18data/geto18.cgi')

    # else:()


            
        ############################################################
    
    
    
    
    # "# streamlit-foliums"
    
    # with st.echo():
    #     import streamlit as st
    #     from streamlit_folium import folium_static
    #     import folium
    #     import pandas as pd
    
    # center on Liberty Bell
    # m = folium.Map(location=[35, 135], tiles="Stamen Terrain", zoom_start=5)
    
    # add marker for Liberty Bell
    # tooltip = "Liberty Bell"
    # folium.Marker(
    #     [39.949610, -75.150282], popup="Liberty Bell", tooltip=tooltip
    # ).add_to(m)
    
    
    
    # #海水 
    # #データソースによって選ぶファイルを変える
    # if ref_data == data_source_JAPAN_SEA:
    #     excel_file = 'd18O_20230513-1_NA2_2021add.xlsx'

    # elif ref_data == data_source_AROUND_JAPAN:
    #     excel_file = 'd18O_20240927_ref_YSKH.xlsx'
        
    # elif ref_data == data_source_GLOBAL:
    #     excel_file = 'd18O_NASA_全データ_Python_20250123.xlsx'
        
    # else:()
    

    # sheet_num = 1
    
    # df = pd.read_excel(excel_file, sheet_name=sheet_num)
    
    
    # df1 = envgeo_utils.load_isotope_data(ref_data)

    
    
    
    
    
    
    
    # """選択描画範囲の設定用"""
    def data_limit():
    
            # sheet_num = 1
            # df1 = pd.read_excel(excel_file, sheet_name=sheet_num)
            df1 = envgeo_utils.load_isotope_data(ref_data)
            # df1 = df_fig_ALL
        
            #緯度経度と水深とTransectで制限
            # df1 = df_fig_add
            
            df1 = df1[(df1['Depth_m'] == 'xxx') 
                        
                        |(df1['Depth_m'] <= sld_depth_max) & (df1['Depth_m'] >= sld_depth_min )#調整用
                        | df1.isnull().all(axis=1)]      
            
            df1 = df1[(df1['Transect'].isin(selected_cruise))
                        | df1.isnull().all(axis=1)]
            
            
            
            
                
            # Transectのデータ制限せず，サイドバーで制限されたまま出力する場合
            df1 = df1[df1['Transect'].isin(selected_cruise) | df1['Transect'].isna()].copy()
                # なぜこれで青色の線のスキマが復活するのか
                # 元のデータ (df):
                # 　　「データA」→「データA」→「空白行」→「データA」
                # これまでの抽出 (df1):
                #　　 reference が「データA」のものだけを抽出した結果、「空白行」が条件に合わず消されてしまい、「データA」同士が隣り合って線が繋がってしまった
                # 新しい抽出:
                #　　| df['reference'].isna() （または reference が空であること）という条件を加えることで、「データA」の間にあった「空白行」も一緒に df1 にコピーされるようになる
           
            # # Transectの手動でデータ制限する場合
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
            # elif ref_data == data_source_AROUND_JAPAN:
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
              
            # elif ref_data == data_source_GLOBAL:
            #     df1 = df1[ (df1['Transect'] == 0) 
            #                 | (df1['Transect'] == Transect000) 
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
                       
            # else:()
              

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
            df1 = df1[(df1['Year'] <= sld_year_max) & (df1['Year'] >= sld_year_min) 
                        | df1.isnull().all(axis=1)] 

     
            return df1
        
        
        
    df1 = data_limit()
    
    
    # st.write(df_empty)
    data_found_num = str(len(df1["d18O"]))

    # # with表記 (推奨)
    # with st.expander("selected data", expanded=False):

    # #選んだパラメーター表示
    #     st.write('YEAR:'+str(sld_year_min)+'-'+str(sld_year_max)+', ' 
    #               +'MONTH:'+str(sld_month_min)+'-'+str(sld_month_max)+', '
    #               +'Longitude:'+str(sld_lon_min)+'-'+str(sld_lon_max)+', '
    #               +'Latitude:'+str(sld_lat_min)+'-'+str(sld_lat_max)+', '
    #               +'Water_depth:'+str(sld_depth_min)+'-'+str(sld_depth_max)+', '
    #               +'Salinity:'+str(sld_sal_min)+'-'+str(sld_sal_max))
    #     # st.write('Area(Cruise)',selected_cruise)
    #     selected_cruise_indicate =str(list(selected_cruise[:]))
    #     st.write('Selected Area (Cruise)', selected_cruise_indicate)
    #     # print('Area(Cruise)', list(selected_cruise[:]))
    #     #テキストの色変更
    #     # st.write(""":red['test']""")

 
    #テキストの色変更

    # # バリデーション処理
    # if df30m_empty == 1:  #データが無かったとき
    #     st.warning('no data found')
    #     # 条件を満たないときは処理を停止する
    #     st.stop()
    # elif df30m_empty == 0: #データがあったとき
    #     st.write(data_found_num,'data found for depth profile (below 30m)')
    st.write(data_found_num,'data found')
    
    
    
    df1['lat'] = df1['Latitude_degN']
    df1['lon'] = df1['Longitude_degE']
    df1['Depth_m'] = df1['Depth_m']*(-1)
    
    
                  
                        
    ###############################################################################################
    ############################### 選択データ表示　2024/10/07 #######################################
    # 選択されたデータの表示，平均値計算など
    # st.expander to show selected data
    ###############################################################################################
    
    selected_row = "Transect"
    #列の要素を表示
    d_select_add2 = df1[selected_row].value_counts().to_dict()
    d_select_add2_sum = df1[selected_row].count().sum()
    print('要素と出現数:', d_select_add2)
    print('要素と出現数:', d_select_add2_sum)
    print('---------------')

    
    
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
    ###############################################################################################
    
    
    
    
    
    ###############################################################################################
    ###############################################################################################
    ###############################################################################################
    ###############################################################################################  
    

    
    ##########################################################################
    # --- 共通スタイル設定関数の定義 (すべての図にこれを適用) ---
    ##########################################################################
    def unify_plot_layout(fig, x_label, y_label, color_title):
        fig.update_layout(
            plot_bgcolor="white",
            paper_bgcolor="white",
            
            # 1. 全体サイズを固定
            width=850,   # 右側のマージンを考慮して少し広めに設定
            height=600,
            autosize=False,
            
            xaxis=dict(
                title=x_label,
                showline=True, linewidth=1, linecolor='grey', mirror=True,
                showgrid=True, gridcolor='rgba(220, 220, 220, 0.4)', gridwidth=0.5,
                ticks="inside", ticklen=5
            ),
            yaxis=dict(
                title=y_label,
                showline=True, linewidth=1, linecolor='grey', mirror=True,
                showgrid=True, gridcolor='rgba(220, 220, 220, 0.4)', gridwidth=0.5,
                ticks="inside", ticklen=5
            ),
            
            # 2. カラーバーを「枠の外」に固定配置する設定
            coloraxis_colorbar=dict(
                title=color_title,
                thickness=15,
                len=0.8,
                x=1.02,           # グラフ枠のすぐ右外側に固定（1.0が枠の右端）
                xanchor='left',   # 左端を基準に配置
                y=0.5,
                yanchor='middle'
            ),
            
            # 3. マージンの設定
            # 右側(r)を150px程度確保することで、文字が長くても枠サイズに影響を与えません
            margin=dict(l=80, r=150, t=50, b=80), 
            
            font=dict(size=12)
        )
        
        fig.update_traces(marker=dict(size=6, opacity=0.8))
        
        return fig
    


   
    ###############################################################################################
    ############################################################################################### 
    ###############################################################################################
    ###############################################################################################
    

    ##########################################################################
    ###### Salinity - δ18O Plot (X, Y 固定 / Colorbar 切り替え) #######
    ##########################################################################
    
    
    # st.subheader('Salinity - δ18O Relationship')

    # # 1. 色の要素選択（選択肢を3つに限定）
    # col_map = {
    #     "Latitude": "Latitude_degN", 
    #     "Longitude": "Longitude_degE", 
    #     "Water Depth": "Depth_m"
    # }
    # sel_col = st.radio("Select color element:", list(col_map.keys()), horizontal=True, key="col_fixed_xy")

    # # --- 選択された列名を定義 ---
    # target_item = col_map[sel_col]

    # # --- envgeo_utilsからカスタムスケールを取得 (target_itemを基準にする) ---
    # c_scale_final = envgeo_utils.get_custom_colorscale(target_item)

    # # 2. グラフ作成 (X=Salinity, Y=d18O 固定)
    # fig_fixed_xy = px.scatter(
    #     df1, x="Salinity", y="d18O", 
    #     color=col_map[sel_col], 
    #     color_continuous_scale=c_scale_final,
    #     hover_data=[
    #                 "lat",  
    #                 "lon",  
    #                 "d18O", 
    #                 "dD", 
    #                 "Salinity", 
    #                 "Temperature_degC", 
    #                 "Year", 
    #                 "Month", 
    #                 "Day", 
    #                 "Cruise", 
    #                 "Station",
    #                 "Depth_m",
    #                 "reference",  
    #                 ]
    # )

    # # 3. スタイル適用 (unify_plot_layout を使用)
    # fig_fixed_xy = unify_plot_layout(
    #     fig_fixed_xy, 
    #     "Salinity", 
    #     "δ18O (‰)", 
    #     sel_col.split(' ')[0] # 「緯度」などを抽出
    # )

    # st.plotly_chart(fig_fixed_xy, use_container_width=True)
    # # st.plotly_chart(fig_fixed_xy, use_container_width=False)
    
    
    

    
    ###############################################################################################
    ############################################################################################### 
    ###############################################################################################
    ###############################################################################################
    
    
    
    ##########################################################################
    ###### Salinity - Temperature Plot (X, Y 固定 / Colorbar 切り替えり替え) #####
    ##########################################################################
    
    
    # st.subheader('Salinity - Temperature Relationship')

    # # 1. 色の要素選択（選択肢を3つに限定）
    # col_map = {
    #     "Latitude": "Latitude_degN", 
    #     "Longitude": "Longitude_degE", 
    #     "Water Depth": "Depth_m"
    # }
    # sel_col = st.radio("Select color element:", list(col_map.keys()), horizontal=True, key="fig_fixed_TS")

    # # --- 選択された列名を定義 ---
    # target_item = col_map[sel_col]

    # # --- envgeo_utilsからカスタムスケールを取得 (target_itemを基準にする) ---
    # c_scale_final = envgeo_utils.get_custom_colorscale(target_item)

    # # 2. グラフ作成 (X=Salinity, Y=d18O 固定)
    # fig_fixed_TS = px.scatter(
    #     df1, x="Salinity", y="Temperature_degC", 
    #     color=col_map[sel_col], 
    #     color_continuous_scale=c_scale_final,
    #     hover_data=[
    #                 "lat",  
    #                 "lon",  
    #                 "d18O", 
    #                 "dD", 
    #                 "Salinity", 
    #                 "Temperature_degC", 
    #                 "Year", 
    #                 "Month", 
    #                 "Day", 
    #                 "Cruise", 
    #                 "Station",
    #                 "Depth_m",
    #                 "reference",  
    #                 ]
    # )

    # # 3. スタイル適用 (unify_plot_layout を使用)
    # fig_fixed_TS = unify_plot_layout(
    #     fig_fixed_TS, 
    #     "Salinity", 
    #     "Temperature (C)", 
    #     sel_col.split(' ')[0] # 「緯度」などを抽出
    # )

    # st.plotly_chart(fig_fixed_TS, use_container_width=True)
    
    
    ###############################################################################################
    ############################################################################################### 
    ###############################################################################################
    ###############################################################################################
    
    # 区切り線
    # st.divider()
    
    
    ###############################################################################################
    ############################################################################################### 
    ###############################################################################################
    ###############################################################################################
    
    
    # ###### Fig1 #######
    # st.subheader('3D salinity-d18O-longitude')
    # # color_continuous_scale= ('darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'blue', 'blue', 'blue', 'blue', 'blue', 'lightblue',  'lightblue',  'lightblue',  'lightblue',  'lightblue',  'lightblue',  'lightblue', 'lightgray', 'lightgreen', 'yellow', 'orange', 'red', )
    # color_continuous_scale= ('darkblue', 'blue', 'lightblue',  'lightgreen', 'green', 'yellow', 'orange', 'red', )
    

                      
    # fig1 = px.scatter(df1, x="Salinity", y="d18O", color="lon", trendline='ols',trendline_color_override='gray', 
    #             width=700,
    #             height=600,
    #             color_continuous_scale=color_continuous_scale,
    #             #############################ポップアップ情報ここから##########################
    #             hover_data={
    #                 "lat": True,  
    #                 "lon": True,  
    #                 "d18O": True, 
    #                 "dD": True, 
    #                 "Salinity": True, 
    #                 "Temperature_degC": True, 
    #                 "Year": True, 
    #                 "Month": True, 
    #                 "Day": True, 
    #                 "Cruise": True, 
    #                 "Station": True,
    #                 "Depth_m": True,
    #                 "reference": True,  
    #             }
    #             #############################ポップアップ情報ここまで##########################
    #             )
    

    
    # # # 図を枠で囲む設定
    # # fig1.update_layout(
    # #     shapes=[
    # #         dict(
    # #             type="rect",  # 矩形を指定
    # #             xref="paper",  # x軸は図全体を基準
    # #             yref="paper",  # y軸は図全体を基準
    # #             x0=0, x1=1,  # X軸の範囲（0～1は全体を表す）
    # #             y0=0, y1=1,  # Y軸の範囲（0～1は全体を表す）
    # #             line=dict(
    # #                 color="black",  # 枠線の色
    # #                 width=0.5,  # 枠線の太さ
    # #                 dash="solid",  # 枠線のスタイル（例: "solid", "dash", "dot"）
                
    # #             ),
    # #         )
    # #     ]
    # # )
    
    
    # # # gridcolor：グリッドの色, gridwidth：グリッドの幅、griddash='dot'：破線
    # # fig1.update_xaxes(gridcolor='lightgrey', gridwidth=1, griddash='dot')
    # # fig1.update_yaxes(gridcolor='lightgrey', gridwidth=1, griddash='dot')
    
    
    # # マーカー、ラインの設定
    # fig1.update_traces(
    # #     # mode = 'markers+lines', # 'markers+lines', 'markers'
    # #     mode = 'markers', # 'markers+lines', 'markers'
    #     marker = dict(size = 5),
    # #     # line = dict(width = 2), #color = 'Black',
    # )
    

    
    # # --- レイアウト調整 (枠線と格子) ---
    # fig1.update_layout(
    #     plot_bgcolor="white",
    #     paper_bgcolor="white",
    #     xaxis=dict(
    #         showline=True,
    #         linewidth=0.7,            
    #         linecolor='lightgray',         
    #         mirror=True,              # 四方を囲む
    #         showgrid=True,
    #         gridcolor='rgba(220, 220, 220, 0.5)', 
    #         gridwidth=0.5,
    #         zeroline=False,
    #         ticks="inside",
    #         ticklen=4,
    #         tickcolor='grey'       
    #     ),
    #     yaxis=dict(
    #         showline=True,
    #         linewidth=0.7,
    #         linecolor='lightgray',         
    #         mirror=True,
    #         showgrid=True,
    #         gridcolor='rgba(220, 220, 220, 0.5)',
    #         gridwidth=0.5,
    #         zeroline=False,
    #         ticks="inside",
    #         ticklen=4,
    #         tickcolor='grey'
    #     ),
    #     margin=dict(l=60, r=40, t=40, b=60)
    # )
    
    # # st.write(fig1)  
    # st.plotly_chart(fig1, use_container_width=True)  # ブラウザの幅に合わせる
    
    
    ###############################################################################################
    ###############################################################################################
    ###############################################################################################
    ###############################################################################################
    
    
        
    # ###### Fig2 #######
    # st.subheader('3D salinity-d18O-latitude')
    # # color_continuous_scale= ('darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'blue', 'blue', 'blue', 'blue', 'blue', 'lightblue',  'lightblue',  'lightblue',  'lightblue',  'lightblue',  'lightblue',  'lightblue', 'lightgray', 'lightgreen', 'yellow', 'orange', 'red', )
    # color_continuous_scale= ('darkblue', 'blue', 'lightblue',  'lightgreen', 'green', 'yellow', 'orange', 'red', )
    
                      
    # fig2 = px.scatter(df1, x="Salinity", y="d18O", color="lat", trendline='ols',trendline_color_override='gray', 
    #             width=700,
    #             height=600,
    #             color_continuous_scale=color_continuous_scale,
                
                

    #             #############################ポップアップ情報ここから##########################
    #             hover_data={
    #                 "lat": True,  
    #                 "lon": True,  
    #                 "d18O": True, 
    #                 "dD": True, 
    #                 "Salinity": True, 
    #                 "Temperature_degC": True, 
    #                 "Year": True, 
    #                 "Month": True, 
    #                 "Day": True, 
    #                 "Cruise": True, 
    #                 "Station": True,
    #                 "Depth_m": True,
    #                 "reference": True,  
    #             }
    #             #############################ポップアップ情報ここまで##########################
    #             )
    

    
    # # # 図を枠で囲む設定
    # # fig2.update_layout(
    # #     shapes=[
    # #         dict(
    # #             type="rect",  # 矩形を指定
    # #             xref="paper",  # x軸は図全体を基準
    # #             yref="paper",  # y軸は図全体を基準
    # #             x0=0, x1=1,  # X軸の範囲（0～1は全体を表す）
    # #             y0=0, y1=1,  # Y軸の範囲（0～1は全体を表す）
    # #             line=dict(
    # #                 color="black",  # 枠線の色
    # #                 width=0.5,  # 枠線の太さ
    # #                 dash="solid",  # 枠線のスタイル（例: "solid", "dash", "dot"）
                
    # #             ),
    # #         )
    # #     ]
    # # )
    
    
    # # # gridcolor：グリッドの色, gridwidth：グリッドの幅、griddash='dot'：破線
    # # fig2.update_xaxes(gridcolor='lightgrey', gridwidth=1, griddash='dot')
    # # fig2.update_yaxes(gridcolor='lightgrey', gridwidth=1, griddash='dot')
    
    
    # # マーカー、ラインの設定
    # fig2.update_traces(
    # #     # mode = 'markers+lines', # 'markers+lines', 'markers'
    # #     mode = 'markers', # 'markers+lines', 'markers'
    #     marker = dict(size = 5),
    # #     # line = dict(width = 2), #color = 'Black',
    # )
    

    
    # # --- レイアウト調整 (枠線と格子) ---
    # fig2.update_layout(
    #     plot_bgcolor="white",
    #     paper_bgcolor="white",
    #     xaxis=dict(
    #         showline=True,
    #         linewidth=0.7,            
    #         linecolor='lightgray',         
    #         mirror=True,              # 四方を囲む
    #         showgrid=True,
    #         gridcolor='rgba(220, 220, 220, 0.5)', 
    #         gridwidth=0.5,
    #         zeroline=False,
    #         ticks="inside",
    #         ticklen=4,
    #         tickcolor='grey'       
    #     ),
    #     yaxis=dict(
    #         showline=True,
    #         linewidth=0.7,
    #         linecolor='lightgray',         
    #         mirror=True,
    #         showgrid=True,
    #         gridcolor='rgba(220, 220, 220, 0.5)',
    #         gridwidth=0.5,
    #         zeroline=False,
    #         ticks="inside",
    #         ticklen=4,
    #         tickcolor='grey'
    #     ),
    #     margin=dict(l=60, r=40, t=40, b=60)
    # )
    
    # # st.write(fig1)  
    # st.plotly_chart(fig2, use_container_width=True)  # ブラウザの幅に合わせる
    
    
    ###############################################################################################
    ###############################################################################################
    ###############################################################################################
    ###############################################################################################
    
        
    # ###### Fig3 #######
    # st.subheader('3D salinity-d18O-depth')
    # color_continuous_scale= ('darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'blue', 'blue', 'blue', 'blue', 'blue', 'lightblue',  'lightblue',  'lightblue',  'lightblue',  'lightblue',  'lightblue',  'lightblue', 'lightgray', 'lightgreen', 'yellow', 'orange', 'red', )
    
    # fig3 = px.scatter(df1, x="Salinity", y="d18O", color="Depth_m", trendline='ols',trendline_color_override='gray', 
    #             width=700,
    #             height=600,
    #             color_continuous_scale=color_continuous_scale,
                
                
    #             #############################ポップアップ情報ここから##########################
    #             hover_data={
    #                 "lat": True,  
    #                 "lon": True,  
    #                 "d18O": True, 
    #                 "dD": True, 
    #                 "Salinity": True, 
    #                 "Temperature_degC": True, 
    #                 "Year": True, 
    #                 "Month": True, 
    #                 "Day": True, 
    #                 "Cruise": True, 
    #                 "Station": True,
    #                 "Depth_m": True,
    #                 "reference": True,  
    #             }
    #             #############################ポップアップ情報ここまで##########################
    #             )
    
    # # マーカー、ラインの設定
    # fig3.update_traces(
    # #     # mode = 'markers+lines', # 'markers+lines', 'markers'
    # #     mode = 'markers', # 'markers+lines', 'markers'
    #     marker = dict(size = 5),
    # #     # line = dict(width = 2), #color = 'Black',
    # )
    

        
    # # --- レイアウト調整 (枠線と格子) ---
    # fig3.update_layout(
    #     plot_bgcolor="white",
    #     paper_bgcolor="white",
    #     xaxis=dict(
    #         showline=True,
    #         linewidth=0.7,            
    #         linecolor='lightgray',         
    #         mirror=True,              # 四方を囲む
    #         showgrid=True,
    #         gridcolor='rgba(220, 220, 220, 0.5)', 
    #         gridwidth=0.5,
    #         zeroline=False,
    #         ticks="inside",
    #         ticklen=4,
    #         tickcolor='grey'       
    #     ),
    #     yaxis=dict(
    #         showline=True,
    #         linewidth=0.7,
    #         linecolor='lightgray',         
    #         mirror=True,
    #         showgrid=True,
    #         gridcolor='rgba(220, 220, 220, 0.5)',
    #         gridwidth=0.5,
    #         zeroline=False,
    #         ticks="inside",
    #         ticklen=4,
    #         tickcolor='grey'
    #     ),
    #     margin=dict(l=60, r=40, t=40, b=60)
    # )
    
    # # st.write(fig11)  
    
    # st.plotly_chart(fig3, use_container_width=True)  # ブラウザの幅に合わせる
    
    
    
    ###############################################################################################
    ###############################################################################################
    ###############################################################################################
    ############################################################################################### 
    
    
    
    
    
    # ###### Fig4 #######
    # st.subheader('3D T-S salinity-temperature-longitude')
    # # color_continuous_scale= ('darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'blue', 'blue', 'blue', 'blue', 'blue', 'lightblue',  'lightblue',  'lightblue',  'lightblue',  'lightblue',  'lightblue',  'lightblue', 'lightgray', 'lightgreen', 'yellow', 'orange', 'red', )
    # color_continuous_scale= ('darkblue', 'blue', 'lightblue',  'lightgreen', 'green', 'yellow', 'orange', 'red', )

    # fig4 = px.scatter(df1, x="Salinity", y="Temperature_degC", color="lon",
    #             width=700,
    #             height=600,
    #             color_continuous_scale=color_continuous_scale,
                
    #             #############################ポップアップ情報ここから##########################
    #             hover_data={
    #                 "lat": True,  
    #                 "lon": True,  
    #                 "d18O": True, 
    #                 "dD": True, 
    #                 "Salinity": True, 
    #                 "Temperature_degC": True, 
    #                 "Year": True, 
    #                 "Month": True, 
    #                 "Day": True, 
    #                 "Cruise": True, 
    #                 "Station": True,
    #                 "Depth_m": True,
    #                 "reference": True,  
    #             }
    #             #############################ポップアップ情報ここまで##########################
    #             )
    
    # # マーカー、ラインの設定
    # fig4.update_traces(
    # #     # mode = 'markers+lines', # 'markers+lines', 'markers'
    # #     mode = 'markers', # 'markers+lines', 'markers'
    #     marker = dict(size = 5),
    # #     # line = dict(width = 2), #color = 'Black',
    # )
    
    
    # # --- レイアウト調整 (枠線と格子) ---
    # fig4.update_layout(
    #     plot_bgcolor="white",
    #     paper_bgcolor="white",
    #     xaxis=dict(
    #         showline=True,
    #         linewidth=0.7,            
    #         linecolor='lightgray',         
    #         mirror=True,              # 四方を囲む
    #         showgrid=True,
    #         gridcolor='rgba(220, 220, 220, 0.5)', 
    #         gridwidth=0.5,
    #         zeroline=False,
    #         ticks="inside",
    #         ticklen=4,
    #         tickcolor='grey'       
    #     ),
    #     yaxis=dict(
    #         showline=True,
    #         linewidth=0.7,
    #         linecolor='lightgray',         
    #         mirror=True,
    #         showgrid=True,
    #         gridcolor='rgba(220, 220, 220, 0.5)',
    #         gridwidth=0.5,
    #         zeroline=False,
    #         ticks="inside",
    #         ticklen=4,
    #         tickcolor='grey'
    #     ),
    #     margin=dict(l=60, r=40, t=40, b=60)
    # )
    
    
    # # st.write(fig31)  
    # st.plotly_chart(fig4, use_container_width=True)  # ブラウザの幅に合わせる
    
        
    ###############################################################################################
    ###############################################################################################
    ###############################################################################################
    ###############################################################################################
    
    
    # ###### Fig5 #######
    # st.subheader('3D T-S salinity-temperature-latitude')
    # # color_continuous_scale= ('darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'blue', 'blue', 'blue', 'blue', 'blue', 'lightblue',  'lightblue',  'lightblue',  'lightblue',  'lightblue',  'lightblue',  'lightblue', 'lightgray', 'lightgreen', 'yellow', 'orange', 'red', )
    # color_continuous_scale= ('darkblue', 'blue', 'lightblue',  'lightgreen', 'green', 'yellow', 'orange', 'red', )

    # fig5 = px.scatter(df1, x="Salinity", y="Temperature_degC", color="lat",
    #             width=700,
    #             height=600,
    #             color_continuous_scale=color_continuous_scale,
                
    #             #############################ポップアップ情報ここから##########################
    #             hover_data={
    #                 "lat": True,  
    #                 "lon": True,  
    #                 "d18O": True, 
    #                 "dD": True, 
    #                 "Salinity": True, 
    #                 "Temperature_degC": True, 
    #                 "Year": True, 
    #                 "Month": True, 
    #                 "Day": True, 
    #                 "Cruise": True, 
    #                 "Station": True,
    #                 "Depth_m": True,
    #                 "reference": True,  
    #             }
    #             #############################ポップアップ情報ここまで##########################
    #             )
    
    # # マーカー、ラインの設定
    # fig5.update_traces(
    # #     # mode = 'markers+lines', # 'markers+lines', 'markers'
    # #     mode = 'markers', # 'markers+lines', 'markers'
    #     marker = dict(size = 5),
    # #     # line = dict(width = 2), #color = 'Black',
    # )
    

    
    # # --- レイアウト調整 (枠線と格子) ---
    # fig5.update_layout(
    #     plot_bgcolor="white",
    #     paper_bgcolor="white",
    #     xaxis=dict(
    #         showline=True,
    #         linewidth=0.7,            
    #         linecolor='lightgray',         
    #         mirror=True,              # 四方を囲む
    #         showgrid=True,
    #         gridcolor='rgba(220, 220, 220, 0.5)', 
    #         gridwidth=0.5,
    #         zeroline=False,
    #         ticks="inside",
    #         ticklen=4,
    #         tickcolor='grey'       
    #     ),
    #     yaxis=dict(
    #         showline=True,
    #         linewidth=0.7,
    #         linecolor='lightgray',         
    #         mirror=True,
    #         showgrid=True,
    #         gridcolor='rgba(220, 220, 220, 0.5)',
    #         gridwidth=0.5,
    #         zeroline=False,
    #         ticks="inside",
    #         ticklen=4,
    #         tickcolor='grey'
    #     ),
    #     margin=dict(l=60, r=40, t=40, b=60)
    # )
    
    
    
    # # st.write(fig5)  
    # st.plotly_chart(fig5, use_container_width=True)  # ブラウザの幅に合わせる
    
    
    
    ###############################################################################################
    ###############################################################################################
    ###############################################################################################
    ###############################################################################################
    
    
    
    # ###### Fig6 #######
    # st.subheader('3D T-S salinity-temperature-depth')
    # color_continuous_scale= ('darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'blue', 'blue', 'blue', 'blue', 'blue', 'lightblue',  'lightblue',  'lightblue',  'lightblue',  'lightblue',  'lightblue',  'lightblue', 'lightgray', 'lightgreen', 'yellow', 'orange', 'red', )
    
    # fig6 = px.scatter(df1, x="Salinity", y="Temperature_degC", color="Depth_m", 
    #             width=700,
    #             height=600,
    #             color_continuous_scale=color_continuous_scale,
                
    #             #############################ポップアップ情報ここから##########################
    #             hover_data={
    #                 "lat": True,  
    #                 "lon": True,  
    #                 "d18O": True, 
    #                 "dD": True, 
    #                 "Salinity": True, 
    #                 "Temperature_degC": True, 
    #                 "Year": True, 
    #                 "Month": True, 
    #                 "Day": True, 
    #                 "Cruise": True, 
    #                 "Station": True,
    #                 "Depth_m": True,
    #                 "reference": True,  
    #             }
    #             #############################ポップアップ情報ここまで##########################
    #             )
    
    # # マーカー、ラインの設定
    # fig6.update_traces(
    # #     # mode = 'markers+lines', # 'markers+lines', 'markers'
    # #     mode = 'markers', # 'markers+lines', 'markers'
    #     marker = dict(size = 5),
    # #     # line = dict(width = 2), #color = 'Black',
    # )
    
    
    # # --- レイアウト調整 (枠線と格子) ---
    # fig6.update_layout(
    #     plot_bgcolor="white",
    #     paper_bgcolor="white",
    #     xaxis=dict(
    #         showline=True,
    #         linewidth=0.7,            
    #         linecolor='lightgray',         
    #         mirror=True,              # 四方を囲む
    #         showgrid=True,
    #         gridcolor='rgba(220, 220, 220, 0.5)', 
    #         gridwidth=0.5,
    #         zeroline=False,
    #         ticks="inside",
    #         ticklen=4,
    #         tickcolor='grey'       
    #     ),
    #     yaxis=dict(
    #         showline=True,
    #         linewidth=0.7,
    #         linecolor='lightgray',         
    #         mirror=True,
    #         showgrid=True,
    #         gridcolor='rgba(220, 220, 220, 0.5)',
    #         gridwidth=0.5,
    #         zeroline=False,
    #         ticks="inside",
    #         ticklen=4,
    #         tickcolor='grey'
    #     ),
    #     margin=dict(l=60, r=40, t=40, b=60)
    # )
    
    
    # # st.write(fig32)
    # st.plotly_chart(fig6, use_container_width=True)  # ブラウザの幅に合わせる


    
    
    ###############################################################################################
    ############################################################################################### 
    ###############################################################################################
    ###############################################################################################
    
    
    
    
    # ##########採取地点のsimple map　拡大可能 simple ##################




    # # 1. NASAデータベースかどうかに基づいてパラメータを切り替え
    # if ref_data == data_source_GLOBAL:
    #     # 全世界が見える設定
    #     target_center = {"lat": 35, "lon": 135}
    #     target_zoom = 0
    # else:
    #     # デフォルト（日本近海など）の設定
    #     target_center = {"lat": 35, "lon": 135}
    #     target_zoom = 3
    
    # # 2. 地図の描画
    # fig_map = px.scatter_mapbox(
    #     df1, 
    #     lat="Latitude_degN", 
    #     lon="Longitude_degE", 
    #     hover_data=["d18O",'dD',"Salinity",'Temperature_degC','Year','Month','Day','Cruise','Station','Depth_m','reference'],
    #     opacity=0.4,
    # )
    
    # # 3. レイアウトで位置とズームを固定
    # fig_map.update_layout(
    #     mapbox={
    #         "style": "carto-positron",
    #         "center": target_center,
    #         "zoom": target_zoom
    #     },
    #     margin={"r":0, "t":0, "l":0, "b":0}
    # )
    
    # st.plotly_chart(fig_map, use_container_width=True)
    
    
        

    ###############################################################################################
    ###############################################################################################
    ###############################################################################################
    ###############################################################################################
    
    
    # 区切り線
    # st.divider()
    
    
    ###############################################################################################
    ############################################################################################### 
    ###############################################################################################
    ###############################################################################################
    
    
    
    ##########################################################################
    # --- 7. Sampling Map (Color 切り替え & カラーバー下配置) ---
    ##########################################################################
    
    # st.subheader('Interactive Map')

    # # 他の図と共通のカラースケールを使用
    # c_scale_final = ['darkblue', 'blue', 'lightblue', 'lightgreen', 'green', 'yellow', 'orange', 'red']

    # # エラー回避のため、キー名をユニークにするか、変数を整理します
    # map_color_option = st.radio(
    #     "select color element (Salinity or d18O):",
    #     ["d18O", "Salinity"],
    #     horizontal=True,
    #     key="map_color_selector_unique"  # キー名を変更して重複を回避
    # )

    # # 1. ズーム設定
    # if ref_data == data_source_GLOBAL:
    #     target_center = {"lat": 35, "lon": 135}; target_zoom = 0
    # else:
    #     target_center = {"lat": 35, "lon": 135}; target_zoom = 3
    
    # # 2. 地図の描画
    # fig_map = px.scatter_mapbox(
    #     df1, lat="Latitude_degN", lon="Longitude_degE", 
    #     color=map_color_option, 
    #     color_continuous_scale=c_scale_final,
    #     hover_data=["d18O",'dD',"Salinity",'Temperature_degC','Year','Month','Day','Cruise','Station','Depth_m','reference'],
    #     opacity=0.6,
    # )
    
    # # 3. レイアウト設定（カラーバーを下へ）
    # fig_map.update_layout(
    #     mapbox={
    #         "style": "carto-positron",
    #         "center": target_center,
    #         "zoom": target_zoom
    #     },
    #     margin={"r":0, "t":0, "l":0, "b":100}, # 下側にカラーバー用の十分な余白を確保
    #     height=700, # カラーバーが下に来るため、少し高めに設定
        
    #     coloraxis_colorbar=dict(
    #         title=map_color_option,
    #         orientation='h',   # 水平配置
    #         yanchor='bottom', 
    #         y=-0.2,            # 地図の下端からの位置（調整可）
    #         xanchor='center', 
    #         x=0.5,             # 中央配置
    #         thickness=15, 
    #         len=0.8            # バーの長さ
    #     )
    # )
    
    # st.plotly_chart(fig_map, use_container_width=True)
    

   




    ###############################################################################################
    ###############################################################################################
    ###############################################################################################
    ###############################################################################################
    
    # 区切り線
    # st.divider()
    
    
    ###############################################################################################
    ############################################################################################### 
    ###############################################################################################
    ###############################################################################################
    
    # # from streamlit_plotly_events import plotly_events
    
    # # --- 1. セッション状態の初期化 ---
    # if 'ts_selected_indices' not in st.session_state:
    #     st.session_state.ts_selected_indices = []
    
    # st.subheader('Salinity - Temperature Relationship & Auto-Zoom Map')
    
    # # (ラジオボタンやスケール設定)
    # col_map = {"d18O": "d18O", "Latitude": "Latitude_degN", "Longitude": "Longitude_degE", "Water Depth": "Depth_m"}
    # sel_col = st.radio("Select color element:", list(col_map.keys()), horizontal=True, key="fig_TS_zoom")
    # target_item = col_map[sel_col]
    # c_scale_final = envgeo_utils.get_custom_colorscale(target_item)
    
    # # --- 2. T-S図の描画とサイズ圧縮 ---
    # fig_fixed_TS = px.scatter(
    #     df1, x="Salinity", y="Temperature_degC", 
    #     color=target_item, color_continuous_scale=c_scale_final,
    #     hover_data=[
    #                 "lat",  
    #                 "lon",  
    #                 "d18O", 
    #                 "dD", 
    #                 "Salinity", 
    #                 "Temperature_degC", 
    #                 "Year", 
    #                 "Month", 
    #                 "Day", 
    #                 "Cruise", 
    #                 "Station",
    #                 "Depth_m",
    #                 "reference",  
    #                 ]
    # )
    
    # # ① 共通レイアウト適用
    # fig_fixed_TS = unify_plot_layout(fig_fixed_TS, "Salinity", "Temperature (C)", sel_col)
    
    # # ② 【枠サイズを固定するための修正】
    # fig_fixed_TS.update_layout(
    #     width=800,           # 全体の幅を固定
    #     height=600,          # 全体の高さを固定
        
    #     # マージンを「自動計算」させないよう、すべての値を明示的に固定します
    #     margin=dict(l=80, r=200, t=50, b=80, autoexpand=False), 
        
    #     coloraxis_colorbar=dict(
    #         x=1.02,          # グラフ枠の右端(1.0)のすぐ外側に固定
    #         xanchor='left',
    #         len=0.8,
    #         thickness=15,
    #         # タイトルなどが原因で枠が動かないよう設定
    #     ),
        
    #     # 軸の設定（ゼロラインをグレーに）
    #     xaxis=dict(
    #         zeroline=False, zerolinewidth=1, zerolinecolor='grey',
    #         range=[df1["Salinity"].min()*0.95, df1["Salinity"].max()*1.05] # 軸範囲を固定するとより安定します
    #     ),
    #     yaxis=dict(
    #         zeroline=False, zerolinewidth=1, zerolinecolor='grey',
    #         range=[df1["Temperature_degC"].min()-1, df1["Temperature_degC"].max()+1]
    #     )
    # )

    
    # # ③ 表示枠（窓枠）は 850 のままにする
    # # 窓(850)の中に小さな図(450)を入れるので、右端が切れることは物理的にあり得なくなります
    # selected_points = plotly_events(
    #     fig_fixed_TS, 
    #     select_event=True, 
    #     key="ts_zoom_event",
    #     override_height=600, 
    #     override_width=850
    # )
    
    # # --- 【選択個数の処理】 ---
    # if selected_points:
    #     st.session_state.ts_selected_indices = [p['pointIndex'] for p in selected_points]
    #     num_selected = len(selected_points)
    #     # 地図のすぐ上に個数を表示
    #     st.write(f"📊 **Number of selected points: {num_selected}**")
    # else:
    #     # 何も選択されていない場合は全データ（初期状態）
    #     st.session_state.ts_selected_indices = []
        
    
    # # --- 3. 地図の表示データ決定 ---
    # # 選択されているか判定
    # is_selected = len(st.session_state.ts_selected_indices) > 0

    # if is_selected:
    #     # 選択されたデータのみ
    #     df_ts_map_display = df1.iloc[st.session_state.ts_selected_indices]
    # else:
    #     # 初期状態は全データ（または特定のデフォルト範囲）
    #     df_ts_map_display = df1

    # # --- 4. 範囲とズームの計算 ---
    # lat_min, lat_max = df_ts_map_display["Latitude_degN"].min(), df_ts_map_display["Latitude_degN"].max()
    # lon_min, lon_max = df_ts_map_display["Longitude_degE"].min(), df_ts_map_display["Longitude_degE"].max()
    
    # # center_lat = (lat_min + lat_max) / 2
    # # center_lon = (lon_min + lon_max) / 2
    

    # lat_diff = lat_max - lat_min if lat_max != lat_min else 0.5
    # lon_diff = lon_max - lon_min if lon_max != lon_min else 0.5
    
    # #　地図の中心を設定
    # center_lat = df1['Latitude_degN'].mean()
    # center_lon = df1['Longitude_degE'].mean()
    
    
    # # 地図サイズに基づいたズーム計算
    # map_width_px = 850
    # map_height_px = 600
    # zoom_lon = math.log2((map_width_px * 360) / (lon_diff * 256))
    # zoom_lat = math.log2((map_height_px * 180) / (lat_diff * 256))
    
    # # 選択時はズーム、初期状態は少し引き気味にするなどの調整
    # auto_zoom = min(zoom_lon, zoom_lat) - (0.8 if is_selected else 1.5)
    # auto_zoom = max(1, min(15, auto_zoom))

    # # --- 5. 地図の描画 (常に実行) ---
    # fig_ts_map = px.scatter_mapbox(
    #     df_ts_map_display, 
    #     lat="Latitude_degN", lon="Longitude_degE", 
    #     color=target_item, color_continuous_scale=c_scale_final,
    #     mapbox_style="carto-positron",
    #     hover_data=["d18O",'dD',"Salinity",'Temperature_degC','Year','Month','Day','Cruise','Station','Depth_m','reference'],
    # )

    # fig_ts_map = unify_plot_layout(fig_ts_map, "Lon", "Lat", sel_col)
    
    # fig_ts_map.update_layout(
    #     mapbox=dict(
    #         center=dict(lat=center_lat, lon=center_lon),
    #         zoom=auto_zoom
            
    #     ),
    #     margin=dict(l=0, r=0, t=0, b=0),
    #     width=750,
    #     height=500
    # )
    
    
    

    
    # # 案内を出す
    # # st.info("T-S図で範囲を選択すると、その範囲にズームします。")
    # st.info("Select a range on the Salinity-δ18O Relationship  to zoom into that area on the map.")
    
    
    
    # # 地図背景の選択　envgeo_utilsｋara
    # #  モード選択（keyをユニークにする）
    # map_mode_ts = st.radio(
    #     "Map Style (d18O):", 
    #     ["Standard", "Satellite", "Bathymetry (Sea)", "Contour (GSI)"], 
    #     horizontal=True, key="ms_ts"
    # )

    
    # #  設定ファイルからスタイルを適用
    # fig_ts_map = envgeo_utils.apply_map_style(fig_ts_map, map_mode_ts)
    
    
    
    
    # # 地図を表示
    # # st.plotly_chart(fig_ts_map, use_container_width=False)
    

    # # ID重複を割けるために，Keyを追加。　修正後（一意のキーを追加）　
    # # マウスホイールでのズームが強制的に有効
    # st.plotly_chart(
    #     fig_ts_map, 
    #     use_container_width=True, # クラウドではTrueの方が見やすいです
    #     key="3d_visualizer_map_TS",
    #     config={'scrollZoom': True, 'displayModeBar': True} # ズームを有効化
    # )
    
        

    
    
    ###############################################################################################
    ############################################################################################### 
    ###############################################################################################
    ###############################################################################################

    # 区切り線
    # st.divider()
    
    
    ###############################################################################################
    ############################################################################################### 
    ###############################################################################################
    ###############################################################################################
    
    
    # from streamlit_plotly_events import plotly_events
    # import math

    # --- 1. セッション状態の初期化 ---
    if 'd18o_selected_indices' not in st.session_state:
        st.session_state.d18o_selected_indices = []

    st.subheader('Salinity - δ18O Relationship & Auto-Zoom Map')

    # カラー設定
    col_map = {"d18O": "d18O", "Latitude": "Latitude_degN", "Longitude": "Longitude_degE", "Water Depth": "Depth_m"}
    sel_col_d18o = st.radio("Select color element (δ18O plot):", list(col_map.keys()), horizontal=True, key="fig_d18O_zoom")
    target_item = col_map[sel_col_d18o]
    c_scale_final = envgeo_utils.get_custom_colorscale(target_item)

    # --- 2. Salinity - δ18O 図の描画 ---
    fig_d18O = px.scatter(
        df1, x="Salinity", y="d18O", 
        color=target_item, color_continuous_scale=c_scale_final,
        hover_data=[
                    "lat",  
                    "lon",  
                    "d18O", 
                    "dD", 
                    "Salinity", 
                    "Temperature_degC", 
                    "Year", 
                    "Month", 
                    "Day", 
                    "Cruise", 
                    "Station",
                    "Depth_m",
                    "reference",  
                    ]
    )
    
    fig_d18O = unify_plot_layout(fig_d18O, "Salinity", "δ18O (‰)", sel_col_d18o)
    
    # レイアウト固定設定
    fig_d18O.update_layout(
        width=800, 
        margin=dict(l=80, r=200, t=50, b=80, autoexpand=False), 
        coloraxis_colorbar=dict(x=1.02, xanchor='left', len=0.8),
        xaxis=dict(
            zeroline=False, zerolinewidth=1, zerolinecolor='grey',
            showline=True, linewidth=1, linecolor='grey', mirror=True,
            range=[df1["Salinity"].min()*0.95, df1["Salinity"].max()*1.05]
        ),
        yaxis=dict(
            zeroline=False, zerolinewidth=1, zerolinecolor='grey',
            showline=True, linewidth=1, linecolor='grey', mirror=True,
            range=[df1["d18O"].min()-0.5, df1["d18O"].max()+0.5]
        )
    )

    selected_points_d18o = plotly_events(
        fig_d18O, select_event=True, key="d18o_zoom_event",
        override_height=600, override_width=850
    )

        
        # --- 【個数表示とセッション更新の処理】 ---
    if selected_points_d18o:
        st.session_state.d18o_selected_indices = [p['pointIndex'] for p in selected_points_d18o]
        num_selected_d18o = len(selected_points_d18o)
        # 地図のすぐ上に個数を太字で表示
        st.write(f"📊 **Number of selected points: {num_selected_d18o}**")
    else:
        st.session_state.d18o_selected_indices = []
        

    # --- 3. 地図の表示データ決定 ---
    is_selected = len(st.session_state.d18o_selected_indices) > 0
    df_map_d18o = df1.iloc[st.session_state.d18o_selected_indices] if is_selected else df1

    # --- 4. 範囲とズームの計算 (TypeError修正済み) ---
    lat_min, lat_max = df_map_d18o["Latitude_degN"].min(), df_map_d18o["Latitude_degN"].max()
    lon_min, lon_max = df_map_d18o["Longitude_degE"].min(), df_map_d18o["Longitude_degE"].max()
    
    # 分けて計算
    # center_lat = (lat_min + lat_max) / 2
    # center_lon = (lon_min + lon_max) / 2
    
    #　地図の中心を設定
    center_lat = df1['Latitude_degN'].mean()
    center_lon = df1['Longitude_degE'].mean()
    
    
    lat_diff = max(lat_max - lat_min, 0.1)
    lon_diff = max(lon_max - lon_min, 0.1)
    
    # ズーム計算
    zoom_lon = math.log2((850 * 360) / (lon_diff * 256))
    zoom_lat = math.log2((600 * 180) / (lat_diff * 256))
    auto_zoom = min(zoom_lon, zoom_lat) - (0.8 if is_selected else 1.5)
    auto_zoom = max(1, min(15, auto_zoom))

    # --- 5. 地図の描画 ---
    fig_map_d18o = px.scatter_mapbox(
        df_map_d18o, lat="Latitude_degN", lon="Longitude_degE", 
        color=target_item, color_continuous_scale=c_scale_final,
        mapbox_style="carto-positron",
        hover_data=["d18O",'dD',"Salinity",'Temperature_degC','Year','Month','Day','Cruise','Station','Depth_m','reference'],
    )
    fig_map_d18o = unify_plot_layout(fig_map_d18o, "Lon", "Lat", sel_col_d18o)
    fig_map_d18o.update_layout(
        mapbox=dict(center=dict(lat=center_lat, lon=center_lon), zoom=auto_zoom),
        margin=dict(l=0, r=0, t=0, b=0), width=750, height=500
    )
    
    
    
    
    # 案内を出す
    # st.info("T-S図で範囲を選択すると、その範囲にズームします。")
    st.info("Select a range on the Salinity-δ18O Relationship  to zoom into that area on the map.")
    
    
    
    # 地図背景の選択　envgeo_utilsｋara
    #  モード選択（keyをユニークにする）
    map_mode_d18o = st.radio(
        "Map Style (d18O):", 
        ["Standard", "Satellite", "Bathymetry (Sea)", "Contour (GSI)"], 
        horizontal=True, key="ms_d18o"
    )

    
    #  設定ファイルからスタイルを適用
    fig_map_d18o = envgeo_utils.apply_map_style(fig_map_d18o, map_mode_d18o)
    


    
    # 地図を表示
    # st.plotly_chart(fig_map_d18o, use_container_width=False)
    
    
    # ID重複を割けるために，Keyを追加。　修正後（一意のキーを追加）　
    # マウスホイールでのズームが強制的に有効
    st.plotly_chart(
        fig_map_d18o, 
        use_container_width=True, # クラウドではTrueの方が見やすいです
        key="3d_visualizer_map_d18O",
        config={'scrollZoom': True, 'displayModeBar': True} # ズームを有効化
    )
    
    
    #htmlで書き出す場合
    # fig_map_d18o.write_html('filename.html')
    
    

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

    # 区切り線
    # st.divider()
    
    
    ###############################################################################################
    ############################################################################################### 
    ###############################################################################################
    ###############################################################################################
        
if __name__ == '__main__':
    main()
    








