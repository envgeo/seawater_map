# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import numpy as np


# def main():
#     # 東京のランダムな経度・緯度を生成する
#     data = {
#         'lat': np.random.randn(100) / 100 + 33.68,
#         'lon': np.random.randn(100) / 100 + 135.75,
#     }
#     map_data = pd.DataFrame(data)
#     # 地図に散布図を描く
#     st.map(map_data)


# if __name__ == '__main__':
#     main()
    
#     # -*- coding: utf-8 -*-

# import streamlit as st
# import numpy as np
# from matplotlib import pyplot as plt


# def main():
#     # 描画領域を用意する
#     fig = plt.figure()
#     ax = fig.add_subplot()
#     # ランダムな値をヒストグラムとしてプロットする
#     x = np.random.normal(loc=.0, scale=1., size=(100,))
#     ax.hist(x, bins=20)
#     # Matplotlib の Figure を指定して可視化する
#     st.pyplot(fig)


# if __name__ == '__main__':
#     main()
    
    
    
    
    
    
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import matplotlib.dates as dates
from matplotlib.ticker import FormatStrFormatter
# from matplotlib.ticker import MultipleLocator
# import matplotlib.ticker as ticker



from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score



@st.cache_resource(experimental_allow_widgets=True)
def main():
    
        
    # selected_cruise = st.multiselect('Choose cruise area',
    #                             ['CK',
    #                               'Nansei',
    #                               'nECS',
    #                               'Noto',
    #                               'Pacific',
    #                               'Pacific_west',
    #                               'sECS',
    #                               'Shimane&Tottori',
    #                               'SI',
    #                               'Toyama',
    #                               'Tsushima',
    #                               'Yamato',
    #                               'NA2',
    #                              ])
    # st.write(f'Selected: {selected_cruise}')
    
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
    

    
    
    # """      Spyderのメニューボタンの実行ボタンを使わないと作業ディレクトリが反映されないので注意！     """
    # """      Spyderのメニューボタンの実行ボタンを使わないと作業ディレクトリが反映されないので注意！     """
    # """      Spyderのメニューボタンの実行ボタンを使わないと作業ディレクトリが反映されないので注意！     """
    # """      ファイルの読み込みと保存が別の場所を参照してしまう！！！！     """
    
    

    
    
    
    
    # """手動設定項目"""
    #####################################
    ######    EXCEL BOOK import     #####
    #####################################
    # """"Excelブックインポート"""
    #読み込みExcelブックファイルを指定  (xls, xlsxのどちらでも可能?)
    #Spyderのメニューボタンの実行ボタンを使わないと作業ディレクトリが反映されないので注意！
    
    #耳石
    # excel_file = 'otolith_test.xlsx'
    
    #海水
    excel_file = 'd18O_20210626-3_NA2.xlsx'
    
    
    
    #####################################
    ######    EXCEL SHEET select    #####
    #####################################
    # 
    # """EXCELブックのシート選択、シートごとの描画色も"""
    #読み込まれたExcelファイルから，シート番号を指定。一番左のシートが[0],２番目が[1]
    #4枚目と8枚目と9枚目であれば，[3,7,8]と書く
    #sheet_num = [8,3,7] #順番を入れ替えれば，描画の背面と前面も入れ替わる
    # sheet_num = [1,2,3,4,5,6,7,8]
    sheet_num = [1]
    # sheet_num = [3,4,5,6,7,8]
    
    ######　プロットの色選択，sheet_numの順番に対応 10以上の数がある場合には色を追加 ######
    # https://matplotlib.org/stable/gallery/color/named_colors.html
    color = ["red","blue","lime","green","darkcyan","cyan","orange","yellow","fuchsia","violet","greenyellow"]
    # color = ["red","blue","blue","blue","blue","blue","blue","lime","green","darkcyan","cyan","orange","yellow","fuchsia"]
    
    # #単色の場合
    # uni_color = "blue"
    # color = uni_color,uni_color,uni_color,uni_color,uni_color,uni_color,uni_color,uni_color,uni_color,uni_color,uni_color,uni_color,uni_color
    
    # #自動で色を割り振りたい場合
    # import matplotlib.colors as mcolors
    # tab_colors = mcolors.BASE_COLORS #7色まで
    # tab_colors = mcolors.TABLEAU_COLORS #10色まで
    # tab_colors = mcolors.CSS4_COLORS #148色まで
    # tab_colors = mcolors.XKCD_COLORS #949色まで
    # colorlist = list(tab_colors.keys())
    # color =  colorlist
    
    
    
    
    
    
    ############################################
    ######      font size line etc..       #####
    ############################################
    
    # """凡例（legend）を入れるかどうか"""
    legend = 1 #1以外だと凡例無し
    
    # """図のフォント設定、サイズも"""
    ##### ベースのフォントとフォントサイズの指定
    plt.rcParams['font.family'] = 'Arial'
    plt.rcParams["font.size"] = 15
    
    # """図のサイズと解像度"""
    fig_size = [12,9] #図のサイズ
    fig_dpi = 150 #図の解像度
    
    # """線の太さとマーカーのサイズ"""
    ##### 線の太さとマーカーのサイズと種類
    # lw_select = 2 #プロットラインの太さ
    # marker_select = '.' #プロットマーカーの種類，種類はweb参照
    # ms_select = 15 #プロットマーカーのサイズ
    
    #軸のメモリの長さ
    ax_length = 15
    
    #ラインとプロットの透明度
    # fig_alpha = 0.85 #不透明度、1は透過なし,0.1-1の間の数
    
    
    
    
    ########################################
    ######    SUB FIG: d13C vs d18O    #####
    ########################################
    
    
    # """XYの列を指定 エクセルシートから"""
    
    # # d13C, d18Oの時
    # X_data = "d13C"
    # Y_data = "d18O"
    
    # # #d18O-dDの時
    # X_data = "d18O"
    # Y_data = "dD"
    
    #塩分-d18Oの時
    X_data = "Salinity"
    Y_data = "d18O"
    
    
    # """XYの表示用のラベルを指定"""
    
    # # x=d13C y=d18O
    # X_label = "$\delta^{13}$C"
    # Y_label = "$\delta^{18}$O"
    
    # # # x=d18O, Y=dD
    # X_label = "$\delta^{18}$O"
    # Y_label = "$\delta$D"
    
    # # x=salinity, Y=d18O
    X_label = "salinity"
    Y_label = "$\delta^{18}$O"
    
    
    
    
    
    # """XYの表示用のラベルのスケールを指定"""
    # # x=d13C y=d18O
    # iso_scale_X = "(VPDB)"
    # iso_scale_Y = "(VPDB)"
    
    
    # # dD, d18O
    # iso_scale_X = "(VSMOW)"
    # iso_scale_Y = "(VSMOW)"
    
    # salinity-dD
    iso_scale_X = ""
    iso_scale_Y = "(VSMOW)"
    
    
    
    # """作図用,色とマーカーとサイズやタイトルも"""
    
    sheet_num_XY = sheet_num #ここは変更しない
    ###### 別途，X_Yのプロットをするかどうか,色を一括にするか ######
    #する場合は1,しない場合は2
    X_Y = 1
    
    #メインプロットの設定
    X_Y_C = "red" #色の設定
    X_Y_M = "." #現時点で色は変更設定なしマーカーの種類
    X_Y_S = 100
    
    
    #全体の回帰直線を書く場合「１」　書かない場合には「２」
    reg_line_write = 1
    
    
    
    
    
    #追加でTransect毎の強調プロットをする場合は,d13C_d18O_addを「1」しない場合は「2」　シートナンバー選択、
    X_Y_add1 = 2
    # sheet_num_add = [3,4,5,6]
    # sheet_num_add = [2,3]
    
    # 条件抽出する場合「1」しない場合は「2」　
    fig_add_sort = 1
    selected_row = "Transect"
    
    selected_area = 'CK'
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
    # selected_area = 'NA2'
    
    
    
    
    #追加で緯度経度、海域毎毎の強調プロットをする場合は,d13C_d18O_addを「1」しない場合は「2」　シートナンバー選択、
    X_Y_add2 = 1
    # sheet_num_add = [3,4,5,6]
    # sheet_num_add = [2,3]
    
    #追加用の参照シート、
    sheet_num_add = [1]
    
    
    
    
    
    
    
    
    
    
    
    #タイトル
    # fig_title_X_Y = "XY_PLOT" #d13C_d18O書き出し専用
    fig_title_X_Y= X_label + " - "+ Y_label + "" #d13C_d18O書き出し専用
    
    #追加データのlabel
    sheet_names_add2 = "selected data"
    
    #プロットの透明度
    alpha_all = 0.2 #メインプロット
    alpha_selected = 0.9 #強調プロット
    
    #強調プロットの色の指定
    X_Y_C_add =  "blue" #単色にしたい場合
    X_Y_C_add_each = 1  #シート毎に塗り分けたい場合は「１」　そうでなければ「２」
    
    #個別に近似直線を引く場合「１」，引かない場合はそれ以外の数字
    reg_line_add_write = 1
    
    
    
    #############################################
    ######      data range for SUB FIG      #####
    #############################################
    
    # # #d13C-d18Oの時
    # lim_min_X = -12
    # lim_max_X = -3
    # lim_min_Y = -2
    # lim_max_Y = 1
    
    
    
    # #d18O-dDの時
    # lim_min_X = -5
    # lim_max_X = 1
    # lim_min_Y = -30
    # lim_max_Y = 4
    
    
    # salinity-d18Oの時
    lim_min_X = 20
    lim_max_X = 36
    lim_min_Y = -4
    lim_max_Y = 1
    
    
    ########################################
    ######       save as PDF/PNG       #####
    ########################################
    # """PDFとPNGに書き出しするかどうか、保存場所は作業ディレクトリ"""
    #pdfやpngに書き出すときは「1」　そうでなければ「2」など，1以外の数字
    
    
    
    # # sub fig (d13C-d18O)
    # PDF_export_SUB = 2
    # PNG_export_SUB = 2
    
    
    
    
    
    ############################################
    ######      　　　設定ここまで！！　　       #####
    ############################################
    
    
    
    
    
    
    
    
    
    
    
    
    # """------------------ここから先はさわらない！----------------------"""
    # """------------------ここから先はさわらない！----------------------"""
    # """------------------ここから先はさわらない！----------------------"""
    # """------------------ここから先はさわらない！----------------------"""
    # """以下の設定は基本的に変更しない"""
    
    
    #もとのエクセルファイルのシートリストを表示
    print()
    sheet_all = pd.read_excel(excel_file, sheet_name=None)
    print("選択したExcelのSheetリスト:",list(sheet_all.keys()))
    
    
    
    
    # """オプションでd13C-d18Oのプロットをする場合，回帰直線付き　変更しない"""
    if X_Y == 1:
        # sheet_num_XY = [3,4,5,6,7,8]
        
        print('-------------SUB_FIG   d13C vs d18O-------------')
        fig = plt.figure(figsize = (fig_size),dpi=fig_dpi)
        ax = plt.subplot(111)
    
    
  
    
    
        ax.set_xlabel(X_label + iso_scale_X)
        ax.set_ylabel(Y_label + iso_scale_Y)  #LateX形式で特殊文字
        ax.scatter(-1000, -1000, s=X_Y_S,c=X_Y_C,marker=X_Y_M, alpha=alpha_all, label='ALL') #凡例等のダミー
        # #軸のラベル
        # ax.set_xlabel("$\delta^{13}$C (VPDB)")
        # ax.set_ylabel("$\delta^{18}$O (VPDB)")  #LateX形式で特殊文字
        
        input_sheet_name = pd.ExcelFile(excel_file).sheet_names
        for sheet_num in sheet_num:    
            print("読み込まれたSheet:", [sheet_num], input_sheet_name[sheet_num])
        
        for sheet_num_XY in sheet_num_XY:
            df_fig_ALL = pd.read_excel(excel_file, sheet_name=input_sheet_name[sheet_num_XY])
            
            
            
            
    
            # print(df_fig_ALL)
            Ya = df_fig_ALL[Y_data]
            Xa = df_fig_ALL[X_data]
            # print(d18Oa)
            Ya = Ya.dropna()
            Xa = Xa.dropna()
            # print(d18Oa)
            
    
            #列の要素を表示
            d_select_main = df_fig_ALL[selected_row].value_counts().to_dict()
            d_select_main_sum = df_fig_ALL[selected_row].count().sum()
            print('要素と出現数:', d_select_main)
            print('要素と出現数:', d_select_main_sum)
            print('---------------')
    
            
        
            # for sheet_num_add in sheet_num_add:    
            #     df_fig = pd.read_excel(excel_file, sheet_name=sheet_num)
            #     d18O = df_fig["d18O"]
            #     d13C = df_fig["d13C"]
            ax.set_xlim(lim_min_X, lim_max_X) 
            # ax.set_xticks(np.linspace(-11, -3, 9))
            ax.set_ylim(lim_min_Y, lim_max_Y) 
            
            if X_data == 'Salinity':
                ax.xaxis.set_major_formatter(FormatStrFormatter("%.f"))
            else:
                ax.xaxis.set_major_formatter(FormatStrFormatter("%+.1f"))
            
            
            ax.yaxis.set_major_formatter(FormatStrFormatter("%+.1f"))
            ax.tick_params(length=ax_length)
            # ax.annotate("point A", xy = (-7, 0), size = 15,
            #             color = "red", arrowprops = dict())
            
            
            ax.scatter(Xa, Ya, s=X_Y_S,c=X_Y_C,marker=X_Y_M,lw=0.5, ec="black", alpha=alpha_all)
        plt.title(fig_title_X_Y) #
        plt.legend(fontsize = 20) # 凡例の数字のフォントサイズを設定
        
        
    
        # 回帰直線を追-------------------------------------
        if reg_line_write ==1: 
        # #近似式の係数
            # res1=np.polyfit(d13Ca, d18Oa, 1)
            # # res2=np.polyfit(d13Ca, d18Oa, 2)
            # # res3=np.polyfit(d13Ca, d18Oa, 3)
            # #近似式の計算
            # y1 = np.poly1d(res1)(d13Ca) #1次
            # # y2 = np.poly1d(res2)(d13Ca) #2次
            # # y3 = np.poly1d(res3)(d13Ca) #3次
            
            # #グラフ表示
            # # plt.scatter(d13Ca, d18Oa, label='元データ')
            # plt.plot(d13Ca, y1, label='1次')
            # # plt.plot(d13Ca, y2, label='2次')
            # # plt.plot(d13Ca, y3, label='3次')
        
        
        # 一次関数で多項式近似を行う
        #近似式の係数
            coef = np.polyfit(Xa, Ya, 1)
        #近似式の計算
            y1 = np.poly1d(coef)(Xa) #1次
        #グラフ表示
            plt.plot(Xa, y1, label='regression line (ALL)', c=X_Y_C)
        
            reg_line = 'ALL:  y' + ' = ' + '{:.2f}'.format(coef[0]) + 'x ' +' + ' + '{:.2f}'.format(coef[1]) 
            line_r = np.corrcoef(Xa, Ya)
        
            ax.text(0.99, 0.05+0.01, reg_line + "    (R=" + '{:.2f}'.format(line_r[0,1])+', N=' + str(d_select_main_sum)+')', horizontalalignment='right', transform=ax.transAxes)
        # ax.text(0.99, 0.01, line_r, horizontalalignment='right', transform=ax.transAxes)
    
    
    
        # 作成した多項式近似を表示
            print("回帰直線　ALL:", Y_data + '=' + '{:.2f}'.format(coef[0]) + ' * ' + Y_data + '+' + '{:.2f}'.format(coef[1]))
            print("相関係数（ｒ）:", np.corrcoef(Xa, Ya))
            print("----------------")
    
        else:()    
        
        
    
        # 回帰直線を追-------------------------------------
    
        # 条件抽出する場合
        # fig_add_sort = 1
        # selected_row = "Transect"
        # selected_area = 'Noto'
    
        
        #追加でTransectごとの強調プロットをする場合
        if X_Y_add1 == 1:
            # sheet_num_add = [1]
            # sheet_num_add = [2,3]
            for sheet_num_add in sheet_num_add:    
        
                if X_Y_C_add_each == 1:
                    
                    plt.title(fig_title_X_Y+'_with_selected') #
                    
                    X_Y_C_add  =  color[sheet_num_add] #メインFigと同じくシート毎に分けたい場合
    
                    df_fig_add = pd.read_excel(excel_file, sheet_name=sheet_num_add)
                    
                    
      
    
                    if fig_add_sort == 1:
                        df_fig_add = df_fig_add[df_fig_add[selected_row] == selected_area]
                        plt.title(fig_title_X_Y+'_with_'+ selected_area) #
                    else:()
                        
                    #列の要素を表示
                    d_select_add = df_fig_add[selected_row].value_counts().to_dict()
                    d_select_add_sum = df_fig_add[selected_row].count().sum()
                    print('要素と出現数:', d_select_add)
                    print('要素と出現数:', d_select_add_sum)
                    print('---------------')
                    
                    
                    
                    Y_add = df_fig_add[Y_data]
                    X_add = df_fig_add[X_data]
                    Y_add = Y_add.dropna()
                    X_add = X_add.dropna()
                    
                    ax.scatter(X_add, Y_add, s=X_Y_S,c=X_Y_C_add,marker=X_Y_M, alpha=alpha_selected,lw=0.5, ec="black", label= pd.ExcelFile(excel_file).sheet_names[sheet_num_add])
                    # plt.legend(fontsize = 15) # 凡例の数字のフォントサイズを設定
    
                    
                    #読み込んだシート名の表示用
                    input_file = pd.ExcelFile(excel_file)
                    sheet_names = input_file.sheet_names
                    print("d13C_d18O強調用に読み込まれたSheet:", [sheet_num_add], sheet_names[sheet_num_add])
                    print("　　　　サンプルID:",df_fiｇ_add.iloc[1,0])
                    
                    if reg_line_add_write ==1: 
                    # 一次関数で多項式近似を行う
                    #近似式の係数
                        coef_add = np.polyfit(X_add, Y_add, 1)
                    #近似式の計算
                        y1_add = np.poly1d(coef_add)(X_add) #1次
                    #グラフ表示
                        plt.plot(X_add, y1_add, label='regression line (' + sheet_names[sheet_num_add]+')', c=X_Y_C_add,)
                    
                        reg_line_add = sheet_names[sheet_num_add] + ':  y' + ' = ' + '{:.2f}'.format(coef_add[0]) + 'x ' +' + ' + '{:.2f}'.format(coef_add[1]) 
                        line_r_add = np.corrcoef(X_add, Y_add)
                    
                        ax.text(0.99, 0.05*3.5+0.01, reg_line_add + "    (R=" + '{:.2f}'.format(line_r_add[0,1])+', N=' + str(d_select_add_sum)+')', horizontalalignment='right', transform=ax.transAxes)
                    # ax.text(0.99, 0.01, line_r, horizontalalignment='right', transform=ax.transAxes)
                    
                    
                        plt.legend(fontsize = 10) # 凡例の数字のフォントサイズを設定
                    # 作成した多項式近似を表示
                        print("回帰直線　add:", Y_data + '=' + '{:.2f}'.format(coef_add[0]) + ' * ' + Y_data + '+' + '{:.2f}'.format(coef_add[1]))
                        print("相関係数（ｒ）:", np.corrcoef(X_add, Y_add))
                        print("----------------")
                    else:()
                    
                else:()
                
        else:()
    
        
    
    
    
        #追加で緯度経度とTransevtごとの強調プロットをする場合
        if X_Y_add2 == 1:
            # sheet_num_add = [1]
            # sheet_num_add = [2,3]
            for sheet_num_add in sheet_num_add:    
        
                if X_Y_C_add_each == 1:
                    
                    plt.title(fig_title_X_Y+'_with_selected') #
                    
                    X_Y_C_add  =  color[sheet_num_add] #メインFigと同じくシート毎に分けたい場合
    
                    df_fig_add = pd.read_excel(excel_file, sheet_name=sheet_num_add)
                    
                    
                    ####################################################################################################################################################
    
                    #緯度経度と水深とTransectで制限
                    df1 = df_fig_add
                    
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
                                
                                | df1.isnull().all(axis=1)]      
                      
    
    
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
                    
                    
                    df_fig_add = df1
                    
                    #上記の制限要素用の名前
                    # sheet_names_add2 = 'Area B (N:25-130,E:135-140,D:>10m)'
                    sheet_names_add2 = sheet_names_add2
                    
                    
                    
                    ####################################################################################################################################################
                    
                    
                    
                    
          
                    # if fig_add_sort == 1:
                    #     df_fig_add = df_fig_add[df_fig_add[selected_row] == selected_area]
                    #     plt.title(fig_title_X_Y+'_with_'+ selected_area) #
                    # else:()
                        
                    Y_add = df_fig_add[Y_data]
                    X_add = df_fig_add[X_data]
                    Y_add = Y_add.dropna()
                    X_add = X_add.dropna()
                    
                    
                    #列の要素を表示
                    d_select_add2 = df_fig_add[selected_row].value_counts().to_dict()
                    d_select_add2_sum = df1[selected_row].count().sum()
                    print('要素と出現数:', d_select_add2)
                    print('要素と出現数:', d_select_add2_sum)
                    print('---------------')
    
                    
                    ax.scatter(X_add, Y_add, s=X_Y_S,c=X_Y_C_add,marker=X_Y_M, alpha=alpha_selected,lw=0.5, ec="black", label= sheet_names_add2)
                    # plt.legend(fontsize = 15) # 凡例の数字のフォントサイズを設定
    
                    
                    #読み込んだシート名の表示用
                    input_file = pd.ExcelFile(excel_file)
                    sheet_names = input_file.sheet_names
                    print("d13C_d18O強調用に読み込まれたSheet:", [sheet_num_add], sheet_names[sheet_num_add])
                    print("　　　　サンプルID:",df_fiｇ_add.iloc[1,0])
                    
                    if reg_line_add_write ==1: 
                    # 一次関数で多項式近似を行う
                    #近似式の係数
                        coef_add = np.polyfit(X_add, Y_add, 1)
                    #近似式の計算
                        y1_add = np.poly1d(coef_add)(X_add) #1次
                    #グラフ表示
                        plt.plot(X_add, y1_add, label='regression line (' + sheet_names_add2 +')', c=X_Y_C_add,)
                    
                        reg_line_add = sheet_names_add2 + ':  y' + ' = ' + '{:.2f}'.format(coef_add[0]) + 'x ' +' + ' + '{:.2f}'.format(coef_add[1]) 
                        line_r_add = np.corrcoef(X_add, Y_add)
                    
                        ax.text(0.99, 0.05*3+0.01, reg_line_add + "    (R=" + '{:.2f}'.format(line_r_add[0,1])+', N=' + str(d_select_add2_sum)+')', horizontalalignment='right', transform=ax.transAxes)
                        # ax.text(0.99, 0.01, line_r, horizontalalignment='right', transform=ax.transAxes)
                    
                    
                        plt.legend(fontsize = 10) # 凡例の数字のフォントサイズを設定
                    # 作成した多項式近似を表示
                        print("回帰直線　add:", Y_data + '=' + '{:.2f}'.format(coef_add[0]) + ' * ' + Y_data + '+' + '{:.2f}'.format(coef_add[1]))
                        print("相関係数（ｒ）:", np.corrcoef(X_add, Y_add))
                        print("----------------")
                    else:()
                    
                else:()
                
        else:()
    
    
    
        
            
        # if PDF_export_SUB == 1:
        #     plt.savefig('Fig_'+X_data+'_'+Y_data+'_'+selected_area+'.pdf')
        #     print('pdfに書き出しました')
        # else:
        #     print('pdf書き出し無し')
        
        # if PNG_export_SUB == 1:
        #     plt.savefig('Fig_'+X_data+'_'+Y_data+'_'+selected_area+'.png')
        #     print('pngに書き出しました')
        # else:
        #     print('png書き出し無し')
    
    
    
    
    
    
    

        
        #==========  以下，検証　============
        
        print(("--------MES RMSE R2 (all)--------"))
        
        Y_all_pred = coef[0]*Xa + coef[1]
        print("回帰直線　ALL:", Y_data + '=' + '{:.2f}'.format(coef[0]) + ' * ' + Y_data + '+' + '{:.2f}'.format(coef[1]))
        print('a=',coef[0])
        print('b=',coef[1])
        
        # print(Ya)
        # print(Y_all_pred)
        print()
        ###############　MSE，RMSEの計算
        #https://pythondatascience.plavox.info/scikit-learn/回帰モデルの評価
        
        # from sklearn.metrics import mean_squared_error
        # import numpy as np
        MSE_all = mean_squared_error(Ya, Y_all_pred)
        RMES_all = np.sqrt(mean_squared_error(Ya, Y_all_pred))
            
        print('MES_all:', '{:.4f}'.format(MSE_all))
        print('RMSE_all:', '{:.4f}'.format(RMES_all))
        
        ###############　R2の計算
        # from sklearn.metrics import r2_score
        R2_all =  r2_score(Ya, Y_all_pred)  
        print('R2_all:', '{:.3f}'.format(R2_all))
        
    
        ax.text(0.99, 0+0.01, 'RMSE_all: ' + '{:.3f}'.format(RMES_all)+', R$^{2}$_all: ' + '{:.2f}'.format(R2_all), horizontalalignment='right', transform=ax.transAxes, fontsize=12, c='red')
        
        
        
        print(("--------MES RMSE R2 (add)--------"))
        
        Y_add_pred = coef_add[0]*X_add + coef_add[1]
        print("回帰直線　add:", Y_data + '=' + '{:.2f}'.format(coef_add[0]) + ' * ' + Y_data + '+' + '{:.2f}'.format(coef_add[1]))
        print('a=',coef_add[0])
        print('b=',coef_add[1])
        
        # print(Y_add)
        # print(Y_add_pred)
        print()
        ###############　MSE，RMSEの計算
        #https://pythondatascience.plavox.info/scikit-learn/回帰モデルの評価
        
        # from sklearn.metrics import mean_squared_error
        # import numpy as np
        MSE_add = mean_squared_error(Y_add, Y_add_pred)
        RMES_add = np.sqrt(mean_squared_error(Y_add, Y_add_pred))
            
        print('MES_add:', '{:.4f}'.format(MSE_add))
        print('RMSE_add:', '{:.4f}'.format(RMES_add))
        
        ###############　R2の計算
        # from sklearn.metrics import r2_score
        R2_add =  r2_score(Y_add, Y_add_pred)  
        print('R2_add:', '{:.3f}'.format(R2_add))
        
        ax.text(0.99, 0.05*2+0.01, 'RMSE_add: ' + '{:.3f}'.format(RMES_add)+', R$^{2}$_add: ' + '{:.2f}'.format(R2_add), horizontalalignment='right', transform=ax.transAxes, fontsize=12, c='blue')
    
    
    
    
    #全体のタイトル名　　手入力
        main_title = 'SEAWATER DATA WEB (b01)'
        main_title2 = 'Lon:'+str(sld_lon_min)+'-'+str(sld_lon_max)+', Lat:'+str(sld_lat_min)+'-'+str(sld_lat_max)+', Y:'+str(sld_year_min)+'-'+str(sld_year_max)+', M:'+str(sld_month_min)+'-'+str(sld_month_max)+', S:'+str(sld_sal_min)+'-'+str(sld_sal_max)+', D:'+str(sld_depth_min)+'-'+str(sld_depth_max)+'m'
        # sub_title = 'Area B (N:25-130,E:135-140,D:>10m)'
        # sub_title = '(N:25-130,E:135-140,D:>10m)'
        sub_title2 = ''
        
        # title_head = 'seawater_data_(Sea_of_Japan) \n selected_area'
        title_head = str(main_title+'\n'+main_title2+'\n'+sub_title2)
        
        title_head2 = title_head.replace('_', ' ') #図のタイトル表示用
        fig.suptitle(title_head2,fontsize=20)
        
        
    
        #plt.show()
    

        
        
        #範囲をタイトルに入れる
    else:()
            
    
    
    
    #######################画像を保存するためのボタン作成########################
    sub_title2 = main_title2
    sub_title2 = sub_title2.replace(':', '') #pdf書き出し用
    # sub_title2 = sub_title2.replace('>', '') #pdf書き出し用
    # sub_title2 = sub_title2.replace('<', '') #pdf書き出し用
    sub_title2 = sub_title2.replace(',', '_') #pdf書き出し用
    sub_title2 = sub_title2.replace(' ', '') #pdf書き出し用
    sub_tite = str('Fig_sal_d18O_SW'+'_'+sub_title2+".png")


        
    #画像を保存，以下の方法だとローカルにも保存されてしまう
    # fn = sub_tite
    # # plt.savefig(fn)

    # with open(fn, "rb") as img:
    #     btn = st.download_button(
    #         label="Download image",
    #         data=img,
    #         file_name=fn,
    #         mime="image/png"
    #     )

    #Save to memory first. の場合は，ローカルに保存されないので安心
    import io
    fn = sub_tite
    img = io.BytesIO()
    plt.savefig(img, format='png')
     
    btn = st.download_button(
       label="Download image",
       data=img,
       file_name=fn,
       mime="image/png")
    
    
    
    # st.subheader('Area Chart')
    # st.area_chart(df_fig_ALL)
    
    # Matplotlib の Figure を指定して可視化する
    st.pyplot(fig)



    
    ##########採取地点のmap　拡大可能##################
    
    df1['lat'] = df1['Latitude_degN']
    df1['lon'] = df1 ['Longitude_degE']
    
    # df = pd.DataFrame(
    #     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    #     columns=['lat', 'lon'])
    
    st.map(df1)


if __name__ == '__main__':
    main()
    
