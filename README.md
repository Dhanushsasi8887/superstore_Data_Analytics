# Superstore Data Analytics Project

## 1. Project Overview

The Superstore Data Analytics project focuses on analyzing retail sales data to understand business performance, customer purchasing behavior, product sales and profitability.

This project uses Python for data cleaning, data analysis and visualization. An interactive dashboard is developed using Streamlit to present meaningful business insights.

## 2. Problem Statement

Retail businesses generate large amounts of sales data. Understanding this data is important for identifying profitable products, improving sales performance and making better business decisions.

This project analyzes Superstore sales data to identify trends, patterns and business opportunities.

## 3. Project Objectives

- Analyze overall sales and profit performance.
- Identify top-selling products.
- Analyze region-wise sales performance.
- Understand category-wise sales and profit.
- Analyze monthly sales trends.
- Generate useful business insights.
- Build an interactive dashboard.

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming |
| Pandas | Data cleaning and analysis |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Streamlit | Interactive dashboard |
| VS Code | Development environment |

## 5. Dataset Description

Dataset: Superstore Sales Dataset

The dataset contains retail transaction information, including:

- Order ID
- Customer ID
- Order Date
- Ship Date
- Region
- Category
- Sub-Category
- Product Name
- Sales
- Quantity
- Discount
- Profit

## 6. Project Modules

### Module 1: Data Cleaning
- Handle missing values.
- Remove duplicate records.
- Correct data types.
- Prepare clean data for analysis.

### Module 2: Data Analysis
- Calculate total sales.
- Calculate total profit.
- Identify top 10 products.
- Analyze region-wise sales.
- Analyze category-wise performance.

### Module 3: Data Visualization
- Monthly sales trend.
- Category-wise sales chart.
- Region-wise sales chart.
- Sales vs Profit chart.

### Module 4: Business Insights
- Identify profitable products.
- Compare customer segments.
- Analyze regional performance.
- Understand overall business performance.

### Module 5: Interactive Dashboard

Developed using Streamlit.

Dashboard features:
- Total Sales KPI.
- Total Profit KPI.
- Total Orders KPI.
- Total Customers KPI.
- Region filter.
- Category filter.
- Segment filter.
- Year filter.
- Interactive charts.

## 7. Project Folder Structure

```text
superstore_Data_Analytics/
│
├── dashboard.py
├── data_cleaning.py
├── data_analysis.py
├── data_visualization.py
├── business_insights.py
│
├── sample-superstore.csv
├── superstore_clean.csv
│
├── monthly_sales.png
├── category_sales.png
├── region_sales.png
├── sales_vs_profit.png
├── top_10_products.png
│
└── README.md
```

## 8. Installation

Install the required Python libraries:

```bash
py -m pip install pandas numpy matplotlib seaborn streamlit
```

## 9. How to Run the Project

Step 1: Open the project folder in VS Code.

Step 2: Open the terminal.

Step 3: Run the Streamlit dashboard:

```bash
py -m streamlit run dashboard.py
```

Step 4: Open the following address in your browser:

```text
http://localhost:8501
```

## 10. Expected Results

The project provides:

- Interactive sales dashboard.
- Business performance analysis.
- Monthly sales visualization.
- Product performance analysis.
- Regional sales comparison.
- Profitability insights.

## 11. Conclusion

The Superstore Data Analytics project demonstrates how Python can be used to clean, analyze and visualize retail sales data.

The interactive Streamlit dashboard helps users understand business performance and make data-driven decisions.

## 12. Author

**Dhanush M.M.**

B.Tech – Artificial Intelligence and Data Science

Skills: Python, SQL, Pandas, Data Analysis, Data Visualization and Streamlit.