
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

import plotly.express as px
from io import BytesIO
# uploaded_file = st.file_uploader("ファイルを選択", type=["csv", "txt", "xlsx"])

# 純粋なテキスト
st.text('2024/12/01 test version')
st.text('3番目の4Dプロットは日本周辺の可視化用で，描画する緯度経度を固定しています')
st.text('アップしたファイルはメモリ上に格納されるだけでサーバーには保存されません。御安心ください')

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
    
  
    
    
    # #海岸線を重ね書きする場合
    # # 海岸線の座標データを手動で用意
    # coastline_excel = 'extra_data.xlsx'
    # coastline_df = pd.read_excel(coastline_excel, sheet_name=0)
    # coastline_y = coastline_df['Latitude']  # 海岸線のx座標
    # coastline_x = coastline_df['Longitude']  # 海岸線のy座標  
    # color_continuous_scale= ('gray', 'gray', 'gray', 'gray', 'lightgray', 'lightgray', 'lightgray', 'lightgreen', 'lightgreen', 'green', 'green', 'blue', 'lightblue', 'yellow', 'orange', 'red')
 
    
    # fig1.add_traces(go.Scatter(x=coastline_x, y=coastline_y, mode='lines',     marker = dict(size = 3),
    #     # line = dict(width = 2), #color = 'Black',
    #     name='coastline', line=dict(color='blue', width=0.8)))
    
    
    
    st.write(fig1)  
    
    

    
    ###### Fig2 #######
    st.subheader('4D plot')
    color_continuous_scale= ('darkblue', 'blue', 'blue', 'blue','lightgray', 'lightgray', 'gray', 'lightgreen', 'lightgreen', 'green',  'yellow', 'orange', 'red')
   
    fig2=px.scatter_3d(df1, x='x', y='y', z='z',
                    color='index', 
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



    




    ###### Fig3 #######
    st.subheader('4D with coastline')
    



    #z軸を反転
    # st.subheader('data source:')
    
    z_inversion = st.radio("z-axis inversion ", ("YES", "NO"), horizontal=True, args=[1, 0])
    
    if z_inversion == "YES":
            df1['z'] = df1['z']*(-1)

    else:()
    
    

    # データの準備（サンプルデータとしてランダムな3Dデータを生成）
    y = df1['x']
    x = df1['y']
    z = df1['z']
    c = df1['index']




    # 海岸線の座標データを手動で用意
    coastline_excel = 'extra_data.xlsx'
    coastline_df = pd.read_excel(coastline_excel, sheet_name=0)
    coastline_y = coastline_df['Latitude']  # 海岸線のx座標
    coastline_x = coastline_df['Longitude']  # 海岸線のy座標  
    color_continuous_scale= ('gray', 'gray', 'gray', 'gray', 'lightgray', 'lightgray', 'lightgray', 'lightgreen', 'lightgreen', 'green', 'green', 'blue', 'lightblue', 'yellow', 'orange', 'red')
 
    
    # 3Dプロットを作成する
    
    fig3=px.scatter_3d(df1, x='x', y='y', z='z',
                    color='index', 
                    #symbol='species'
                    width=700,
                    height=600,
                    color_continuous_scale=color_continuous_scale,
                )
    # fig3 = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='markers', 
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
    
    # fig11.update_layout(coloraxis=dict(colorbar=dict(len=0.5)))
    
    
    # マーカー、ラインの設定
    fig3.update_traces(
        # mode = 'markers+lines', # 'markers+lines', 'markers'
        mode = 'markers', # 'markers+lines', 'markers'
        marker = dict(size = 3),
        # line = dict(width = 2), #color = 'Black',
        name='index'
        )
        

    
    # ###水深をスケールバーで変える設定
    # fig_depth_max_minus = fig_depth_max*(-1)
    # fig_depth_min_minus = fig_depth_min*(-1)


    ##図のスケール

    fig3.update_layout(
            scene = dict(
        # #各軸の範囲
        xaxis = dict(range=[160,120],),
        yaxis = dict(range=[55,20],),
        # zaxis = dict(range=[fig_depth_max_minus, fig_depth_min_minus],),


        #各軸のタイトル
        yaxis_title='Latitude N',
        xaxis_title='Longitude E',
        zaxis_title='Water Depth',
        ),
        width=700,
        height=600,
        # margin=dict(r=20, l=10, b=10, t=10),

            )
    
    # 海岸線を底面に追加する
    # データの最上部の場合
    fig3.add_traces(go.Scatter3d(x=coastline_x, y=coastline_y, z=[max(z)] * len(coastline_x), mode='lines',     marker = dict(size = 3),
        # line = dict(width = 2), #color = 'Black',
        name='coastline', line=dict(color='blue', width=0.8)))
    
    #スケールの底面の場合
    # fig3.add_traces(go.Scatter3d(x=coastline_x, y=coastline_y, z=[fig_depth_max_minus] * len(coastline_x), mode='lines',     marker = dict(size = 3),
    #     # line = dict(width = 2), #color = 'Black',
    #     name='coastline', line=dict(color='gray', width=0.5)))
    
    
    
    # グラフを表示する
    # fig.show()
    st.write(fig3)
    
    











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





