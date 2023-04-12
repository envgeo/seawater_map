#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 18:09:50 2023

@author: toyoho
"""



import streamlit as st
import numpy as np
import pandas as pd
import cartopy.crs as ccrs
import matplotlib.ticker as mticker
import matplotlib.pyplot as plt
import datetime as dt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes





@st.cache_resource
def main():
    
        
    #元データ読み込み
    # df = pd.read_excel("d18O_20210626-2_test.xlsx")
    
    excel_file = 'd18O_20210626-3_NA2.xlsx'
    sheet_num = 1
    
    df = pd.read_excel(excel_file, sheet_name=sheet_num)
    
    #PDFに書き出すかどうか
    PDF_export_SUB = 2
    
    
    
    #日本地図描画
    
    fig = plt.figure(figsize=(8, 6), facecolor="white", dpi=150,tight_layout=False)
    
    
    # ax = fig.add_subplot(111, projection=ccrs.Mercator(central_longitude=140.0), facecolor="white")
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.set_global()
    ax.coastlines()
    ax.set_extent([120-0.001, 145+0.001, 20-0.001, 45+0.001], crs=ccrs.PlateCarree())
    gl = ax.gridlines(draw_labels=True)
    
    #罫線引くかどうか
    # gl.xlocator = mticker.FixedLocator(np.arange(120, 150.1, 0.5))
    # gl.ylocator = mticker.FixedLocator(np.arange(20, 50.1, 0.5))
    # 後ろの transform 以降を追加
    
    #描画する水深範囲を指定 m
    df1 = df[(df['Depth_m'] == 'xxx') 
              |(df['Depth_m'] <= 10) & (df['Depth_m'] >= 0)
              |(df['Depth_m'] <= 500) & (df['Depth_m'] >= 10)
              |(df['Depth_m'] <= 1000) & (df['Depth_m'] >= 501)
              ] 
    #描画する年範囲を指定
    # df1 = df1[(df1['Year'] <= 2022) & (df['Year'] >= 2014)] 
    
    #描画する月範囲を指定 and指定
    # df1 = df1[(df1['Month'] >= 5) & (df['Month'] <= 10)] 
    #描画する月範囲を指定 or指定
    # df1 = df1[(df1['Month'] >= 11) | (df['Month'] <= 4)] 
    #描画する月範囲を指定
    # df1 = df1[(df1['Transect'] == "Noto") & (df['Transect'] == "Noto")] 
    #描画するPI指定
    # df1 = df1[(df1['PI'] == "Kodama") | (df['PI'] == "Kitajima")] 
    
    
    
    
    #描画するTransectを指定 一つだけの場合
    
    # selected_area = 'CK'
    # selected_area = 'Nansei'
    # selected_area = 'nECS'
    # selected_area = 'Noto'
    # selected_area = 'Pacific'
    # selected_area = 'Pacific_west'
    # selected_area = 'sECS'
    # selected_area = 'Shimane&Tottori'
    # selected_area = 'SI'
    # selected_area = 'Toyama'
    # selected_area = 'Tsushima'
    # selected_area = 'Yamato'
    selected_area = 'NA2'
    
    # df1 = df1[(df1['Transect'] == selected_area)] 
    
    
    
    # #描画する緯度経度を指定 複数の場合
    
    df1 = df1[ (df1['Transect'] == 0) 
                # | (df1['Transect'] == 'CK') 
                # | (df1['Transect'] == 'Nansei') 
                # | (df1['Transect'] == 'nECS') 
                | (df1['Transect'] == 'Noto') 
                # | (df1['Transect'] == 'Pacific') 
                # | (df1['Transect'] == 'Pacific_west') 
                # | (df1['Transect'] == 'sECS')          
                # | (df1['Transect'] == 'Shimane&Tottori')          
                # | (df1['Transect'] == 'SI')
                # | (df1['Transect'] == 'Toyama')
                # | (df1['Transect'] == 'Tsushima')
                # | (df1['Transect'] == 'Yamato')
                # | (df1['Transect'] == 'NA2') 
                ] 
    
    
    # #描画する緯度経度を指定 
    df1 = df1[(df1['Longitude_degE'] == 'xxx') 
              |(df1['Longitude_degE'] <= 145) & (df1['Longitude_degE'] >= 140)    
              |(df1['Longitude_degE'] <= 140) & (df1['Longitude_degE'] >= 135)         
              |(df1['Longitude_degE'] <= 135) & (df1['Longitude_degE'] >= 130)
              |(df1['Longitude_degE'] <= 130) & (df1['Longitude_degE'] >= 125)
              |(df1['Longitude_degE'] <= 125) & (df1['Longitude_degE'] >= 120)
              |(df1['Longitude_degE'] <= 120) & (df1['Longitude_degE'] >= 115)
              ] 
    
    df1 = df1[(df1['Latitude_degN'] == 'xxx')
              |(df1['Latitude_degN'] <= 45) & (df1['Latitude_degN'] >= 40)          
              |(df1['Latitude_degN'] <= 40) & (df1['Latitude_degN'] >= 35)
              |(df1['Latitude_degN'] <= 35) & (df1['Latitude_degN'] >= 30)
              |(df1['Latitude_degN'] <= 30) & (df1['Latitude_degN'] >= 25)
              |(df1['Latitude_degN'] <= 25) & (df1['Latitude_degN'] >= 20)
              ] 
    
    df1['lat'] = df1['Latitude_degN']
    df1['lon'] = df1['Longitude_degE']
    
    # print(df.dtypes)
    
    #描画
    ax_cmap = ax.scatter(df1["Longitude_degE"], df1["Latitude_degN"], c=df1['d18O'],cmap='jet', s=10, alpha=0.7, vmin=-1.5, vmax=1, transform=ccrs.PlateCarree())
    
    
    #カラーバーの位置調整
    # from mpl_toolkits.axes_grid1.inset_locator import inset_axes
    axins1 = inset_axes(ax,
                       width="50%",  # width = 10% of parent_bbox width
                       height="2%",  # height : 50%
                       loc='lower right',
                       bbox_to_anchor=(-0.02, 0.1, 1, -0.7),
                       bbox_transform=ax.transAxes,
                       )
    
    
    fig.colorbar(ax_cmap, shrink=0.65, cax=axins1,orientation='horizontal',label="$\delta^{18}$O"+' (VSMOW)')
    
    # ax.set_title('title', fontsize=20)
    ax.set_title(selected_area, fontsize=20) #Transectでソートした場合
    
    
    st.map(df1)
    
if __name__ == '__main__':
    main()
    