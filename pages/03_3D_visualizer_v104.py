
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 16:00:21 2023

@author: toyoho

2023/05/21 update (axis limit)
"""


import streamlit as st
from streamlit_folium import folium_static
import folium
import pandas as pd

import plotly.graph_objects as go


print(("--------03_3D_visualizer_v104--------"))

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
                                    value=(2013, 2022),
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
                                    [
                                      'Pacific',
                                      'Pacific_west',
                                      'Noto',
                                      'Toyama',
                                      'SI',
                                      'Yamato',
                                      'Shimane&Tottori',
                                      'NA2',
                                      'Tsushima',									  
		                              'nECS',							  
                                        'CK',									  
                                      'ECS2021',									  
                                      'sECS',									  
                                      'Nansei',
                                      ],
                                    default=(
                                      'Pacific',
                                      'Pacific_west',
                                      'Noto',
                                      'Toyama',
                                      'SI',
                                      'Yamato',
                                      'Shimane&Tottori',
                                      'NA2',
                                      'Tsushima',									  
		                              'nECS',							  
                                        'CK',									  
                                      'ECS2021',									  
                                      'sECS',									  
                                      'Nansei',
                                               ))
        
        # st.write(f'Selected: {selected_cruise}')
        
        
        st.write('Cruise Area (2015-2021)')
        st.image("data/sites_20230515.gif")
    
        

            
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

    # with表記 (推奨)
    with st.expander("selected data", expanded=False):

    #選んだパラメーター表示
        st.write('YEAR:'+str(sld_year_min)+'-'+str(sld_year_max)+', ' 
                  +'MONTH:'+str(sld_month_min)+'-'+str(sld_month_max)+', '
                  +'Longitude:'+str(sld_lon_min)+'-'+str(sld_lon_max)+', '
                  +'Latitude:'+str(sld_lat_min)+'-'+str(sld_lat_max)+', '
                  +'Water_depth:'+str(sld_depth_min)+'-'+str(sld_depth_max)+', '
                  +'Salinity:'+str(sld_sal_min)+'-'+str(sld_sal_max))
        # st.write('Area(Cruise)',selected_cruise)
        selected_cruise_indicate =str(list(selected_cruise[:]))
        st.write('Selected Area (Cruise)', selected_cruise_indicate)
        # print('Area(Cruise)', list(selected_cruise[:]))
        #テキストの色変更
        # st.write(""":red['test']""")

 
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
    import plotly.express as px
    
    
    
    
    ###### Fig1 #######
    st.subheader('3D salinity-d18O-longitude')
    # color_continuous_scale= ('darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'blue', 'blue', 'blue', 'blue', 'blue', 'lightblue',  'lightblue',  'lightblue',  'lightblue',  'lightblue',  'lightblue',  'lightblue', 'lightgray', 'lightgreen', 'yellow', 'orange', 'red', )
    color_continuous_scale= ('darkblue', 'blue', 'lightblue',  'lightgreen', 'green', 'yellow', 'orange', 'red', )

    fig1 = px.scatter(df1, x="Salinity", y="d18O", color="lon", trendline='ols',trendline_color_override='gray', 
                width=700,
                height=600,
                color_continuous_scale=color_continuous_scale,
                )
    
    # マーカー、ラインの設定
    fig1.update_traces(
    #     # mode = 'markers+lines', # 'markers+lines', 'markers'
    #     mode = 'markers', # 'markers+lines', 'markers'
        marker = dict(size = 5),
    #     # line = dict(width = 2), #color = 'Black',
    )
    

    
    
    st.write(fig1)  
    
    
        
    ###### Fig11 #######
    st.subheader('3D salinity-d18O-depth')
    color_continuous_scale= ('darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'blue', 'blue', 'blue', 'blue', 'blue', 'lightblue',  'lightblue',  'lightblue',  'lightblue',  'lightblue',  'lightblue',  'lightblue', 'lightgray', 'lightgreen', 'yellow', 'orange', 'red', )
    
    fig11 = px.scatter(df1, x="Salinity", y="d18O", color="Depth_m", trendline='ols',trendline_color_override='gray', 
                width=700,
                height=600,
                color_continuous_scale=color_continuous_scale,
                )
    
    # マーカー、ラインの設定
    fig11.update_traces(
    #     # mode = 'markers+lines', # 'markers+lines', 'markers'
    #     mode = 'markers', # 'markers+lines', 'markers'
        marker = dict(size = 5),
    #     # line = dict(width = 2), #color = 'Black',
    )
    

    
    
    st.write(fig11)  
    
    
    
    
    
    
    
    
    
    
    
    ###### Fig31 #######
    st.subheader('3D T-S salinity-temperature-longitude')
    # color_continuous_scale= ('darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'blue', 'blue', 'blue', 'blue', 'blue', 'lightblue',  'lightblue',  'lightblue',  'lightblue',  'lightblue',  'lightblue',  'lightblue', 'lightgray', 'lightgreen', 'yellow', 'orange', 'red', )
    color_continuous_scale= ('darkblue', 'blue', 'lightblue',  'lightgreen', 'green', 'yellow', 'orange', 'red', )

    fig31 = px.scatter(df1, x="Salinity", y="Temperature_degC", color="lon",
                width=700,
                height=600,
                color_continuous_scale=color_continuous_scale,
                )
    
    # マーカー、ラインの設定
    fig31.update_traces(
    #     # mode = 'markers+lines', # 'markers+lines', 'markers'
    #     mode = 'markers', # 'markers+lines', 'markers'
        marker = dict(size = 5),
    #     # line = dict(width = 2), #color = 'Black',
    )
    

    
    
    st.write(fig31)  
    
    
        
    ###### Fig32 #######
    st.subheader('3D T-S salinity-temperature-depth')
    color_continuous_scale= ('darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'blue', 'blue', 'blue', 'blue', 'blue', 'lightblue',  'lightblue',  'lightblue',  'lightblue',  'lightblue',  'lightblue',  'lightblue', 'lightgray', 'lightgreen', 'yellow', 'orange', 'red', )
    
    fig32 = px.scatter(df1, x="Salinity", y="Temperature_degC", color="Depth_m", 
                width=700,
                height=600,
                color_continuous_scale=color_continuous_scale,
                )
    
    # マーカー、ラインの設定
    fig32.update_traces(
    #     # mode = 'markers+lines', # 'markers+lines', 'markers'
    #     mode = 'markers', # 'markers+lines', 'markers'
        marker = dict(size = 5),
    #     # line = dict(width = 2), #color = 'Black',
    )
    

    
    
    st.write(fig32)  
    
    
    
    
    
    
    
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
                            hover_data=["d18O",'dD',"Salinity",'Temperature_degC','Date','Cruise','Station','Depth_m'],
                            opacity=0.4,
                            )
    
    # fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(mapbox_style="carto-positron")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    st.plotly_chart(fig)
    
    
    
    
    
    
    # ###### Fig2 #######
    # st.subheader('3D depth-salinity-d18O-temperature')
    # color_continuous_scale= ('darkblue', 'blue', 'blue', 'blue','lightgray', 'lightgray', 'gray', 'lightgreen', 'lightgreen', 'green',  'yellow', 'orange', 'red')
   
    # fig2=px.scatter_3d(df1, x='Salinity', y='d18O', z='Depth_m',
    #                 color='Temperature_degC', 
    #                 #symbol='species'
    #                 width=700,
    #                 height=600,
    #                 color_continuous_scale=color_continuous_scale,
    #             )
                


    # # マーカー、ラインの設定
    # fig2.update_traces(
    #     # mode = 'markers+lines', # 'markers+lines', 'markers'
    #     mode = 'markers', # 'markers+lines', 'markers'
    #     marker = dict(size = 3),
    #     # line = dict(width = 2), #color = 'Black',
    # )
    

    
    # fig2.update_layout(
    #         scene = dict(
    #     # #各軸の範囲
    #     # xaxis = dict(range=[145,120],),
    #     # yaxis = dict(range=[45,20],),

    #     #各軸のタイトル
    #     xaxis_title='salinity',
    #     yaxis_title='d18O',
    #     zaxis_title='Water Depth',
    #     ),
    #     width=700,
    #     # margin=dict(r=20, l=10, b=10, t=10),

    #         )

    #       # fig1= px.scatter_3d(df1, x='lat', y='lon', z='Depth_m',
    #       #                color='d18O', 
    #       #                # colors=list_colors,
    #       #                #symbol='species'
    #       #                width=700,
    #       #                height=600,
    #       #            )
                   
    #       # fig1.update_layout(
    #       #       scene = dict(
    #       #           xaxis = dict(range=[125,145],),
    #       #           yaxis = dict(range=[45,25],),
    #       #           zaxis = dict(range=[-1000,0],),
    #       #       )
    #       #       )

    # fig2.update_layout(
    #         scene = dict(
    #     # #各軸の範囲
    #     xaxis = dict(range=[36,20],),
    #     yaxis = dict(range=[+1,-4],),
    #     zaxis = dict(range=[-1000,0],),


    #     ),
    #     width=700,
    #     height=600,
    #     # margin=dict(r=20, l=10, b=10, t=10),

    #         )


    # st.write(fig2)




    




    # ###### Fig3 #######
    # st.subheader('3D depth-map-d18O')
    
    # import plotly.graph_objects as go

    # # データの準備（サンプルデータとしてランダムな3Dデータを生成）
    # y = df1['lat']
    # x = df1['lon']
    # z = df1['Depth_m']
    # c = df1['d18O']
    # # 海岸線の座標データを手動で用意
    # coastline_excel = 'extra_data.xlsx'
    # coastline_df = pd.read_excel(coastline_excel, sheet_name=0)
    # coastline_y = coastline_df['Latitude']  # 海岸線のx座標
    # coastline_x = coastline_df['Longitude']  # 海岸線のy座標  
    # color_continuous_scale= ('gray', 'gray', 'gray', 'gray', 'lightgray', 'lightgray', 'lightgray', 'lightgreen', 'lightgreen', 'green', 'green', 'blue', 'lightblue', 'yellow', 'orange', 'red')
 
    
    # # 3Dプロットを作成する
    
    # fig3=px.scatter_3d(df1, x='lon', y='lat', z='Depth_m',
    #                 color='d18O', 
    #                 #symbol='species'
    #                 width=700,
    #                 height=600,
    #                 color_continuous_scale=color_continuous_scale,
    #             )
    # # fig3 = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='markers', 
    # #         marker=dict(
    # #         size=16,
    # #         color=c,  # マーカーの色をyにする
    # #         colorscale=color_continuous_scale,  # カラースケール変更
    # #         showscale=True,  # カラーバーの表示
    # #         # カラーバーの設定
    # #         colorbar=dict(
    # #         # x=0.2, 
    # #         title="d18O",
    # #         # 枠線、目盛線の設定
    # #         outlinecolor='black', ticks='outside', tickcolor='black',
    # #         len=0.8,
    # #         thicknessmode='fraction',  # カラーバーの幅の指定方法を割合モードに設定
    # #         thickness=0.02,  # カラーバーの幅（割合モードで0〜1の範囲で指定）
    # #     ),
    # #     ))])
    
    # # fig11.update_layout(coloraxis=dict(colorbar=dict(len=0.5)))
    
    
    # # マーカー、ラインの設定
    # fig3.update_traces(
    #     # mode = 'markers+lines', # 'markers+lines', 'markers'
    #     mode = 'markers', # 'markers+lines', 'markers'
    #     marker = dict(size = 3),
    #     # line = dict(width = 2), #color = 'Black',
    #     name='d18O'
    #     )
        
    # fig3.update_layout(
    #         scene = dict(
    #     # #各軸の範囲
    #     xaxis = dict(range=[145,120],),
    #     yaxis = dict(range=[45,20],),
    #     zaxis = dict(range=[-1000,0],),


    #     #各軸のタイトル
    #     yaxis_title='Latitude N',
    #     xaxis_title='Longitude E',
    #     zaxis_title='Water Depth',
    #     ),
    #     width=700,
    #     height=600,
    #     # margin=dict(r=20, l=10, b=10, t=10),

    #         )
    
    # # 海岸線を底面に追加する
    # fig3.add_traces(go.Scatter3d(x=coastline_x, y=coastline_y, z=[max(z)] * len(coastline_x), mode='lines',     marker = dict(size = 3),
    #     # line = dict(width = 2), #color = 'Black',
    #     name='coastline', line=dict(color='blue', width=0.5)))
    
    
    # # グラフを表示する
    # # fig.show()
    # st.write(fig3)
    
    
    
    
    
    


    # ###### Fig4 #######
    # st.subheader('3D depth-map-temperature')
    
    # import plotly.graph_objects as go

    # # データの準備（サンプルデータとしてランダムな3Dデータを生成）
    # y = df1['lat']
    # x = df1['lon']
    # z = df1['Depth_m']
    # c = df1['Temperature_degC']
    # # 海岸線の座標データを手動で用意
    # coastline_excel = 'extra_data.xlsx'
    # coastline_df = pd.read_excel(coastline_excel, sheet_name=0)
    # coastline_y = coastline_df['Latitude']  # 海岸線のx座標
    # coastline_x = coastline_df['Longitude']  # 海岸線のy座標  
    # # color_continuous_scale= ('gray', 'gray', 'gray', 'gray', 'lightgray', 'lightgray', 'lightgray', 'lightgreen', 'lightgreen', 'green', 'green', 'blue', 'lightblue', 'yellow', 'orange', 'red')
    # color_continuous_scale= ('darkblue', 'blue', 'blue', 'blue','lightgray', 'lightgray', 'gray', 'lightgreen', 'lightgreen', 'green',  'yellow', 'orange', 'red')

    
    # # 3Dプロットを作成する
    
    # fig4=px.scatter_3d(df1, x='lon', y='lat', z='Depth_m',
    #                 color='Temperature_degC', 
    #                 #symbol='species'
    #                 width=700,
    #                 height=600,
    #                 color_continuous_scale=color_continuous_scale,
    #             )
    
    # # fig4 = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='markers', 
    # #         marker=dict(
    # #         size=16,
    # #         color=c,  # マーカーの色をyにする
    # #         colorscale=color_continuous_scale,  # カラースケール変更
    # #         showscale=True,  # カラーバーの表示
    # #         # カラーバーの設定
    # #         colorbar=dict(
    # #         # x=0.2, 
    # #         title="Temperature(C)",
    # #         # 枠線、目盛線の設定
    # #         outlinecolor='black', ticks='outside', tickcolor='black',
    # #         len=0.8,
    # #         thicknessmode='fraction',  # カラーバーの幅の指定方法を割合モードに設定
    # #         thickness=0.02,  # カラーバーの幅（割合モードで0〜1の範囲で指定）
    # #     ),
    # #     ))])
    
    # # fig11.update_layout(coloraxis=dict(colorbar=dict(len=0.5)))
    
    
    # # マーカー、ラインの設定
    # fig4.update_traces(
    #     # mode = 'markers+lines', # 'markers+lines', 'markers'
    #     mode = 'markers', # 'markers+lines', 'markers'
    #     marker = dict(size = 3),
    #     # line = dict(width = 2), #color = 'Black',
    #     name='Temperature'
    #     )
        
    # fig4.update_layout(
    #         scene = dict(
    #     # #各軸の範囲
    #     xaxis = dict(range=[145,120],),
    #     yaxis = dict(range=[45,20],),
    #     zaxis = dict(range=[-1000,0],),


    #     #各軸のタイトル
    #     yaxis_title='Latitude N',
    #     xaxis_title='Longitude E',
    #     zaxis_title='Water Depth',
    #     ),
    #     width=700,
    #     height=600,
    #     # margin=dict(r=20, l=10, b=10, t=10),

    #         )
    
    # # 海岸線を底面に追加する
    # fig4.add_traces(go.Scatter3d(x=coastline_x, y=coastline_y, z=[max(z)] * len(coastline_x), mode='lines',     marker = dict(size = 3),
    #     # line = dict(width = 2), #color = 'Black',
    #     name='coastline', line=dict(color='blue', width=0.5)))
    
    
    # # グラフを表示する
    # # fig.show()
    # st.write(fig4)
    
    
    
    
    
    
    
    
    
    
    

    # ###### Fig14 #######
    # st.subheader('3D depth-map-dexcess')
    
    # import plotly.graph_objects as go

    # # データの準備（サンプルデータとしてランダムな3Dデータを生成）
    
    # #d-excess（＝δD－8×δ18O）
    # df1['d-excess'] =  df1['dD'] - 8* df1['d18O']
    
    # y = df1['lat']
    # x = df1['lon']
    # z = df1['Depth_m']
    # c = df1['d-excess']
    # # 海岸線の座標データを手動で用意
    # coastline_excel = 'extra_data.xlsx'
    # coastline_df = pd.read_excel(coastline_excel, sheet_name=0)
    # coastline_y = coastline_df['Latitude']  # 海岸線のx座標
    # coastline_x = coastline_df['Longitude']  # 海岸線のy座標  
    # # color_continuous_scale= ('gray', 'gray', 'gray', 'gray', 'lightgray', 'lightgray', 'lightgray', 'lightgreen', 'lightgreen', 'green', 'green', 'blue', 'lightblue', 'yellow', 'orange', 'red')
    # # color_continuous_scale= ('darkblue', 'blue', 'blue', 'blue','lightgray', 'lightgray', 'gray', 'lightgreen', 'lightgreen', 'green',  'yellow', 'orange', 'red')
    # color_continuous_scale= ('darkblue', 'blue','lightgray', 'gray', 'lightgreen', 'lightgreen', 'green',  'yellow', 'orange', 'red','red','red','red')

    
    # # 3Dプロットを作成する
    
    # fig14=px.scatter_3d(df1, x='lon', y='lat', z='Depth_m',
    #                 color='d-excess', 
    #                 #symbol='species'
    #                 width=700,
    #                 height=600,
    #                 color_continuous_scale=color_continuous_scale,
    #             )
    
    # # fig14 = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='markers', 
    # #         marker=dict(
    # #         size=16,
    # #         color=c,  # マーカーの色をyにする
    # #         colorscale=color_continuous_scale,  # カラースケール変更
    # #         showscale=True,  # カラーバーの表示
    # #         # カラーバーの設定
    # #         colorbar=dict(
    # #         # x=0.2, 
    # #         title="Temperature(C)",
    # #         # 枠線、目盛線の設定
    # #         outlinecolor='black', ticks='outside', tickcolor='black',
    # #         len=0.8,
    # #         thicknessmode='fraction',  # カラーバーの幅の指定方法を割合モードに設定
    # #         thickness=0.02,  # カラーバーの幅（割合モードで0〜1の範囲で指定）
    # #     ),
    # #     ))])
    
    # # fig14.update_layout(coloraxis=dict(colorbar=dict(len=0.5)))
    
    
    # # マーカー、ラインの設定
    # fig14.update_traces(
    #     # mode = 'markers+lines', # 'markers+lines', 'markers'
    #     mode = 'markers', # 'markers+lines', 'markers'
    #     marker = dict(size = 3),
    #     # line = dict(width = 2), #color = 'Black',
    #     name='d-excess'
    #     )
        
    # fig14.update_layout(
    #         scene = dict(
    #     # #各軸の範囲
    #     xaxis = dict(range=[145,120],),
    #     yaxis = dict(range=[45,20],),
    #     zaxis = dict(range=[-1000,0],),


    #     #各軸のタイトル
    #     yaxis_title='Latitude N',
    #     xaxis_title='Longitude E',
    #     zaxis_title='Water Depth',
    #     ),
    #     width=700,
    #     height=600,
    #     # margin=dict(r=20, l=10, b=10, t=10),

    #         )
    
    # # 海岸線を底面に追加する
    # fig14.add_traces(go.Scatter3d(x=coastline_x, y=coastline_y, z=[max(z)] * len(coastline_x), mode='lines',     marker = dict(size = 3),
    #     # line = dict(width = 2), #color = 'Black',
    #     name='coastline', line=dict(color='blue', width=0.5)))
    
    
    # # グラフを表示する
    # # fig.show()
    # st.write(fig14)
    
    
    
    
    
    
    
    
    # ## Fig 5 簡易日本地図　　####
    # st.subheader('test Fig5')
    # #簡易日本地図描画
    # import matplotlib.pyplot as plt
    # coastline_excel = 'extra_data.xlsx'
    # coastline_df = pd.read_excel(coastline_excel, sheet_name=0)
    # fig10 = plt.figure(figsize=(12, 9), facecolor="white", dpi=150,tight_layout=False)
    # ax = fig10.add_subplot(1, 1, 1)


    # ax.plot(coastline_df['Longitude'], coastline_df['Latitude'], c='gray')
    # st.write(fig10)
    
    
    
    
    
    
    
    
    

    # ###### fig15 #######
    # st.subheader('3D depth-map-d18O test')
    
    # import plotly.graph_objects as go

    # # データの準備（サンプルデータとしてランダムな3Dデータを生成）
    # # y = df1['lat']
    # # x = df1['lon']
    # # z = df1['Depth_m']
    # # c = df1['d18O']
    # # 海岸線の座標データを手動で用意
    # coastline_excel = 'extra_data.xlsx'
    # coastline_df = pd.read_excel(coastline_excel, sheet_name=0)
    # coastline_y = coastline_df['Latitude']  # 海岸線のx座標
    # coastline_x = coastline_df['Longitude']  # 海岸線のy座標  
    # color_continuous_scale= ('gray', 'gray', 'gray', 'gray', 'lightgray', 'lightgray', 'lightgray', 'lightgreen', 'lightgreen', 'green', 'green', 'blue', 'lightblue', 'yellow', 'orange', 'red')
 
    
    # # 3Dプロットを作成する
    
    
    # fig15=px.scatter_3d(df1, x='lon', y='lat', z='Depth_m',
    #                 color='d18O', 
    #                 #symbol='species'
    #                 width=700,
    #                 height=600,
    #                 color_continuous_scale=color_continuous_scale,
    #             )
    # # fig15 = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='markers', 
    # #         marker=dict(
    # #         size=16,
    # #         color=c,  # マーカーの色をyにする
    # #         colorscale=color_continuous_scale,  # カラースケール変更
    # #         showscale=True,  # カラーバーの表示
    # #         # カラーバーの設定
    # #         colorbar=dict(
    # #         # x=0.2, 
    # #         title="d18O",
    # #         # 枠線、目盛線の設定
    # #         outlinecolor='black', ticks='outside', tickcolor='black',
    # #         len=0.8,
    # #         thicknessmode='fraction',  # カラーバーの幅の指定方法を割合モードに設定
    # #         thickness=0.02,  # カラーバーの幅（割合モードで0〜1の範囲で指定）
    # #     ),
    # #     ))])
    
    # # fig15.update_layout(coloraxis=dict(colorbar=dict(len=0.5)))
    
    
    # # マーカー、ラインの設定
    # fig15.update_traces(
    #     # mode = 'markers+lines', # 'markers+lines', 'markers'
    #     mode = 'markers', # 'markers+lines', 'markers'
    #     marker = dict(size = 3),
    #     # line = dict(width = 2), #color = 'Black',
    #     name='d18O'
    #     )
        
    # fig15.update_layout(
    #         scene = dict(
    #     # #各軸の範囲
    #     xaxis = dict(range=[145,120],),
    #     yaxis = dict(range=[45,20],),
    #     zaxis = dict(range=[-1000,0],),


    #     #各軸のタイトル
    #     yaxis_title='Latitude N',
    #     xaxis_title='Longitude E',
    #     zaxis_title='Water Depth',
    #     ),
    #     width=700,
    #     height=600,
    #     # margin=dict(r=20, l=10, b=10, t=10),

    #         )
    
    # # 海岸線を底面に追加する
    # fig15.add_traces(go.Scatter3d(x=coastline_x, y=coastline_y, z=[max(z)] * len(coastline_x), mode='lines',     marker = dict(size = 3),
    #     # line = dict(width = 2), #color = 'Black',
    #     name='coastline', line=dict(color='blue', width=0.5)))
    
    
    # # グラフを表示する
    # # fig.show()
    # st.write(fig15)
    
    
    
    
    
    
    

    
    
    
    # ### Fig 6 ####
    # st.subheader('test Fig6')
    
    # import plotly.graph_objects as go

    # # データの準備（サンプルデータとしてランダムな3Dデータを生成）
    # y = df1['lat']
    # x = df1['lon']
    # z = df1['Depth_m']
    # c = df1['d18O']
    # # 海岸線の座標データを手動で用意
    # coastline_excel = 'extra_data.xlsx'
    # coastline_df = pd.read_excel(coastline_excel, sheet_name=0)
    # coastline_y = coastline_df['Latitude']  # 海岸線のx座標
    # coastline_x = coastline_df['Longitude']  # 海岸線のy座標  
    # color_continuous_scale= ('gray', 'gray', 'gray', 'gray', 'lightgray', 'lightgray', 'lightgray', 'lightgreen', 'lightgreen', 'green', 'green', 'blue', 'lightblue', 'yellow', 'orange', 'red')
 
    
    # # 3Dプロットを作成する
    # fig11 = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='markers', 
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
    
    # # fig11.update_layout(coloraxis=dict(colorbar=dict(len=0.5)))
    
    
    # # マーカー、ラインの設定
    # fig11.update_traces(
    #     # mode = 'markers+lines', # 'markers+lines', 'markers'
    #     mode = 'markers', # 'markers+lines', 'markers'
    #     marker = dict(size = 3),
    #     # line = dict(width = 2), #color = 'Black',
    #     name='d18O'
    #     )
        
    # fig11.update_layout(
    #         scene = dict(
    #     # #各軸の範囲
    #     xaxis = dict(range=[145,120],),
    #     yaxis = dict(range=[45,20],),
    #     zaxis = dict(range=[-1000,0],),


    #     #各軸のタイトル
    #     yaxis_title='Latitude N',
    #     xaxis_title='Longitude E',
    #     zaxis_title='Water Depth',
    #     ),
    #     width=700,
    #     height=600,
    #     # margin=dict(r=20, l=10, b=10, t=10),

    #         )
    
    # # 海岸線を底面に追加する
    # fig11.add_traces(go.Scatter3d(x=coastline_x, y=coastline_y, z=[max(z)] * len(coastline_x), mode='lines',     marker = dict(size = 3),
    #     # line = dict(width = 2), #color = 'Black',
    #     name='coastline', line=dict(color='blue', width=0.5)))
    
    
    # # グラフを表示する
    # # fig.show()
    # st.write(fig11)
    
    
    
    
    
    
    
    
    
    
    #########    ChatGPTから　　#########
    # import plotly.graph_objects as go

    # # データの準備（サンプルデータとしてランダムな3Dデータを生成）
    # x = [1, 2, 3, 4, 5]
    # y = [1, 2, 3, 4, 5]
    # z = [1, 2, 3, 4, 5]
    
    # # 海岸線の座標データを手動で用意
    # coastline_x = [1, 2, 3, 4, 5]  # 海岸線のx座標
    # coastline_y = [1, 2, 3, 4, 5]  # 海岸線のy座標
    
    # # 3Dプロットを作成する
    # fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='markers')])
    
    # # 海岸線を底面に追加する
    # fig.add_trace(go.Scatter3d(x=coastline_x, y=coastline_y, z=[min(z)] * len(coastline_x), mode='lines', line=dict(color='blue', width=1)))
    
    # # グラフを表示する
    # fig.show()
    
    
    
    
    #####  df表示　#####
    # st.subheader('selected data')
    # st.dataframe(df1)
    
    
    
    
    # fig = px.scatter_mapbox(df1,lat="lat", lon="lon", color="d18O",color_continuous_scale=px.colors.sequential.Viridis)
    # fig.update_layout(mapbox_style="open-street-map", margin={"r":0,"t":0,"l":0,"b":0})
    # fig.show()
    
    # fig.write_html('first_figure.html', auto_open=True)
    
if __name__ == '__main__':
    main()
    



st.cache_data.clear()
st.cache_resource.clear()





