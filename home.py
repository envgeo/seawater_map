# -*- coding: utf-8 -*-

import streamlit as st
from PIL import Image
import base64
import os
# import streamlit.components.v1 as stc



#ワイド表示
# st.set_page_config(page_title="Seawater Japan",layout="wide")


st.set_page_config(
    page_title="Ocean Geochemical Database", 
    # page_icon=image, 
    # layout="wide", 
    initial_sidebar_state="auto", 
    menu_items={
         'Get Help': 'https://envgeo.h.kyoto-u.ac.jp/sw_jpn/',
         'Report a bug': "https://www.h.kyoto-u.ac.jp/academic_f/faculty_f/ishimura_toyoho_4dea/#mailform",
         'About': """
         Interactive 3D-4D Seawater Isotope & Geochemical Database
         – Japan Marginal Seas & Global Ocean –
            by T. Ishimura
              https://envgeo.h.kyoto-u.ac.jp/sw_jpn/"""
     })



# #セレクトボックスのリストを作成
# pagelist = ["page1","page2"]
# #サイドバーのセレクトボックスを配置
# selector=st.sidebar.selectbox( "ページ選択",pagelist)
# if selector=="page1":
#     if st.button('ページ1ボタン'):
#         st.title("ページ1のタイトル")
# elif selector=="page2":
#     if st.button('ページ2ボタン'):
#         st.title("ページ2のタイトル")




@st.cache_resource
def main():

    # タイトル

    #タブページ
    #https://welovepython.net/streamlit-layout-container/
    st.title('SEAWATER DATA AROUND JAPAN')
    st.write(':blue[seawater isotopes (d18O, dD), temperature, salinity, seasonality, and annual variations around JAPAN]')
    st.write('Current Version: v2.10-20260301 (Latest) / b20-202412 (Legacy)')
    st.write(':red[NEW!! Feb 18, 2026: MAJOR UPDATE]')
    # st.write('<span style="color:red;background:white">NEW!!</span> NEW',unsafe_allow_html=True)
    # st.write("This is :blue[test]")
    # st.warning('This site is not able to support multiple simultaneous accesses, so if the display does not work, please reload the page or try again after awhile.')
    st.warning('Note: This application may have limited performance under heavy traffic. If the page fails to load or respond, please refresh your browser or try again after a short while.')

        
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["main", "about", "manual", "update", "Japanese"])
    
    
    ##############################################################
    with tab1:
        # st.header("SEAWATER DATA JAPAN (b02)")
        # st.title('SEAWATER DATA JAPAN (b02)')

    
        #video_file = open('data/d18O_all.mp4', 'rb')
        #video_bytes = video_file.read()
        #st.video(video_bytes)
        
        # 動画の配置
        # st.video('data/d18O_all.mp4',format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=True)
        # st.markdown("<h6 style='text-align: center; color: grey;'>movie outputted by GMT (The Generic Mapping Tools)</h6>", unsafe_allow_html=True)


        # 動画の自動再生
        # 1. まず動画を表示する「道具（関数）」を定義する
        def display_autoplay_video(video_path_or_url):
            import base64
            import os
            
            # 動画ファイルが存在するか、URLであるかを確認
            if not video_path_or_url.startswith(('http://', 'https://')):
                if not os.path.exists(video_path_or_url):
                    st.error(f"動画ファイルが見つかりません: {video_path_or_url}")
                    return
                
                with open(video_path_or_url, "rb") as f:
                    data = f.read()
                    bin_str = base64.b64encode(data).decode()
                    video_url = f"data:video/mp4;base64,{bin_str}"
            else:
                video_url = video_path_or_url
        
            # HTMLで自動再生設定を書き込む
            video_html = f'''
                <video width="100%" autoplay loop muted playsinline>
                    <source src="{video_url}" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
            '''
            st.markdown(video_html, unsafe_allow_html=True)

        # 2. 【ここが重要！】定義した関数を「外側」から呼び出す
        # 動画ファイルのパスを正しく指定してください
        target_video = 'data/d18O_all.mp4' 
        display_autoplay_video(target_video)

        # --- 以下、既存のQRコード表示などのコード ---
        st.markdown("<h6 style='text-align: center; color: grey;'>Animation created with GMT (The Generic Mapping Tools)</h6>", unsafe_allow_html=True)
        
        # image = Image.open('data/qr.jpg')
        # col1, col2, col3 = st.columns(3)
        # with col1:
        #     st.write('    ')
        # with col2:
        #     st.image(image, caption='QR code')
        # with col3:
        #     st.write(' ')
        
        # 使い方例:
        # display_autoplay_video("movie.mp4") 
        # または
        # display_autoplay_video("https://www.example.com/sample.mp4")




    ##############################################################
    with tab2:
        # st.title('SEAWATER DATA JAPAN (b03)')

        st.header("about")
        # st.header('by TOYOHO ISHIMURA')
        
        ###############
        # --- 冒頭のabout　外部ファイル (about.md) の読み込みと実行 ---
        about_file = 'data_text/about.md'

        if os.path.exists(about_file):
            try:
                # ファイルを UTF-8 で読み込みます
                with open(about_file, 'r', encoding='utf-8') as f:
                    ref_content = f.read()
                
                # 読み込んだテキスト（st.writeなど）を Python コードとして実行して表示します
                exec(ref_content)
                
            except Exception as e:
                st.error(f"Error loading {about_file}: {e}")
        else:
            # ファイルがない場合の予備表示（必要なければ消して構いません）
            # st.info(f"情報: {about_file} が見つかりません。")
            st.info(f"情報: {about_file} が見つかりません。")
        ###############

        # 純粋なテキスト
        st.write('_____')
        st.header('data sources')

        
        ###############
        # --- メイン引用文献　外部ファイル (main_references.md) の読み込みと実行 ---
        ref_file_main = 'data_text/main_references.md'

        if os.path.exists(ref_file_main):
            try:
                # ファイルを UTF-8 で読み込みます
                with open(ref_file_main, 'r', encoding='utf-8') as f:
                    ref_content = f.read()
                
                # 読み込んだテキスト（st.writeなど）を Python コードとして実行して表示します
                exec(ref_content)
                
            except Exception as e:
                st.error(f"Error loading {ref_file_main}: {e}")
        else:
            # ファイルがない場合の予備表示（必要なければ消して構いません）
            # st.info(f"情報: {ref_file_main} が見つかりません。")
            st.info(f"情報: {ref_file_main} が見つかりません。")
        ###############

        
        ###############
        # --- その他の引用文献　外部ファイル (other_references.md) の読み込みと実行 ---
        ref_file_others = 'data_text/other_references.md'

        if os.path.exists(ref_file_others):
            try:
                # ファイルを UTF-8 で読み込みます
                with open(ref_file_others, 'r', encoding='utf-8') as f:
                    ref_content = f.read()
                
                # 読み込んだテキスト（st.writeなど）を Python コードとして実行して表示します
                exec(ref_content)
                
            except Exception as e:
                st.error(f"Error loading {ref_file_others}: {e}")
        else:
            # ファイルがない場合の予備表示（必要なければ消して構いません）
            # st.info(f"情報: {ref_file} が見つかりません。")
            st.info(f"情報: {ref_file_others} が見つかりません。")
        ###############

        
        st.write('  ')

        st.subheader(':red[Global Database Integration]')
        st.subheader('NASA GISS Global Seawater Oxygen Isotope Database')
        st.write('https://data.giss.nasa.gov/o18data/')
        
        
        ###############
        # --- NASAデータベースの引用文献　外部ファイル(テキスト/Markdown)からの読み込み ---
        try:
            with open('data_text/nasa_references.md', 'r', encoding='utf-8') as f:
                nasa_refs = f.read()
            st.markdown(nasa_refs, unsafe_allow_html=True)
        except FileNotFoundError:
            st.error("The reference list file cannot be found. Please visit https://data.giss.nasa.gov/o18data/ref.html")
        ###############

        st.write('_____')
        st.link_button("Go to Lab.", "https://envgeo.h.kyoto-u.ac.jp/sw_jpn/")
    
    
        
    ##############################################################
    with tab3:

        st.header('manual')
        
        ###############
        # --- その他の引用文献　外部ファイル (other_references.md) の読み込みと実行 ---
        manual_file = 'data_text/manual.md'

        if os.path.exists(manual_file):
            try:
                # ファイルを UTF-8 で読み込みます
                with open(manual_file, 'r', encoding='utf-8') as f:
                    ref_content = f.read()
                
                # 読み込んだテキスト（st.writeなど）を Python コードとして実行して表示します
                exec(ref_content)
                
            except Exception as e:
                st.error(f"Error loading {manual_file}: {e}")
        else:
            # ファイルがない場合の予備表示（必要なければ消して構いません）
            # st.info(f"情報: {ref_file} が見つかりません。")
            st.info(f"情報: {manual_file} が見つかりません。")
        ###############
        st.write('_____')
        st.link_button("Go to Lab.", "https://envgeo.h.kyoto-u.ac.jp/sw_jpn/")
    

        
    ##############################################################
    with tab4:
        # st.title('SEAWATER DATA JAPAN (b01)')

        st.header('update')
        
        ###############
        # --- アップデートログ　外部ファイル (update_log.md) の読み込みと実行 ---
        update_log_file = 'data_text/update_log.md'

        if os.path.exists(update_log_file):
            try:
                # ファイルを UTF-8 で読み込みます
                with open(update_log_file, 'r', encoding='utf-8') as f:
                    ref_content = f.read()
                
                # 読み込んだテキスト（st.writeなど）を Python コードとして実行して表示します
                exec(ref_content)
                
            except Exception as e:
                st.error(f"Error loading {update_log_file}: {e}")
        else:
            # ファイルがない場合の予備表示（必要なければ消して構いません）
            # st.info(f"情報: {ref_file} が見つかりません。")
            st.info(f"情報: {update_log_file} が見つかりません。")
        ###############
        st.write('_____')
        st.link_button("Go to Lab.", "https://envgeo.h.kyoto-u.ac.jp/sw_jpn/")
    

    



    ##############################################################
    with tab5:


        st.header('このデータベースとwebアプリについて')
        
        ###############
        # --- 日本語簡易説明　外部ファイル (japanese.md) の読み込みと実行 ---
        japanese_file = 'data_text/japanese.md'

        if os.path.exists(japanese_file):
            try:
                # ファイルを UTF-8 で読み込みます
                with open(japanese_file, 'r', encoding='utf-8') as f:
                    ref_content = f.read()
                
                # 読み込んだテキスト（st.writeなど）を Python コードとして実行して表示します
                exec(ref_content)
                
            except Exception as e:
                st.error(f"Error loading {japanese_file}: {e}")
        else:
            # ファイルがない場合の予備表示（必要なければ消して構いません）
            # st.info(f"情報: {ref_file} が見つかりません。")
            st.info(f"情報: {japanese_file} が見つかりません。")
        ###############
        st.write('_____')
        st.link_button("Go to Lab.", "https://envgeo.h.kyoto-u.ac.jp/sw_jpn/")
    



    ##############################################################
    # サブレベルヘッダ
    
    #色を変えるとき
    #st.write('<span style="color:red;background:pink">該当するデータがありません・・・・</span>',unsafe_allow_html=True)


    # st.header('by TOYOHO ISHIMURA')
    # 純粋なテキスト
    # st.text('original data: xxx in prep.')
    # 純粋なテキスト
    # st.text('visualized by TOYOHO ISHIMURA (Python with Streamlit)')

    # # マークダウンテキスト
    # st.markdown('**Markdown is available **')
    # # LaTeX テキスト
    # st.latex(r'\bar{X} = \frac{1}{N} \sum_{n=1}^{N} x_i')
    # # コードスニペット
    # st.code('print(\'Hello, World!\')')
    # # エラーメッセージ
    # st.error('in case of error: push reload button or reload this site')
    # # 警告メッセージ
    # st.warning('Warning message')
    # # 情報メッセージ
    # st.info('Information message')
    # # 成功メッセージ
    # st.success('Success message')
    # # 例外の出力
    # st.exception(Exception('Oops!'))
    # # 辞書の出力
    # d = {
    #     'foo': 'bar',
    #     'users': [
    #         'alice',
    #         'bob',
    #     ],
    # }
    # st.json(d)

    # st.write('in case of error: push reload button or reload this site')
    

    
    #logo_file = Image.open('data/logo.gif')
    #st.image(logo_file,caption='SEAWATER ISOTOPE JAPAN')
    
if __name__ == '__main__':
    main()
    
    
st.cache_data.clear()
st.cache_resource.clear()
