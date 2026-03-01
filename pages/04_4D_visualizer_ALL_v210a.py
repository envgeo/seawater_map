
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
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import envgeo_utils    # 作った設定ファイルを読み込む
import math

print(f"--------04_4D_visualizer_{version}--------")


# datetimeモジュールを使った現在の日付と時刻の取得
import datetime
dt = datetime.datetime.today()  # ローカルな現在の日付と時刻を取得
print(dt)  # 2021-10-29 15:58:08.356501




############論文データ追加用の設定############
# #　足りなくなれば追加で，
# Transect001 = 'Pacific'
# Transect002 = 'Pacific_west'
# Transect003 = 'Noto'
# Transect004 = 'Toyama'
# Transect005 = 'SI'
# Transect006 = 'Yamato'
# Transect007 = 'Shimane&Tottori'
# Transect008 = 'NA2'
# Transect009 = 'Tsushima'							  
# Transect010 = 'nECS'						  
# Transect011 = 'CK'						  
# Transect012 = 'ECS2021'							  
# Transect013 = 'sECS'					  
# Transect014 = 'Nansei'
# Transect015 = 'KUWANO'
# Transect016 = 'Yamamoto_2001'
# Transect017 = 'Sakamoto_2019'
# Transect018 = 'Kodaira_2016'
# Transect019 = 'Horikawa_2023'
# # Transect020 = 'ここの新規項目を入力'
# # Transect021 = 'ここの新規項目を入力'
# # Transect022 = 'ここの新規項目を入力'
# # Transect023 = 'ここの新規項目を入力'
# # Transect024 = 'ここの新規項目を入力'
# # Transect025 = 'ここの新規項目を入力'
# # Transect026 = 'ここの新規項目を入力'
# # Transect027 = 'ここの新規項目を入力'
# # Transect028 = 'ここの新規項目を入力'
# # Transect029 = 'ここの新規項目を入力'
# # Transect030 = 'ここの新規項目を入力'



############ページタイトル設定############

# st.set_page_config(
#     page_title="d18O mapping",
#     # page_icon="🗾",
#     layout="wide"
#     )


# @st.cache_resource(experimental_allow_widgets=True)

def main():
    
    # 注意書き
    st.header(f'4D visualizer ({version})')
    # st.write('Kodama et al. (2024), Yamamoto et al. (2001), Sakamoto et al. (2019), Kodaira et al. (2016), Horikawa et al. (2023)')
    
    

    ############################################################
    # リロードボタン
    st.button('Reload')
    
    
        

    # データソースの変数、envgeo_utilsから読み出す
    data_source_JAPAN_SEA = envgeo_utils.data_source_JAPAN_SEA
    data_source_AROUND_JAPAN = envgeo_utils.data_source_AROUND_JAPAN
    data_source_GLOBAL = envgeo_utils.data_source_GLOBAL
    

    # データソース選択
    ref_data = st.radio("data source (see home>about):", (data_source_JAPAN_SEA, data_source_AROUND_JAPAN, data_source_GLOBAL), horizontal=True, args=[1, 0])




    # sheet_num = 1
    # df1 = pd.read_excel(excel_file, sheet_name=sheet_num)
    df1 = envgeo_utils.load_isotope_data(ref_data)
    # df1 = df_fig_ALL

    
    
    
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
        
        #################文献選択ここから###########################################
        
        
        # st.subheader('data source:')
        
        # ref_data = st.radio("data source (see home>about):", (data_source_JAPAN_SEA, data_source_AROUND_JAPAN), horizontal=True, args=[1, 0])
        
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
        
    
    
    
        st.subheader(':blue[--- for fig scale only ---]')
        # st.sidebar.subheader('描画水深の範囲')
        fig_depth_min, fig_depth_max = st.slider(label='Depth scale',
                                    min_value=0,
                                    max_value=9000,
                                    value=(0, 9000),
                                    )


                            
        submitted = st.form_submit_button(":red[submit!]")

##############################################################################
# サイドバーここまで
##############################################################################



        # キャッシュのクリア　サイドバーの一番下などに配置
        st.sidebar.markdown("---") # 区切り線
        if st.sidebar.button("🔄 clear cache"):
            envgeo_utils.clear_app_cache()
            # st.sidebar.success("キャッシュをクリアしました！再読み込みします...")
            st.rerun() # アプリを再実行して最新のExcelを読み込ませる
        
        
        

    ###################################################################################################### 
    
    # 注意書き
    
    # if ref_data == data_source_JAPAN_SEA:
    #     st.write(':blue[data source:]  Kodama et al. (2024)')
        
    # elif ref_data == data_source_AROUND_JAPAN:
    #     # st.text('including data from previous reports')
    #     st.write(':blue[data source:] Kodama et al. (2024), Yamamoto et al. (2001), Sakamoto et al. (2019), Kodaira et al. (2016), Horikawa et al. (2023).')

        
    # else:
    #     # st.text('including data from previous reports')

    #     st.write(':blue[data source:] Kodama et al. (2024), Yamamoto et al. (2001), Sakamoto et al. (2019), Kodaira et al. (2016), Horikawa et al. (2023).')
    #     st.write(':blue[with:] NASA_database (Jan.23, 2025)]https://data.giss.nasa.gov/cgi-bin/o18data/geto18.cgi')





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
        
        
            
    
    ###################################################################################################### 
    
    
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
        
    # else:
    #     excel_file = 'd18O_NASA_全データ_Python_20250123.xlsx'
    


    # sheet_num = 1
    
    # df = pd.read_excel(excel_file, sheet_name=sheet_num)
    
    
    
    
    
    # """選択描画範囲の設定用"""
    def data_limit():
    
            # sheet_num = 1
            # df1 = pd.read_excel(excel_file, sheet_name=sheet_num)
            df1 = envgeo_utils.load_isotope_data(ref_data)
            # df1 = df_fig_ALL
        
        
            # エラーデータの通知
            removed = df1.attrs.get('removed_count', 0)
            #total = df1.attrs.get('total_count', 0)
            
            #count_text = str(len(df1["d18O"]))
            count_text = str(len(df1))
            # もし欠損値(NaN)を除いた有効なデータ点数を出したい場合
            # count_text = str(df1["d18O"].notna().sum())
            
            if removed > 0:
                # サイドバーに黄色い警告で表示（目立ちます）
                st.sidebar.warning(f"⚠️ データクリーニング通知\n\n不備データ {removed} 件を除外しました。\n(有効データ: {len(df1)} / 全 {total} 件)")
            else:
                # st.sidebar.success(f"✅ 全 {total} 件のデータを正常に読み込みました。")
                # st.sidebar.success(f"✅ Successfully loaded {total} records.")
                st.sidebar.success(f"✅ Successfully loaded {count_text} records.")
        
        
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
              
            # else:
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
            
                    
            df1 = df1[(df1['Temperature_degC'] == 'xxx') 
                        
                        |(df1['Temperature_degC'] <= sld_temp_max) & (df1['Temperature_degC'] >= sld_temp_min )#調整用
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
    
    
    #地図にポップアッププロット
    # for i, row in df1.iterrows():
    #     pop=f"Transect:{row['Transect']} <br> Lon: {row['Longitude_degE']}E <br> Lat: {row['Latitude_degN']}N <br> Depth: {row['Depth_m']}m <br> Date: {row['Date']} <br> Cruise: {row['Cruise']} <br> Station: {row['Station']} <br> Salinity: {row['Salinity']} <br> Temp: {row['Temperature_degC']} <br> d18O: {row['d18O']} <br> dD: {row['dD']}" 
    #     folium.Marker(
    #         # 緯度と経度を指定
    #         location=[row['lat'], row['lon']],
    #         # ツールチップの指定(都道府県名)
    #         tooltip=row['d18O'],
    #         # ポップアップの指定
    #         popup=folium.Popup(pop, max_width=300),
    #         # アイコンの指定(アイコン、色)
    #         icon=folium.Icon(icon_color="white", color="red")
    #     ).add_to(m)
    
    
    # call to render Folium map in Streamlit
    # folium_static(m, width=800, height=800)
    # folium_static(m)
    # st.map(df)



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
    
    ###############################################################################################
    ###### Fig1 #######
    ###############################################################################################
    # st.subheader('4D salinity-d18O-depth-temperature')
    color_continuous_scale= ('darkblue', 'blue', 'lightgray', 'gray', 'lightgreen', 'lightgreen', 'green',  'yellow', 'orange', 'red','darkred','darkred')
   
    fig1=px.scatter_3d(df1, x='Salinity', y='d18O', z='Depth_m',
                    color='Temperature_degC', 
                    #symbol='species'
                    width=700,
                    height=600,
                    color_continuous_scale=color_continuous_scale,
                    
                    
                    #############################ポップアップ情報ここから##########################
                    hover_data={
                        "lat": True,  # 名前を表示
                        "lon": True,  # 値を表示
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
                    }
                    #############################ポップアップ情報ここまで##########################
                )
                


    # マーカー、ラインの設定
    fig1.update_traces(
        # mode = 'markers+lines', # 'markers+lines', 'markers'
        mode = 'markers', # 'markers+lines', 'markers'
        marker = dict(size = 3),
        # line = dict(width = 2), #color = 'Black',
    )
    

    
    fig1.update_layout(
            scene = dict(
        # #各軸の範囲
        # xaxis = dict(range=[145,120],),
        # yaxis = dict(range=[45,20],),

        #各軸のタイトル
        xaxis_title='salinity',
        yaxis_title='d18O',
        zaxis_title='Water Depth',
        ),
        width=700,
        # margin=dict(r=20, l=10, b=10, t=10),

            )

          # fig1= px.scatter_3d(df1, x='lat', y='lon', z='Depth_m',
          #                color='d18O', 
          #                # colors=list_colors,
          #                #symbol='species'
          #                width=700,
          #                height=600,
          #            )
                   
          # fig1.update_layout(
          #       scene = dict(
          #           xaxis = dict(range=[125,145],),
          #           yaxis = dict(range=[45,25],),
          #           zaxis = dict(range=[-1000,0],),
          #       )
          #       )



    ###水深をスケールバーで変える設定
    fig_depth_max_minus = fig_depth_max*(-1)
    fig_depth_min_minus = fig_depth_min*(-1)
    
    
    
    # --- fig2 個別のカスタマイズ（角度とアスペクト比） ---
    fig1.update_layout(
        scene=dict(
            # アスペクト比を個別に設定 (x, y, z の比率を自由に変えられます)
            # 例：xを長くして横長に見せたい場合
            aspectmode='manual',
            aspectratio=dict(x=1, y=1, z=1), 
            
            # カメラ設定（斜め上・反対側）
            camera=dict(
                eye=dict(x=-0.6, y=-1.1, z=1.9),
                center=dict(x=0, y=0, z=-0.1)
            )
        )
    )
    
    
    
    ##図のスケール
    fig1.update_layout(
            scene = dict(
        # #各軸の範囲
        # xaxis = dict(range=[36,20],),
        # yaxis = dict(range=[+1,-4],),
        zaxis = dict(range=[fig_depth_max_minus,fig_depth_min_minus],),


        ),
        width=700,
        height=600,
        # margin=dict(r=20, l=10, b=10, t=10),

            )


    # st.write(fig1)
    # st.plotly_chart(fig1, use_container_width=True)  # ブラウザの幅に合わせる


    
    ###############################################################################################
    ############################################################################################### 
    ###############################################################################################
    ###############################################################################################

    ###############################################################################################
    ###### Fig2 #######
    ###############################################################################################
    # st.subheader('4D salinity-temperature-depth-d18O')
    color_continuous_scale= ('darkblue', 'darkblue', 'darkblue','darkblue', 'darkblue',  'blue', 'blue', 'blue','lightgray', 'lightgray', 'gray', 'lightgreen', 'lightgreen', 'green',  'yellow', 'orange', 'red','darkred')
   
    fig2=px.scatter_3d(df1, x='Salinity', y='Temperature_degC', z='Depth_m',
                    color='d18O', 
                    #symbol='species'
                    width=700,
                    height=600,
                    color_continuous_scale=color_continuous_scale,
                    
                    #############################ポップアップ情報ここから##########################
                    hover_data={
                        "lat": True,  # 名前を表示
                        "lon": True,  # 値を表示
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
                    }
                    #############################ポップアップ情報ここまで##########################
                    
                )
                


    # マーカー、ラインの設定
    fig2.update_traces(
        # mode = 'markers+lines', # 'markers+lines', 'markers'
        mode = 'markers', # 'markers+lines', 'markers'
        marker = dict(size = 3),
        # line = dict(width = 2), #color = 'Black',
    )
    

    
    fig2.update_layout(
            scene = dict(
        # #各軸の範囲
        # xaxis = dict(range=[145,120],),
        # yaxis = dict(range=[45,20],),

        #各軸のタイトル
        xaxis_title='salinity',
        yaxis_title='temperature(C)',
        zaxis_title='Water Depth',
        ),
        width=700,
        # margin=dict(r=20, l=10, b=10, t=10),

            )

          # fig2= px.scatter_3d(df1, x='lat', y='lon', z='Depth_m',
          #                color='d18O', 
          #                # colors=list_colors,
          #                #symbol='species'
          #                width=700,
          #                height=600,
          #            )
                   
          # fig2.update_layout(
          #       scene = dict(
          #           xaxis = dict(range=[125,145],),
          #           yaxis = dict(range=[45,25],),
          #           zaxis = dict(range=[-1000,0],),
          #       )
          #       )


    ###水深をスケールバーで変える設定
    fig_depth_max_minus = fig_depth_max*(-1)
    fig_depth_min_minus = fig_depth_min*(-1)
    
    
    

    
    # --- fig2 個別のカスタマイズ（角度とアスペクト比） ---
    fig2.update_layout(
        scene=dict(
            # アスペクト比を個別に設定 (x, y, z の比率を自由に変えられます)
            # 例：xを長くして横長に見せたい場合
            aspectmode='manual',
            aspectratio=dict(x=1, y=1, z=1), 
            
            # カメラ設定（斜め上・反対側）
            camera=dict(
                eye=dict(x=-0.6, y=-1.1, z=1.9),
                center=dict(x=0, y=0, z=-0.1)
            )
        )
    )
    
    
    ##図のスケール

    fig2.update_layout(
            scene = dict(
        # #各軸の範囲
        # xaxis = dict(range=[36,20],),
        # yaxis = dict(range=[30,0],),
        zaxis = dict(range=[fig_depth_max_minus,fig_depth_min_minus],),


        ),
        width=700,
        height=600,
        # margin=dict(r=20, l=10, b=10, t=10),

            )







    # st.write(Fig2)
    # st.plotly_chart(fig2, use_container_width=True)  # ブラウザの幅に合わせる
    

    
    ###############################################################################################
    ############################################################################################### 
    ###############################################################################################
    ###############################################################################################

    ###############################################################################################
    ###### Fig3 #######
    ###############################################################################################
    # st.subheader('4D map-depth-d18O')
    
    # import plotly.graph_objects as go

    # データの準備（サンプルデータとしてランダムな3Dデータを生成）
    y = df1['lat']
    x = df1['lon']
    z = df1['Depth_m']
    c = df1['d18O']
    
    # # 海岸線の座標データを手動で用意
    # coastline_excel = 'world_coastline_coordinates_50m.xlsx'
    # coastline_df = pd.read_excel(coastline_excel, sheet_name=0)
    # coastline_y = coastline_df['Latitude']  # 海岸線のx座標
    # coastline_x = coastline_df['Longitude']  # 海岸線のy座標  
    

    # --- envgeo_utils を使って読み込み ---
    coastline_x, coastline_y = envgeo_utils.load_coastline_data(ref_data)
    
    

    # color_continuous_scale= ('gray', 'gray', 'gray', 'gray', 'lightgray', 'lightgray', 'lightgray', 'lightgreen', 'lightgreen', 'green', 'green', 'blue', 'lightblue', 'yellow', 'orange', 'red')
    color_continuous_scale= ('darkblue', 'darkblue', 'darkblue','darkblue', 'darkblue',  'blue', 'blue', 'blue','lightgray', 'lightgray', 'gray', 'lightgreen', 'lightgreen', 'green',  'yellow', 'orange', 'red','darkred')

    
    # 3Dプロットを作成する
    
    fig3=px.scatter_3d(df1, x='lon', y='lat', z='Depth_m',
                    color='d18O', 
                    #symbol='species'
                    width=700,
                    height=600,
                    color_continuous_scale=color_continuous_scale,
                    
                    #############################ポップアップ情報ここから##########################
                    hover_data={
                        "lat": True,  # 名前を表示
                        "lon": True,  # 値を表示
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
                    }
                    #############################ポップアップ情報ここまで##########################
                    
                )
    # fig3 = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='markers', 
    #         marker=dict(
    #         size=16,
    #         color=c,  # マーカーの色をyにする
    #         colorscale=color_continuous_scale,  # カラースケール変更
    #         showscale=True,  # カラーバーの表示
    #         # カラーバーの設定
    #         colorbar=dict(
    #         # x=0.2, 
    #         title="d18O",
    #         # 枠線、目盛線の設定
    #         outlinecolor='black', ticks='outside', tickcolor='black',
    #         len=0.8,
    #         thicknessmode='fraction',  # カラーバーの幅の指定方法を割合モードに設定
    #         thickness=0.02,  # カラーバーの幅（割合モードで0〜1の範囲で指定）
    #     ),
    #     ))])
    
    # fig11.update_layout(coloraxis=dict(colorbar=dict(len=0.5)))
    
    

    
    
    
    # マーカー、ラインの設定
    fig3.update_traces(
        # mode = 'markers+lines', # 'markers+lines', 'markers'
        mode = 'markers', # 'markers+lines', 'markers'
        marker = dict(size = 3),
        # line = dict(width = 2), #color = 'Black',
        name='d18O'
        )
        
    
    
    
    ###水深をスケールバーで変える設定
    fig_depth_max_minus = fig_depth_max*(-1)
    fig_depth_min_minus = fig_depth_min*(-1)


    # ##図のスケール

    # fig3.update_layout(
    #         scene = dict(
    #     # #各軸の範囲
    #     # xaxis = dict(range=[180,120],),
    #     # yaxis = dict(range=[55,20],),
    #     zaxis = dict(range=[fig_depth_max_minus, fig_depth_min_minus],),
    #     aspectratio=dict(x=2, y=1, z=1),  # 各軸方向のスケールを指定

    #     #各軸のタイトル
    #     yaxis_title='Latitude N',
    #     xaxis_title='Longitude E',
    #     zaxis_title='Water Depth',
    #     ),
    #     width=700,
    #     height=600,
    #     # margin=dict(r=20, l=10, b=10, t=10),

    #         )
    
    
    # # 3Dプロットのレイアウト設定
    # fig3.update_layout(
    #     scene=dict(
    #         # アスペクト比を手動設定に
    #         aspectmode='manual',
    #         aspectratio=dict(x=1, y=1, z=1), # zを小さくすると深度方向が強調されすぎず綺麗です
            
    #         # 軸のタイトル設定（既存のものを維持）
    #         xaxis_title='Longitude E',
    #         yaxis_title='Latitude N',
    #         zaxis_title='Water Depth',
    #     ),
    #     width=700,
    #     height=600,
    # )
    
    
    
    #     # --- 表示モードに応じたレイアウトパラメータの設定 ---
    # if ref_data == data_source_GLOBAL:
    #     # NASA（世界規模）の設定
    #     # 世界地図は横に長いため x=2 に設定
    #     target_aspectratio = dict(x=2, y=1, z=1)
    #     target_aspectmode = 'manual'
    #     # NASAの時は軸範囲を自動（コメントアウトの状態）にするか、広域に設定
    #     x_range = None 
    #     y_range = None
    # else:
    #     # 日本周辺の設定
    #     target_aspectratio = dict(x=1, y=1, z=1)
    #     target_aspectmode = 'manual'
    #     # 必要に応じて日本近海の範囲を固定する場合
    #     x_range = [120, 160] # 例
    #     y_range = [20, 60]   # 例
    
    # # --- レイアウトの一括更新 ---
    # fig3.update_layout(
    #     scene=dict(
    #         # アスペクト比の設定
    #         aspectmode=target_aspectmode,
    #         aspectratio=target_aspectratio,
            
    #         # 軸の範囲設定（z軸は共通の変数を利用）
    #         zaxis=dict(range=[fig_depth_max_minus, fig_depth_min_minus]),
    #         # NASA以外で範囲を固定したい場合は以下を有効化
    #         xaxis=dict(range=x_range) if x_range else dict(),
    #         yaxis=dict(range=y_range) if y_range else dict(),
    
    #         # 軸のタイトル
    #         xaxis_title='Longitude E',
    #         yaxis_title='Latitude N',
    #         zaxis_title='Water Depth',
    #     ),
    #     width=700,
    #     height=600,
    #     # margin=dict(r=20, l=10, b=10, t=10),
    # )
    
    
    # --- envgeo_utilsから呼び出して，レイアウトの一括更新 ---
     # 1. まず変数を定義する（NASAなどの場合は None、日本近海なら数値が入るように）
    if ref_data == data_source_GLOBAL:
        x_range = None
        y_range = None
    else:
        x_range = [120, 160] # デフォルトの日本近海範囲
        y_range = [20, 60]
    
    # 2. その後で共通レイアウトを呼び出す
    fig3 = envgeo_utils.apply_common_layout(
        fig3, 
        ref_data, 
        fig_depth_max_minus, 
        fig_depth_min_minus, 
        x_range=x_range, 
        y_range=y_range
    )
    
    
    
    # 海岸線を底面に追加する
    # データの最上部の場合
    fig3.add_traces(go.Scatter3d(x=coastline_x, y=coastline_y, z=[max(z)] * len(coastline_x), mode='lines',     marker = dict(size = 3),
        # line = dict(width = 2), #color = 'Black',
        name='coastline', line=dict(color='blue', width=0.8),
        hoverinfo='none' # 海岸線にカーソルが当たっても邪魔しない
        ))
    #スケールの底面の場合
    fig3.add_traces(go.Scatter3d(x=coastline_x, y=coastline_y, z=[fig_depth_max_minus] * len(coastline_x), mode='lines',     marker = dict(size = 3),
        # line = dict(width = 2), #color = 'Black',
        name='coastline', line=dict(color='gray', width=0.5),
        hoverinfo='none' # 海岸線にカーソルが当たっても邪魔しない
        ))
    
    
    
    # グラフを表示する
    # fig.show()
    # st.write(fig3)
    # st.plotly_chart(fig3, use_container_width=True)  # ブラウザの幅に合わせる
    
    
        
    ###############################################################################################
    ############################################################################################### 
    ###############################################################################################
    ###############################################################################################
    
    ###############################################################################################
    ###### Fig4 #######
    ###############################################################################################
    # st.subheader('4D map-depth-temperature')
    
    # import plotly.graph_objects as go

    # # データの準備（サンプルデータとしてランダムな3Dデータを生成）
    y = df1['lat']
    x = df1['lon']
    z = df1['Depth_m']
    c = df1['Temperature_degC']
    # # 海岸線の座標データを手動で用意
    # coastline_excel = 'world_coastline_coordinates_50m.xlsx'
    # coastline_df = pd.read_excel(coastline_excel, sheet_name=0)
    # coastline_y = coastline_df['Latitude']  # 海岸線のx座標
    # coastline_x = coastline_df['Longitude']  # 海岸線のy座標  


    # --- envgeo_utils を使って読み込み ---
    coastline_x, coastline_y = envgeo_utils.load_coastline_data(ref_data)

    # color_continuous_scale= ('gray', 'gray', 'gray', 'gray', 'lightgray', 'lightgray', 'lightgray', 'lightgreen', 'lightgreen', 'green', 'green', 'blue', 'lightblue', 'yellow', 'orange', 'red')
    color_continuous_scale= ('darkblue', 'darkblue', 'darkblue','darkblue', 'darkblue',  'blue', 'blue', 'blue','lightgray', 'lightgray', 'gray', 'lightgreen', 'lightgreen', 'green',  'yellow', 'orange', 'red','darkred')



    # 3Dプロットを作成する
    
    fig4=px.scatter_3d(df1, x='lon', y='lat', z='Depth_m',
                    color='Temperature_degC', 
                    #symbol='species'
                    width=700,
                    height=600,
                    color_continuous_scale=color_continuous_scale,
                    
                    #############################ポップアップ情報ここから##########################
                    hover_data={
                        "lat": True,  # 名前を表示
                        "lon": True,  # 値を表示
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
                    }
                    #############################ポップアップ情報ここまで##########################
                )
    
    # fig4 = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='markers', 
    #         marker=dict(
    #         size=16,
    #         color=c,  # マーカーの色をyにする
    #         colorscale=color_continuous_scale,  # カラースケール変更
    #         showscale=True,  # カラーバーの表示
    #         # カラーバーの設定
    #         colorbar=dict(
    #         # x=0.2, 
    #         title="Temperature(C)",
    #         # 枠線、目盛線の設定
    #         outlinecolor='black', ticks='outside', tickcolor='black',
    #         len=0.8,
    #         thicknessmode='fraction',  # カラーバーの幅の指定方法を割合モードに設定
    #         thickness=0.02,  # カラーバーの幅（割合モードで0〜1の範囲で指定）
    #     ),
    #     ))])
    
    # fig11.update_layout(coloraxis=dict(colorbar=dict(len=0.5)))
    
    
    # マーカー、ラインの設定
    fig4.update_traces(
        # mode = 'markers+lines', # 'markers+lines', 'markers'
        mode = 'markers', # 'markers+lines', 'markers'
        marker = dict(size = 3),
        # line = dict(width = 2), #color = 'Black',
        name='Temperature'
        )
        
    
    
    
    
    ###水深をスケールバーで変える設定
    fig_depth_max_minus = fig_depth_max*(-1)
    fig_depth_min_minus = fig_depth_min*(-1)


    ##図のスケール

    # fig4.update_layout(
    #         scene = dict(
    #     # #各軸の範囲
    #     # xaxis = dict(range=[180,120],),
    #     # yaxis = dict(range=[55,20],),
    #     zaxis = dict(range=[fig_depth_max_minus, fig_depth_min_minus],),
    #     aspectratio=dict(x=2, y=1, z=1),  # 各軸方向のスケールを指定

    #     #各軸のタイトル
    #     yaxis_title='Latitude N',
    #     xaxis_title='Longitude E',
    #     zaxis_title='Water Depth',
    #     ),
    #     width=700,
    #     height=600,
    #     # margin=dict(r=20, l=10, b=10, t=10),

    #         )
    
    
    
    
    #     # --- 表示モードに応じたレイアウトパラメータの設定 ---
    # if ref_data == data_source_GLOBAL:
    #     # NASA（世界規模）の設定
    #     # 世界地図は横に長いため x=2 に設定
    #     target_aspectratio = dict(x=2, y=1, z=1)
    #     target_aspectmode = 'manual'
    #     # NASAの時は軸範囲を自動（コメントアウトの状態）にするか、広域に設定
    #     x_range = None 
    #     y_range = None
    # else:
    #     # 日本周辺の設定
    #     target_aspectratio = dict(x=1, y=1, z=1)
    #     target_aspectmode = 'manual'
    #     # 必要に応じて日本近海の範囲を固定する場合
    #     x_range = [120, 160] # 例
    #     y_range = [20, 60]   # 例
    
    # # --- レイアウトの一括更新 ---
    # fig4.update_layout(
    #     scene=dict(
    #         # アスペクト比の設定
    #         aspectmode=target_aspectmode,
    #         aspectratio=target_aspectratio,
            
    #         # 軸の範囲設定（z軸は共通の変数を利用）
    #         zaxis=dict(range=[fig_depth_max_minus, fig_depth_min_minus]),
    #         # NASA以外で範囲を固定したい場合は以下を有効化
    #         xaxis=dict(range=x_range) if x_range else dict(),
    #         yaxis=dict(range=y_range) if y_range else dict(),
    
    #         # 軸のタイトル
    #         xaxis_title='Longitude E',
    #         yaxis_title='Latitude N',
    #         zaxis_title='Water Depth',
    #     ),
    #     width=700,
    #     height=600,
    #     # margin=dict(r=20, l=10, b=10, t=10),
    # )
    
    
    
    

    # --- envgeo_utilsから呼び出して，レイアウトの一括更新 ---
     # 1. まず変数を定義する（NASAなどの場合は None、日本近海なら数値が入るように）
    if ref_data == data_source_GLOBAL:
        x_range = None
        y_range = None
    else:
        x_range = [120, 160] # デフォルトの日本近海範囲
        y_range = [20, 60]
    
    # 2. その後で共通レイアウトを呼び出す
    fig4 = envgeo_utils.apply_common_layout(
        fig4, 
        ref_data, 
        fig_depth_max_minus, 
        fig_depth_min_minus, 
        x_range=x_range, 
        y_range=y_range
    )
    
    
    
    # 海岸線を底面に追加する
    # データの最上部の場合
    fig4.add_traces(go.Scatter3d(x=coastline_x, y=coastline_y, z=[max(z)] * len(coastline_x), mode='lines',     marker = dict(size = 3),
        # line = dict(width = 2), #color = 'Black',
        name='coastline', line=dict(color='blue', width=0.8),
        hoverinfo='none' # 海岸線にカーソルが当たっても邪魔しない
        ))
    
    #スケールの底面の場合
    fig4.add_traces(go.Scatter3d(x=coastline_x, y=coastline_y, z=[fig_depth_max_minus] * len(coastline_x), mode='lines',     marker = dict(size = 3),
        # line = dict(width = 2), #color = 'Black',
        name='coastline', line=dict(color='gray', width=0.5),
        hoverinfo='none' # 海岸線にカーソルが当たっても邪魔しない
        ))
    
    
    
    # グラフを表示する
    # fig.show()
    # st.write(fig4)
    # st.plotly_chart(fig4, use_container_width=True)  # ブラウザの幅に合わせる
    
    
    
        
    ###############################################################################################
    ############################################################################################### 
    ###############################################################################################
    ###############################################################################################
    
    ###############################################################################################
    ###### Fig5 #######
    ###############################################################################################
    # st.subheader('4D map-depth-salinity')
    
    # import plotly.graph_objects as go

    # データの準備（サンプルデータとしてランダムな3Dデータを生成）
    # y = df1['lat']
    # x = df1['lon']
    # z = df1['Depth_m']
    # c = df1['Salinity']
    # 海岸線の座標データを手動で用意
    # coastline_excel = 'world_coastline_coordinates_50m.xlsx'
    # coastline_df = pd.read_excel(coastline_excel, sheet_name=0)
    # coastline_y = coastline_df['Latitude']  # 海岸線のx座標
    # coastline_x = coastline_df['Longitude']  # 海岸線のy座標  
    
    # --- envgeo_utils を使って読み込み ---
    coastline_x, coastline_y = envgeo_utils.load_coastline_data(ref_data)
    
    # color_continuous_scale= ('gray', 'gray', 'gray', 'gray', 'lightgray', 'lightgray', 'lightgray', 'lightgreen', 'lightgreen', 'green', 'green', 'blue', 'lightblue', 'yellow', 'orange', 'red')
    color_continuous_scale= ('darkblue', 'darkblue', 'darkblue', 'blue', 'blue', 'blue','lightgray', 'lightgray', 'gray',  'gray', 'lightgreen', 'lightgreen', 'green',  'green', 'yellow', 'orange', 'red','darkred')

    
    # 3Dプロットを作成する
    
    fig5=px.scatter_3d(df1, x='lon', y='lat', z='Depth_m',
                    color='Salinity', 
                    #symbol='species'
                    width=700,
                    height=600,
                    color_continuous_scale=color_continuous_scale,
                    
                    #############################ポップアップ情報ここから##########################
                    hover_data={
                        "lat": True,  # 名前を表示
                        "lon": True,  # 値を表示
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
                    }
                    #############################ポップアップ情報ここまで##########################
                )
    
    # fig5 = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='markers', 
    #         marker=dict(
    #         size=16,
    #         color=c,  # マーカーの色をyにする
    #         colorscale=color_continuous_scale,  # カラースケール変更
    #         showscale=True,  # カラーバーの表示
    #         # カラーバーの設定
    #         colorbar=dict(
    #         # x=0.2, 
    #         title="Temperature(C)",
    #         # 枠線、目盛線の設定
    #         outlinecolor='black', ticks='outside', tickcolor='black',
    #         len=0.8,
    #         thicknessmode='fraction',  # カラーバーの幅の指定方法を割合モードに設定
    #         thickness=0.02,  # カラーバーの幅（割合モードで0〜1の範囲で指定）
    #     ),
    #     ))])
    
    # fig5.update_layout(coloraxis=dict(colorbar=dict(len=0.5)))
    
    
    # マーカー、ラインの設定
    fig5.update_traces(
        # mode = 'markers+lines', # 'markers+lines', 'markers'
        mode = 'markers', # 'markers+lines', 'markers'
        marker = dict(size = 3),
        # line = dict(width = 2), #color = 'Black',
        name='Salinity'
        )
        
    ###水深をスケールバーで変える設定
    fig_depth_max_minus = fig_depth_max*(-1)
    fig_depth_min_minus = fig_depth_min*(-1)


    # ##図のスケール

    # fig5.update_layout(
    #         scene = dict(
    #     # #各軸の範囲
    #     # xaxis = dict(range=[165,120],),
    #     # yaxis = dict(range=[55,20],),
    #     zaxis = dict(range=[fig_depth_max_minus, fig_depth_min_minus],),
        
        
        
    #     aspectratio=dict(x=2, y=1, z=1),  # 各軸方向のスケールを指定


    #     #各軸のタイトル
    #     yaxis_title='Latitude N',
    #     xaxis_title='Longitude E',
    #     zaxis_title='Water Depth',
    #     ),
    #     width=700,
    #     height=600,
    #     # margin=dict(r=20, l=10, b=10, t=10),

    #         )
    
    
    
    
    #     # --- 表示モードに応じたレイアウトパラメータの設定 ---
    # if ref_data == data_source_GLOBAL:
    #     # NASA（世界規模）の設定
    #     # 世界地図は横に長いため x=2 に設定
    #     target_aspectratio = dict(x=2, y=1, z=1)
    #     target_aspectmode = 'manual'
    #     # NASAの時は軸範囲を自動（コメントアウトの状態）にするか、広域に設定
    #     x_range = None 
    #     y_range = None
    # else:
    #     # 日本周辺の設定
    #     target_aspectratio = dict(x=1, y=1, z=1)
    #     target_aspectmode = 'manual'
    #     # 必要に応じて日本近海の範囲を固定する場合
    #     x_range = [120, 160] # 例
    #     y_range = [20, 60]   # 例
    
    # # --- レイアウトの一括更新 ---
    # fig5.update_layout(
    #     scene=dict(
    #         # アスペクト比の設定
    #         aspectmode=target_aspectmode,
    #         aspectratio=target_aspectratio,
            
    #         # 軸の範囲設定（z軸は共通の変数を利用）
    #         zaxis=dict(range=[fig_depth_max_minus, fig_depth_min_minus]),
    #         # NASA以外で範囲を固定したい場合は以下を有効化
    #         xaxis=dict(range=x_range) if x_range else dict(),
    #         yaxis=dict(range=y_range) if y_range else dict(),
    
    #         # 軸のタイトル
    #         xaxis_title='Longitude E',
    #         yaxis_title='Latitude N',
    #         zaxis_title='Water Depth',
    #     ),
    #     width=700,
    #     height=600,
    #     # margin=dict(r=20, l=10, b=10, t=10),
    # )
    
    
    
    # --- envgeo_utilsから呼び出して，レイアウトの一括更新 ---
     # 1. まず変数を定義する（NASAなどの場合は None、日本近海なら数値が入るように）
    if ref_data == data_source_GLOBAL:
        x_range = None
        y_range = None
    else:
        x_range = [120, 160] # デフォルトの日本近海範囲
        y_range = [20, 60]
    
    # 2. その後で共通レイアウトを呼び出す
    fig5 = envgeo_utils.apply_common_layout(
        fig5, 
        ref_data, 
        fig_depth_max_minus, 
        fig_depth_min_minus, 
        x_range=x_range, 
        y_range=y_range
    )
    
    
    
    # 海岸線を底面に追加する
    # データの最上部の場合
    fig5.add_traces(go.Scatter3d(x=coastline_x, y=coastline_y, z=[max(z)] * len(coastline_x), mode='lines',     marker = dict(size = 3),
        # line = dict(width = 2), #color = 'Black',
        name='coastline', line=dict(color='blue', width=0.8),
        hoverinfo='none' # 海岸線にカーソルが当たっても邪魔しない
        ))
    
    #スケールの底面の場合
    fig5.add_traces(go.Scatter3d(x=coastline_x, y=coastline_y, z=[fig_depth_max_minus] * len(coastline_x), mode='lines',     marker = dict(size = 3),
        # line = dict(width = 2), #color = 'Black',
        name='coastline', line=dict(color='gray', width=0.5),
        hoverinfo='none' # 海岸線にカーソルが当たっても邪魔しない
        ))
    
    
    
    
    # グラフを表示する
    # fig.show()
    # st.write(fig5)
    # st.plotly_chart(fig5, use_container_width=True)  # ブラウザの幅に合わせる
    
    
    
    
        
    ###############################################################################################
    ############################################################################################### 
    ###############################################################################################
    ###############################################################################################
    
    
    ##############################################################################################
    ##### Fig6 #######
    ##############################################################################################
    # st.subheader('4D map-depth-dexcess')
    # st.write('black indicate no-data')
    
    # import plotly.graph_objects as go

    # データの準備（サンプルデータとしてランダムな3Dデータを生成）
    
    df_dexcess = df1
    
    original_len = len(df_dexcess)
    #d-excess（＝δD－8×δ18O）
    # 1. 計算する
    df_dexcess['d-excess'] = df_dexcess['dD'] - 8 * df_dexcess['d18O']
    
    # 2. 【追加】計算できなかった行（null）をその場で除外する
    df_dexcess = df_dexcess.dropna(subset=['d-excess'])
   
    # 消えた数を出力
    removed = original_len - len(df_dexcess)
    if removed > 0:
        # st.sidebar.info(f"d-excess計算不可により {removed} 件除外しました")
        st.sidebar.info(f"For d-excess plot, {removed} samples were excluded due to calculation errors.")
    y = df_dexcess['lat']
    x = df_dexcess['lon']
    z = df_dexcess['Depth_m']
    c = df_dexcess['d-excess']
    
    # # 海岸線の座標データを手動で用意
    # coastline_excel = 'world_coastline_coordinates_50m.xlsx'
    # coastline_df = pd.read_excel(coastline_excel, sheet_name=0)
    # coastline_y = coastline_df['Latitude']  # 海岸線のx座標
    # coastline_x = coastline_df['Longitude']  # 海岸線のy座標  
    
    # --- envgeo_utils を使って読み込み ---
    coastline_x, coastline_y = envgeo_utils.load_coastline_data(ref_data)


    # color_continuous_scale= ('gray', 'gray', 'gray', 'gray', 'lightgray', 'lightgray', 'lightgray', 'lightgreen', 'lightgreen', 'green', 'green', 'blue', 'lightblue', 'yellow', 'orange', 'red')
    # color_continuous_scale= ('darkblue', 'blue', 'blue', 'blue','lightgray', 'lightgray', 'gray', 'lightgreen', 'lightgreen', 'green',  'yellow', 'orange', 'red')
    color_continuous_scale= ('darkblue', 'blue','lightgray', 'gray', 'lightgreen', 'lightgreen', 'green',  'yellow', 'orange', 'red','red','red','red')

    
    # 3Dプロットを作成する
    
    fig6=px.scatter_3d(df_dexcess, x='lon', y='lat', z='Depth_m',
                    color='d-excess', 
                    #symbol='species'
                    width=700,
                    height=600,
                    color_continuous_scale=color_continuous_scale,
                    
                    #############################ポップアップ情報ここから##########################
                    hover_data={
                        "lat": True,  # 名前を表示
                        "lon": True,  # 値を表示
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
                        "d-excess": True, 
                    }
                    #############################ポップアップ情報ここまで##########################
                )
    
    # fig14 = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='markers', 
    #         marker=dict(
    #         size=16,
    #         color=c,  # マーカーの色をyにする
    #         colorscale=color_continuous_scale,  # カラースケール変更
    #         showscale=True,  # カラーバーの表示
    #         # カラーバーの設定
    #         colorbar=dict(
    #         # x=0.2, 
    #         title="Temperature(C)",
    #         # 枠線、目盛線の設定
    #         outlinecolor='black', ticks='outside', tickcolor='black',
    #         len=0.8,
    #         thicknessmode='fraction',  # カラーバーの幅の指定方法を割合モードに設定
    #         thickness=0.02,  # カラーバーの幅（割合モードで0〜1の範囲で指定）
    #     ),
    #     ))])
    
    # fig14.update_layout(coloraxis=dict(colorbar=dict(len=0.5)))
    
    
    # マーカー、ラインの設定
    fig6.update_traces(
        # mode = 'markers+lines', # 'markers+lines', 'markers'
        mode = 'markers', # 'markers+lines', 'markers'
        marker = dict(size = 3),
        # line = dict(width = 2), #color = 'Black',
        name='d-excess'
        )
        
    
    ###水深をスケールバーで変える設定
    fig_depth_max_minus = fig_depth_max*(-1)
    fig_depth_min_minus = fig_depth_min*(-1)


    # ##図のスケール

    # fig11.update_layout(
    #         scene = dict(
    #     # #各軸の範囲
    #     xaxis = dict(range=[165,120],),
    #     yaxis = dict(range=[55,20],),
    #     zaxis = dict(range=[fig_depth_max_minus, fig_depth_min_minus],),


    #     #各軸のタイトル
    #     yaxis_title='Latitude N',
    #     xaxis_title='Longitude E',
    #     zaxis_title='Water Depth',
    #     ),
    #     width=700,
    #     height=600,
    #     # margin=dict(r=20, l=10, b=10, t=10),

    #         )
    
    
    
     
    
    #     # --- 表示モードに応じたレイアウトパラメータの設定 ---
    # if ref_data == data_source_GLOBAL:
    #     # NASA（世界規模）の設定
    #     # 世界地図は横に長いため x=2 に設定
    #     target_aspectratio = dict(x=2, y=1, z=1)
    #     target_aspectmode = 'manual'
    #     # NASAの時は軸範囲を自動（コメントアウトの状態）にするか、広域に設定
    #     x_range = None 
    #     y_range = None
    # else:
    #     # 日本周辺の設定
    #     target_aspectratio = dict(x=1, y=1, z=1)
    #     target_aspectmode = 'manual'
    #     # 必要に応じて日本近海の範囲を固定する場合
    #     x_range = [120, 160] # 例
    #     y_range = [20, 60]   # 例
    
    # # --- レイアウトの一括更新 ---
    # fig11.update_layout(
    #     scene=dict(
    #         # アスペクト比の設定
    #         aspectmode=target_aspectmode,
    #         aspectratio=target_aspectratio,
            
    #         # 軸の範囲設定（z軸は共通の変数を利用）
    #         zaxis=dict(range=[fig_depth_max_minus, fig_depth_min_minus]),
    #         # NASA以外で範囲を固定したい場合は以下を有効化
    #         xaxis=dict(range=x_range) if x_range else dict(),
    #         yaxis=dict(range=y_range) if y_range else dict(),
    
    #         # 軸のタイトル
    #         xaxis_title='Longitude E',
    #         yaxis_title='Latitude N',
    #         zaxis_title='Water Depth',
    #     ),
    #     width=700,
    #     height=600,
    #     # margin=dict(r=20, l=10, b=10, t=10),
    # )
    
    
    
    # --- envgeo_utilsから呼び出して，レイアウトの一括更新 ---
     # 1. まず変数を定義する（NASAなどの場合は None、日本近海なら数値が入るように）
    if ref_data == data_source_GLOBAL:
        x_range = None
        y_range = None
    else:
        x_range = [120, 160] # デフォルトの日本近海範囲
        y_range = [20, 60]
    
    # 2. その後で共通レイアウトを呼び出す
    fig6 = envgeo_utils.apply_common_layout(
        fig6, 
        ref_data, 
        fig_depth_max_minus, 
        fig_depth_min_minus, 
        x_range=x_range, 
        y_range=y_range
    )
    
    

    
    
    # 海岸線を底面に追加する
    # データの最上部の場合
    fig6.add_traces(go.Scatter3d(x=coastline_x, y=coastline_y, z=[max(z)] * len(coastline_x), mode='lines',     marker = dict(size = 3),
        # line = dict(width = 2), #color = 'Black',
        name='coastline', line=dict(color='blue', width=0.8),
        hoverinfo='none' # 海岸線にカーソルが当たっても邪魔しない
        ))
    #スケールの底面の場合
    fig6.add_traces(go.Scatter3d(x=coastline_x, y=coastline_y, z=[fig_depth_max_minus] * len(coastline_x), mode='lines',     marker = dict(size = 3),
        # line = dict(width = 2), #color = 'Black',
        name='coastline', line=dict(color='gray', width=0.5),
        hoverinfo='none' # 海岸線にカーソルが当たっても邪魔しない
        ))
    
    
    

    
    
    # グラフを表示する

    # st.plotly_chart(fig6, use_container_width=True)  # ブラウザの幅に合わせる
    
        
    ###############################################################################################
    ############################################################################################### 
    ###############################################################################################
    ###############################################################################################

    # ここから本格的に表示用の図
    ###############################################################################################
    ############################################################################################### 
    ###############################################################################################
    ###############################################################################################
    
    
    # ここから本格的に表示用の図
    
   
    # fig1-fig6を選択して表示
    # 個別のfigは st.plotly_chartで書き出さず，ここで選ぶようにする
        
    # --- 1. 二段組み（グリッド）にするためのCSS ---
    st.markdown("""
        <style>
        /* ラジオボタンの項目を2列の並びにする */
        div[role="radiogroup"] {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 10px;
        }
        /* ラジオボタンのタイトル（Choose data...）の文字を大きく太く */
        .stRadio > label {
            font-size: 22px !important;
            font-weight: bold;
            color: #1f77b4;
        }
        /* 選択肢それぞれの文字サイズを調整 */
        div[role="radiogroup"] label {
            font-size: 16px !important;
        }
        </style>
        """, unsafe_allow_html=True)

    # --- 2. 選択肢の定義 ---
    # リストにしておくことで、if文での判定ミス（一文字違いなど）を物理的に防ぎます
    options = [
        "4D salinity-δ18O-depth-temperature", 
        "4D salinity-temperature-depth-d18O", 
        "4D map-depth-d18O", 
        "4D map-depth-temperature", 
        "4D map-depth-salinity", 
        "4D map-depth-dexcess"
    ]

    # --- 3. ラジオボタンの設置 ---
    display_option = st.radio(
        "Choose data to display:",
        options
    )

    # --- 4. 選択された項目に応じて表示するfigを決定する ---
    if display_option == options[0]:
        target_fig = fig1
        plot_key = "p1"
        df_map = df1
    elif display_option == options[1]:
        target_fig = fig2
        plot_key = "p2"
        df_map = df1
    elif display_option == options[2]:
        target_fig = fig3
        plot_key = "p3"
        df_map = df1
    elif display_option == options[3]:
        target_fig = fig4
        plot_key = "p4"
        df_map = df1
    elif display_option == options[4]:
        target_fig = fig5
        plot_key = "p5"
        df_map = df1
    else:
        # ここがfig6 (d-excess) です
        target_fig = fig6
        plot_key = "p6"
        df_map = df_dexcess
        
        
    st.write("---")
    
    # --- 3D Plots (Fig1-6) 専用のカラースライダー ---
    # st.write("---")
    # st.subheader("🎨 Adjust Color Range: 3D Plots (Fig1-6)")
    st.subheader(display_option) # タイトルを表示
    # 現在の選択項目から列名を特定
    # cols_internal = ["Temperature_degC", "d18O", "d18O", "Temperature_degC", "Salinity", "d-excess"]
    # try:
    #     idx = options.index(display_option)
    #     target_col_3d = cols_internal[idx]
    # except:
    #     target_col_3d = display_option
        
        
        

    # # スライダーの設置
    # d_min_3d = float(df_map[target_col_3d].min())
    # d_max_3d = float(df_map[target_col_3d].max())
    
    # range_3d = st.slider(
    #     f"Color Range for 3D Plots ({display_option}):",
    #     min_value=float(np.floor(d_min_3d*10)/10),
    #     max_value=float(np.ceil(d_max_3d*10)/10),
    #     value=(d_min_3d, d_max_3d),
    #     step=0.1,
    #     key="slider_3d_unique"
    # )

    # # Fig1〜Fig6に適用
    # for f_name in ['fig1', 'fig2', 'fig3', 'fig4', 'fig5', 'fig6']:
    #     if f_name in locals():
    #         try:
    #             locals()[f_name].update_coloraxes(cmin=range_3d[0], cmax=range_3d[1])
    #         except:
    #             pass
            
            
    import math   
    # --- 3D図（Fig1-6）共通：短縮ラベルの設定 ---
    c_int = ["Temperature_degC", "d18O", "d18O", "Temperature_degC", "Salinity", "d-excess"]
    c_lbl = ["Temperature(C)", "d18O", "d18O", "Temperature(C)", "Salinity", "d-excess"]
    
    # display_option から現在のインデックスを取得して短縮名に変換
    idx = options.index(display_option) if display_option in options else 0
    t_col = c_int[idx]
    t_lbl = c_lbl[idx]

    # --- 3D図専用のスライダー (断面図の直前に配置) ---
    v1, v2 = float(df_map[t_col].min()), float(df_map[t_col].max())
    r_3d = st.slider(
        f"Colorbar scale adjustment: {t_lbl} ", 
        float(math.floor(v1*10)/10), float(math.ceil(v2*10)/10), (v1, v2), 
        0.1, key="c3_slider"
    )

    # 各Fig(1-6)のカラーバーを「下」に移動し、スライダー値を反映
    for f_name in ['fig1', 'fig2', 'fig3', 'fig4', 'fig5', 'fig6']:
        if f_name in locals():
            f = locals()[f_name]
            if f is not None:
                # カラーバーの設定を水平（下側）に変更
                f.update_layout(
                    coloraxis_colorbar=dict(
                        title=t_lbl,
                        orientation="h",  # 水平
                        yanchor="top",
                        y=-0.15,          # 図の下に配置
                        x=0.5,
                        xanchor="center",
                        thickness=15
                    ),
                    margin=dict(b=80)     # 下側の余白を確保
                )
                # スライダーの範囲を反映
                f.update_coloraxes(cmin=r_3d[0], cmax=r_3d[1])
    
        

    # --- 5. 最後に一回だけ表示を実行 ---
    st.plotly_chart(
        target_fig, 
        use_container_width=True, 
        key=plot_key,
        config={'scrollZoom': True}
    )
    
    
           
    ###############################################################################################
    ############################################################################################### 
    ###############################################################################################
    ###############################################################################################
    
    
    ###############################################################################################
    ###############################################################################################
    ###############################################################################################
    ###############################################################################################


    # 選択されたデータの地点プロット
    # --- 採取地点の地図表示 (Auto-Zoom & 幅広設定) ---
    st.divider()
    # st.subheader('Location Map (Auto-Zoom)')
    st.subheader("Geographical Distribution Map (Auto-Zoom)")
    import math

    # 1. 地図背景の選択
    map_mode = st.radio(
        "Map Style:", 
        ["Standard", "Satellite", "Bathymetry (Sea)", "Contour (GSI)"], 
        horizontal=True,
        key="map_style_31_auto"
    )

 # 2. データの範囲から中心座標とズームレベルを計算
    lat_min, lat_max = df_map["Latitude_degN"].min(), df_map["Latitude_degN"].max()
    lon_min, lon_max = df_map["Longitude_degE"].min(), df_map["Longitude_degE"].max()

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
    # c_scale_d18o = envgeo_utils.get_custom_colorscale("d18O")
    
    # 3. 地図の作成 (固定の "d18O" を 変数 target_col_3d に変更)
    # c_scale_custom = envgeo_utils.get_custom_colorscale(target_col_3d)
    
    # --- Map 専用設定 ---
    # 内部列名と短縮ラベルのリスト（Map側で独自に定義）

    m_cols = ["Temperature_degC", "d18O", "d18O", "Temperature_degC", "Salinity", "d-excess"]
    m_lbls = ["Temperature", "d18O", "d18O", "Temperature", "Salinity", "d-excess"]
    
    # 現在の選択から項目を特定
    m_idx = options.index(display_option) if display_option in options else 0
    m_target = m_cols[m_idx]
    m_label = m_lbls[m_idx]
    
    # Map専用スライダーの作成（ここで r_map を定義します）
    # st.write(f"### Map Scale Control ({m_label})")
    mv1, mv2 = float(df_map[m_target].min()), float(df_map[m_target].max())
    r_map = st.slider(
        f"Colorbar scale adjustment: {t_lbl} ", 
        float(math.floor(mv1*10)/10), float(math.ceil(mv2*10)/10), (mv1, mv2), 
        0.1, key="slider_map_unique"
    )
    
    # 地図作成 (color="d18O" 固定を解除)
    # 地図の作成
    c_scale_map = envgeo_utils.get_custom_colorscale(m_target)
    fig_map = px.scatter_mapbox(
        df_map, lat="Latitude_degN", lon="Longitude_degE",
        color=m_target,                   # 選択項目で色付け
        color_continuous_scale=c_scale_map,
        #############################ポップアップ情報ここから##########################
        hover_data={
            "lat": True,  # 名前を表示
            "lon": True,  # 値を表示
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
            "d-excess": True, # d-excess用
            # "x": False,  # X座標はツールチップから除外
            # "y": False  # Y座標はツールチップから除外
        },
        #############################ポップアップ情報ここまで##########################
        opacity=0.6, height=500
    )
    
    
    # fig_map = px.scatter_mapbox(
    #     df_map, 
    #     lat="Latitude_degN", 
    #     lon="Longitude_degE",
    #     # color="d18O", 
    #     # color_continuous_scale=c_scale_d18o,
    #     color=target_col_3d,             # ← ここを target_col_3d に変更
    #     color_continuous_scale=c_scale_custom, # ← 専用スケールを適用
    #     #############################ポップアップ情報ここから##########################
    #     hover_data={
    #         "lat": True,  # 名前を表示
    #         "lon": True,  # 値を表示
    #         "d18O": True, 
    #         "dD": True, 
    #         "Salinity": True, 
    #         "Temperature_degC": True, 
    #         "Year": True, 
    #         "Month": True, 
    #         "Day": True, 
    #         "Cruise": True, 
    #         "Station": True,
    #         "Depth_m": True,
    #         "reference": True,  # カテゴリを表示
    #         "d-excess": True, # d-excess用
    #         # "x": False,  # X座標はツールチップから除外
    #         # "y": False  # Y座標はツールチップから除外
    #     },
    #     #############################ポップアップ情報ここまで##########################
    #     opacity=0.6,
    #     height=500  # 高さはここで固定
    # )

    # 4. 背景スタイルの適用
    fig_map = envgeo_utils.apply_map_style(fig_map, map_mode)
    
    

    

    # 5. レイアウト設定
    # fig_map.update_layout(
    #     mapbox=dict(
    #         center=dict(lat=center_lat, lon=center_lon),
    #         zoom=auto_zoom
    #     ),
    #     margin=dict(l=0, r=0, t=0, b=0),
    #     autosize=True, 
    #     coloraxis_colorbar=dict(
    #         # title=f"{display_option}", # ← タイトルを選択項目名に連動
    #         x=1.0, 
    #         xanchor='right'
    #     )
    # )
    
    # 地図のレイアウト設定（カラーバーを水平に下配置）
    fig_map = envgeo_utils.apply_map_style(fig_map, map_mode)
    fig_map.update_layout(
        coloraxis_colorbar=dict(
            title=m_label,
            orientation="h",       # 水平
            yanchor="top", y=-0.15, # 図の下
            x=0.5, xanchor="center",
            thickness=15
        ),
        mapbox=dict(center=dict(lat=center_lat, lon=center_lon), zoom=auto_zoom),
        margin=dict(l=0, r=0, t=0, b=100),
        autosize=True
    )
    
    # スライダー r_map の値を地図に反映
    fig_map.update_coloraxes(cmin=r_map[0], cmax=r_map[1])



    # # --- Map 専用のカラースライダー ---
    # # st.write("---")
    # # st.subheader("🎨 Adjust Color Range: Map")
    
    # # スライダーの設置（Map専用）
    # d_min_map = float(df_map[target_col_3d].min())
    # d_max_map = float(df_map[target_col_3d].max())
    
    # range_map = st.slider(
    #     f"Color Range for Map ({display_option}):",
    #     min_value=float(np.floor(d_min_map*10)/10),
    #     max_value=float(np.ceil(d_max_map*10)/10),
    #     value=(d_min_map, d_max_map),
    #     step=0.1,
    #     key="slider_map_unique"
    # )
    
    

    # # Mapにのみ適用
    # fig_map.update_coloraxes(cmin=range_map[0], cmax=range_map[1])


    # 6. 表示 (use_container_width=True を確実に使う)
    # ID重複を割けるために，Keyを追加。　修正後（一意のキーを追加）　
    # マウスホイールでのズームが強制的に有効

    st.plotly_chart(
        fig_map, 
        use_container_width=True,
        key="dynamic_map_final", # キーも一応ユニークに
        config={'scrollZoom': True, 'displayModeBar': True}
    )




    ###############################################################################################
    ###############################################################################################
    ###############################################################################################
    ###############################################################################################

    ##選ばれたデータを表示
    # 例：特定の列だけを選択して新しいデータフレームを作成
    
    # with表記 (推奨)
    # with st.expander("selected dataset (CSV)", expanded=False):
        
    #     # d-excessの時だけd-excess追加
    #     if display_option == options[5]:
    #         df1_table = df_map[['reference','Cruise', 'Station', 'Date', 'Longitude_degE', 'Latitude_degN', 'Depth_m', 'Temperature_degC', 'Salinity', 'd18O', 'dD', 'd-excess']]
    #     else:
    #         df1_table = df_map[['reference','Cruise', 'Station', 'Date', 'Longitude_degE', 'Latitude_degN', 'Depth_m', 'Temperature_degC', 'Salinity', 'd18O', 'dD']]


                
    #     # df1_table = df_map[['reference','Cruise', 'Station', 'Date', 'Longitude_degE', 'Latitude_degN', 'Depth_m', 'Temperature_degC', 'Salinity', 'd18O', 'dD']]

    #     st.dataframe(df1_table)    
        
        

    with st.expander("selected dataset (CSV)", expanded=False):
        
        # d-excessの時だけd-excess追加
        if display_option == options[5]:
            df1_table = df_map[['reference','Cruise', 'Station', 'Date', 'Longitude_degE', 'Latitude_degN', 'Depth_m', 'Temperature_degC', 'Salinity', 'd18O', 'dD', 'd-excess']].copy()   
        else:
            df1_table = df_map[['reference','Cruise', 'Station', 'Date', 'Longitude_degE', 'Latitude_degN', 'Depth_m', 'Temperature_degC', 'Salinity', 'd18O', 'dD']].copy()   

      
        # 【重要】表示直前に全列を文字列化（これでArrowエラーは100%消えます）
        df1_table = df1_table.astype(str) 
        
        # 最新の width='stretch' を使用しない　1.42まで
        st.dataframe(df1_table, use_container_width=True)
    
    ###############################################################################################
    ###############################################################################################
    ###############################################################################################
    ###############################################################################################

if __name__ == '__main__':
    main()
    






