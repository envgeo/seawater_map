# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import numpy as np
# import numpy as np
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

print(("--------17_depth_temperature_v105--------"))
# datetimeモジュールを使った現在の日付と時刻の取得
import datetime
dt = datetime.datetime.today()  # ローカルな現在の日付と時刻を取得
print(dt)  # 2021-10-29 15:58:08.356501




# ############論文データ追加用の設定############
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
    # st.subheader('including data from previous reports')
    # st.write('Kodama et al. (2024), Yamamoto et al. (2001), Sakamoto et al. (2019), Kodaira et al. (2016), Horikawa et al. (2023)')
    st.header('Temperature-Depth Ver.201')
    
    
    # リロードボタン
    st.button('Reload')
    
    
    
    
    #################論文選択ここから###########################################


    ref_data = st.radio("data source (see home>about):", ("Kodama et al. (2024) only", "Kodama et al. (2024) with other reports"), horizontal=True, args=[1, 0])

    plot_all_data = st.radio("Plot all data on the background as gray line:", ("YES", "NO"), horizontal=True, args=[1, 0])



    
######  scalebarで制御してsubmitする場合 ################

    with st.sidebar.form("parameter", clear_on_submit=False):
        
        st.header('select parameters ➡ submit')
        
        
        
        
        #################文献選択ここから###########################################
        
        
        # st.subheader('data source:')
        
        # ref_data = st.radio("data source (see home>about):", ("Kodama et al. (2024) only", "Kodama et al. (2024) with other reports"), horizontal=True, args=[1, 0])
        
        if ref_data == "Kodama et al. (2024) only":
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
        else:
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
        
        #################文献選択ここまで###########################################
        
        
        
        
        
        
        
        submitted = st.form_submit_button(":red[submit]")
        
        st.subheader(':blue[--- for data range ---]') 
     
    
    
        
    
        # country=st.text_input('国を入力', 'Japan')
        # year=st.number_input('年(1952~5年おき)',1952,2007,1952,step=5)
    
    
        #スペース入れる
    
    
        #年の範囲       # サブレベルヘッダ
        # st.sidebar.subheader('年の範囲')
        
        sld_year_min, sld_year_max = st.slider(label='Year selected',
                                    min_value=1996,
                                    max_value=2028,
                                    value=(1996, 2028),
                                    )
        # st.sidebar.write(f'Selected: {sld_year_min} ~ {sld_year_max}')
        
        #月の範囲       # サブレベルヘッダ
        # st.sidebar.subheader('月の範囲')
        
        sld_month_min, sld_month_max = st.slider(label='Month selected',
                                    min_value=1,
                                    max_value=12,
                                    value=(1, 12),
                                    )
        # st.sidebar.write(f'Selected: {sld_month_min} ~ {sld_month_max}')
        
        
        #経度longitudeの範囲   
        # st.sidebar.subheader('経度の範囲')
        sld_lon_min, sld_lon_max = st.slider(label='Longitude selected',
                                    min_value=-180,
                                    max_value=180,
                                    value=(115, 180),
                                    )
        # st.sidebar.write(f'Selected: {sld_lon_min} ~ {sld_lon_max}')
        
        
        #緯度の範囲   
        # st.sidebar.subheader('緯度の範囲')
        sld_lat_min, sld_lat_max = st.slider(label='Latitude selected',
                                    min_value=-70,
                                    max_value=55,
                                    value=(20, 55),
                                    )
        # st.sidebar.write(f'Selected: {sld_lat_min} ~ {sld_lat_max}')
        
        
        #水深の範囲   
        # st.sidebar.subheader('水深の範囲')
        sld_depth_min, sld_depth_max = st.slider(label='Water depth selected',
                                    min_value=0,
                                    max_value=3500,
                                    value=(0, 3200),
                                    )
        # st.sidebar.write(f'Selected: {sld_depth_min} ~ {sld_depth_max}')
        
        #塩分の範囲   
        # st.sidebar.subheader('塩分の範囲')
        sld_sal_min, sld_sal_max = st.slider(label='Salinity selected',
                                    min_value=0,
                                    max_value=40,
                                    value=(20, 38),
                                    )
        # st.sidebar.write(f'Selected: {sld_sal_min} ~ {sld_sal_max}')
        
            
        
           
        # st.sidebar.subheader('航海区の範囲')
        if ref_data == "Kodama et al. (2024) only":
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
        else:
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
        
        # st.write(f'Selected: {selected_cruise}')
        
        
        
        st.write('Cruise Area (2015-2021) in Kodama et al.(2024)')
        st.image("data/sites_20230515.gif") 
    
          
          
        
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
        if ref_data == "Kodama et al. (2024) only":
            fig_depth_min, fig_depth_max = st.slider(label='Depth scale',
                                        min_value=0,
                                        max_value=1000,
                                        value=(0, 500),
                                        )
            # st.sidebar.write(f'Selected: {fig_depth_min} ~ {fig_depth_max}')
            
        else:
            fig_depth_min, fig_depth_max = st.slider(label='Depth scale',
                                        min_value=0,
                                        max_value=3500,
                                        value=(0, 2000),
                                        )
            # st.sidebar.write(f'Selected: {fig_depth_min} ~ {fig_depth_max}')
            
            
            
            
            
    # 注意書き
    
    if ref_data == "Kodama et al. (2024) only":
        st.write(':blue[data source:]  Kodama et al. (2024)')
        
 
    else:
        # st.text('including data from previous reports')
        st.write(':blue[data source:] Kodama et al. (2024), Yamamoto et al. (2001), Sakamoto et al. (2019), Kodaira et al. (2016), Horikawa et al. (2023).  :blue[(see "home > about > data source")]')


        
                
                
    
    
    
    # # """      Spyderのメニューボタンの実行ボタンを使わないと作業ディレクトリが反映されないので注意！     """
    # # """      Spyderのメニューボタンの実行ボタンを使わないと作業ディレクトリが反映されないので注意！     """
    # # """      Spyderのメニューボタンの実行ボタンを使わないと作業ディレクトリが反映されないので注意！     """
    # # """      ファイルの読み込みと保存が別の場所を参照してしまう！！！！     """
    
    # #選んだパラメーター表示
    # st.write('YEAR:'+str(sld_year_min)+'-'+str(sld_year_max)+', ' 
    #           +'MONTH:'+str(sld_month_min)+'-'+str(sld_month_max)+', '
    #           +'Longitude:'+str(sld_lon_min)+'-'+str(sld_lon_max)+', '
    #           +'Latitude:'+str(sld_lat_min)+'-'+str(sld_lat_max)+', '
    #           +'Water_depth:'+str(sld_depth_min)+'-'+str(sld_depth_max)+', '
    #           +'Salinity:'+str(sld_sal_min)+'-'+str(sld_sal_max))
    # # st.write('Area(Cruise)',selected_cruise)
    # selected_cruise_indicate =str(list(selected_cruise[:]))
    # st.write('Selected Area (Cruise)', selected_cruise_indicate)
    # # print('Area(Cruise)', list(selected_cruise[:]))
    # #テキストの色変更
    # # st.write(""":red['test']""")

    
    # st.write(":red[temperature depth profile]")
    
    
    # """手動設定項目"""
    #####################################
    ######    EXCEL BOOK import     #####
    #####################################
 
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    ####################################################################################################################################################
    
    

                    
                    
                    ####################################################################################################################################################
                    
                        
        
    fig = plt.figure(figsize = (12, 16),dpi=150)
    
    fig.subplots_adjust(wspace=0.3, hspace=0.3)
    
    
    #PDFに書き出すかどうか
    # PDF_export_SUB = 1
    
    
    
    #元データ読み込み
    #データソースによって選ぶファイルを変える
    if ref_data == "Kodama et al. (2024) only":
        excel_file = 'dataset/d18O_20230513-1_NA2_2021add.xlsx'
    else:
        excel_file = 'dataset/d18O_20240927_ref_YSKH.xlsx'
    
    
    
    # sheet_num = 2
    
    # df = pd.read_excel(excel_file, sheet_name=sheet_num)
    
    
    # """図のフォント設定、サイズも"""
    ##### ベースのフォントとフォントサイズの指定
    # plt.rcParams['font.family'] = 'Arial'
    plt.rcParams["font.size"] = 20
    
    
    
    
    
    # """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    # """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    

    

    
    # """選択描画範囲の設定用"""
    def data_limit():
    
            # sheet_num = 1
            df1 = pd.read_excel(excel_file, sheet_name=sheet_num)
            
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
        
            df1 = df1[(df1['Transect'].isin(selected_cruise))
                       | df1.isnull().all(axis=1)]
            # #streamlitのマルチ選択用
                
                 
    
            if ref_data == "Kodama et al. (2024) only":
                df1 = df1[ (df1['Transect'] == 0) 
                            | (df1['Transect'] == Transect001) 
                            | (df1['Transect'] == Transect002)
                            | (df1['Transect'] == Transect003)
                            | (df1['Transect'] == Transect004)
                            | (df1['Transect'] == Transect005)
                            | (df1['Transect'] == Transect006)
                            | (df1['Transect'] == Transect007)
                            | (df1['Transect'] == Transect008)
                            | (df1['Transect'] == Transect009)
                            | (df1['Transect'] == Transect010)
                            | (df1['Transect'] == Transect011)
                            | (df1['Transect'] == Transect012)
                            | (df1['Transect'] == Transect013)
                            | (df1['Transect'] == Transect014)
                            | df1.isnull().all(axis=1)]      
            else:
                df1 = df1[ (df1['Transect'] == 0) 
                            | (df1['Transect'] == Transect001) 
                            | (df1['Transect'] == Transect002)
                            | (df1['Transect'] == Transect003)
                            | (df1['Transect'] == Transect004)
                            | (df1['Transect'] == Transect005)
                            | (df1['Transect'] == Transect006)
                            | (df1['Transect'] == Transect007)
                            | (df1['Transect'] == Transect008)
                            | (df1['Transect'] == Transect009)
                            | (df1['Transect'] == Transect010)
                            | (df1['Transect'] == Transect011)
                            | (df1['Transect'] == Transect012)
                            | (df1['Transect'] == Transect013)
                            | (df1['Transect'] == Transect014)
                            # | (df1['Transect'] == Transect015)
                            | (df1['Transect'] == Transect016)
                            | (df1['Transect'] == Transect017)
                            | (df1['Transect'] == Transect018)
                            | (df1['Transect'] == Transect019)
                            # | (df1['Transect'] == Transect020)
                            # | (df1['Transect'] == Transect021)
                            # | (df1['Transect'] == Transect022)
                            # | (df1['Transect'] == Transect023)
                            # | (df1['Transect'] == Transect024)
                            # | (df1['Transect'] == Transect025)
                            # | (df1['Transect'] == Transect026)
                            # | (df1['Transect'] == Transect027)
                            # | (df1['Transect'] == Transect028)
                            # | (df1['Transect'] == Transect029)
                            # | (df1['Transect'] == Transect030)
                            | df1.isnull().all(axis=1)]      


            # #描画する緯度経度を指定 
            df1 = df1[(df1['Longitude_degE'] == 'xxx') 
                        
                        |(df1['Longitude_degE'] <= sld_lon_max) & (df1['Longitude_degE'] >= sld_lon_min) #調整用
                        | df1.isnull().all(axis=1)]      
              

            df1 = df1[(df1['Latitude_degN'] == 'xxx')
                        
                        |(df1['Latitude_degN'] <= sld_lat_max) & (df1['Latitude_degN'] >= sld_lat_min) #調整用
                        | df1.isnull().all(axis=1)]      
              
                      
            df1 = df1[(df1['Month'] == 'xxx')
                        
                        |(df1['Month'] <= sld_month_max) & (df1['Month'] >= sld_month_min)  
                        | df1.isnull().all(axis=1)]      
              
            
            
            df1 = df1[(df1['Salinity'] == 'xxx')
                      
                        |(df1['Salinity'] >= sld_sal_min) & (df1['Salinity'] <= sld_sal_max)
                      | df1.isnull().all(axis=1)]      
            
            #描画する年範囲を指定
            df1 = df1[(df1['Year'] <= sld_year_max) & (df1['Year'] >= sld_year_min) | df1.isnull().all(axis=1)] 

            
            return df1
    
    
    
    
        
    #全体のタイトル名　　手入力
    main_title = 'DEPTH PROFILE (V02)'
    sub_title = 'Lon:'+str(sld_lon_min)+'-'+str(sld_lon_max)+', Lat:'+str(sld_lat_min)+'-'+str(sld_lat_max)+', Y:'+str(sld_year_min)+'-'+str(sld_year_max)+', M:'+str(sld_month_min)+'-'+str(sld_month_max)+', S:'+str(sld_sal_min)+'-'+str(sld_sal_max)+', D:'+str(sld_depth_min)+'-'+str(sld_depth_max)+'m'
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
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    # """top right """
    # """水深"""
    
    
    
    #####################################
    ######    EXCEL SHEET select    #####
    #####################################
    
    # """EXCELブックのシート選択、シートごとの描画色も"""
    #シート２はdepthプロファイルのみ抽出したシート
    sheet_num = [2]
    
    
    ######　プロットの色選択，sheet_numの順番に対応 10以上の数がある場合には色を追加 ######
    color = ["red","lime","blue","green","darkcyan","cyan","orange","yellow","fuchsia","violet","greenyellow"]
    
    # color = ["blue","blue","blue","blue","blue","blue","blue","blue","blue","blue","blue"]
    
    
    ############################################
    ######      font size line etc..       #####
    ############################################
    
    # """凡例（legend）を入れるかどうか"""
    # legend = 1 #1以外だと凡例無し
    
    
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
    X_data = "Temperature_degC"
    Y_data = "Depth_m"
    
    
    
    # """XYの表示用のラベルを指定"""
    
    X_label = "Temperature(°C)"
    Y_label = "water depth (m)"
    
    
    
    # """XYの表示用のラベルのスケールを指定"""
    
    iso_scale_X = ""
    iso_scale_Y = ""
    
    
    
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
    lim_min_X = 0
    lim_max_X = 30
    lim_min_Y = fig_depth_max
    # lim_min_Y = 1000
    lim_max_Y = fig_depth_min
    

    
    # """------------------ここから先はさわらない！----------------------"""
    # """以下の設定は基本的に変更しない"""
    
    
    #もとのエクセルファイルのシートリストを表示
    print()
    sheet_all = pd.read_excel(excel_file, sheet_name=None)
    print("選択したExcelのSheetリスト:",list(sheet_all.keys()))
    
    
    
    
    
    
    # """ここからdepth"""
    if X_Y == 1:
        # sheet_num_XY = [3,4,5,6,7,8]
        
        print('-------------SUB_FIG   d13C vs d18O-------------')
        
        # ax = plt.subplot(323)
        # fig = plt.figure()
        # grid = plt.GridSpec(3,2, wspace=0.76, hspace=0.45)
        grid = plt.GridSpec(1,1, )
        ax = fig.add_subplot(grid[0, 0])
        
        ax.set_xlabel(X_label + iso_scale_X, fontsize=30)
        ax.set_ylabel(Y_label + iso_scale_Y, fontsize=20)  #LateX形式で特殊文字
    
        
        input_sheet_name = pd.ExcelFile(excel_file).sheet_names
        for sheet_num in sheet_num:    
            print("読み込まれたSheet:", [sheet_num], input_sheet_name[sheet_num])
        
        for sheet_num_XY in sheet_num_XY:
            # df_fig_ALL = pd.read_excel(excel_file, sheet_name=input_sheet_name[sheet_num_XY])
    
     #Excelファイルの読み込み
            df_fig_ALL = pd.read_excel(excel_file, sheet_name=sheet_num_XY)
            
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
    
    
            plt.legend(fontsize = 20) # 凡例の数字のフォントサイズを設定
    
    
            ax.set_xlim(lim_min_X, lim_max_X) 
            ax.set_ylim(lim_min_Y, lim_max_Y) 
            plt.tick_params(labelsize=20)
            ax.set_xticks(np.linspace(lim_min_X, lim_max_X,11))
            ax.set_yticks(np.linspace(lim_min_Y, lim_max_Y, 11))
            
            
    
            ax.xaxis.set_major_formatter(FormatStrFormatter("%.f"))
            ax.yaxis.set_major_formatter(FormatStrFormatter("%.f"))
                
    
            ax.tick_params(length=ax_length)
            # ax.annotate("point A", xy = (-7, 0), size = 15,
            #             color = "red", arrowprops = dict())
    
        plt.title(fig_title_X_Y, fontsize=30) #
        plt.legend(fontsize = 20) # 凡例の数字のフォントサイズを設定
        
    
        
        #追加で強調プロットをする場合
        if X_Y_add == 1:
            # sheet_num_add = [1]
            # sheet_num_add = [2,3]
            for sheet_num_add in sheet_num_add:    
        
                if X_Y_C_add_each == 1:
                    
                    plt.title(fig_title_X_Y+'_with_selected', fontsize=20) #
                    
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
    
        
                    plt.legend(fontsize = 20) # 凡例の数字のフォントサイズを設定
    
                    
                    
                    #############################
                    if selected_add3 == 1:
    
                        #個別に色を変えてもう一つプロット
                        # Excelファイルの読み込み
                        df_fiｇ_add = pd.read_excel(excel_file, sheet_name=sheet_num_add)
                        selected_row2 = selected_row2
                        selected_value = selected_value
                        
                        # 特定の列に特定の変数を持つ行と空白行を残す
                        df_fiｇ_add = df_fiｇ_add[(df_fiｇ_add[selected_row2] == selected_value) | df_fiｇ_add.isnull().all(axis=1)]
                        plt.plot(df_fiｇ_add[X_data], df_fiｇ_add[Y_data],c='red', marker=X_Y_M, lw=2, alpha=alpha_selected, label=selected_value)
                        plt.legend(fontsize = 15) # 凡例の数字のフォントサイズを設定
                        
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
                        st.write(':green[YEAR]:'+str(sld_year_min)+'-'+str(sld_year_max)+', ' 
                                  +':green[MONTH]:'+str(sld_month_min)+'-'+str(sld_month_max)+', '
                                  +':green[Longitude]:'+str(sld_lon_min)+'-'+str(sld_lon_max)+', '
                                  +':green[Latitude]:'+str(sld_lat_min)+'-'+str(sld_lat_max)+', '
                                  +':green[Water_depth]:'+str(sld_depth_min)+'-'+str(sld_depth_max)+', '
                                  +':green[Salinity]:'+str(sld_sal_min)+'-'+str(sld_sal_max))
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
    
    
    
    # ##########採取地点のmap　拡大可能##################
    # df1 = data_limit()
    # df1['lat'] = df1['Latitude_degN']
    # df1['lon'] = df1['Longitude_degE']
    
    # # df = pd.DataFrame(
    # #     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    # #     columns=['lat', 'lon'])
    
    # st.map(df1)



    ##########採取地点のmap　その２　拡大可能##################
    import plotly.express as px

    fig = px.scatter_mapbox(df1, lat="Latitude_degN", lon="Longitude_degE", zoom=3,
                            # color='Month',
                            hover_data=["d18O",'dD',"Salinity",'Temperature_degC','Date','Cruise','Station','Depth_m', 'reference'],
                            opacity=0.4,
                            )
    
    # fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(mapbox_style="carto-positron")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    # st.plotly_chart(fig)
    st.plotly_chart(fig, use_container_width=True)  # ブラウザの幅に合わせる



if __name__ == '__main__':
    main()
    
    
# st.cache_data.clear()
# st.cache_resource.clear()
