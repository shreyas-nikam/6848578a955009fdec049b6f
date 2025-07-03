
import streamlit as st
import pandas as pd
import plotly.express as px

def run_country_comparison():
    st.markdown("## Country Comparison")

    # Synthetic Data
    data = {
        'Country': ['USA', 'China', 'Germany', 'Japan', 'India'],
        'Trade Volume': [1500, 1800, 1200, 1000, 900],
        'Foreign Investment': [800, 700, 600, 500, 400],
        'Cultural Exchange': [70, 60, 80, 75, 50],
        'Economic Growth': [2.5, 6.0, 1.5, 1.0, 7.0]
    }
    df = pd.DataFrame(data)

    # User Selections
    countries = st.multiselect("Select Countries", df['Country'].tolist(), default=['USA', 'China'])
    metric = st.selectbox("Select Metric", ['Trade Volume', 'Foreign Investment', 'Cultural Exchange', 'Economic Growth'])

    # Filter Data
    filtered_df = df[df['Country'].isin(countries)]

    # Create Bar Chart
    fig = px.bar(filtered_df, x='Country', y=metric, title=f'{metric} Comparison')
    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    run_country_comparison()
