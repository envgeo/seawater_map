# -*- coding: utf-8 -*-

import streamlit as st
from PIL import Image
import base64
# import streamlit.components.v1 as stc



#ワイド表示
# st.set_page_config(page_title="Seawater Japan",layout="wide")


st.set_page_config(
    page_title="Seawater Japan", 
    # page_icon=image, 
    # layout="wide", 
    initial_sidebar_state="auto", 
    menu_items={
         'Get Help': 'https://envgeo.h.kyoto-u.ac.jp/sw_jpn/',
         'Report a bug': "https://www.h.kyoto-u.ac.jp/academic_f/faculty_f/ishimura_toyoho_4dea/#mailform",
         'About': """
         # 日本周辺海水同位体DB
         テスト公開中
         """
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
    st.write('Version b04-202405')
    st.warning('This site is not able to support multiple simultaneous accesses, so if the display does not work, please reload the page or try again after awhile.')
        

        
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["main", "about", "manual", "update", "note in Japanese"])
    
    with tab1:
        # st.header("SEAWATER DATA JAPAN (b02)")
        # st.title('SEAWATER DATA JAPAN (b02)')

    
        #video_file = open('data/d18O_all.mp4', 'rb')
        #video_bytes = video_file.read()
        #st.video(video_bytes)
        
        st.video('data/d18O_all.mp4',format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=True)
    
        st.markdown("<h6 style='text-align: center; color: grey;'>movie outputed by GMT (The Generic Mapping Tools)</h6>", unsafe_allow_html=True)


        #画像をセンタリングするためcolumnを分ける
        image = Image.open('data/qr.jpg')
        col1, col2, col3 = st.columns(3)

        with col1:
            st.write('    ')

        with col2:
            st.image(image, caption='QR code')

        with col3:
            st.write(' ')


            
    with tab2:
        # st.title('SEAWATER DATA JAPAN (b03)')

        st.header("about")
        # st.header('by TOYOHO ISHIMURA')
        # 純粋なテキスト
        st.text('visualized by TOYOHO ISHIMURA (Python with Streamlit)')
        
        st.link_button("For more information and permissions for use, click here", "https://envgeo.h.kyoto-u.ac.jp/sw_jpn/")
        
        # 純粋なテキスト
        st.write('_____')
        st.header('data source')
        st.subheader('#01 Kodama et al., 2024.')
        #st.write('Kodama, T., Kitajima, S., Takahashi, M., and Ishimura T. (2024) Spatiotemporal variations of seawater δ18O and δD in the Western North Pacific marginal seas near Japan. Geochemical Journal. DOI: 10.2343/geochemj.GJ24009')
        st.markdown(
            """<a style='display: block; text-align: left;' href="https://www.jstage.jst.go.jp/article/geochemj/advpub/0/advpub_GJ24009/_article">Kodama, T., Kitajima, S., Takahashi, M., and Ishimura T. (2024) Spatiotemporal variations of seawater δ18O and δD in the Western North Pacific marginal seas near Japan. Geochemical Journal. DOI: 10.2343/geochemj.GJ24009</a>
            """,
            unsafe_allow_html=True,
        )

        st.header("")
        #gifアニメを読み込む
        st.subheader('🚢 Cruise Area (2015-2021)')
        st.image("data/sites_20230515.gif")
        
                #gifアニメを読み込む
        st.subheader('🚢 Sampling sites by Year')
        st.image("data/year_20230517.gif")
        
        st.write('_____')
        st.link_button("Go to Lab.", "https://envgeo.h.kyoto-u.ac.jp/sw_jpn/")
        
        
    with tab3:
        # st.title('SEAWATER DATA JAPAN (b03)')

        st.header("manual")
        st.subheader('select sub menu')
        st.write('PC operation recommended')
        st.link_button("Description of each page", "https://envgeo.h.kyoto-u.ac.jp/sw_jpn/#pages")
        

        


        
        # ヘッダ
    with tab4:
        # st.title('SEAWATER DATA JAPAN (b01)')

        st.header('update')
        st.write('2024/05/15 opend to the public')
        st.write('2023/07/22 bug fix')
        st.write('2023/05/22 version b03 pre-opened')
            

        # ヘッダ
    with tab5:
        # st.title('SEAWATER DATA JAPAN (b01)')

        st.text('note by T.Ishimura')
        st.markdown(
            """<a style='display: block; text-align: left;' href="https://www.h.kyoto-u.ac.jp/academic_f/faculty_f/ishimura_toyoho_4dea/#mailform">問い合わせ</a>
            """,
            unsafe_allow_html=True,
        )
        st.link_button("Go to Lab.", "https://envgeo.h.kyoto-u.ac.jp/sw_jpn/")
        
        st.subheader('2024/05/11')
        st.write('MacのSafariの古いバージョン(16.3以前)では表示されないようです。その他不具合・ご要望など，ご連絡いただければ幸いです。')
        st.write('複数アクセスには対応できておりませんので，表示が上手く行かないときには時間をおいてからおためしください。')
        st.write('今後，公表されている各種データを追加してデータの拡充をしたいと考えています。')



    # サブレベルヘッダ

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
