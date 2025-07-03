
import streamlit as st

st.set_page_config(page_title="Globalization Impact Visualizer", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("Globalization Impact Visualizer")
st.divider()

st.markdown(""" 
In this lab, we explore the multifaceted impacts of globalization on various countries. 
Using interactive visualizations based on a synthetic dataset, users can compare metrics such as trade volume, foreign investment, cultural exchange, and economic growth. 
This helps understand how globalization influences geopolitics and economic development.

**Key Concepts and Formulas:**

- **Globalization:** The interconnectedness of countries. No single formula; often measured by indices like the KOF Globalization Index.
- **Geopolitics:** The influence of geography on politics and international relations.
- **Trade Volume:** $Trade\ Volume = Exports + Imports$
- **Foreign Investment:** Investment in foreign enterprises, measured in monetary units.
- **Cultural Exchange:** Proxy metrics include international tourism, student exchanges, etc.
- **Economic Growth Rate:** $\text{Growth Rate} = \frac{GDP_{current} - GDP_{previous}}{GDP_{previous}} \times 100$

""")
# Navigation selection
page = st.sidebar.selectbox(
    label="Navigation",
    options=["Data Visualization", "Comparative Analysis", "Global Map"]
)

# Page routing
if page == "Data Visualization":
    from application_pages.data_visualization import run_data_visualization
    run_data_visualization()
elif page == "Comparative Analysis":
    from application_pages.comparative_analysis import run_comparative_analysis
    run_comparative_analysis()
elif page == "Global Map":
    from application_pages.global_map import run_global_map
    run_global_map()

st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity. "
           "This lab was generated using the QuCreate platform. QuCreate relies on AI models for generating code, which may contain inaccuracies or errors.")
