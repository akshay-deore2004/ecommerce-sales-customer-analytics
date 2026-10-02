
# E-Commerce Sales & Customer Analytics

## Project Overview
This project analyzes a sample e-commerce dataset to understand sales performance, customer spending, product revenue, city-wise sales, and payment methods.

## Objectives
- Calculate total revenue and order counts.
- Identify products with the highest sales.
- Compare sales across cities.
- Analyze customer spending.
- Examine revenue by payment method.
- Create charts to communicate findings.

## Tools and Technologies
- Python
- Pandas
- Matplotlib
- Jupyter Notebook
- CSV dataset

## Dataset
The project uses a small, synthetic dataset containing 20 sample orders. It is created for learning and demonstration purposes and does not represent real company transactions.

## Key Results
- Total orders: 20
- Total revenue: ₹188,500
- Unique customers: 10
- Highest-revenue product: Laptop
- Highest-revenue city: Pune

## Visualizations
The project includes charts for:
- Sales by product
- Sales by city
- Sales by payment method

## Project Structure
```text
ecommerce-sales-customer-analytics/
├── data/
│   └── ecommerce_data.csv
├── notebooks/
│   └── ecommerce_analysis.ipynb
├── src/
│   ├── analyze_sales.py
│   ├── visualize_sales.py
│   └── visualize_city_sales.py
├── visualizations/
├── reports/
└── README.md
```

## How to Run
1. Install Python.
2. Install dependencies:
   `python -m pip install pandas matplotlib`
3. Run the analysis from the project root:
   `python src/analyze_sales.py`
4. Run the product chart:
   `python src/visualize_sales.py`
5. Run the city chart:
   `python src/visualize_city_sales.py`

## Learning Outcomes
This project demonstrates basic data cleaning and inspection, exploratory data analysis, aggregation with Pandas, customer and payment analysis, and data visualization.

## Disclaimer
This is an educational portfolio project using synthetic sample data.
