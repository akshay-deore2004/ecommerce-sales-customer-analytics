import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/ecommerce_data.csv")

# Calculate total sales
df["total_sales"] = df["quantity"] * df["unit_price"]

# Sales by city
city_sales = df.groupby("city")["total_sales"].sum()
city_sales = city_sales.sort_values(ascending=False)

# Create bar chart
plt.figure(figsize=(8, 5))
city_sales.plot(kind="bar")

plt.title("Sales by City")
plt.xlabel("City")
plt.ylabel("Total Sales (₹)")
plt.xticks(rotation=0)
plt.tight_layout()

# Save visualization
plt.savefig("visualizations/sales_by_city.png")

# Display chart
plt.show()