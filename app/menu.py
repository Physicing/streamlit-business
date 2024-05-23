import streamlit as st
from streamlit_option_menu import option_menu


def menu_handler():
    if st.session_state["menu_option"] == "Home":
        st.switch_page("./pages/home.py")
    elif st.session_state["menu_option"] == "About Me":
        st.switch_page("./pages/about.py")


def streamlit_menu(options_list: list):
    selected = option_menu(
        menu_title=None,
        options=options_list,
        icons=["house", "about", "tools", "envelope", "book"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        key="menu_option"
    )
    return selected
