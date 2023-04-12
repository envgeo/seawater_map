















import streamlit as st
from streamlit_folium import folium_static
import folium
import pandas as pd

@st.cache_resource
def main():
    # "# streamlit-foliums"
    
    # with st.echo():
    #     import streamlit as st
    #     from streamlit_folium import folium_static
    #     import folium
    #     import pandas as pd
    
    # center on Liberty Bell
    m = folium.Map(location=[36.56583, 139.88361], zoom_start=6)
    
    # add marker for Liberty Bell
    # tooltip = "Liberty Bell"
    # folium.Marker(
    #     [39.949610, -75.150282], popup="Liberty Bell", tooltip=tooltip
    # ).add_to(m)
    
    excel_file = 'd18O_20210626-3_NA2.xlsx'
    sheet_num = 1
    
    df = pd.read_excel(excel_file, sheet_name=sheet_num)
    df = df[(df['Depth_m'] <= 15) & (df['Depth_m'] >= 0)] 
    df['lat'] = df['Latitude_degN']
    df['lon'] = df ['Longitude_degE']
    
    for i, row in df.iterrows():
        pop=f"{row['Transect']}"
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
    folium_static(m)
    
if __name__ == '__main__':
    main()
    