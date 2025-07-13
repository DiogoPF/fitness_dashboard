import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import base64
from datetime import date


# df = pd.read_csv("../data/body_composition_agg.csv")
# iso_calendar = date.today().isocalendar()
# current_week = df[
#     (df["week_number"] == iso_calendar.week) & (df["year"] == iso_calendar.year)
# ]


# def placeholder_data():
#     return pd.DataFrame(
#         {
#             "x": range(20),
#             "A": np.random.randn(20).cumsum(),
#             "B": np.random.randn(20).cumsum(),
#             "C": np.random.randn(20).cumsum(),
#         }
#     )


# def plotly_chart(data):
#     fig = go.Figure()
#     for col in ["A", "B", "C"]:
#         fig.add_trace(go.Scatter(x=data["x"], y=data[col], mode="lines", name=col))

#     fig.update_layout(
#         margin=dict(l=0, r=0, t=30, b=0),
#         plot_bgcolor="rgba(0,0,0,0)",  # transparent plot area
#         paper_bgcolor="rgba(0,0,0,0)",  # transparent entire figure background
#         legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
#         height=250,
#     )
#     fig.update_xaxes(showgrid=False)
#     fig.update_yaxes(showgrid=False)
#     return fig


# def get_image_base64(path):
#     with open(path, "rb") as f:
#         data = f.read()
#     return base64.b64encode(data).decode()


# def render():
#     st.title("Body Composition")

#     col1, col2, col3, col4 = st.columns(4)

#     def render_col(col, img_path, label, value, past_value, unit="Kg"):
#         img_b64 = get_image_base64(img_path)
#         sign = "+" if past_value > 0 else ""
#         with col.container():
#             st.markdown(
#                 f"""
#                 <div style="
#                     display: flex;
#                     align-items: center;
#                     gap: 20px;
#                     min-height: 100px;
#                     padding: 16px 20px;
#                     border: 1px solid rgba(230, 230, 230, 0.5);
#                     border-radius: 10px;
#                     box-shadow: 0 1px 3px rgb(0 0 0 / 0.1);
#                     box-sizing: border-box;
#                     width: fit-content;
#                     max-width: 100%;
#                     margin: auto;
#                     background-color: rgba(255, 255, 255, 0.05);
#                 ">
#                     <img src="data:image/png;base64,{img_b64}" width="50" style="margin-right: 15px;"/>
#                     <div style="
#                         text-align: left;
#                         padding-top: 10px;
#                         padding-bottom: 20px;
#                     ">
#                         <div style="font-weight: bold; font-size: 24px;">{label}</div>
#                         <div>{value} {unit} ({sign}{past_value})</div>
#                     </div>
#                 </div>
#                 """,
#                 unsafe_allow_html=True,
#             )

#     render_col(
#         col1,
#         "assets/weight_icon.png",
#         "Weight",
#         current_week["weight"].iloc[0],
#         -10,
#         unit="Kg",
#     )
#     render_col(
#         col2,
#         "assets/muscle_icon.png",
#         "Muscle Mass",
#         current_week["skeletal_muscle_mass"].iloc[0],
#         -10,
#         unit="Kg",
#     )
#     render_col(
#         col3,
#         "assets/lipid.png",
#         "Fat Mass",
#         current_week["body_fat_mass"].iloc[0],
#         10,
#         unit="Kg",
#     )
#     render_col(
#         col4,
#         "assets/fat_percentage_icon.png",
#         "Body Fat %",
#         current_week["body_fat_percentage"].iloc[0],
#         -10,
#         unit="%",
#     )

#     # Add a horizontal line
#     st.markdown("---")

#     col1, col2 = st.columns(2)

#     with col1:
#         with st.container(border=True):
#             st.subheader("Weight")
#             st.plotly_chart(plotly_chart(placeholder_data()), use_container_width=True)
#         with st.container(border=True):
#             st.subheader("Muscle Mass")
#             st.plotly_chart(plotly_chart(placeholder_data()), use_container_width=True)

#     with col2:
#         with st.container(border=True):
#             st.subheader("Fat Mass")
#             st.plotly_chart(plotly_chart(placeholder_data()), use_container_width=True)
#         with st.container(border=True):
#             st.subheader("Body Fat %")
#             st.plotly_chart(plotly_chart(placeholder_data()), use_container_width=True)


# # # tabs = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

# # # with tabs[0]:
# # #     st.write("Page 1 - Tab 1 content")
# # #     st.subheader("Placeholder Graph")
# # #     x = np.linspace(0, 10, 100)
# # #     y = np.sin(x)
# # #     fig, ax = plt.subplots()
# # #     ax.plot(x, y)
# # #     ax.set_title("Sine Wave")
# # #     st.pyplot(fig)

# # # with tabs[1]:
# # #     st.write("Page 1 - Tab 2 content")

# # # with tabs[2]:
# # #     st.write("Page 1 - Tab 3 content")


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
