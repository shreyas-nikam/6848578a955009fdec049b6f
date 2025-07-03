
import streamlit as st
import pandas as pd
import plotly.express as px

def run_comparative_analysis():
    # Synthetic dataset
    data = {
        'Country': ['USA', 'China', 'Germany', 'Japan', 'UK', 'India', 'France', 'Brazil', 'Canada', 'Italy'],
        'Trade Volume': [1500, 1800, 1200, 900, 800, 700, 600, 500, 400, 300],
        'Foreign Investment': [800, 700, 600, 500, 400, 300, 200, 100, 50, 25],
        'Cultural Exchange': [70, 60, 80, 50, 75, 40, 65, 30, 55, 20],
        'Economic Growth': [3.0, 6.0, 2.5, 1.0, 1.5, 7.0, 2.0, 1.0, 2.0, 0.5]
    }
    df = pd.DataFrame(data)
    
    # User selection
    countries = st.sidebar.multiselect("Select Countries for Comparison", options=df['Country'], default=['USA', 'China'])
    
    # Filter dataset
    filtered_df = df[df['Country'].isin(countries)]
    
    st.markdown("### Comparative Analysis of Selected Countries")
    st.write("This analysis compares metrics across selected countries.")
    
    # Visualization 1: Bar charts for each metric
    metrics = ['Trade Volume', 'Foreign Investment', 'Cultural Exchange', 'Economic Growth']
    for metric in metrics:
        fig = px.bar(filtered_df, x='Country', y=metric, title=f'{metric} Comparison')
        st.plotly_chart(fig, use_container_width=True)
    
    # Visualization 2: Scatter plot showing correlation between Foreign Investment and Economic Growth
    fig2 = px.scatter(filtered_df, x='Foreign Investment', y='Economic Growth', 
                      hover_name='Country',
                      title='Foreign Investment vs Economic Growth')
    st.plotly_chart(fig2, use_container_width=True)
    
    st.markdown("""
This comparison highlights how these key metrics vary among the selected countries. 
Observe the relationships and differences in economic indicators to understand geopolitical and economic dynamics.
    """)
