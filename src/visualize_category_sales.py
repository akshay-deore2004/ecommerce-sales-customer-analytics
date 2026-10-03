import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/ecommerce_data.csv")

# Calculate total sales
df["total_sales"] = df["quantity"] * df["unit_price"]

# Calculate sales by category
category_sales = (
    df.groupby("category")["total_sales"]
    .sum()
    .sort_values(ascending=False)
)

# Create bar chart
plt.figure(figsize=(8, 5))

category_sales.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales (₹)")
plt.xticks(rotation=0)
plt.tight_layout()

# Save visualization
plt.savefig("visualizations/sales_by_category.png")

# Display chart
plt.show()