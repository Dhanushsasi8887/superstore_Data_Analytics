 
import pandas as pd

# 1. Load dataset
df = pd.read_csv("sample-superstore.csv", encoding="cp1252")

# 2. Check dataset
print("Superstore Data Cleaning Started!")
print("Dataset Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# 3. Clean column names
df.columns = (df.columns.str.strip()
              .str.lower()
              .str.replace(" ", "_")
              .str.replace("-", "_"))

# 4. Convert dates
df["order_date"] = pd.to_datetime(df["order_date"])
df["ship_date"] = pd.to_datetime(df["ship_date"])

# 5. Remove duplicates
df = df.drop_duplicates()

# 6. Standardize text
for col in ["region", "category", "sub_category", "segment"]:
    df[col] = df[col].str.strip().str.title()

# 7. Create new columns
df["year"] = df["order_date"].dt.year
df["month"] = df["order_date"].dt.month
df["month_name"] = df["order_date"].dt.month_name()
df["profit_margin"] = (df["profit"] / df["sales"]) * 100
df["delivery_days"] = (df["ship_date"] - df["order_date"]).dt.days

# 8. Save cleaned dataset
df.to_csv("superstore_clean.csv", index=False)

print("\nData Cleaning Completed Successfully!")
print("Cleaned dataset saved.")