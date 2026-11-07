import pandas as pd
import matplotlib.pyplot as plt

# 1. Load dataset
df = pd.read_csv("sample-superstore.csv", encoding="cp1252")

print("SUPERSTORE DATA ANALYSIS")
print("------------------------")

# 2. Basic information
print("\nDataset Shape:", df.shape)

print("\nDataset Information:")
print(df.info())

# 3. Sales Analysis
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()

print("\nTotal Sales:", round(total_sales, 2))
print("Total Profit:", round(total_profit, 2))
print("Total Orders:", total_orders)

# 4. Category Analysis
print("\nCategory-wise Sales:")
category_sales = df.groupby("Category")["Sales"].sum()
print(category_sales)

# 5. Region Analysis
print("\nRegion-wise Sales:")
region_sales = df.groupby("Region")["Sales"].sum()
print(region_sales)

# 6. Top 5 Products
print("\nTop 5 Products:")
top_products = df.groupby("Product Name")["Sales"].sum()
print(top_products.sort_values(ascending=False).head(5))

# 7. Category Sales Chart
category_sales.plot(kind="bar", title="Category-wise Sales")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("category_sales.png")
plt.show()

# 8. Region Sales Chart
region_sales.plot(kind="bar", title="Region-wise Sales")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("region_sales.png")
plt.show()

print("\nData Analysis Completed Successfully!")