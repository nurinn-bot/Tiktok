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

#Heatmap
# Create a sub-dataframe with only 'Scarcity' and 'Serendipity'
correlation_data = df[['Scarcity', 'Serendipity']]

# Calculate the correlation matrix
correlation_matrix = correlation_data.corr()

# Create Plotly heatmap
fig = px.imshow(
    correlation_matrix,
    text_auto=".2f",
    color_continuous_scale="RdBu",
    zmin=-1,
    zmax=1
)

fig.update_layout(
    title="Correlation Heatmap Between Scarcity and Serendipity Scores",
    width=500,
    height=450
)

# Display in Streamlit
st.plotly_chart(fig, use_container_width=True)
