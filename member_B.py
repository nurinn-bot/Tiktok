import streamlit as st
import pandas as pd
import plotly.express as px

# --- Streamlit Configuration ---
st.set_page_config(
    page_title="member_B",
    layout="wide"
)

st.header("Evaluate the Influence of Scarcity and Unexpected Discovery on Shopping Behavior 📊", divider="blue")

# ######################################################################
# --- 1. DATA LOADING FROM URL (Replaced Dummy Data) ---
url = 'https://raw.githubusercontent.com/nurinn-bot/Tiktok/refs/heads/main/TT_dataframe.csv'

# Consider using @st.cache_data for improved performance in a real Streamlit app
df = pd.read_csv(url)
