
import streamlit as st
import pandas as pd
import plotly.express as px

def run_data_visualization():
    # Sample Data
    data = {
        'Country': ['USA', 'China', 'Germany', 'Japan', 'UK', 'India', 'France', 'Brazil', 'Canada', 'Italy'],
        'Trade Volume': [1500, 1800, 1200, 900, 800, 700, 600, 500, 400, 300],
        'Foreign Investment': [800, 700, 600, 500, 400, 300, 200, 100, 50, 25],
        'Cultural Exchange': [70, 60, 80, 50, 75, 40, 65, 30, 55, 20],
        'Economic Growth': [3.0, 6.0, 2.5, 1.0, 1.5, 7.0, 2.0, 1.0, 2.0, 0.5]
    }
    df = pd.DataFrame(data)

    # Sidebar selections
    countries = st.sidebar.multiselect("Select Countries", options=df['Country'].unique(), default=['USA', 'China'])
    metric = st.sidebar.selectbox("Select Metric", options=['Trade Volume', 'Foreign Investment', 'Cultural Exchange', 'Economic Growth'])

    # Filter data
    filtered_df = df[df['Country'].isin(countries)]

    # Create bar chart
    fig = px.bar(filtered_df, x='Country', y=metric, title=f'{metric} by Country')
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    This page allows you to visualize the selected metric for different countries. 
    Select countries and a metric from the sidebar to update the bar chart.
    The bar chart displays the values of the chosen metric for the selected countries, enabling easy comparison.
    """)

