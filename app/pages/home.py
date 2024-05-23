import streamlit as st
from streamlit_option_menu import option_menu


def home():
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
        default_index=0,
        orientation="horizontal",
        key="menu_option"
    )
    if st.session_state["menu_option"] == "About":
        st.switch_page("./pages/about.py")
    elif st.session_state["menu_option"] == "Free Tools!":
        st.switch_page("./pages/free_tools.py")
    elif st.session_state["menu_option"] == "Contact":
        st.switch_page("./pages/contact.py")

    with st.container():
        left_col, mid_col, right_col = st.columns((3, 7, 3))
        with mid_col:
            st.write("#")
            st.markdown("""
            # <div style="text-align: center"> Your marketing data is a bit\
             :orange[tongue-tied] right? I'll make it :blue[talk]! </div>""", unsafe_allow_html=True)
            st.markdown("""
            ### <div style="text-align: center">\
            So that you can examine your past and, reap the benefits of your future!\
            </div>
            """, unsafe_allow_html=True)
            _, second_mid_col, _ = st.columns((3, 2, 3))
            with second_mid_col:
                st.markdown("""
                ## <div style="text-align: center">\
                But how?\
                </div>
                """, unsafe_allow_html=True)

    st.divider()
    with st.container():
        left_col, mid_col, right_col = st.columns((3, 7, 3))
        _, second_mid_col, _ = st.columns((3, 5, 3))
        with mid_col:
            with second_mid_col:
                st.markdown("""
                #
                #### You have been collecting data from:
                ###
                - ##### Your ad campaigns
                - ##### Website traffic
                - ##### Manual sources
                - ##### CRM's etc.
                #
                #### Now, imagine this:
                ###
                - ##### A sales forecast from your previous ad campaigns to predict what your sales could be in a near\
                 future including the seasonality.
                - ##### An extensive descriptive analysis revealing your weakest links in your website that effects\
                 your marketing potential.
                - ##### A sentiment analysis of your customer's feedback that you collected from manual sources to\
                 reassess your strategies.
                - ##### An individualized prediction model trained on your CRM sales funnel that can calculate\
                 whether a  specific customer will be onboarded.
                #
                """)
                st.markdown("""
                ### <div style="text-align: center">\
                What has mentioned are just the tip of the iceberg that we can achieve together! </div>
                                """, unsafe_allow_html=True)
                # st.subheader("What has mentioned are just the tip of the iceberg that we can achieve together!")

    st.divider()
    with st.container():
        left_col, mid_col, right_col = st.columns((3, 7, 3))
        _, second_mid_col, _ = st.columns((3, 5, 3))
        with mid_col:
            with second_mid_col:
                st.markdown("""
                ### <div style="text-align: center"> Intrigued? Reach out to me for more detail! </div>
                """, unsafe_allow_html=True)
                st.button(label="Contact for Availability",
                          type="primary",
                          use_container_width=True,
                          key="contact_button_home")
                if st.session_state["contact_button_home"]:
                    st.switch_page("./pages/contact.py")


if __name__ == "__main__":
    home()