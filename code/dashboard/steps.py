import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objects as go


def placeholder_data():
    return pd.DataFrame(
        {
            "x": range(20),
            "A": np.random.randn(20).cumsum(),
            "B": np.random.randn(20).cumsum(),
            "C": np.random.randn(20).cumsum(),
        }
    )


def plotly_chart(data):
    fig = go.Figure()
    for col in ["A", "B", "C"]:
        fig.add_trace(go.Scatter(x=data["x"], y=data[col], mode="lines", name=col))

    fig.update_layout(
        margin=dict(l=0, r=0, t=30, b=0),
        plot_bgcolor="rgba(0,0,0,0)",  # transparent plot area
        paper_bgcolor="rgba(0,0,0,0)",  # transparent entire figure background
        legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
        height=250,
    )
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    return fig


# def circular_progress(value, max_value=100, width=250, height=250, color="royalblue"):
#     fig = go.Figure(
#         go.Indicator(
#             mode="gauge+number",
#             value=value,
#             number={"font": {"size": 36, "color": "white"}},
#             gauge={
#                 "shape": "angular",
#                 "axis": {"range": [0, max_value], "visible": False},
#                 "bar": {"color": color, "thickness": 0.9},
#                 "bgcolor": "rgba(0,0,0,0)",  # transparent gauge background
#                 "borderwidth": 0,  # no border
#                 "steps": [{"range": [0, max_value], "color": "#1a1b1f"}],
#                 "threshold": {
#                     "line": {"color": "rgba(0,0,0,0)", "width": 0},
#                     "thickness": 0,
#                     "value": max_value,
#                 },
#             },
#             domain={"x": [0, 1], "y": [0, 1]},
#         )
#     )

#     fig.update_layout(
#         width=width,
#         height=height,
#         margin=dict(t=0, b=0, l=0, r=0),
#         paper_bgcolor="rgba(0,0,0,0)",
#         plot_bgcolor="rgba(0,0,0,0)",
#     )


#     return fig
def circular_progress(value, max_value=100, width=250, height=250, color="royalblue"):
    # Calculate progress percentage
    progress = (value / max_value) * 360 if max_value > 0 else 0
    remaining = 360 - progress

    # Create a pie chart that looks like a circular progress bar
    fig = go.Figure(
        go.Pie(
            values=[progress, remaining] if remaining > 0 else [360],
            labels=["Progress", "Remaining"] if remaining > 0 else ["Complete"],
            marker=dict(
                colors=[color, "#1a1b1f"] if remaining > 0 else [color],
                line=dict(width=0),
            ),
            hole=0.7,  # Creates the donut effect
            sort=False,
            direction="clockwise",
            rotation=0,  # Start from top
            showlegend=False,
            hoverinfo="none",
            textinfo="none",
        )
    )

    # Add the value text in the center
    fig.add_annotation(
        text=f"{value}",
        x=0.5,
        y=0.5,
        font=dict(size=36, color="white"),
        showarrow=False,
        xref="paper",
        yref="paper",
    )

    # Add max value text below
    fig.add_annotation(
        text=f"/ {max_value}",
        x=0.5,
        y=0.35,
        font=dict(size=18, color="gray"),
        showarrow=False,
        xref="paper",
        yref="paper",
    )

    fig.update_layout(
        width=width,
        height=height,
        margin=dict(t=0, b=0, l=0, r=0),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
    )

    return fig


def render():
    st.title("Body Composition")

    ####################################################################################################

    with st.container(border=True):
        left, middle, right = st.columns(3)
        with left:
            st.write("Current Streak")
            fig = circular_progress(50, 100, width=200, height=200)
            st.plotly_chart(fig, use_container_width=False, key="current_streak_chart")
        with middle:
            st.write("Average Steps per day \n (current month)")
            fig = circular_progress(90, 100, width=200, height=200)
            st.plotly_chart(fig, use_container_width=False, key="avg_steps_chart")

        with right:
            c1, c2, c3 = st.columns([1, 2, 1])
            with c2:
                st.markdown(
                    "<div style='text-align: center;'>Average Steps per day<br>(last month)</div>",
                    unsafe_allow_html=True,
                )
                fig = circular_progress(35, 100, width=200, height=200)
                st.plotly_chart(
                    fig, use_container_width=False, key="avg_steps_last_month_chart"
                )

    ####################################################################################################
    # First row
    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True):
            st.subheader("Top Left")
            st.plotly_chart(plotly_chart(placeholder_data()), use_container_width=True)

    with col2:
        with st.container(border=True):
            st.subheader("Top Right")
            st.plotly_chart(plotly_chart(placeholder_data()), use_container_width=True)

    with col3:
        with st.container(border=True):
            st.subheader("Top Right")
            st.plotly_chart(plotly_chart(placeholder_data()), use_container_width=True)
