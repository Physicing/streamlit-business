import streamlit as st
import json
from menu import streamlit_menu


def app():

    st.switch_page("./pages/home.py")


if __name__ == "__main__":
    st.set_page_config(page_title="Data Science For Marketing", page_icon=":bar_chart:", layout="wide")
    app()