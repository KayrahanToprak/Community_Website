import os

import streamlit as st
from modules.utils import add_bg_from_local, local_css, set_page_config


def main():
    set_page_config()

    background_img_file = os.path.join("input", "Community Logo.png")
    sidebar_background_img_file = os.path.join("input", "Lila Gradient.png")
    add_bg_from_local(
        background_img_file=background_img_file,
        sidebar_background_img_file=sidebar_background_img_file,
    )
    local_css("style/style.css")

    st.markdown(
        "<h1 style='text-align: center; color: black; font-size: 60px;'> 📧 Geri Bildirim Formu </h1> <br>",
        unsafe_allow_html=True,
    )

    feedback_message = '<p style="font-family:Arial; font-size: 30px;" align="center"> \
    Aşağıdaki metin alanını doldurarak topluluk hakkındaki görüşlerinizi bize iletebilirsiniz. Teşekkürler!</p>'
    st.markdown(feedback_message, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    contact_form = """
    <form action="https://formsubmit.co/kuantum21fizik@gmail.com" method="POST" align="center">
        <input type="hidden" name="_captcha" value="false">
        <input type="hidden" name="_subject" value="CS Community Feedback!">
        <input type="text" name="name" placeholder="İsminiz" required>
        <input type="email" name="email" placeholder="Mailiniz" required>
        <textarea name="message" placeholder="Mesajınızı buraya yazın."></textarea>
        <button type="submit">Gönder</button>
        <input type="hidden" name="_next" value="https://tobbetu-bilgisayar-toplulugu.streamlit.app">
    </form>
    """
    _, center_col, _ = st.columns([1, 3, 1])
    center_col.markdown(contact_form, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
