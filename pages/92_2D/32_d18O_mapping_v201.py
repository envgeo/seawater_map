# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import numpy as np
import cartopy.crs as ccrs
# import matplotlib.ticker as mticker
import matplotlib.pyplot as plt


print(("--------12_map_d18O_zoom_select_v201--------"))

# datetimeモジュールを使った現在の日付と時刻の取得
import datetime
dt = datetime.datetime.today()  # ローカルな現在の日付と時刻を取得
print(dt)  # 2021-10-29 15:58:08.356501


st.header('d18O mapping Ver.201')

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









st.cache_data.clear()
st.cache_resource.clear()
@st.cache_resource(experimental_allow_widgets=True)
def main():
    
        
    
    # リロードボタン
    st.button('Reload')



    #################論文選択ここから###########################################


    ref_data = st.radio("data source (see home>about):", ("Kodama et al. (2024) only", "Kodama et al. (2024) with other reports"), horizontal=True, args=[1, 0])

    # plot_all_data = st.radio("Plot all data on the background as red:", ("YES", "NO"), horizontal=True, args=[1, 0])





######  scalebarで制御してsubmitする場合 ################

    with st.sidebar.form("parameter", clear_on_submit=False):
        
        
        
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
        
        st.header('select parameters ➡ submit')
        
        submitted = st.form_submit_button(":red[submit]")
        
        st.subheader(':blue[--- for data range ---]') 

        #年の範囲       # サブレベルヘッダ
        # st.sidebar.subheader('年の範囲')
        
        sld_year_min, sld_year_max = st.slider(label='Year selected',
                                    min_value=1996,
                                    max_value=2028,
                                    value=(1996,2028),
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
                                    value=(115, 170),
                                    )
        # st.sidebar.write(f'Selected: {sld_lon_min} ~ {sld_lon_max}')
        
        
        #緯度の範囲   
        # st.sidebar.subheader('緯度の範囲')
        sld_lat_min, sld_lat_max = st.slider(label='Latitude selected',
                                    min_value=-70,
                                    max_value=55,
                                    value=(0, 55),
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
        
    
        # #スペース入れる
        # st.subheader(':blue[  ]')
        # st.subheader(':blue[  ]')
        st.subheader(':blue[--- for fig scale only ---]')
        
    
        
    
        
        if ref_data == "Kodama et al. (2024) only":

            #地図の描画範囲（拡大）
            # # 120-0.001, 145+0.001, 20-0.001, 45+0.001
            
            # # st.sidebar.subheader('地図の経度の範囲（拡大）')
            map_lon_min, map_lon_max = st.slider(label='Map Longitude selected',
                                        min_value=120-0.001,
                                        max_value=145+0.001,
                                        value=(120-0.001, 145+0.001),
                                        )
            # # st.sidebar.write(f'Selected: {map_lon_min} ~ {map_lon_max}')
            
            # # st.sidebar.subheader('地図の緯度の範囲（拡大）')
            map_lat_min, map_lat_max = st.slider(label='Map Latitude selected',
                                        min_value=20-0.001,
                                        max_value=45+0.001,
                                        value=(20-0.001, 45+0.001),
                                        )
            # # st.sidebar.write(f'Selected: {map_lat_min} ~ {map_lat_max}')
        else:
            #地図の描画範囲（拡大）
            # # 120-0.001, 145+0.001, 20-0.001, 45+0.001
            
            # # st.sidebar.subheader('地図の経度の範囲（拡大）')
            map_lon_min, map_lon_max = st.slider(label='Map Longitude selected',
                                        min_value=-180-0.001,
                                        max_value=180+0.001,
                                        value=(120-0.001, 180+0.001),
                                        )
            # # st.sidebar.write(f'Selected: {map_lon_min} ~ {map_lon_max}')
            
            # # st.sidebar.subheader('地図の緯度の範囲（拡大）')
            map_lat_min, map_lat_max = st.slider(label='Map Latitude selected',
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
            
            
    # 注意書き
    
    if ref_data == "Kodama et al. (2024) only":
        st.write(':blue[data source:]  Kodama et al. (2024)')
        
 
    else:
        # st.text('including data from previous reports')
        st.write(':blue[data source:] Kodama et al. (2024), Yamamoto et al. (2001), Sakamoto et al. (2019), Kodaira et al. (2016), Horikawa et al. (2023).  :blue[(see "home > about > data source")]')



    








    #データソースによって選ぶファイルを変える
    if ref_data == "Kodama et al. (2024) only":
        excel_file = 'd18O_20230513-1_NA2_2021add.xlsx'
    else:
        excel_file = 'd18O_20240927_ref_YSKH.xlsx'
        
        
    sheet_num = 1
    
    df1 = pd.read_excel(excel_file, sheet_name=sheet_num)
    


    
    
    
    
    
    df1 = df1[(df1['Depth_m'] == 'xxx') 
                # |(df1['Depth_m'] <= 10) & (df1['Depth_m'] >= 0)
                # |(df1['Depth_m'] <= 200) & (df1['Depth_m'] > 10)
                # |(df1['Depth_m'] <= 500) & (df1['Depth_m'] > 200)
                # |(df1['Depth_m'] <= 1000) & (df1['Depth_m'] > 500)
                
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
      
              
    df1 = df1[(df1['Month'] == 'xxx')
                # |(df1['Month'] <= 12) & (df1['Month'] >= 10)          
                # |(df1['Month'] <= 9) & (df1['Month'] >= 7)
                # |(df1['Month'] <= 6) & (df1['Month'] >= 4)
                # |(df1['Month'] <= 3) & (df1['Month'] >= 1)     
                
                |(df1['Month'] <= sld_month_max) & (df1['Month'] >= sld_month_min)  
                | df1.isnull().all(axis=1)]      
      
    
    
    df1 = df1[(df1['Salinity'] == 'xxx')
              # |(df1['Salinity'] >= 0) & (df1['Salinity'] <= 38)
              
                |(df1['Salinity'] >= sld_sal_min) & (df1['Salinity'] <= sld_sal_max)
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

    
    
    # st.write(":red[d18O map (select parameters)]")
    st.write(":blue[--- The map area can be adjusted with 'fig scale'.---]")

    

    
    
    #日本地図描画
    
    # fig = plt.figure(figsize=(8, 6), facecolor="white", dpi=150,tight_layout=False)
    fig = plt.figure(figsize=(12, 8),facecolor="white", dpi=150,tight_layout=False)
    
    
    # ax = fig.add_subplot(111, projection=ccrs.Mercator(central_longitude=140.0), facecolor="white")
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    
    # ax.set_global()
    # ax.coastlines()
    ax.coastlines(resolution='50m')
    
    # ax.set_extent([120-0.01, 145+0.01, 20-0.01, 45+0.01]) #この行を入れるとStreamlitでおかしくなる
    # ax.set_extent([120-0.001, 145+0.001, 20-0.001, 45+0.001], crs=ccrs.PlateCarree())
    
    # ax.set_xlim([120-0.01, 145+0.01])
    # ax.set_ylim([20-0.01, 45+0.01])
    

    
    #############川とを描画したいとき#############
    # import cartopy.feature as cfeature
    # ax.add_feature(cfeature.NaturalEarthFeature ('physical', 'land', '10m', facecolor='darkgrey'))
    # ax.add_feature(cfeature.NaturalEarthFeature\
    #           ('physical', 'rivers_lake_centerlines', '10m', facecolor='none',edgecolor='dodgerblue'))
    #############川ここまで#############
    
    # #############いろいろ描画したいとき#############
    # import cartopy.feature as cfeature
    # ax.add_feature(cfeature.LAND)
    # ax.add_feature(cfeature.OCEAN)
    # ax.add_feature(cfeature.COASTLINE)
    # ax.add_feature(cfeature.BORDERS, linestyle=":")
    # ax.add_feature(cfeature.LAKES)
    # ax.add_feature(cfeature.RIVERS)
    # #############いろおろここまで#############
    
    ax.set_xlim([map_lon_min, map_lon_max])
    ax.set_ylim([map_lat_min, map_lat_max])
    
    # """図のフォント設定、サイズも"""
    ##### ベースのフォントとフォントサイズの指定
    # plt.rcParams['font.family'] = 'Arial'
    plt.rcParams["font.size"] = 15
    
    
    
    
    
    gl = ax.gridlines(draw_labels=True)
    
    ####################################################################################################################################################
    
    #緯度経度と水深とTransectで制限
    # df1 = df
    
    
    
    
    
    
    
    # # print(df.dtypes)
    
    # #描画
    # ax_cmap = ax.scatter(df1["Longitude_degE"], df1["Latitude_degN"], c=df1['d18O'],cmap='jet', s=10, alpha=0.7, vmin=-1.5, vmax=1, transform=ccrs.PlateCarree())
    
    
    # #カラーバーの位置調整
    # from mpl_toolkits.axes_grid1.inset_locator import inset_axes
    # axins1 = inset_axes(ax,
    #                    width="50%",  # width = 10% of parent_bbox width
    #                    height="2%",  # height : 50%
    #                    loc='lower right',
    #                    bbox_to_anchor=(-0.02, 0.1, 1, -0.7),
    #                    bbox_transform=ax.transAxes,
    #                    )
    
    
    # fig.colorbar(ax_cmap, shrink=0.65, cax=axins1,orientation='horizontal',label="$\delta^{18}$O"+' (VSMOW)')
    
    # # ax.set_title('title', fontsize=20)
    # # ax.set_title(selected_area, fontsize=20) #Transectでソートした場合
    
    # st.pyplot(fig)
    
    
    
    ax_cmap = ax.scatter(df1["Longitude_degE"], df1["Latitude_degN"], c=df1['d18O'],cmap='jet', s=10, alpha=0.7, vmin=-1.5, vmax=1, transform=ccrs.PlateCarree())
    
    
    
    
# =============================================================================
#     2023/07/22ここから不具合　修正
# =============================================================================
    
    # カラーバーの位置調整
    # from mpl_toolkits.axes_grid1.inset_locator import inset_axes
    # axins1 = inset_axes(ax,
    #                     width="50%",  # width = 10% of parent_bbox width
    #                     height="2%",  # height : 50%
    #                     loc='lower right',
    #                     bbox_to_anchor=(-0.02, 0.1, 1, -0.7),
    #                     bbox_transform=ax.transAxes,
    #                     )
    
    
    # fig.colorbar(ax_cmap, shrink=0.65, cax=axins1,orientation='horizontal',label="$\delta^{18}$O"+' (VSMOW)')
    
    cax = fig.add_axes((0.47, 0.19, 0.25, 0.015))
    
    fig.colorbar(ax_cmap, shrink=0.2, orientation='horizontal',label="$\delta^{18}$O"+' (VSMOW)',cax=cax)

# =============================================================================
# 　2023/07/22ここまで不具合 修正
# =============================================================================
    
    # ax.set_title('title', fontsize=20)
    # ax.set_title(selected_area, fontsize=20) #Transectでソートした場合
    #全体のタイトル名　　手入力
    main_title = 'SEAWATER $\delta^{18}$O MAP WEB (b02)'
    sub_title = 'Lon:'+str(sld_lon_min)+'-'+str(sld_lon_max)+', Lat:'+str(sld_lat_min)+'-'+str(sld_lat_max)+', Y:'+str(sld_year_min)+'-'+str(sld_year_max)+', M:'+str(sld_month_min)+'-'+str(sld_month_max)+', S:'+str(sld_sal_min)+'-'+str(sld_sal_max)+', D:'+str(sld_depth_min)+'-'+str(sld_depth_max)+'m'
    sub_title2 = ''
    
    title_head = str(main_title+'\n'+sub_title+'\n'+sub_title2)
    title_head2 = title_head.replace('_', ' ') #図のタイトル表示用
    fig.suptitle(title_head2,fontsize=15)
        

    
    # import io
    # fn = sub_tite
    # img = io.BytesIO()
    # plt.savefig(img, format='png')
     
    # btn = st.download_button(
    #    label="Download image",
    #    data=img,
    #    file_name=fn,
    #    mime="image/png")
    
    
    

    
    #######################画像を保存するためのボタン作成########################
    sub_title2 = sub_title
    sub_title2 = sub_title2.replace(':', '') #pdf書き出し用
    # sub_title2 = sub_title2.replace('>', '') #pdf書き出し用
    # sub_title2 = sub_title2.replace('<', '') #pdf書き出し用
    sub_title2 = sub_title2.replace(',', '_') #pdf書き出し用
    sub_title2 = sub_title2.replace(' ', '') #pdf書き出し用
    sub_tite = str('Fig_d18O_map'+'_'+sub_title2+".png")


    
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
    
    
    st.pyplot(fig)

    
  
    
    # ##########採取地点のmap　拡大可能##################
    
    # df1['lat'] = df1['Latitude_degN']
    # df1['lon'] = df1 ['Longitude_degE']
    
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
    st.plotly_chart(fig)





if __name__ == '__main__':
    main()
    
    
st.cache_data.clear()
st.cache_resource.clear()
    
    
