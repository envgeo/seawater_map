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
    # st.subheader('Please select a sub-menu')
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
    
    
    ############################################
    
    # st.write(':green[DOI:] ')
    # st.write(':green[analytical method:] ')
    # st.write(':green[analytical precision:] ')
    # st.write(':green[analytical PI:] ')
    ############################################

    
    
    
    st.header("about")
    # st.header('by TOYOHO ISHIMURA')
    
    st.write("The geochemical data of more than 2000 seawater samples analyzed around Japan have been visualized. You can visualize any data you like, including salinity, hydrogen isotopes, oxygen isotopes, time period and location, and download a plotted figure from this web application. Interactive 3D/4D display is also available.")
    st.write("Figures can be freely downloaded and used. Please cite the original articles (see data sources, and search results shown in -Selected Data-) and the URL “https://envgeo.h.kyoto-u.ac.jp/sw_jpn/ by T.Ishimura“. (Dec.,2024).")
             
    # 純粋なテキスト

    
    st.link_button("For more information and permissions for use, click here", "https://envgeo.h.kyoto-u.ac.jp/sw_jpn/")
    
    st.text('visualization by TOYOHO ISHIMURA at Kyoto Univ. (created with Python and Streamlit)')
    
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
    
    st.subheader(':red[sub data set included from other papers]')
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
    st.link_button("Go to Lab.", "https://envgeo.h.kyoto-u.ac.jp/sw_jpn/")


if __name__ == '__main__':
    main()
