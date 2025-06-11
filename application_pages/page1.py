
import streamlit as st
import pandas as pd
import plotly.express as px
import random

def generate_synthetic_data(num_countries=10):
    countries = [f"Country {i+1}" for i in range(num_countries)]
    data = {
        "Country": countries,
        "Trade Volume": [random.randint(100, 1000) for _ in range(num_countries)],
        "Foreign Investment": [random.randint(50, 500) for _ in range(num_countries)],
        "Cultural Exchange": [random.randint(20, 200) for _ in range(num_countries)],
        "Economic Growth": [random.uniform(1.0, 5.0) for _ in range(num_countries)],
    }
    df = pd.DataFrame(data)
    return df

def run_page1():
    st.header("Data Visualization")
    st.markdown("Explore the relationship between different metrics of globalization using interactive visualizations.")

    df = generate_synthetic_data()

    # Sidebar for user inputs
    selected_countries = st.sidebar.multiselect("Select Countries", options=df["Country"].unique(), default=df["Country"].unique())
    metric_to_visualize = st.sidebar.selectbox("Select Metric to Visualize", options=["Trade Volume", "Foreign Investment", "Cultural Exchange", "Economic Growth"])

    # Filter data based on user selections
    filtered_df = df[df["Country"].isin(selected_countries)]

    # Create visualizations
    st.subheader("Bar Chart")
    fig_bar = px.bar(filtered_df, x="Country", y=metric_to_visualize, title=f"{metric_to_visualize} by Country")
    st.plotly_chart(fig_bar, use_container_width=True)

    st.subheader("Scatter Plot")
    # Choose a second metric for the scatter plot
    second_metric = st.sidebar.selectbox("Select Second Metric for Scatter Plot", options=["Trade Volume", "Foreign Investment", "Cultural Exchange", "Economic Growth"], index=1)

    fig_scatter = px.scatter(filtered_df, x=metric_to_visualize, y=second_metric, color="Country",
                             title=f"Correlation between {metric_to_visualize} and {second_metric}")
    st.plotly_chart(fig_scatter, use_container_width=True)

    st.subheader("Choropleth Map")
    # Create a simplified dataset for the choropleth map (using only one metric)
    choropleth_data = {
        "Country": filtered_df["Country"],
        "Value": filtered_df[metric_to_visualize]
    }
    choropleth_df = pd.DataFrame(choropleth_data)
    # Add a column for country codes (ISO Alpha-3)
    country_codes = ['USA', 'CHN', 'JPN', 'DEU', 'GBR', 'FRA', 'ITA', 'CAN', 'KOR', 'AUS']  # Example codes, replace with actual codes
    choropleth_df["iso_alpha"] = country_codes[:len(filtered_df)] # ensures the correct number of country codes
    fig_choropleth = px.choropleth(choropleth_df,
                                    locations="iso_alpha",
                                    color="Value",
                                    hover_name="Country",
                                    color_continuous_scale=px.colors.sequential.Plasma,
                                    title=f"{metric_to_visualize} Distribution")
    st.plotly_chart(fig_choropleth, use_container_width=True)

    st.markdown("The visualizations above display the selected metric for different countries. "
                "Use the sidebar to select countries and metrics for comparison.")

if __name__ == "__main__":
    run_page1()
