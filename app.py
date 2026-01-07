"""
Streamlit App: Marketing Insight Dashboard
"""

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Marketing AI Insights", layout="wide")

st.title("📱 Social Media Performance Dashboard")
st.sidebar.header("Filter Options")

# Load data from the Notebook output
try:
    df = pd.read_csv("cleaned_social_data.csv")

    # Sidebar Filters
    category = st.sidebar.multiselect(
        "Select Category",
        options=df["Category"].unique(),
        default=df["Category"].unique(),
    )
    filtered_df = df[df["Category"].isin(category)]

    # Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Posts", len(filtered_df))
    col2.metric("Avg Likes", int(filtered_df["Likes"].mean()))
    col3.metric(
        "Top Category", filtered_df.groupby("Category")["Likes"].mean().idxmax()
    )

    # Visualizations
    st.subheader("Category Performance Analysis")
    fig = px.box(
        filtered_df,
        x="Category",
        y="Likes",
        color="Category",
        title="Engagement Distribution",
    )
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Raw Data Preview")
    st.dataframe(filtered_df.head(20))

except FileNotFoundError:
    st.error(
        "Please run the Jupyter Notebook first to generate 'cleaned_social_data.csv'."
    )
