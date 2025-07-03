
import streamlit as st

def run_overview():
    st.markdown("""
    ## Overview of Globalization Impact

    This page provides an overview of the Globalization Impact Visualizer.
    The application allows you to explore the effects of globalization on various countries
    by visualizing key metrics such as trade volume, foreign investment, cultural exchange, and economic growth.

    **Understanding the Visualizations:**

    - **Trade Volume:** Represents the total value of goods and services traded between countries. Higher trade volume indicates greater integration into the global economy.

    - **Foreign Investment:** Indicates the level of investment made by foreign entities in a country.
      Increased foreign investment can lead to economic growth and development.

    - **Cultural Exchange:** Measures the extent of cultural interaction between countries.
      Greater cultural exchange can foster understanding and collaboration.

    - **Economic Growth:** Shows the rate at which a country's economy is expanding.
      Globalization can impact economic growth through increased trade, investment, and competition.

    **Formulae:**

    - **Trade Volume:** $Trade Volume = Total Exports + Total Imports$
    - **Economic Growth Rate:** $Economic Growth = ((GDP_{Current Year} - GDP_{Previous Year}) / GDP_{Previous Year}) * 100$

    Use the navigation sidebar to explore different visualizations and analyses.
    """)

if __name__ == "__main__":
    run_overview()
