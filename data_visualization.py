import pandas as pd
import matplotlib.pyplot as plt

# Load dataset

df = pd.read_csv("sample-superstore.csv", encoding="cp1252")

# Convert order date

df["Order Date"] = pd.to_datetime(df["Order Date"])

print("SUPERSTORE DATA VISUALIZATION")
print("-----------------------------")

# 1. Monthly Sales Trend

df["Month"] = df["Order Date"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Sales"].sum()

plt.figure(figsize=(12, 5))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.show()

# 2. Category-wise Profit

category_profit = df.groupby("Category")["Profit"].sum()

plt.figure(figsize=(8, 5))
category_profit.plot(kind="bar")
plt.title("Category-wise Profit")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig("category_profit.png")
plt.show()

# 3. Sales vs Profit

plt.figure(figsize=(8, 5))
plt.scatter(df["Sales"], df["Profit"], alpha=0.5)
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig("sales_vs_profit.png")
plt.show()

# 4. Top 10 Products

top_products = df.groupby("Product Name")["Sales"].sum()
top_products = top_products.sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
top_products.plot(kind="barh")
plt.title("Top 10 Products by Sales")
plt.xlabel("Sales")
plt.tight_layout()
plt.savefig("top_10_products.png")
plt.show()

# 5. Region-wise Sales

region_sales = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(8, 5))
region_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Region-wise Sales Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig("region_distribution.png")
plt.show()

print("\nAll Visualizations Created Successfully!")
