import streamlit as st
from streamlit_option_menu import option_menu
import base64


def contact():
    # Use local CSS
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    local_css("style/style.css")
    options_list = ["Home", "About", "Free Tools!", "Contact"]
    option_menu(
        menu_title=None,
        options=options_list,
        icons=["house", "book", "tools", "envelope"],
        menu_icon="cast",
        default_index=3,
        orientation="horizontal",
        key="menu_option"
    )
    if st.session_state["menu_option"] == "Home":
        st.switch_page("./pages/home.py")
    elif st.session_state["menu_option"] == "About":
        st.switch_page("./pages/about.py")
    elif st.session_state["menu_option"] == "Free Tools!":
        st.switch_page("./pages/free_tools.py")

    with st.container():
        _, mid_col, _ = st.columns((1, 2, 1))
        with mid_col:
            st.title("""
            Let's Uncover What Your Data is Telling You Together!""")
            st.markdown("""
            #
            #### Are you looking for a 'Data-tamer' that can help you to better understand what your marketing data is\
            telling you? Look no further! Let's discuss together about what invaluable information that we can\
            extract from your marketing data so that you will improve your marketing capabilities significantly. \
            Directly message me from below, connect with me on LinkedIn, or send me an e-mail!
            #
            """)
    st.divider()
    st.markdown("#")
    with st.container():
        _, mid_col, _ = st.columns((1, 2, 1))
        with mid_col:
            with st.expander("Message Directly"):
                contact_form = """
                <form action="https://formsubmit.co/hi@datasciencefor.marketing" method="POST">
                <input type="hidden" name="_captcha" value="false">
                <input type="text" name="name" placeholder="Your Name" required>
                <input type="email" name="email" placeholder="Your E-Mail" required>
                <textarea name="message" placeholder="Your Message" required></textarea>
                <button type="submit">Send</button>
                </form>
                """
                st.markdown(contact_form, unsafe_allow_html=True)
                st.markdown("#")
            left_col, right_col = st.columns((1, 1))

            with left_col:
                st.markdown(
                    """<div style="text-align: center">
                    <a href="https://www.linkedin.com/in/atadvc/">
                    <img src="data:image/png;base64,{}" width="20%">
                    </a></div>""".format(
                        base64.b64encode(open("./images/linkedin.png", "rb").read()).decode()
                    ),
                    unsafe_allow_html=True,
                )
            with right_col:
                st.markdown(
                    """<div style="text-align: center">
                    <a href="mailto:hi@datasciencefor.marketing">
                    <img src="data:image/png;base64,{}" width="20%">
                    </a></div>""".format(
                        base64.b64encode(open("./images/mail.png", "rb").read()).decode()
                    ),
                    unsafe_allow_html=True,
                )


if __name__ == "__main__":
    st.set_page_config(page_title="Data Science For Marketing - Contact", page_icon=":bar_chart:", layout="wide")
    contact()