
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Introduction to Geopolitics", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("Introduction to Geopolitics")
st.divider()

st.markdown("""
In this lab, we will explore the impacts of globalization on various countries using interactive visualizations.
We will use a synthetic dataset to analyze key metrics such as trade volume, foreign investment, cultural exchange, and economic growth.
This will help us understand the complex relationship between globalization and economic performance from a geopolitical perspective.

**Key Concepts:**

-   **Globalization:** The increasing interconnectedness and interdependence of countries through trade, investment, migration, and cultural exchange.
    *Example:* The global supply chain for automobiles.

-   **Geopolitics:** The study of the influence of geography (human and physical) on politics and international relations.
    *Example:* Russia's control over natural gas pipelines and its influence on European countries.

-   **Trade Volume:** The total value of goods and services traded between countries.
    *Formula:* Trade Volume = Total Value of Exports + Total Value of Imports

-   **Foreign Investment:** Investment made to acquire lasting interest in enterprises operating outside of the economy of the investor.
    *Types:* Foreign Direct Investment (FDI) and portfolio investment.

-   **Cultural Exchange:** The reciprocal exchange of ideas, values, beliefs, and traditions between cultures.

-   **Economic Growth:** The increase in the value of goods and services produced by an economy over a period.
    *Formula:* Economic Growth Rate = ((GDP in Current Year - GDP in Previous Year) / GDP in Previous Year) \* 100

-   **State Actors:** Typically national governments, political organizations, or country leaders that exert authority over a country's national security and resources.

-   **Non-State Actors:** Those that participate in global political, economic, or financial affairs but do not directly control national security or country resources.
""")

# Your code starts here
page = st.sidebar.selectbox(label="Navigation", options=["Data Visualization", "Comparative Analysis"])

if page == "Data Visualization":
    from application_pages.page1 import run_page1
    run_page1()
elif page == "Comparative Analysis":
    from application_pages.page2 import run_page2
    run_page2()
# Your code ends

st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity.")
