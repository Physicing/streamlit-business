import streamlit as st
import json
from menu import streamlit_menu


def app():
    st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")
    st.switch_page("./pages./home.py")


if __name__ == "__main__":
    app()