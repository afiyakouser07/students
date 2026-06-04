import streamlit as st
import pandas as pd
import plotly.express as px

from utils.data_loader import load_data

df = load_data()

st.title("📈 Business Insights")

st.subheader("Top Correlations")

corr = df.select_dtypes(
    include="number"
).corr()["exam_score"]

corr = corr.sort_values(
    ascending=False
)

st.dataframe(
    corr,
    use_container_width=True
)

st.subheader(
    "Average Exam Score by Placement"
)

avg_scores = (
    df.groupby("placement_status")
    ["exam_score"]
    .mean()
    .reset_index()
)

fig = px.bar(
    avg_scores,
    x="placement_status",
    y="exam_score",
    title="Average Exam Score"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("Key Findings")

st.markdown("""
### Insights

- Higher study hours generally increase exam score.
- Attendance positively affects performance.
- Previous scores are strong indicators of future performance.
- Placement likelihood increases with exam score.
- Students with consistent assignments perform better.
""")
