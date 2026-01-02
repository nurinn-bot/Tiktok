import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def app():
    st.header(
        "Sub-Objective 2: Evaluate the Influence of Scarcity and Unexpected Discovery on Shopping Behavior"
    )

    # --------------------------------------------------
    # Problem Statement
    # --------------------------------------------------
    st.subheader("Problem Statement")
    st.write("""
    Scarcity cues such as time-limited promotions and limited product availability, as well as unexpected product discovery, 
    are commonly used in digital commerce. Without proper analysis, it is difficult to determine how strongly these factors 
    influence users’ shopping perceptions and behaviors.
    """)

    # --------------------------------------------------
    # Load dataset
    # --------------------------------------------------
    try:
        df = pd.read_excel("cleaned_tiktok_data.xlsx")  # or pd.read_csv("TikTok_DataFrame.csv")
        st.success("Dataset loaded successfully!")
        st.dataframe(df.head())
    except Exception as e:
        st.error("Failed to load dataset.")
        st.exception(e)
        st.stop()

    # --------------------------------------------------
    # Define factor groups
    # --------------------------------------------------
    Scarcity_vars = [
        'promo_deadline_focus',
        'promo_time_worry',
        'limited_quantity_concern',
        'out_of_stock_worry' 
    ]

    Serendipity_vars = [
        'product_recall_exposure',
        'surprise_finds',
        'exceeds_expectations',
        'fresh_interesting_info',
        'relevant_surprising_info'
    ]

    # --------------------------------------------------
    # Create composite scores
    # --------------------------------------------------
    df['Scarcity'] = df[Scarcity_vars].mean(axis=1)
    df['Serendipity'] = df[Serendipity_vars].mean(axis=1)

    # --------------------------------------------------
    # Correlation heatmap
    # --------------------------------------------------
    correlation_matrix = df[['Scarcity', 'Serendipity']].corr()
    fig = px.imshow(
        correlation_matrix,
        text_auto=".2f",
        color_continuous_scale="RdBu",
        zmin=-1,
        zmax=1,
        width=600,
        height=500
    )
    fig.update_layout(
        title="Correlation Heatmap Between Scarcity and Serendipity Scores",
        xaxis_title="Variables",
        yaxis_title="Variables"
    )
    st.plotly_chart(fig, use_container_width=True)

    # --------------------------------------------------
    # Average scores by monthly_income
    # --------------------------------------------------
    average_scores_by_income = df.groupby('monthly_income')[['Scarcity', 'Serendipity']].mean().reset_index()
    income_order = ['Under RM100', 'RM100 - RM300', 'Over RM300']
    average_scores_by_income['monthly_income'] = pd.Categorical(
        average_scores_by_income['monthly_income'],
        categories=income_order,
        ordered=True
    )
    average_scores_by_income = average_scores_by_income.sort_values('monthly_income')

    melted_scores_income = average_scores_by_income.melt(
        id_vars='monthly_income',
        value_vars=['Scarcity', 'Serendipity'],
        var_name='Score_Type',
        value_name='Average_Score'
    )

    fig = px.bar(
        melted_scores_income,
        x='monthly_income',
        y='Average_Score',
        color='Score_Type',
        barmode='group',
        text_auto='.2f',
        category_orders={'monthly_income': income_order},
        title='Average Scarcity and Serendipity Scores by Monthly Income',
        labels={'monthly_income': 'Monthly Income (RM)', 'Average_Score': 'Average Score', 'Score_Type': 'Score Type'},
        width=900,
        height=500
    )
    fig.update_layout(xaxis_tickangle=-45, legend_title_text='Score Type')
    st.plotly_chart(fig, use_container_width=True)

    # --------------------------------------------------
    # Average scores by gender
    # --------------------------------------------------
    average_scores_by_gender = df.groupby('gender')[['Scarcity', 'Serendipity']].mean().reset_index()
    melted_scores_gender = average_scores_by_gender.melt(
        id_vars='gender',
        value_vars=['Scarcity', 'Serendipity'],
        var_name='Score_Type',
        value_name='Average_Score'
    )

    fig = px.bar(
        melted_scores_gender,
        x='gender',
        y='Average_Score',
        color='Score_Type',
        barmode='group',
        text_auto='.2f',
        title='Average Scarcity and Serendipity Scores by Gender',
        labels={'gender': 'Gender', 'Average_Score': 'Average Score', 'Score_Type': 'Score Type'},
        width=800,
        height=450
    )
    fig.update_layout(legend_title_text='Score Type')
    st.plotly_chart(fig, use_container_width=True)

    # --------------------------------------------------
    # Box plots
    # --------------------------------------------------
    fig = make_subplots(rows=1, cols=2, subplot_titles=["Distribution of Scarcity Score","Distribution of Serendipity Score"])
    fig.add_trace(go.Box(y=df['Scarcity'], name='Scarcity', boxmean=True), row=1, col=1)
    fig.add_trace(go.Box(y=df['Serendipity'], name='Serendipity', boxmean=True), row=1, col=2)
    fig.update_layout(height=500, width=900, showlegend=False)
    fig.update_yaxes(title_text="Scarcity Score", row=1, col=1)
    fig.update_yaxes(title_text="Serendipity Score", row=1, col=2)
    st.plotly_chart(fig, use_container_width=True)

    # --------------------------------------------------
    # Histograms
    # --------------------------------------------------
    fig = make_subplots(rows=1, cols=2, subplot_titles=["Distribution of Scarcity Score","Distribution of Serendipity Score"])
    fig.add_trace(go.Histogram(x=df['Scarcity'], nbinsx=5, name='Scarcity', opacity=0.75), row=1, col=1)
    fig.add_trace(go.Histogram(x=df['Serendipity'], nbinsx=5, name='Serendipity', opacity=0.75), row=1, col=2)
    fig.update_layout(height=500, width=950, showlegend=False)
    fig.update_xaxes(title_text="Scarcity Score", row=1, col=1)
    fig.update_xaxes(title_text="Serendipity Score", row=1, col=2)
    fig.update_yaxes(title_text="Frequency")
    st.plotly_chart(fig, use_container_width=True)
