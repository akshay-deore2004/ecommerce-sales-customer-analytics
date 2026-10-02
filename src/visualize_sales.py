import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/ecommerce_data.csv")

# Calculate total sales
df["total_sales"] = df["quantity"] * df["unit_price"]

# Sales by product
product_sales = df.groupby("product")["total_sales"].sum()
product_sales = product_sales.sort_values(ascending=False)

# Create bar chart
plt.figure(figsize=(10, 6))
product_sales.plot(kind="bar")

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales (₹)")
plt.xticks(rotation=45)
plt.tight_layout()

# Save visualization
plt.savefig("visualizations/sales_by_product.png")

# Display chart
plt.show()