# -*- coding: utf-8 -*-

import streamlit as st
from PIL import Image

@st.cache_resource
def main():



    #logo_file = Image.open('data/logo.gif')
    #st.image(logo_file,caption='SEAWATER ISOTOPE JAPAN')

    
    
    # タイトル
    st.title('SEAWATER DATA JAPAN (b01)')
    # サブレベルヘッダ
    st.subheader('select sub menu')
    # ヘッダ
    # st.header('by TOYOHO ISHIMURA')
    # 純粋なテキスト
    st.text('original data: xxx in prep.')
    # 純粋なテキスト
    st.text('visualized by TOYOHO ISHIMURA (Python with Streamlit)')

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

    video_file = open('data/d18O_all.mp4', 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes)
    
    st.write('movie output by GMT')
    
if __name__ == '__main__':
    main()
    
    
st.cache_data.clear()
st.cache_resource.clear()
