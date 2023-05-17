


import streamlit as st
from streamlit_folium import folium_static
import folium
import pandas as pd
import numpy as np





# st.set_page_config(
#     page_title="d18O mapping",
#     # page_icon="🗾",
#     layout="wide"
#     )


@st.cache_resource(experimental_allow_widgets=True)

def main():

    ############################################################
    # リロードボタン
    st.button('Reload')
    
    
######  scalebarで制御してsubmitする場合 ################

    with st.sidebar.form("parameter", clear_on_submit=False):
        
        st.header('select parameters ➡ submit')
        
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
                                    value=(0, 15),
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
    
    
        st.write('Cruise Area (2015-2021)')
        st.image("data/sites_20230515.gif") 
    
    
    
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
    
    df1['lat'] = df1['Latitude_degN']
    df1['lon'] = df1['Longitude_degE']
    
    
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
        
        
    
    st.write(":blue[''d18O map (defoult depth: 0-15m) with info (click!)']")
    
    for i, row in df1.iterrows():
        pop=f"Transect:{row['Transect']} <br> Lon: {row['Longitude_degE']}E <br> Lat: {row['Latitude_degN']}N <br> Depth: {row['Depth_m']}m <br> Date: {row['Date']} <br> Cruise: {row['Cruise']} <br> Station: {row['Station']} <br> Salinity: {row['Salinity']} <br> Temp: {row['Temperature_degC']} <br> d18O: {row['d18O']} <br> dD: {row['dD']}" 
        folium.Marker(
            # 緯度と経度を指定
            location=[row['lat'], row['lon']],
            # ツールチップの指定(都道府県名)
            tooltip=row['d18O'],
            # ポップアップの指定
            popup=folium.Popup(pop, max_width=300),
            # アイコンの指定(アイコン、色)
            icon=folium.Icon(icon_color="white", color="red")
        ).add_to(m)
    
    
    # call to render Folium map in Streamlit
    # folium_static(m, width=800, height=800)
    folium_static(m)
    # st.map(df)

    



if __name__ == '__main__':
    main()
    



st.cache_data.clear()
st.cache_resource.clear()





