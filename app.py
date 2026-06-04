import streamlit as st
import pandas as pd
import plotly.express as px

from utils.data_loader import load_data
from utils.plots import *

st.set_page_config(
    page_title="Student Analytics Dashboard",
    layout="wide"
)

df = load_data()

st.title("🎓 Student Performance Analytics Dashboard")

st.markdown("---")

col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "Total Students",
    len(df)
)

col2.metric(
    "Average Score",
    round(df["exam_score"].mean(),2)
)

placement_rate = (
    (df["placement_status"]=="Placed")
    .mean()*100
)

col3.metric(
    "Placement Rate",
    f"{placement_rate:.1f}%"
)

col4.metric(
    "Average Attendance",
    round(df["attendance"].mean(),1)
)

st.markdown("---")

st.subheader("Dataset Preview")

st.dataframe(
    df.head(20),
    use_container_width=True
)

st.markdown("---")

st.subheader("Dataset Information")

info = pd.DataFrame({
    "Column":df.columns,
    "Data Type":df.dtypes.astype(str)
})

st.dataframe(
    info,
    use_container_width=True
)

st.markdown("---")

st.subheader("Missing Values")

missing = pd.DataFrame(
    df.isnull().sum(),
    columns=["Missing Values"]
)

st.dataframe(
    missing,
    use_container_width=True
)

st.markdown("---")

st.subheader("Exam Score Distribution")

st.plotly_chart(
    score_distribution(df),
    use_container_width=True
)

st.markdown("---")

st.subheader("Correlation Heatmap")

num_df = df.select_dtypes(include="number")

fig = px.imshow(
    num_df.corr(),
    text_auto=True,
    aspect="auto",
    title="Correlation Matrix"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
