import streamlit as st
import json
from menu import streamlit_menu


def app():
    st.switch_page("./pages/home.py")


if __name__ == "__main__":
    app()