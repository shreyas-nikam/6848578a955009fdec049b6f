
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

def run_page2():
    st.header("Comparative Analysis")
    st.markdown("Compare the metrics of different countries to understand the impact of globalization.")

    df = generate_synthetic_data()

    # Sidebar for user inputs
    selected_countries = st.sidebar.multiselect("Select Countries for Comparison", options=df["Country"].unique(), default=["Country 1", "Country 2"])
    metrics_to_compare = st.sidebar.multiselect("Select Metrics to Compare", options=["Trade Volume", "Foreign Investment", "Cultural Exchange", "Economic Growth"], default=["Trade Volume", "Foreign Investment"])

    # Filter data based on user selections
    filtered_df = df[df["Country"].isin(selected_countries)]

    # Create a grouped bar chart for comparison
    st.subheader("Grouped Bar Chart")
    fig_grouped_bar = px.bar(filtered_df, x="Country", y=metrics_to_compare, barmode="group",
                             title="Comparison of Metrics for Selected Countries")
    st.plotly_chart(fig_grouped_bar, use_container_width=True)

    # Display the data as a table
    st.subheader("Data Table")
    st.dataframe(filtered_df)

    st.markdown("The grouped bar chart and data table above allow you to compare the selected metrics for the chosen countries. "
                "Use the sidebar to adjust your selections and explore the data.")

if __name__ == "__main__":
    run_page2()
