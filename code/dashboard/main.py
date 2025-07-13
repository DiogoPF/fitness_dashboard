import streamlit as st
from streamlit_option_menu import option_menu

# Import your pages
import body_comp
import steps
import gym_progression
import habits
import nutrition

st.set_page_config(layout="wide")

# Custom CSS
st.markdown(
    """
    <style>
        .stApp {
            background-color: #282830;
        }
        .stApp > header {
            background-color: transparent !important;
        }
        section[data-testid="stSidebar"] {
            background-color: #1e1e24 !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar menu
with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=[
            "🧍🏻Body Composition",
            "🥦Nutrition",
            "📋Habits",
            "🚶🏻‍♂️Steps",
            "💪🏻Gym Progression",
        ],
        icons=["dumb", "dumb", "dumb", "dumb", "dumb"],
        menu_icon="",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#1e1e24"},
            "icon": {"transparent": "inherit", "font-size": "18px"},
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "0",
                "--hover-color": "#282830",
            },
            "nav-link-selected": {"background-color": "#ec937e", "color": "white"},
        },
    )


# Dispatch to selected page
PAGES = {
    "🧍🏻Body Composition": body_comp,
    "🚶🏻‍♂️Steps": steps,
    "💪🏻Gym Progression": gym_progression,
    "📋Habits": habits,
    "🥦Nutrition": nutrition,
}

PAGES[selected].render()
