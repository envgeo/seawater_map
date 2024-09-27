# -*- coding: utf-8 -*-

import streamlit as st


def main():
    
    # 注意書き
    st.subheader('including data from previous reports')
    st.info('Kodama et al. (2024), Yamamoto et al. (2001), Sakamoto et al. (2019), Kodaira et al. (2016), Horikawa et al. (2023)')
    st.write('Kodama, T., Kitajima, S., Takahashi, M., & Ishimura, T. (2024). Spatiotemporal variations of seawater δ18O and δD in the Western North Pacific marginal seas near Japan. GEOCHEMICAL JOURNAL, 58(3), 94-108.')
    st.write('Yamamoto, M., Tanaka, N., & Tsunogai, S. (2001). Okhotsk Sea intermediate water formation deduced from oxygen isotope systematics. Journal of Geophysical Research: Oceans, 106(C12), 31075-31084.')
    st.write('Sakamoto, T., Komatsu, K., Shirai, K., Higuchi, T., Ishimura, T., Setou, T., ... & Kawabata, A. (2019). Combining microvolume isotope analysis and numerical simulation to reproduce fish migration history. Methods in Ecology and Evolution, 10(1), 59-69.')
    st.write('Horikawa, K., Kodaira, T., Zhang, J., & Obata, H. (2023). Salinity–oxygen isotope relationship during an El Niño (2014–2015) in the southwestern Pacific and comparisons with GEOSECS data (La Niña, 1973–1974). Marine Chemistry, 249, 104222.')
    st.write('Kodaira,  T.,  Horikawa,  K.,  Zhang,  J. and  Senjyu,  T. (2016) Relationship between seawater oxygen isotope ratio and salinity in the Tsushima Current, the Sea of Japan. Chikyukagaku (Geochemistry). 50, 263–277. (in Japanese with English abstract) https://doi.org/10.14934/chikyukagaku.50.263')
    st.write('')


    # # タイトル
    # st.title('SEAWATER DATA on WEB ')
    # # ヘッダ
    # st.header('powered by streamlit')
    # # 純粋なテキスト
    # st.text('Toyoho Isihimura')
    # サブレベルヘッダ
    # st.subheader('⬅ Select a sub-menu in the sidebar')
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



if __name__ == '__main__':
    main()
