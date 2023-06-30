import os

import streamlit as st
from modules.utils import add_bg_from_local, set_page_config


def main():
    set_page_config()

    background_img_path = os.path.join(
        "static", "background", "Community Logo.png"
    )
    sidebar_background_img_path = os.path.join(
        "static", "background", "Lila Gradient.png"
    )
    add_bg_from_local(
        background_img_path=background_img_path,
        sidebar_background_img_path=sidebar_background_img_path,
    )

    st.markdown(
        """<h1 style='text-align: center; color: black; font-size: 60px;'> TOBB ETU Bilgisayar Topluluğu
         Web Sayfasına Hoşgeldiniz 👋</h1> \
        <br>""",
        unsafe_allow_html=True,
    )

    st.markdown(
        """<p style='text-align: center;  font-size: 20px;'>
        TOBB ETU Bilgisayar Topluluğu, 2022 yılının Nisan ayında kurulmuş bir öğrenci topluluğudur. Bu topluluğun
        temel amacı, öğrencilerin kendilerini sosyal ve teknik becerilerde en iyi şekilde geliştirebilmesi için
        fırsatlar yaratmaktır. Bu amaçla online ya da yüz yüze etkinlikler düzenliyor, ulusal ve uluslararası
        yarışmalara katılıyor ve açık kaynak kodlu projeler geliştiriyoruz. Türkiye'nin her yerinden ve her eğitim
        seviyesinden insanla birlikte topluluğumuz için birlikte çalışmaya hazırız.
        <br> <br>
        <a href='https://linktr.ee/tobbbilgisayartoplulugu'>Linktr.ee</a> adresimizden farklı platformlardaki
        hesaplarımıza ulaşabilirsiniz.
        </p> """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
