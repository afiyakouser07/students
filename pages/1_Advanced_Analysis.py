import streamlit as st
import pandas as pd
from utils.data_loader import load_data
from utils.plots import *

df = load_data()

st.title("📊 Advanced Analysis")

st.plotly_chart(
    study_vs_score(df),
    use_container_width=True
)

st.plotly_chart(
    attendance_vs_score(df),
    use_container_width=True
)

st.plotly_chart(
    sleep_vs_score(df),
    use_container_width=True
)
