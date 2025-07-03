
import streamlit as st

st.set_page_config(page_title="Globalization Impact Visualizer", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("Globalization Impact Visualizer")
st.divider()

st.markdown("""
### Introduction to Geopolitics: Globalization Impact Visualizer

This application visualizes the multifaceted impacts of globalization on various countries.
By leveraging a synthetic dataset containing key metrics such as trade volume, foreign investment, cultural exchange, and economic growth,
the application provides interactive visualizations and comparative analyses.

**Key Concepts:**

- **Globalization:** The increasing interconnectedness and interdependence of countries through trade, investment, migration, and cultural exchange.
  For example, the global supply chain for automobiles, where parts are manufactured in various countries and assembled in another.
  Metrics such as the KOF Globalization Index are used to quantify it.

- **Geopolitics:** The study of the influence of geography (human and physical) on politics and international relations.
  It analyzes how a country's geography affects its foreign policy, military strategy, and economic interests.
  For example, Russia's control over natural gas pipelines gives it significant political leverage over European countries dependent on it for energy.

**Metrics:**

- **Trade Volume:** The total value of goods and services traded between countries.
  Formula: $Trade Volume = Total Value of Exports + Total Value of Imports$

- **Foreign Investment:** Investment made to acquire lasting interest in enterprises operating outside of the economy of the investor.
  There are two forms of investment: Foreign Direct Investment (FDI) and portfolio investment.

- **Cultural Exchange:** The reciprocal exchange of ideas, values, beliefs, and traditions between cultures.

- **Economic Growth:** The increase in the value of goods and services produced by an economy over a period.
  Formula: $Economic Growth Rate = ((GDP_{Current Year} - GDP_{Previous Year}) / GDP_{Previous Year}) * 100$

**State Actors:** National governments, political organizations, or country leaders.
**Non-State Actors:** Entities that participate in global affairs but do not directly control national security or country resources.
""")

page = st.sidebar.selectbox(label="Navigation", options=["Overview", "Country Comparison", "Global Map"])

if page == "Overview":
    from application_pages.overview import run_overview
    run_overview()
elif page == "Country Comparison":
    from application_pages.country_comparison import run_country_comparison
    run_country_comparison()
elif page == "Global Map":
    from application_pages.global_map import run_global_map
    run_global_map()

st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity. "
           "This lab was generated using the QuCreate platform. QuCreate relies on AI models for generating code, which may contain inaccuracies or errors")
