# Globalization Impact Visualizer

![QuantUniversity Logo](https://www.quantuniversity.com/assets/img/logo5.jpg)

## Project Description

This Streamlit application, **Globalization Impact Visualizer**, serves as an interactive lab project designed to explore the multifaceted impacts of globalization on various countries. Using a synthetic dataset, the application provides interactive visualizations that allow users to compare key metrics such as Trade Volume, Foreign Investment, Cultural Exchange, and Economic Growth. The goal is to help users understand how globalization influences geopolitical landscapes and economic development through data exploration.

The application also includes explanations of core concepts related to globalization and the metrics used.

## Features

*   **Interactive Data Visualization:** Generate bar charts to visualize key metrics for selected countries.
*   **Comparative Analysis:** Compare multiple metrics across chosen countries side-by-side, including a scatter plot to analyze relationships between indicators.
*   **Global Map View:** Visualize a selected metric (e.g., Trade Volume) on a global choropleth map to see worldwide distribution.
*   **Sidebar Navigation:** Easy navigation between different visualization modules using a sidebar menu.
*   **Key Concepts Explained:** Brief explanations and formulas for core terms like Globalization, Geopolitics, Trade Volume, Foreign Investment, Cultural Exchange, and Economic Growth are provided within the app.
*   **Synthetic Dataset:** Utilizes a sample synthetic dataset for demonstration and exploration purposes.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

*   Python 3.6 or higher
*   `pip` package installer

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url> # Replace <repository_url> with the actual URL
    cd <repository_directory> # Change to the project directory
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows:
    # venv\Scripts\activate
    # On macOS/Linux:
    # source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    Create a `requirements.txt` file in the root directory of the project with the following content:

    ```
    streamlit
    pandas
    plotly
    plotly-express
    ```

    Now, install the packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Ensure your virtual environment is activated** (if you created one).
2.  **Navigate to the root directory** of the cloned project in your terminal.
3.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```
4.  Your web browser should automatically open a new tab with the application running.
5.  Use the sidebar to navigate between the different visualization pages and select countries or metrics as desired.

## Project Structure

The project is organized as follows:

```
.
├── app.py                         # Main Streamlit application entry point
├── requirements.txt               # List of required Python packages
└── application_pages/             # Directory containing code for different application pages/modules
    ├── __init__.py                # Initializes the application_pages directory as a Python package
    ├── data_visualization.py      # Code for the Data Visualization page
    ├── comparative_analysis.py    # Code for the Comparative Analysis page
    └── global_map.py              # Code for the Global Map page
```

*   `app.py`: Sets up the page, displays the title and description, handles sidebar navigation, and routes to the specific page modules.
*   `application_pages/`: Contains the logic and UI components for each distinct page of the application.

## Technology Stack

*   **Framework:** Streamlit
*   **Data Handling:** pandas
*   **Visualization:** Plotly / Plotly Express
*   **Language:** Python

## Contributing

This project is provided primarily for educational and lab purposes by QuantUniversity. Contributions are generally not expected for this specific version.

If you are interested in similar projects or educational labs, please refer to the contact information below.

## License

This project is developed by QuantUniversity and is subject to their terms.

© 2025 QuantUniversity. All Rights Reserved.

Reproduction or distribution of this demonstration requires prior written consent from QuantUniversity. Please refer to the disclaimer within the application footer for specific details regarding its educational use and AI generation.

## Contact

For inquiries related to this project or QuantUniversity's educational offerings, please visit the QuantUniversity website (linked via the logo in the app sidebar) or refer to their official contact channels.
