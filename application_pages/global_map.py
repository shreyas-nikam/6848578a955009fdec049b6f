
import streamlit as st
import pandas as pd
import plotly.express as px

def run_global_map():
    # Sample data with country codes
    data = {
        'Country': ['USA', 'China', 'Germany', 'Japan', 'UK', 'India', 'France', 'Brazil', 'Canada', 'Italy'],
        'Trade Volume': [1500, 1800, 1200, 900, 800, 700, 600, 500, 400, 300],
        'iso_alpha': ['USA', 'CHN', 'DEU', 'JPN', 'GBR', 'IND', 'FRA', 'BRA', 'CAN', 'ITA']
    }
    df = pd.DataFrame(data)
    
    # Metric selection
    metric = st.sidebar.selectbox("Select Metric for Global Map", options=['Trade Volume']) # Can add other metrics after populating data
    
    # Create choropleth map
    fig = px.choropleth(df,
                        locations="iso_alpha",
                        color=metric,
                        hover_name="Country",
                        color_continuous_scale=px.colors.sequential.Plasma,
                        title=f'Global {metric}')
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    This page displays a global map visualizing the selected metric. 
    The choropleth map illustrates the distribution of the metric across different countries, providing a global perspective.
    """)
