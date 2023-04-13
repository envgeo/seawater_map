# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import numpy as np




# import numpy as np
# import pandas as pd
# import cartopy.crs as ccrs
# import matplotlib.ticker as mticker
# import matplotlib.pyplot as plt
# import datetime as dt


@st.cache_resource(experimental_allow_widgets=True)
def main():
    
        
    # selected_cruise = st.multiselect('Choose cruise area',
    #                             ['CK',
    #                               'Nansei',
    #                               'nECS',
    #                               'Noto',
    #                               'Pacific',
    #                               'Pacific_west',
    #                               'sECS',
    #                               'Shimane&Tottori',
    #                               'SI',
    #                               'Toyama',
    #                               'Tsushima',
    #                               'Yamato',
    #                               'NA2',
    #                              ])
    # st.write(f'Selected: {selected_cruise}')
    
    # リロードボタン
    st.button('Reload')


    #年の範囲       # サブレベルヘッダ
    # st.sidebar.subheader('年の範囲')
    
    sld_year_min, sld_year_max = st.sidebar.slider(label='Year selected',
                                min_value=2013,
                                max_value=2022,
                                value=(2014, 2020),
                                )
    # st.sidebar.write(f'Selected: {sld_year_min} ~ {sld_year_max}')
    
    #月の範囲       # サブレベルヘッダ
    # st.sidebar.subheader('月の範囲')
    
    sld_month_min, sld_month_max = st.sidebar.slider(label='Month selected',
                                min_value=1,
                                max_value=12,
                                value=(1, 12),
                                )
    # st.sidebar.write(f'Selected: {sld_month_min} ~ {sld_month_max}')
    
    
    #経度longitudeの範囲   
    # st.sidebar.subheader('経度の範囲')
    sld_lon_min, sld_lon_max = st.sidebar.slider(label='Longitude selected',
                                min_value=115,
                                max_value=145,
                                value=(115, 145),
                                )
    # st.sidebar.write(f'Selected: {sld_lon_min} ~ {sld_lon_max}')
    
    
    #緯度の範囲   
    # st.sidebar.subheader('緯度の範囲')
    sld_lat_min, sld_lat_max = st.sidebar.slider(label='Latitude selected',
                                min_value=20,
                                max_value=45,
                                value=(20, 45),
                                )
    # st.sidebar.write(f'Selected: {sld_lat_min} ~ {sld_lat_max}')
    
    
    #水深の範囲   
    # st.sidebar.subheader('水深の範囲')
    sld_depth_min, sld_depth_max = st.sidebar.slider(label='Water depth selected',
                                min_value=0,
                                max_value=1000,
                                value=(0, 1000),
                                )
    # st.sidebar.write(f'Selected: {sld_depth_min} ~ {sld_depth_max}')
    
    #塩分の範囲   
    # st.sidebar.subheader('塩分の範囲')
    sld_sal_min, sld_sal_max = st.sidebar.slider(label='Salinity selected',
                                min_value=0,
                                max_value=40,
                                value=(20, 38),
                                )
    # st.sidebar.write(f'Selected: {sld_sal_min} ~ {sld_sal_max}')
    
        
    # st.sidebar.subheader('航海区の範囲')
    selected_cruise = st.sidebar.multiselect('Choose cruise area',
                                ['CK',
                                  'Nansei',
                                  'nECS',
                                  'Noto',
                                  'Pacific',
                                  'Pacific_west',
                                  'sECS',
                                  'Shimane&Tottori',
                                  'SI',
                                  'Toyama',
                                  'Tsushima',
                                  'Yamato',
                                  'NA2',
                                  ],
                                default=('CK',
                                           'Nansei',
                                           'nECS',
                                           'Noto',
                                           'Pacific',
                                           'Pacific_west',
                                           'sECS',
                                           'Shimane&Tottori',
                                           'SI',
                                           'Toyama',
                                           'Tsushima',
                                           'Yamato',
                                           'NA2'))
    
    # st.write(f'Selected: {selected_cruise}')
    

    
    excel_file = 'd18O_20210626-3_NA2.xlsx'
    sheet_num = 1
    
    df = pd.read_excel(excel_file, sheet_name=sheet_num)
    
    
    
    
    #日本地図描画
    
    # fig = plt.figure(figsize=(8, 6), facecolor="white", dpi=150,tight_layout=False)
    
    
    # # ax = fig.add_subplot(111, projection=ccrs.Mercator(central_longitude=140.0), facecolor="white")
    # ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    # ax.set_global()
    # ax.coastlines()
    # ax.set_extent([120-0.001, 145+0.001, 20-0.001, 45+0.001], crs=ccrs.PlateCarree())
    # gl = ax.gridlines(draw_labels=True)
    
    #罫線引くかどうか
    # gl.xlocator = mticker.FixedLocator(np.arange(120, 150.1, 0.5))
    # gl.ylocator = mticker.FixedLocator(np.arange(20, 50.1, 0.5))
    # 後ろの transform 以降を追加
    
    
    
    
    
    
    ####################################################################################################################################################
    
    #緯度経度と水深とTransectで制限
    df1 = df
    
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
    #                   ])
    
    df1 = df1[(df1['Transect'].isin(selected_cruise))
               | df1.isnull().all(axis=1)]
    # #streamlitのマルチ選択用
    
     
    
    
    
    
    
    df1 = df1[ (df1['Transect'] == 0) 
                | (df1['Transect'] == 'CK') 
                | (df1['Transect'] == 'Nansei') 
                | (df1['Transect'] == 'nECS') 
                | (df1['Transect'] == 'Noto') 
                | (df1['Transect'] == 'Pacific') 
                | (df1['Transect'] == 'Pacific_west') 
                | (df1['Transect'] == 'sECS')          
                | (df1['Transect'] == 'Shimane&Tottori')          
                | (df1['Transect'] == 'SI')
                | (df1['Transect'] == 'Toyama')
                | (df1['Transect'] == 'Tsushima')
                | (df1['Transect'] == 'Yamato')
                | (df1['Transect'] == 'NA2') 
                
                | df1.isnull().all(axis=1)]      
      
    
    
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
    
    
    
    
    
    
    
    ############################
    
    df1['lat'] = df1['Latitude_degN']
    df1['lon'] = df1 ['Longitude_degE']
    
    # df = pd.DataFrame(
    #     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    #     columns=['lat', 'lon'])
    
    st.map(df1)


if __name__ == '__main__':
    main()
    