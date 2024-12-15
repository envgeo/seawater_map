# -*- coding: utf-8 -*-

import streamlit as st


def main():
    # # タイトル
    # st.title('SEAWATER DATA on WEB ')
    # # ヘッダ
    # st.header('powered by streamlit')
    # # 純粋なテキスト
    # st.text('Toyoho Isihimura')
    # サブレベルヘッダ
    st.subheader('Please select a sub-menu')
    # マークダウンテキスト
    # st.markdown('**Markdown is available **')
    # # LaTeX テキスト
    # st.latex(r'\bar{X} = \frac{1}{N} \sum_{n=1}^{N} x_i')
    # # コードスニペット
    # st.code('print(\'Hello, World!\')')
    # # エラーメッセージ
    # st.error('Error message')
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

    # st.title('SEAWATER DATA JAPAN (b03)')
    
    st.header("about")
    # st.header('by TOYOHO ISHIMURA')
    # 純粋なテキスト
    st.text('visualized by TOYOHO ISHIMURA (Python with Streamlit)')
    
    st.link_button("For more information and permissions for use, click here", "https://envgeo.h.kyoto-u.ac.jp/sw_jpn/")
    
    # 純粋なテキスト
    st.write('_____')
    st.header('data source')
    st.subheader('#01 Kodama et al., 2024. (main data set)')
    #st.write('Kodama, T., Kitajima, S., Takahashi, M., and Ishimura T. (2024) Spatiotemporal variations of seawater δ18O and δD in the Western North Pacific marginal seas near Japan. Geochemical Journal. DOI: 10.2343/geochemj.GJ24009')
    st.markdown(
        """<a style='display: block; text-align: left;' href="https://doi.org/10.2343/geochemj.GJ24009">Kodama, T., Kitajima, S., Takahashi, M., and Ishimura T. (2024) Spatiotemporal variations of seawater δ18O and δD in the Western North Pacific marginal seas near Japan. Geochemical Journal. DOI: 10.2343/geochemj.GJ24009</a>
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
    
    st.subheader('sub data set included in the section of  "including data from other papers"')
    st.subheader('#02 Yamamoto et al., 2001.')
    st.write('Yamamoto, M., Tanaka, N., & Tsunogai, S. (2001). Okhotsk Sea intermediate water formation deduced from oxygen isotope systematics. Journal of Geophysical Research: Oceans, 106(C12), 31075-31084.')
    st.subheader('#03 Sakamoto et al., 2019.')
    st.write('Sakamoto, T., Komatsu, K., Shirai, K., Higuchi, T., Ishimura, T., Setou, T., ... & Kawabata, A. (2019). Combining microvolume isotope analysis and numerical simulation to reproduce fish migration history. Methods in Ecology and Evolution, 10(1), 59-69.')
    st.subheader('#04 Horikawa et al., 2023.')
    st.write('Horikawa, K., Kodaira, T., Zhang, J., & Obata, H. (2023). Salinity–oxygen isotope relationship during an El Niño (2014–2015) in the southwestern Pacific and comparisons with GEOSECS data (La Niña, 1973–1974). Marine Chemistry, 249, 104222.')
    st.subheader('#05 Kodaira et al., 2016.')
    st.write('Kodaira,  T.,  Horikawa,  K.,  Zhang,  J. and  Senjyu,  T. (2016) Relationship between seawater oxygen isotope ratio and salinity in the Tsushima Current, the Sea of Japan. Chikyukagaku (Geochemistry). 50, 263–277. (in Japanese with English abstract) https://doi.org/10.14934/chikyukagaku.50.263')
    st.write('')
    
    
    
    st.write('_____')
    st.link_button("Go to Lab.", "https://envgeo.h.kyoto-u.ac.jp/sw_jpn/")


if __name__ == '__main__':
    main()
