# -*- coding: utf-8 -*-

import streamlit as st
from PIL import Image
import base64
# import streamlit.components.v1 as stc

@st.cache_resource
def main():

    # タイトル
    #タブページ
    #https://welovepython.net/streamlit-layout-container/
    st.title('SEAWATER DATA JAPAN (b02)')
        
    tab1, tab2, tab3, tab4 = st.tabs(["main", "about", "manual", "update"])
    
    with tab1:
        # st.header("SEAWATER DATA JAPAN (b01)")
        # st.title('SEAWATER DATA JAPAN (b01)')

    
        video_file = open('data/d18O_all.mp4', 'rb')
        video_bytes = video_file.read()
    
        st.video(video_bytes)
        
        st.write('movie output by GMT(The Generic Mapping Tools)')
        
    
        image = Image.open('data/qr.jpg')
        st.image(image, caption='QR code')
            
            
    with tab2:
        # st.title('SEAWATER DATA JAPAN (b01)')

        st.header("about")
        # st.header('by TOYOHO ISHIMURA')
        # 純粋なテキスト
        st.text('original data: xxx in prep.')
        # 純粋なテキスト
        st.text('visualized by TOYOHO ISHIMURA (Python with Streamlit)')
        st.header("")
        #gifアニメを読み込む
        st.write('Cruise Area (2015-2021)')
        st.image("data/sites_20230515.gif") 
        
    with tab3:
        # st.title('SEAWATER DATA JAPAN (b01)')

        st.header("manual")
        st.subheader('select sub menu')
        st.write('負荷をかけるとよく落ちます。。。再起動までしばしお待ちください')
        
        

        


        
        # ヘッダ
    with tab4:
        # st.title('SEAWATER DATA JAPAN (b01)')

        st.header('update')
        st.write('2023/05/15 version v02')
            

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
