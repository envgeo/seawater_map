
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

from io import BytesIO
# uploaded_file = st.file_uploader("ファイルを選択", type=["csv", "txt", "xlsx"])





# ファイルアップロード
uploaded_file = st.file_uploader("excelファイル(upload_data_tmp.xlsx)をアップロードしてください", type="xlsx")

# ファイルがアップロードされた場合
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    df1 = df
    st.write("アップロードされたデータフレーム:")
    st.write(df1)
    








    
    
    
    

        




    ############################################################
    # リロードボタン
    st.button('Reload')
    

    

    
    
    # excel_file = 'upload_data_tmp.xlsx'
    # sheet_num = 0
    
    # df1 = pd.read_excel(excel_file, sheet_name=sheet_num)

    
    
    
    x_value = df1.iloc[0, 0]
    print(x_value)
    

    
    import plotly.express as px
    
    
    
    
    ###### Fig1 #######
    st.subheader('3D plot')
    # color_continuous_scale= ('darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'blue', 'blue', 'blue', 'blue', 'blue', 'lightblue',  'lightblue',  'lightblue',  'lightblue',  'lightblue',  'lightblue',  'lightblue', 'lightgray', 'lightgreen', 'yellow', 'orange', 'red', )
    color_continuous_scale= ('darkblue', 'blue', 'lightblue',  'lightgreen', 'green', 'yellow', 'orange', 'red', )

    fig1 = px.scatter(df1, x="x", y="y", color="z", trendline='ols',trendline_color_override='gray', 
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
    
    
        

    
    
    
    ###### Fig2 #######
    st.subheader('4D plot')
    color_continuous_scale= ('darkblue', 'blue', 'blue', 'blue','lightgray', 'lightgray', 'gray', 'lightgreen', 'lightgreen', 'green',  'yellow', 'orange', 'red')
   
    fig2=px.scatter_3d(df1, x='x', y='y', z='z',
                    color='index', 
                    #symbol='species'
                    # width=700,
                    # height=600,
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
        # xaxis = dict(range=[145,120],),
        # yaxis = dict(range=[45,20],),

        #各軸のタイトル
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z',
        ),
        # width=700,
        # margin=dict(r=20, l=10, b=10, t=10),

            )






    fig2.update_layout(
            scene = dict(
        # #各軸の範囲
        # xaxis = dict(range=[36,20],),
        # yaxis = dict(range=[+1,-4],),
        # zaxis = dict(range=[-1000,0],),


        ),
        width=700,
        height=600,
        # margin=dict(r=20, l=10, b=10, t=10),

            )


    st.write(fig2)




else:  

#データフレームを作ってexcelで書き出し，ダウンロード

    list1=[[1,11,21,"area1"], [2,12,22,'area2'], [3,13,23,'area3'],[4,14,24,'area4']]
    index1 = ["Row1", "Row2", "Row3","Row4"]
    columns1 =["x", "y", "z", "index"]
    df =     pd.DataFrame(data=list1, index=index1, columns=columns1)
    
    df.to_excel(buf := BytesIO(), index=False)
    
    st.download_button(
        "excelテンプレファイルのダウンロードはここから",
        buf.getvalue(),
        "upload_data_tmp.xlsx",
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
    

st.cache_data.clear()
st.cache_resource.clear()





