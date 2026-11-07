import pandas as pd

# Load dataset

df = pd.read_csv("sample-superstore.csv", encoding="cp1252")

print("SUPERSTORE BUSINESS INSIGHTS")
print("============================")

# 1. Region-wise Sales

region_sales = df.groupby("Region")["Sales"].sum()

print("\n1. Region-wise Sales:")
print(region_sales.sort_values(ascending=False))

print("Highest Sales Region:", region_sales.idxmax())

# 2. Category-wise Profit

category_profit = df.groupby("Category")["Profit"].sum()

print("\n2. Category-wise Profit:")
print(category_profit.sort_values(ascending=False))

print("Most Profitable Category:", category_profit.idxmax())

# 3. Top 5 Products

product_sales = df.groupby("Product Name")["Sales"].sum()

print("\n3. Top 5 Products:")
print(product_sales.sort_values(ascending=False).head(5))

# 4. Loss-making Products

product_profit = df.groupby("Product Name")["Profit"].sum()

loss_products = product_profit[product_profit < 0]

print("\n4. Loss-making Products:")
print(loss_products.sort_values().head(10))

# 5. Segment-wise Sales

segment_sales = df.groupby("Segment")["Sales"].sum()

print("\n5. Segment-wise Sales:")
print(segment_sales.sort_values(ascending=False))

# 6. Overall Business Performance

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()

print("\n6. Overall Business Performance:")
print("Total Sales:", round(total_sales, 2))
print("Total Profit:", round(total_profit, 2))

print("\nBusiness Insights Generated Successfully!")

