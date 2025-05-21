# Solar Data Insights Project

## Overview
This project analyzes solar datasets from Benin, Sierra Leone, and Togo, focusing on data profiling, cleaning, exploratory data analysis (EDA), cross-country comparison, and building an interactive dashboard using Streamlit.

## Tasks Overview

### Task 2: Data Profiling, Cleaning & EDA
**Objective**: Prepare each country’s dataset for comparison and region-ranking.

1. **Data Loading**: Load datasets for Benin, Sierra Leone, and Togo.
2. **Summary Statistics**: Generate summary statistics and identify missing values.
3. **Outlier Detection**: Identify outliers using Z-scores and clean the data by imputing or dropping missing values.
4. **Time Series Analysis**: Create visualizations for GHI, DNI, DHI over time.
5. **Cleaning Impact**: Analyze the effect of cleaning on sensor readings (ModA, ModB).
6. **Correlation Analysis**: Generate heatmaps and scatter plots to explore relationships.
7. **Distribution Analysis**: Create histograms and wind rose plots.
8. **Temperature Analysis**: Investigate the influence of relative humidity on temperature and solar radiation.
9. **Bubble Chart**: Visualize GHI vs. temperature with bubble sizes representing humidity.

### Task 3: Cross-Country Comparison
**Objective**: Synthesize cleaned datasets to identify solar potential differences across countries.

1. **Data Loading**: Load cleaned CSVs for all three countries.
2. **Metric Comparison**: Create boxplots for GHI, DNI, DHI and summarize statistics (mean, median, std).
3. **Statistical Testing**: Conduct a one-way ANOVA on GHI values to assess significance.
4. **Key Observations**: Provide insights and notable findings.
5. **Visual Summary**: Create a bar chart ranking countries by average GHI.

### Bonus Task: Interactive Dashboard
**Objective**: Develop a Streamlit app for dynamic data visualization.

1. **Design Dashboard**: Create an interactive UI for data exploration.
2. **Integrate Data Processing**: Use Python scripts to fetch and process data dynamically.
3. **Interactive Features**: Add sliders and buttons for user customization.
4. **Deployment**: Deploy the dashboard to Streamlit Community Cloud for public access.

## Installation Instructions

To run this project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository