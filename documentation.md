id: 6848578a955009fdec049b6f_documentation
summary: Introduction to Geopolitics Documentation
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# Globalization Impact Visualizer Codelab

## Introduction and Application Setup
Duration: 05:00

Welcome to the Globalization Impact Visualizer Codelab. In this lab, you will learn how to build and understand a Streamlit application designed to explore the multifaceted impacts of globalization across different countries using interactive visualizations.

Understanding globalization is crucial in today's interconnected world. This application provides a tool to visualize and analyze key metrics that reflect the extent and effects of globalization, such as trade volume, foreign investment, cultural exchange, and economic growth. By comparing countries across these dimensions, we can gain insights into geopolitical dynamics and economic development patterns.

**Key Concepts and Formulas Explored:**

*   **Globalization:** This refers to the increasing interconnectedness of the world's economies, cultures, populations, and technologies. While complex to quantify, it's often measured through various indices and indicators. There is no single definitive formula, but it encompasses various flows across borders.
*   **Geopolitics:** The study of how geography and economics influence politics and international relations. Visualizing globalization metrics geographically helps understand geopolitical landscapes.
*   **Trade Volume:** A fundamental measure of economic exchange between countries.
    $Trade\ Volume = Exports + Imports$
*   **Foreign Investment:** Capital flows from one country to another, often indicative of economic integration and trust.
*   **Cultural Exchange:** Represents the flow of ideas, values, and cultural products across borders. Metrics like tourism, student exchanges, and communication flows serve as proxies.
*   **Economic Growth Rate:** Measures the percentage change in a country's Gross Domestic Product (GDP) over a period.
    $\text{Growth Rate} = \frac{GDP_{current} - GDP_{previous}}{GDP_{previous}} \times 100$

**Application Structure:**

The application is built using Streamlit and is structured into a main application file (`app.py`) and separate files for each navigation page within an `application_pages` directory. This modular design helps organize the code for different functionalities.

*   `app.py`: The main entry point, handles layout, introduction text, and navigation.
*   `application_pages/data_visualization.py`: Handles the single-metric visualization page.
*   `application_pages/comparative_analysis.py`: Handles the multi-metric comparison page.
*   `application_pages/global_map.py`: Handles the global map visualization page.

**Setup:**

To run this application, you need Python installed. You also need to install the required libraries: Streamlit, pandas, and plotly.

```console
pip install streamlit pandas plotly
```

Next, create the necessary file structure and files:

```console
mkdir application_pages
touch app.py
touch application_pages/data_visualization.py
touch application_pages/comparative_analysis.py
touch application_pages/global_map.py
```

Now, populate the files with the provided code.

**`app.py` Code:**

Copy and paste the following code into your `app.py` file:

```python
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
```

**`app.py` Explanation:**

*   `st.set_page_config`: Configures the browser tab title and sets the layout to wide.
*   `st.sidebar.image` and `st.sidebar.divider`: Adds branding to the sidebar.
*   `st.title` and `st.divider`: Sets the main title of the application.
*   `st.markdown`: Displays the introductory text, including the importance of the topic and key concepts with formulas. Markdown is used for formatting, including bold text and mathematical expressions.
*   `st.sidebar.selectbox`: Creates the navigation menu in the sidebar, allowing users to switch between different pages/functionalities.
*   `if/elif` block: This is the core of the multi-page routing. Based on the user's selection in the selectbox, it imports and calls the corresponding function from the appropriate file in the `application_pages` directory.
*   Footer: Displays copyright and disclaimer information.

This setup provides the basic structure and navigation for the application.

## Exploring Data Visualization
Duration: 10:00

This step focuses on the "Data Visualization" page, which allows users to view a single chosen metric for selected countries using a bar chart.

Copy and paste the following code into `application_pages/data_visualization.py`:

```python
import streamlit as st
import pandas as pd
import plotly.express as px

def run_data_visualization():
    st.markdown("## Single Metric Visualization")
    st.write("Visualize a specific globalization impact metric for selected countries.")

    # Sample Data
    data = {
        'Country': ['USA', 'China', 'Germany', 'Japan', 'UK', 'India', 'France', 'Brazil', 'Canada', 'Italy'],
        'Trade Volume': [1500, 1800, 1200, 900, 800, 700, 600, 500, 400, 300],
        'Foreign Investment': [800, 700, 600, 500, 400, 300, 200, 100, 50, 25],
        'Cultural Exchange': [70, 60, 80, 50, 75, 40, 65, 30, 55, 20],
        'Economic Growth': [3.0, 6.0, 2.5, 1.0, 1.5, 7.0, 2.0, 1.0, 2.0, 0.5]
    }
    df = pd.DataFrame(data)

    # Sidebar selections (placed in app.py sidebar by default)
    # These controls will appear in the sidebar alongside the navigation
    countries = st.sidebar.multiselect("Select Countries", options=df['Country'].unique(), default=['USA', 'China'])
    metric = st.sidebar.selectbox("Select Metric", options=['Trade Volume', 'Foreign Investment', 'Cultural Exchange', 'Economic Growth'])

    # Filter data
    filtered_df = df[df['Country'].isin(countries)]

    # Create bar chart
    fig = px.bar(filtered_df, x='Country', y=metric, title=f'{metric} by Country')
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    This page allows you to visualize the selected metric for different countries.
    Select countries and a metric from the sidebar to update the bar chart.
    The bar chart displays the values of the chosen metric for the selected countries, enabling easy comparison.
    """)

```

**`application_pages/data_visualization.py` Explanation:**

*   `import streamlit as st`, `import pandas as pd`, `import plotly.express as px`: Imports the necessary libraries.
*   `def run_data_visualization():`: Defines the function called by `app.py` when this page is selected.
*   `st.markdown` and `st.write`: Adds a header and introductory text for the page.
*   `data = {...}` and `df = pd.DataFrame(data)`: Creates a small synthetic dataset using a Python dictionary and converts it into a pandas DataFrame. This DataFrame holds the sample globalization metrics for a few countries.
*   `st.sidebar.multiselect`: Creates a multiselect box in the sidebar, allowing users to choose one or more countries from the DataFrame. The default selection is 'USA' and 'China'.
*   `st.sidebar.selectbox`: Creates a selectbox in the sidebar, allowing users to choose which metric ('Trade Volume', 'Foreign Investment', 'Cultural Exchange', 'Economic Growth') to display.
*   `filtered_df = df[df['Country'].isin(countries)]`: Filters the DataFrame to include only the rows corresponding to the countries selected by the user.
*   `fig = px.bar(...)`: Uses Plotly Express to create a bar chart. The `x` axis is set to 'Country', the `y` axis to the selected `metric`, and the chart title is dynamically set based on the chosen metric.
*   `st.plotly_chart(fig, use_container_width=True)`: Renders the Plotly chart in the Streamlit application, making it interactive. `use_container_width=True` makes the chart expand to the width of its container.
*   Final `st.markdown`: Provides a brief explanation of how to use the page.

This page demonstrates how to use Streamlit widgets (multiselect, selectbox) to control data filtering and dynamically update a visualization (Plotly bar chart) based on user input.

## Performing Comparative Analysis
Duration: 12:00

This step focuses on the "Comparative Analysis" page, which allows users to compare multiple metrics across selected countries.

Copy and paste the following code into `application_pages/comparative_analysis.py`:

```python
import streamlit as st
import pandas as pd
import plotly.express as px

def run_comparative_analysis():
    st.markdown("## Comparative Analysis")
    st.write("Compare multiple globalization impact metrics across selected countries.")

    # Synthetic dataset (same as Data Visualization page for consistency)
    data = {
        'Country': ['USA', 'China', 'Germany', 'Japan', 'UK', 'India', 'France', 'Brazil', 'Canada', 'Italy'],
        'Trade Volume': [1500, 1800, 1200, 900, 800, 700, 600, 500, 400, 300],
        'Foreign Investment': [800, 700, 600, 500, 400, 300, 200, 100, 50, 25],
        'Cultural Exchange': [70, 60, 80, 50, 75, 40, 65, 30, 55, 20],
        'Economic Growth': [3.0, 6.0, 2.5, 1.0, 1.5, 7.0, 2.0, 1.0, 2.0, 0.5]
    }
    df = pd.DataFrame(data)

    # User selection (placed in app.py sidebar by default)
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
    st.markdown("### Relationship Analysis")
    st.write("Exploring potential relationships between different metrics.")
    fig2 = px.scatter(filtered_df, x='Foreign Investment', y='Economic Growth',
                      hover_name='Country',
                      title='Foreign Investment vs Economic Growth')
    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("""
This comparison highlights how these key metrics vary among the selected countries.
Observe the relationships and differences in economic indicators to understand geopolitical and economic dynamics.
    """)
```

**`application_pages/comparative_analysis.py` Explanation:**

*   Imports: Same libraries as the previous page.
*   `def run_comparative_analysis():`: Defines the function for this page.
*   Data: Uses the same synthetic DataFrame.
*   `st.sidebar.multiselect`: Allows selecting countries for comparison. This control will also appear in the sidebar.
*   Filtering: Filters the DataFrame based on the selected countries.
*   Display Headers: Adds specific headers and introductory text for this page's analysis section.
*   **Visualization 1 (Bar Charts):**
    *   It iterates through a list of all metrics (`metrics`).
    *   For each metric, it creates and displays a separate bar chart comparing the selected countries. This provides a side-by-side view of how each country performs on every chosen metric.
*   **Visualization 2 (Scatter Plot):**
    *   Creates a scatter plot using `px.scatter`.
    *   This plot specifically visualizes the relationship between 'Foreign Investment' and 'Economic Growth' for the selected countries.
    *   `hover_name='Country'` ensures that hovering over a point shows the country name.
    *   This type of visualization can help identify potential correlations or lack thereof between different indicators of globalization's impact.
*   Final `st.markdown`: Summarizes the purpose and insights from this analysis page.

This page shows how to generate multiple visualizations on a single page, including different chart types, to provide a more comprehensive analysis of the data. It also highlights how specific relationships between metrics can be explored.

## Visualizing Global Map Data
Duration: 10:00

This step focuses on the "Global Map" page, which visualizes a selected metric on a world map using a choropleth map.

Copy and paste the following code into `application_pages/global_map.py`:

```python
import streamlit as st
import pandas as pd
import plotly.express as px

def run_global_map():
    st.markdown("## Global Map Visualization")
    st.write("Visualize a selected globalization impact metric across the globe.")

    # Sample data with country codes (ISO alpha-3)
    data = {
        'Country': ['USA', 'China', 'Germany', 'Japan', 'UK', 'India', 'France', 'Brazil', 'Canada', 'Italy'],
        'Trade Volume': [1500, 1800, 1200, 900, 800, 700, 600, 500, 400, 300],
        'iso_alpha': ['USA', 'CHN', 'DEU', 'JPN', 'GBR', 'IND', 'FRA', 'BRA', 'CAN', 'ITA'] # ISO 3166-1 alpha-3 codes
    }
    df = pd.DataFrame(data)

    # Metric selection (placed in app.py sidebar by default)
    metric = st.sidebar.selectbox("Select Metric for Global Map", options=['Trade Volume']) # Can add other metrics after populating data

    # Create choropleth map
    fig = px.choropleth(df,
                        locations="iso_alpha", # Column with ISO codes
                        color=metric, # Column determining color intensity
                        hover_name="Country", # Text shown on hover
                        color_continuous_scale=px.colors.sequential.Plasma, # Color scale
                        title=f'Global {metric}') # Map title

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    This page displays a global map visualizing the selected metric.
    The choropleth map illustrates the distribution of the metric across different countries, providing a global perspective.
    """)

```

**`application_pages/global_map.py` Explanation:**

*   Imports: Same libraries as before.
*   `def run_global_map():`: Defines the function for this page.
*   Data: Creates a synthetic DataFrame. **Crucially**, this DataFrame includes an `iso_alpha` column. This column contains the 3-letter ISO 3166-1 alpha-3 country codes, which are required by Plotly Express to map data values to specific countries on a world map.
*   `st.sidebar.selectbox`: Allows selecting the metric to visualize on the map. Currently, only 'Trade Volume' is available in the synthetic data for mapping, but this could be extended.
*   `fig = px.choropleth(...)`: Creates the choropleth map using Plotly Express.
    *   `df`: The DataFrame containing the data.
    *   `locations="iso_alpha"`: Tells Plotly which column contains the country identifiers (the ISO codes).
    *   `color=metric`: Specifies which column's values determine the color intensity of each country on the map. Higher values typically result in a darker or lighter shade depending on the chosen color scale.
    *   `hover_name="Country"`: Sets the column whose value is displayed when the user hovers over a country on the map.
    *   `color_continuous_scale=px.colors.sequential.Plasma`: Defines the color scheme used for the intensity scale. Plotly provides many built-in scales.
    *   `title=f'Global {metric}'`: Sets the title of the map.
*   `st.plotly_chart(fig, use_container_width=True)`: Renders the interactive Plotly map in the Streamlit application.
*   Final `st.markdown`: Explains the purpose of the map visualization.

<aside class="positive">
Using standard country codes like ISO alpha-3 is essential for creating accurate and easily renderable maps with libraries like Plotly or Folium.
</aside>

This page demonstrates how to use Plotly Express to create geographical visualizations, linking data values to countries on a map based on standard country codes.

## Running the Application
Duration: 03:00

Now that you have all the code in place, you can run the Streamlit application.

Open your terminal or command prompt, navigate to the directory where you saved `app.py`, and run the following command:

```console
streamlit run app.py
```

This command will start the Streamlit server, and your web browser should automatically open a new tab displaying the application. If it doesn't, check the terminal output for a local URL (usually `http://localhost:8501`).

Explore the different navigation options in the sidebar:

*   **Data Visualization:** Select different countries and metrics to see how the bar chart updates.
*   **Comparative Analysis:** Select countries and view the side-by-side bar charts for all metrics, plus the scatter plot showing Foreign Investment vs. Economic Growth.
*   **Global Map:** See the distribution of Trade Volume across the countries present in the sample data visualized on a world map.

<aside class="negative">
The application uses synthetic data for demonstration purposes. Real-world globalization data would be significantly larger and more complex, potentially requiring database integration or data loading from external sources.
</aside>

Congratulations! You have successfully set up and run the Globalization Impact Visualizer application. You have learned how to structure a multi-page Streamlit application, load and filter data with pandas, and create various interactive visualizations (bar charts, scatter plots, choropleth maps) using Plotly Express.

The application concludes with the copyright and disclaimer information defined in `app.py`.

```markdown
