# -*- coding: utf-8 -*-

import streamlit as st
from PIL import Image
import base64
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
    st.write('Current Version: v2.0-202602 (Latest) / b20-202412 (Legacy)')
    st.write(':red[NEW!! Feb 18, 2026: MAJOR UPDATE]')
    # st.write('<span style="color:red;background:white">NEW!!</span> NEW',unsafe_allow_html=True)
    # st.write("This is :blue[test]")
    # st.warning('This site is not able to support multiple simultaneous accesses, so if the display does not work, please reload the page or try again after awhile.')
    st.warning('Note: This application may have limited performance under heavy traffic. If the page fails to load or respond, please refresh your browser or try again after a short while.')

        
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["main", "about", "manual", "update", "Japanese"])
    
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




            
    with tab2:
        # st.title('SEAWATER DATA JAPAN (b03)')

            st.header("about")
            # st.header('by TOYOHO ISHIMURA')
            
            st.write("The geochemical data of more than 2000 seawater samples analyzed around Japan have been visualized. You can visualize any data you like, including salinity, hydrogen isotopes, oxygen isotopes, time period and location, and download a plotted figure from this web application. Interactive 3D/4D display is also available.")
            st.write("As of 2025, the database has expanded to incorporate over 22,000 global ocean isotope records, integrated from the NASA GISS database.")
            st.write("Figures can be freely downloaded and used. Please cite the original articles (see data sources, and search results shown in -Selected Data-) and the URL “https://envgeo.h.kyoto-u.ac.jp/sw_jpn/ by T.Ishimura“. (Dec.,2024).")
                     
            # 純粋なテキスト

            
            st.link_button("For more information and permissions for use, click here", "https://envgeo.h.kyoto-u.ac.jp/sw_jpn/")
            
            st.text('visualization by TOYOHO ISHIMURA @ Kyoto Univ. (Built with Python and Streamlit)')
            
            # 純粋なテキスト
            st.write('_____')
            st.header('data sources')
            

            st.subheader('#01 Kodama et al., 2024. :red[(main data set)]')
            #st.write('Kodama, T., Kitajima, S., Takahashi, M., and Ishimura T. (2024) Spatiotemporal variations of seawater δ18O and δD in the Western North Pacific marginal seas near Japan. Geochemical Journal. DOI: 10.2343/geochemj.GJ24009')
            # st.markdown(
            #     """<a style='display: block; text-align: left;' href="https://doi.org/10.2343/geochemj.GJ24009">Kodama, T., Kitajima, S., Takahashi, M., and Ishimura T. (2024) Spatiotemporal variations of seawater δ18O and δD in the Western North Pacific marginal seas near Japan. Geochemical Journal. DOI: 10.2343/geochemj.GJ24009</a>
            #     """,
            #     unsafe_allow_html=True,
            # )
            
            st.write('Kodama, T., Kitajima, S., Takahashi, M., and Ishimura T. (2024). Spatiotemporal variations of seawater δ18O and δD in the Western North Pacific marginal seas near Japan. Geochemical Journal.')

            
            st.write(':green[DOI:] https://doi.org/10.2343/geochemj.GJ24009')
            st.write(':green[analytical method:] Picarro L2130i-I (at Ibaraki-KOSEN and Kyoto Univ.)')
            st.write(':green[analytical precision:] ±0.03 and ±0.2‰ for δ18O and δD')
            st.write(':green[analytical PI:] Toyoho Ishimura')
            
            st.header("")
            #gifアニメを読み込む
            st.subheader('🚢 Cruise Area (2015-2021)')
            st.image("data/sites_20230515.gif")
            
                    #gifアニメを読み込む
            st.subheader('🚢 Sampling sites by Year')
            st.image("data/year_20230517.gif")
            
            
            st.write('_____')
            
            st.subheader(':red[sub data set included from other papers around JAPAN]')
            st.subheader('#02 Yamamoto et al., 2001.')
            st.write('Yamamoto, M., Tanaka, N., Tsunogai, S. (2001). Okhotsk Sea intermediate water formation deduced from oxygen isotope systematics. Journal of Geophysical Research: Oceans, 106(C12), 31075-31084.')
            st.write(':green[DOI:] https://doi.org/10.1029/2000JC000754')
            st.write(':green[analytical method:] FinniganMAT delta-S with a CO2- H20 equilibration unit')
            st.write(':green[analytical precision:] ±0.02% for δ18O')
            st.write(':green[analytical PI:] ')
            
            
            st.subheader('#03 Sakamoto et al., 2019.')
            st.write('Sakamoto, T., Komatsu, K., Shirai, K., Higuchi, T., Ishimura, T., Setou, T., Kamimura, Y., Watanaebe, C., Kawabata, A. (2019). Combining microvolume isotope analysis and numerical simulation to reproduce fish migration history. Methods in Ecology and Evolution, 10(1), 59-69.')
            st.write(':green[DOI:] https://doi.org/10.1111/2041-210X.13098')
            st.write(':green[analytical method:] Picarro L2120-I (at AORI, Univ. of Tokyo)')
            st.write(':green[analytical precision:] ±0.07‰ for δ18O')
            st.write(':green[analytical PI:] ')
            
            
            st.subheader('#04 Horikawa et al., 2023.')
            st.write('Horikawa, K., Kodaira, T., Zhang, J., Obata, H. (2023). Salinity–oxygen isotope relationship during an El Niño (2014–2015) in the southwestern Pacific and comparisons with GEOSECS data (La Niña, 1973–1974). Marine Chemistry, 249, 104222.')
            st.write(':green[DOI:] https://doi.org/10.1016/j.marchem.2023.104222')
            st.write(':green[analytical method:] Micromass PRISM or Thermo Delta V advantage (at Toyama Univ.)')
            st.write(':green[analytical precision:] ± 0.05‰  for δ18O')
            st.write(':green[analytical PI:] ')
            
            
            st.subheader('#05 Kodaira et al., 2016.')
            st.write('Kodaira, T., Horikawa, K., Zhang, J., Senjyu, T. (2016) Relationship between seawater oxygen isotope ratio and salinity in the Tsushima Current, the Sea of Japan. Chikyukagaku (Geochemistry). 50, 263–277. (in Japanese with English abstract)')
            st.write(':green[DOI:] https://doi.org/10.14934/chikyukagaku.50.263')
            st.write(':green[analytical method:] Micromass PRISM  (at Toyama Univ.)')
            st.write(':green[analytical precision:] ±0.02‰    for δ18O')
            st.write(':green[analytical PI:] ')
            
            st.write('')
            
            st.write('_____')
            
            st.subheader(':red[Global Database Integration]')
            st.write('NASA GISS Global Seawater Oxygen Isotope Database (Jan.23, 2025)]https://data.giss.nasa.gov/o18data/')

            # --- 外部ファイル(テキスト/Markdown)からの読み込み ---
            try:
                with open('dataset/nasa_references.md', 'r', encoding='utf-8') as f:
                    nasa_refs = f.read()
                st.markdown(nasa_refs, unsafe_allow_html=True)
            except FileNotFoundError:
                st.error("The reference list file cannot be found. Please visit https://data.giss.nasa.gov/o18data/ref.html")




            
            st.write('_____')
            st.link_button("Go to Lab.", "https://envgeo.h.kyoto-u.ac.jp/sw_jpn/")
        
        
    with tab3:
        # st.title('SEAWATER DATA JAPAN (b03)')

        st.header("manual")
        st.write('Please select a feature from the Sub-Menu (located in the sidebar).')
        st.write('Recommended Device: PC / Desktop operation is highly recommended for full interactive functionality.')
        st.write('Note: Mobile or tablet displays may have limited features or layout constraints.')
        st.link_button("Description of each page is Here", "https://envgeo.h.kyoto-u.ac.jp/sw_jpn/#pages")
        st.video('https://envgeo.h.kyoto-u.ac.jp/wp-content/uploads/2024/10/envgeo20241016-HD-720p.mp4',format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=True)
        

        


        
        # ヘッダ
    with tab4:
        # st.title('SEAWATER DATA JAPAN (b01)')

        st.header('update')
        
        
        # st.write(':blue[Version 2.00-202602]')
        # st.write(':red[NEW!!] Feb 18, 2026: Major Update (Current Version).')

        # st.write(':blue[Version b20-202412]')
        # st.write('Dec 14, 2024: Added support for Excel file uploads and custom plotting.')
        # st.write('Oct 7, 2024: Added datasets from additional references.')
        # st.write('Sep 26, 2024: Expanded the "Including data from other papers" section with new reference data.')
        # st.write('Jul 26, 2024: Minor updates and optimizations for all visualizers.')
        # st.write('May 15, 2024: Official public release.')
        # st.write('Jul 22, 2023: General bug fixes.')

        # st.write(':blue[Version b03-202305]')
        # st.write('May 22, 2023: Pre-release (Version b03).')
        
   
        # 以下の部分にベタうちでOK，色の強調は「:blue[xxxx]」などで
        """
            :blue[Version 2.00-202602]
            
            :red[NEW!!] Feb 18, 2026: Major Update (Current Version).

            :blue[Version b20-202412]
            
            Dec 14, 2024: Added support for Excel file uploads and custom plotting.
            
            Oct 7, 2024: Added datasets from additional references.
            
            Sep 26, 2024: Expanded the "Including data from other papers" section with new reference data.
            
            Jul 26, 2024: Minor updates and optimizations for all visualizers.
            
            May 15, 2024: Official public release.
            
            Jul 22, 2023: General bug fixes.
           
            :blue[Version b03-202305]
           
            May 22, 2023: Pre-release (Version b03)
            
                    
        """




        # ヘッダ
    with tab5:
        # st.title('SEAWATER DATA JAPAN (b01)')

        st.text('note by T.Ishimura')
        st.write('日本近海で採取した2000以上の海水試料の地球化学データに加えて，NASAのデータベースから全世界20000点以上のデータを統合しデータベース化した上で，インタラクティブな可視化アプリとして公開しました。')
        st.write('塩分、水素同位体(dD)、酸素同位体(d18O)、時間、場所など、お好きなパラメーターでデータを可視化し、ウェブアプリケーション上でプロットした図をダウンロードできます。インタラクティブな3D/4D表示も可能です。  図は自由にダウンロードして利用できますが，お使いの際には引用元（data sources、および「Selected Data」に表示される検索結果を参照）と海洋化学データ可視化サイト「https://envgeo.h.kyoto-u.ac.jp/sw_jpn/ by Toyoho Ishimura」を明記してください。')

        st.markdown(
            """<a style='display: block; text-align: left;' href="https://www.h.kyoto-u.ac.jp/academic_f/faculty_f/ishimura_toyoho_4dea/#mailform">問い合わせ</a>
            """,
            unsafe_allow_html=True,
        )
        st.link_button("Go to Lab.", "https://envgeo.h.kyoto-u.ac.jp/sw_jpn/")
        
        st.write('2024/05/11')
        st.write('MacのSafariの古いバージョン(16.3以前)では表示されないようです。その他不具合・ご要望など，ご連絡いただければ幸いです。')
        st.write('複数アクセスには対応できておりませんので，表示が上手く行かないときには時間をおいてからおためしください。')
        st.write('今後，公表されている各種データを追加してデータの拡充をしたいと考えています。')



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
