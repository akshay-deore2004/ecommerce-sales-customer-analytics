import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/ecommerce_data.csv")

# Calculate total sales
df["total_sales"] = df["quantity"] * df["unit_price"]

# Calculate total spending by customer
customer_sales = (
    df.groupby("customer_id")["total_sales"]
    .sum()
    .sort_values(ascending=False)
)

# Create bar chart
plt.figure(figsize=(10, 6))

customer_sales.plot(kind="bar")

plt.title("Customer Spending Analysis")
plt.xlabel("Customer")
plt.ylabel("Total Spending (₹)")
plt.xticks(rotation=0)
plt.tight_layout()

# Save visualization
plt.savefig("visualizations/customer_spending.png")

# Display chart
plt.show()