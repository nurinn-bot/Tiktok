import streamlit as st
import pandas as pd
import plotly.express as px

# --- Streamlit Configuration ---
st.set_page_config(
    page_title="Arts Faculty Gender Visualization",
    layout="wide"
)

st.header("Arts Faculty Data Analysis and Visualization 📊", divider="blue")

# ######################################################################
# --- 1. DATA LOADING FROM URL (Replaced Dummy Data) ---
url = 'https://raw.githubusercontent.com/nurinn-bot/EC2024/refs/heads/main/arts_df_exported.csv'
col1, col2, col3, col4 = st.columns(4)
    
col1.metric(label="PLO 2", value=f"3.3", help="PLO 2: Cognitive Skill", border=True)
col2.metric(label="PLO 3", value=f"3.5", help="PLO 3: Digital Skill", border=True)
col3.metric(label="PLO 4", value=f"4.0", help="PLO 4: Interpersonal Skill", border=True)
col4.metric(label="PLO 5", value=f"4.3", help="PLO 5: Communication Skill", border=True)
# Load data from the remote CSV file
# Consider using @st.cache_data for improved performance in a real Streamlit app
arts_df = pd.read_csv(url)
