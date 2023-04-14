# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import numpy as np
import cartopy.crs as ccrs
# import matplotlib.ticker as mticker
import matplotlib.pyplot as plt





@st.cache_resource(experimental_allow_widgets=True)
def main():
    
        
    
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

    
    
    
    
    
    
    
    
    #日本地図描画
    
    # fig = plt.figure(figsize=(8, 6), facecolor="white", dpi=150,tight_layout=False)
    fig = plt.figure(figsize=(8, 6))
    
    
    # ax = fig.add_subplot(111, projection=ccrs.Mercator(central_longitude=140.0), facecolor="white")
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    # ax.set_global()
    ax.coastlines()
    # ax.set_extent([120-0.01, 145+0.01, 20-0.01, 45+0.01]) #この行を入れるとStreamlitでおかしくなる
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
    
    
    #カラーバーの位置調整
    from mpl_toolkits.axes_grid1.inset_locator import inset_axes
    axins1 = inset_axes(ax,
                       width="50%",  # width = 10% of parent_bbox width
                       height="2%",  # height : 50%
                       loc='lower right',
                       bbox_to_anchor=(-0.02, 0.1, 1, -0.7),
                       bbox_transform=ax.transAxes,
                       )
    
    
    fig.colorbar(ax_cmap, shrink=0.65, cax=axins1,orientation='horizontal',label="$\delta^{18}$O"+' (VSMOW)')
    
    # ax.set_title('title', fontsize=20)
    # ax.set_title(selected_area, fontsize=20) #Transectでソートした場合
    #全体のタイトル名　　手入力
    # main_title = 'SEAWATER DATA WEB (b01)'
    main_title2 = 'Lon:'+str(sld_lon_min)+'-'+str(sld_lon_max)+', Lat:'+str(sld_lat_min)+'-'+str(sld_lat_max)+', Y:'+str(sld_year_min)+'-'+str(sld_year_max)+', M:'+str(sld_month_min)+'-'+str(sld_month_max)+', S:'+str(sld_sal_min)+'-'+str(sld_sal_max)+', D:'+str(sld_depth_min)+'-'+str(sld_depth_max)+'m'
    # sub_title = 'Area B (N:25-130,E:135-140,D:>10m)'
    # sub_title = '(N:25-130,E:135-140,D:>10m)'
    sub_title2 = ''
    
    # title_head = 'seawater_data_(Sea_of_Japan) \n selected_area'
    title_head = str('d18O: '+main_title2+'\n'+sub_title2)
    
    title_head2 = title_head.replace('_', ' ') #図のタイトル表示用
    fig.suptitle(title_head2,fontsize=10)
        
    
    sub_tite = str('Fig_d18O_map'+'_'+sub_title2+".png")
    
    # import io
    # fn = sub_tite
    # img = io.BytesIO()
    # plt.savefig(img, format='png')
     
    # btn = st.download_button(
    #    label="Download image",
    #    data=img,
    #    file_name=fn,
    #    mime="image/png")
    
    
    st.pyplot(fig)
    
    
    
    ############################
    
    df1['lat'] = df1['Latitude_degN']
    df1['lon'] = df1 ['Longitude_degE']
    
    # df = pd.DataFrame(
    #     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    #     columns=['lat', 'lon'])
    
    st.map(df1)


if __name__ == '__main__':
    main()
    
    
    
    
    
    