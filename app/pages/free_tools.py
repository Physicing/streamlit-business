import streamlit as st
from streamlit_option_menu import option_menu


def free_tools():
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
        default_index=2,
        orientation="horizontal",
        key="menu_option"
    )
    if st.session_state["menu_option"] == "Home":
        st.switch_page("./pages/home.py")
    elif st.session_state["menu_option"] == "About":
        st.switch_page("./pages/about.py")
    elif st.session_state["menu_option"] == "Contact":
        st.switch_page("./pages/contact.py")

    with st.container():
        _, mid_col, _ = st.columns((1, 2, 1))
        with mid_col:
            st.markdown("#")
            st.title("There will be free tools for you in near future!")


if __name__ == "__main__":
    st.set_page_config(page_title="Data Science For Marketing - Free Tools!", page_icon=":bar_chart:", layout="wide")
    free_tools()
