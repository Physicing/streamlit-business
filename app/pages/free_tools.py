import streamlit as st
from streamlit_option_menu import option_menu
from bs4 import BeautifulSoup
import pathlib
import shutil

GA_ID = "google_analytics"
GA_SCRIPT = """
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-FC8YS9BH40"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-FC8YS9BH40');
</script>
"""


def inject_ga():
    index_path = pathlib.Path(st.__file__).parent / "static" / "index.html"
    soup = BeautifulSoup(index_path.read_text(), features="html.parser")
    if not soup.find(id=GA_ID):
        bck_index = index_path.with_suffix('.bck')
        if bck_index.exists():
            shutil.copy(bck_index, index_path)
        else:
            shutil.copy(index_path, bck_index)
        html = str(soup)
        new_html = html.replace('<head>', '<head>\n' + GA_SCRIPT)
        index_path.write_text(new_html)


def free_tools():
    # Use local CSS
    inject_ga()

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
