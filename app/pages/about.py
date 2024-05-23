import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import json


def about_me():
    # Use local CSS
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    local_css("style/style.css")

    def load_lottie(path: str):
        with open(path, "r") as f:
            return json.load(f)

    options_list = ["Home", "About", "Free Tools!", "Contact"]
    option_menu(
        menu_title=None,
        options=options_list,
        icons=["house", "book", "tools", "envelope"],
        menu_icon="cast",
        default_index=1,
        orientation="horizontal",
        key="menu_option"
    )
    if st.session_state["menu_option"] == "Home":
        st.switch_page("./pages/home.py")
    elif st.session_state["menu_option"] == "Free Tools!":
        st.switch_page("./pages/free_tools.py")
    elif st.session_state["menu_option"] == "Contact":
        st.switch_page("./pages/contact.py")

    lottie_datascience = load_lottie("./app/anims/datascience.json")
    lottie_current = load_lottie("./app/anims/current.json")
    lottie_done = load_lottie("./app/anims/done.json")
    lottie_visualization = load_lottie("./app/anims/visualization.json")
    lottie_segmentation = load_lottie("./app/anims/segmentation.json")
    lottie_customer_behavior = load_lottie("./app/anims/customer_behavior.json")
    lottie_recommendation = load_lottie("./app/anims/recommendation.json")
    lottie_forecast = load_lottie("./app/anims/forecast.json")
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("Meet with who will got your back!")
            st.subheader("An Unorthodox Datascientist, who")
            st.title(
                "helps :blue[marketeers] uncover the true meaning of their :orange[hard-to-tackle] data."
            )
            st.subheader("Statistics and data science for marketeers and marketing agencies.")
            st.write("#")
        with right_column:
            st_lottie(lottie_datascience, height=200, key="datascience")
    st.divider()
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown("""
            #
            - #### **:blue[Custom Visualizations:]** So you are tired of all the pre-made visualizations of your marketing\
            data and you think unorthodox like me? No problem! I've done it hundreds of times. We can create\
            interactive dashboards together so that you can have more meaningful insights from your data.
            """)
        with right_column:
            st_lottie(lottie_visualization, height=200, key="visualization")
    st.divider()
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown("""
            #
            - #### **:blue[Customer Segmentation:]** Do you feel your tool's segmentation capability is not enough?\
            No worries! We can create meaningful segments according to their footsteps.
            """)
        with right_column:
            st_lottie(lottie_segmentation, height=200, key="segmentation")
    st.divider()
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown("""
                #
                - #### **:blue[Predicting Customer Behavior:]** Are you wondering how your customer segments decide\
                to buy the producsts in your current circumstances? Fear not! we can extract their analytics and\
                 then train a machine learning algorithm for it to predict their behavior together.
                """)
        with right_column:
            st_lottie(lottie_customer_behavior, height=200, key="customer_behavior")
    st.divider()
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown("""
                    #
                    - #### **:blue[Recommendation Engines]:** Want to recommend users a new content based on their\
                    previous choices? I've been there. We can create state-of-the art recommendation algorithms to\
                    automatically recommend new items together with the power of machine learning and statistics!
                    #
                    """)
        with right_column:
            st_lottie(lottie_recommendation, height=200, key="recommendation")
    st.divider()
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown("""
                        #
                        - #### **:blue[Sales or Conversions Forecasts:]**  Want to predict what your sales or \
                        conversions going to be in the future based on what you have? I'm by your side! We can create\
                         powerful regression algorithms to solve your forecasting need.
                        """)
        with right_column:
            st_lottie(lottie_forecast, height=200, key="forecast")
    st.divider()
    with st.expander("Expand For Detailed Background!"):
        with st.container():

            left_column, right_column = st.columns(2)
            with left_column:
                st.header("What I do")
                st.write("###")
                st.write(
                    """
                    On daily basis:
    
                    - Developing a tool for marketeers, check [GYB Website](https://growgrowgrowyourboat.io/)
                     or our [LinkedIn](https://www.linkedin.com/company/growyourboat/)
                    - Teaching individuals and corporates about data science, maths and statistics.
                    - Consulting startups about cutting-edge AI's, integrating to their workflow.
                    - Helping marketeers to better assess their campaigns according to their past data.
                    - Bragging about how people overestimate the AI's and underestimate the power of statistics.
                    """
                )
            with right_column:
                st_lottie(lottie_current, height=200, key="current")

        with st.container():
            st.write("---")
            left_column, right_column = st.columns(2)
            with left_column:
                st.header("What I did")
                st.write("###")
                st.write(
                    """
                    You believe you had an interesting, yet filled with unrelated experiences in your career? Check mine!
    
                    - Found an untamed land in the construction field, and used that opportunity to
                     market and sell the product while managing a team of hard-laborers, salesman, and specialists. 
                     **(P.S: Yes, I am a data scientist)**
                    - Consulted a cutting-edge AI startup that aims to prevent phone-call scams in technology, and product
                     development.
                    - Found my own startup with great talents to automatize the machine learning processes for
                    data scientists, data scientist-wannabes, and non-professionals without writing any line of code.
                    **(P.S: Amazon killed us so quickly :expressionless:)**
                    - Worked in a team to detect movement and heat for military drones on a really large scale
                     drone cameras.(Oh boy, I really don't like defense industry.)
                    - Made a heat and fire detection systems for drones that can detect even a lighter from
                     dozen kilometers to catch people who lights a fire in forest. (Don't you ever BBQ on my forests.)
                    - Made an autonomous disinfection robot to be used on hospitals while COVID was raging. (The only
                     feature missing is the beeping sound for being the R2-D2)
                    - Worked in a team to make a smart physiotherapy system for stroke-survivors, so that their
                     physiotherapists can evaluate their progress by just looking at their pose estimation analysis.
                    - Worked in a team to make a surgery room assistant with AI to help doctors when they perform the
                     surgery. With simple hand movements, they can control their computer without an external help and
                     without violating their sterilization routine. 
                    - Got my M. Sc. from Physics :tada: :tada:
                    - Got my B. Sc. from Physics :tada:
                    """
                )
            with right_column:
                st_lottie(lottie_done, height=200, key="done")


if __name__ == "__main__":
    st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")
    about_me()