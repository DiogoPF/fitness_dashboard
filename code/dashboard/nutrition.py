import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


def render():
    tabs = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

    with tabs[0]:
        st.write("Page 1 - Tab 1 content")
        st.subheader("Placeholder Graph")
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_title("Sine Wave")
        st.pyplot(fig)

    with tabs[1]:
        st.write("Page 1 - Tab 2 content")

    with tabs[2]:
        st.write("Page 1 - Tab 3 content")
