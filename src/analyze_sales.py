print("ANALYSIS PROGRAM STARTED")
import pandas as pd

# Load the e-commerce dataset
df = pd.read_csv("data/ecommerce_data.csv")

# Calculate total sales for each order
df["total_sales"] = df["quantity"] * df["unit_price"]

# Display basic information
print("===== E-COMMERCE SALES ANALYSIS =====")
print("Total orders:", len(df))
print("Total revenue: ₹", df["total_sales"].sum())
print("Unique customers:", df["customer_id"].nunique())

# Sales by product
print("\n===== SALES BY PRODUCT =====")
product_sales = df.groupby("product")["total_sales"].sum()
print(product_sales.sort_values(ascending=False))

# Sales by city
print("\n===== SALES BY CITY =====")
city_sales = df.groupby("city")["total_sales"].sum()
print(city_sales.sort_values(ascending=False))
