


import streamlit as st
from streamlit_folium import folium_static
import folium
import pandas as pd






# st.set_page_config(
#     page_title="d18O mapping",
#     # page_icon="🗾",
#     layout="wide"
#     )


# @st.cache_resource(experimental_allow_widgets=True)

def main():

    ############################################################
    # リロードボタン
    st.button('Reload')
    
######  scalebarで制御してsubmitする場合 ################

    with st.sidebar.form("parameter", clear_on_submit=False):
        
        st.header('select parameters >>> submit')
        
        submitted = st.form_submit_button(":red[submit]")
        
        st.subheader(':blue[--- for data range ---]')   
    
        
    
    
        #年の範囲       # サブレベルヘッダ
        # st.sidebar.subheader('年の範囲')
        
        sld_year_min, sld_year_max = st.slider(label='Year selected',
                                    min_value=2013,
                                    max_value=2022,
                                    value=(2014, 2020),
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
                                    min_value=115,
                                    max_value=145,
                                    value=(115, 145),
                                    )
        # st.sidebar.write(f'Selected: {sld_lon_min} ~ {sld_lon_max}')
        
        
        #緯度の範囲   
        # st.sidebar.subheader('緯度の範囲')
        sld_lat_min, sld_lat_max = st.slider(label='Latitude selected',
                                    min_value=20,
                                    max_value=45,
                                    value=(20, 45),
                                    )
        # st.sidebar.write(f'Selected: {sld_lat_min} ~ {sld_lat_max}')
        
        
        #水深の範囲   
        # st.sidebar.subheader('水深の範囲')
        sld_depth_min, sld_depth_max = st.slider(label='Water depth selected',
                                    min_value=0,
                                    max_value=1000,
                                    value=(0, 1000),
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
        selected_cruise = st.multiselect('Choose cruise area',
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
                                      'ECS2021',
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
                                               'NA2',
                                               'ECS2021'))
        
        # st.write(f'Selected: {selected_cruise}')
        
        
        
    
        

            
        ############################################################
    
    
    
    
    # "# streamlit-foliums"
    
    # with st.echo():
    #     import streamlit as st
    #     from streamlit_folium import folium_static
    #     import folium
    #     import pandas as pd
    
    # center on Liberty Bell
    m = folium.Map(location=[35, 135], tiles="Stamen Terrain", zoom_start=5)
    
    # add marker for Liberty Bell
    # tooltip = "Liberty Bell"
    # folium.Marker(
    #     [39.949610, -75.150282], popup="Liberty Bell", tooltip=tooltip
    # ).add_to(m)
    
    excel_file = 'd18O_20230513-1_NA2_2021add.xlsx'
    sheet_num = 1
    
    df = pd.read_excel(excel_file, sheet_name=sheet_num)
    
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
            
            df1 = df1[(df1['Transect'].isin(selected_cruise))
                        | df1.isnull().all(axis=1)]
                
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
                        | (df1['Transect'] == 'ECS2021') 
                        | df1.isnull().all(axis=1)]      
              

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
            df1 = df1[(df1['Year'] <= sld_year_max) & (df1['Year'] >= sld_year_min) 
                        | df1.isnull().all(axis=1)] 

     
            return df1
        
        
        
    df1 = data_limit()
    
    
    # st.write(df_empty)
    data_found_num = str(len(df1["d18O"]))

    

    #選んだパラメーター表示
    # st.write('YEAR:'+str(sld_year_min)+'-'+str(sld_year_max)+', ' 
    #           +'MONTH:'+str(sld_month_min)+'-'+str(sld_month_max)+', '
    #           +'Longitude:'+str(sld_lon_min)+'-'+str(sld_lon_max)+', '
    #           +'Latitude:'+str(sld_lat_min)+'-'+str(sld_lat_max)+', '
    #           +'Water_depth:'+str(sld_depth_min)+'-'+str(sld_depth_max)+', '
    #           +'Salinity:'+str(sld_sal_min)+'-'+str(sld_sal_max))
    # st.write('Area(Cruise)',selected_cruise)
    selected_cruise_indicate =str(list(selected_cruise[:]))
    st.write('Selected Area (Cruise)', selected_cruise_indicate)
    # print('Area(Cruise)', list(selected_cruise[:]))
    #テキストの色変更
    # st.write(""":red['test']""")



    # # バリデーション処理
    # if df30m_empty == 1:  #データが無かったとき
    #     st.warning('no data found')
    #     # 条件を満たないときは処理を停止する
    #     st.stop()
    # elif df30m_empty == 0: #データがあったとき
    #     st.write(data_found_num,'data found for depth profile (below 30m)')
    st.write(data_found_num,'data found for depth profile (below 30m)')
    
    
    
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



    df1['Depth_m_rev'] = df1['Depth_m']*(-1)
    import plotly.express as px
    
    
    st.subheader('2D salinity-d18O-depth')
    st.write(px.scatter(df1, x="Salinity", y="d18O", color="Depth_m_rev", trendline='ols',trendline_color_override='darkblue', 
                width=700,
                height=600
                ))
    
    
    
    st.subheader('3D depth-sakinity-d18O-temperature')
    fig1=px.scatter_3d(df1, x='Salinity', y='d18O', z='Depth_m_rev',
                    color='Temperature_degC', 
                    #symbol='species'
                    width=700,
                    height=600,
                )
                


    # マーカー、ラインの設定
    fig1.update_traces(
        # mode = 'markers+lines', # 'markers+lines', 'markers'
        mode = 'markers', # 'markers+lines', 'markers'
        marker = dict(size = 3),
        # line = dict(width = 2), #color = 'Black',
    )

    st.write(fig1)





    # import plotly.graph_objects as go


    st.subheader('3D depth-map-d18O')
    #3Dプロット！！！！
    # st.write(
    color_continuous_scale= ('green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'blue', 'lightblue', 'yellow', 'orange', 'red')
    fig2= px.scatter_3d(df1, x='lon', y='lat', z='Depth_m',
                    color='d18O', 
                    # colors=list_colors,
                    #symbol='species'
                    width=700,
                    height=600,
                    color_continuous_scale=color_continuous_scale,

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
        xaxis = dict(range=[145,120],),
        yaxis = dict(range=[45,20],),
        zaxis = dict(range=[1000,0],),

        #各軸のタイトル
        xaxis_title='Latitude E',
        yaxis_title='Longitude N',
        zaxis_title='Water Depth',
        ),
        width=700,
        # margin=dict(r=20, l=10, b=10, t=10),

            )

          # fig1= px.scatter_3d(df1, x='lat', y='lon', z='Depth_m_rev',
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
              
    st.write(fig2)
    
    
    
    

    st.subheader('selected data')
    st.dataframe(df1)
    
    
    # fig = px.scatter_mapbox(df1,lat="lat", lon="lon", color="d18O",color_continuous_scale=px.colors.sequential.Viridis)
    # fig.update_layout(mapbox_style="open-street-map", margin={"r":0,"t":0,"l":0,"b":0})
    # fig.show()
    
    # fig.write_html('first_figure.html', auto_open=True)
    
if __name__ == '__main__':
    main()
    



st.cache_data.clear()
st.cache_resource.clear()





