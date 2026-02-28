#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 17:15:03 2023
@author: toyoho
V205: JAPAN & GLOBAL 統合版 (NASA database対応)
元のサイドバー選択機能をすべて維持し、Matplotlibによる論文品質出力を継続
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import io
import envgeo_utils_legacy
from sklearn.metrics import r2_score

# --- バージョン管理の設定 ---
version = "2.05"
print(f"--------31_salinity-d18O_reg-line_{version}--------")

import datetime
dt = datetime.datetime.today()
print(dt)

def main():
    st.header(f'Salinity-d18O Relationship Ver.{version}')

    # --- 1. データソース選択 (NASA対応) ---
    ref_data = st.radio(
        "Select Data Source:",
        ["Kodama et al. (2024) only", "Kodama et al. (2024) with other reports", "with NASA_database"],
        horizontal=True
    )

    # 共通ユーティリティから読み込み
    df = envgeo_utils_legacy.load_isotope_data(ref_data)
    
    if df.empty:
        st.warning("No data found.")
        return

    # 基本フィルタリング（元の構造を維持）
    df1 = df[df['Salinity'] > 0].copy()

    # --- 2. サイドバー設定 (元のコードのロジックを完全維持) ---
    st.sidebar.header('Data Selection')

    # Cruise選択
    selected_cruise = st.sidebar.multiselect(
        'Select Cruise:',
        df1['Cruise'].unique(),
        default=df1['Cruise'].unique()
    )
    df1 = df1[df1['Cruise'].isin(selected_cruise)]

    # Station選択 (JAPAN版にあったロジック)
    selected_station = st.sidebar.multiselect(
        'Select Station (Optional):',
        df1['Station'].unique(),
        default=df1['Station'].unique()
    )
    df1 = df1[df1['Station'].isin(selected_station)]

    # 深度フィルタ
    max_d = int(df1['Depth_m'].max())
    min_d = int(df1['Depth_m'].min())
    depth_limit = st.sidebar.slider('Depth (m) filter:', min_d, max_d, (min_d, max_d))
    df1 = df1[(df1['Depth_m'] >= depth_limit[0]) & (df1['Depth_m'] <= depth_limit[1])]

    # プロット設定
    st.sidebar.header('Plot Settings')
    dot_size = st.sidebar.number_input('Dot size:', value=10)
    dot_alpha = st.sidebar.slider('Dot transparency:', 0.0, 1.0, 0.5)

    if df1.empty:
        st.error("Filtered data is empty. Please check selections.")
        return

    # --- 3. 回帰計算 ---
    x_data = df1['Salinity']
    y_data = df1['d18O']
    
    # 線形回帰係数の算出 (numpy)
    coef = np.polyfit(x_data, y_data, 1)
    poly1d_fn = np.poly1d(coef)
    r2 = r2_score(y_data, poly1d_fn(x_data))

    # --- 4. Matplotlib 描画 (論文用書式) ---
    fig = plt.figure(figsize=(7, 6))
    ax = fig.add_subplot(111)

    # 散布図
    ax.scatter(x_data, y_data, s=dot_size, alpha=dot_alpha, color='blue', edgecolors='black', linewidth=0.5)
    
    # 回帰直線
    x_range = np.linspace(x_data.min(), x_data.max(), 100)
    ax.plot(x_range, poly1d_fn(x_range), '--r', label=f'y = {coef[0]:.3f}x + {coef[1]:.3f}')

    # 軸の書式 (Matplotlib独自の詳細設定を維持)
    ax.set_xlabel('Salinity', fontsize=12)
    ax.set_ylabel('$\delta^{18}$O (‰)', fontsize=12)
    ax.tick_params(direction='in', top=True, right=True)
    ax.legend(frameon=False)
    
    # 統計情報の書き出し
    st.write(f"Equation: **y = {coef[0]:.4f}x + {coef[1]:.4f}**")
    st.write(f"R² = {r2:.4f}, n = {len(df1)}")

    # Matplotlib表示
    st.pyplot(fig)

    # 画像保存ボタン (io.BytesIOを使用しローカル保存を回避)
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=300, bbox_inches='tight')
    st.download_button(
        label="Download Publication-Quality Figure",
        data=buf.getvalue(),
        file_name=f"Salinity_d18O_Reg_v{version}.png",
        mime="image/png"
    )

    # --- 5. 地図表示 (Plotly) ---
    st.divider()
    st.subheader('Location Map')
    import plotly.express as px
    
    fig_map = px.scatter_mapbox(
        df1, lat="Latitude_degN", lon="Longitude_degE",
        color="d18O", color_continuous_scale="RdYlBu_r",
        mapbox_style="carto-positron",
        hover_data=["Cruise", "Station", "Depth_m", "Salinity", "d18O"],
        zoom=3
    )
    fig_map.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, height=600)
    st.plotly_chart(fig_map, use_container_width=True)

if __name__ == '__main__':
    main()

# キャッシュのクリアは軽快な動作を妨げるため、ここには記述しません。
