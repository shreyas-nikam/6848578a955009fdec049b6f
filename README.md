
# Globalization Impact Visualizer

This Streamlit application visualizes the impact of globalization on various countries using a synthetic dataset. 
It allows users to compare key metrics such as trade volume, foreign investment, cultural exchange, and economic growth.

## Getting Started

1.  Clone the repository.
2.  Install Docker.
3.  Build the Docker image: `docker build -t globalization-impact .`
4.  Run the Docker container: `docker run -p 8501:8501 globalization-impact`
5.  Open your browser and go to `http://localhost:8501`.

## Application Pages

-   **Data Visualization:** Visualize individual metrics for selected countries.
-   **Comparative Analysis:** Compare multiple metrics across selected countries.
-   **Global Map:** View a global choropleth map of a selected metric.
