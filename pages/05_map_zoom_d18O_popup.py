


import streamlit as st
from streamlit_folium import folium_static
import folium
import pandas as pd






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
        
        
        
    st.sidebar.subheader(':blue[---水深範囲の設定---]') 
        
    
    
    
    #水深の範囲   
    st.sidebar.subheader('水深の範囲')
    sld_depth_min, sld_depth_max = st.sidebar.slider(label='Water depth selected',
                                min_value=0,
                                max_value=1000,
                                value=(0, 15),
                                )
    
    st.write('d18O map (defoult depth: 0-15m) with info')
        
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
    
    excel_file = 'd18O_20210626-3_NA2.xlsx'
    sheet_num = 1
    
    df = pd.read_excel(excel_file, sheet_name=sheet_num)
    
    # df = df[(df['Depth_m'] <= 15) & (df['Depth_m'] >= 0)] 
    
    df = df[(df['Depth_m'] == 'xxx') 
                 
                 |(df['Depth_m'] <= sld_depth_max) & (df['Depth_m'] >= sld_depth_min )#調整用
                 | df.isnull().all(axis=1)]      
    
    
    df['lat'] = df['Latitude_degN']
    df['lon'] = df['Longitude_degE']
    
    for i, row in df.iterrows():
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
    









