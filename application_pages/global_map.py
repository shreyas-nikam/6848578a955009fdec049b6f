
import streamlit as st
import pandas as pd
import plotly.express as px

def run_global_map():
    st.markdown("## Global Map Visualization")
    # Synthetic Data for Map
    data = {
        'Country': ['USA', 'China', 'Germany', 'Japan', 'India'],
        'Trade Volume': [1500, 1800, 1200, 1000, 900],
        'Foreign Investment': [800, 700, 600, 500, 400],
        'Cultural Exchange': [70, 60, 80, 75, 50],
        'Economic Growth': [2.5, 6.0, 1.5, 1.0, 7.0]
    }
    df = pd.DataFrame(data)
    
    metric = st.selectbox("Select Metric to Display", ['Trade Volume', 'Foreign Investment', 'Cultural Exchange', 'Economic Growth'])
    
    fig = px.choropleth(
        df,
        locations='Country',
        locationmode='country names',
        color=metric,
        color_continuous_scale=px.colors.sequential.Plasma,
        title=f"Global Distribution of {metric}"
    )
    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    run_global_map()
