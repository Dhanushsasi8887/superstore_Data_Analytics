import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Superstore Data Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 SUPERSTORE DATA ANALYTICS DASHBOARD")
st.markdown("### Sales, Profit and Business Performance Analysis")
st.divider()


# ==========================================
# 2. LOAD DATASET
# ==========================================

@st.cache_data
def load_data():

    selected_file = "superstore_clean.csv"

    # Load dataset
    df = pd.read_csv(
        selected_file,
        encoding="latin1"
    )

    # Convert column names
    df.columns = (
        df.columns
        .str.strip()
        .str.replace("_", " ")
        .str.title()
    )

    # Convert date columns
    df["Order Date"] = pd.to_datetime(
        df["Order Date"],
        errors="coerce"
    )

    df["Ship Date"] = pd.to_datetime(
        df["Ship Date"],
        errors="coerce"
    )

    return df, selected_file

    # Normalize column names
    column_mapping = {}

    for col in df.columns:

        key = "".join(
            ch.lower() for ch in col if ch.isalnum()
        )

        aliases = {
            "orderdate": "Order Date",
            "shipdate": "Ship Date",
            "orderid": "Order ID",
            "sales": "Sales",
            "profit": "Profit",
            "quantity": "Quantity",
            "discount": "Discount",
            "region": "Region",
            "category": "Category",
            "subcategory": "Sub-Category",
            "productname": "Product Name",
            "segment": "Segment",
            "city": "City",
            "state": "State",
            "customername": "Customer Name"
        }

        if key in aliases:
            column_mapping[col] = aliases[key]

    df.rename(columns=column_mapping, inplace=True)

    # Check required columns
    required_columns = [
        "Order Date",
        "Sales",
        "Profit",
        "Order ID",
        "Region",
        "Category",
        "Product Name"
    ]

    missing = [
        col for col in required_columns
        if col not in df.columns
    ]

    if missing:
        raise ValueError(
            f"Missing columns: {missing}. "
            f"Available columns: {df.columns.tolist()}"
        )

    # Convert data types
    df["Order Date"] = pd.to_datetime(
        df["Order Date"],
        errors="coerce"
    )

    if "Ship Date" in df.columns:
        df["Ship Date"] = pd.to_datetime(
            df["Ship Date"],
            errors="coerce"
        )

    numeric_columns = [
        "Sales",
        "Profit",
        "Quantity",
        "Discount"
    ]

    for col in numeric_columns:
        if col in df.columns:
            df[col] = pd.to_numeric(
                df[col], errors="coerce"
            )

    return df, selected_file


# ==========================================
# 3. LOAD DATA SAFELY
# ==========================================

try:

    df, selected_file = load_data()

    st.success(
        f"Dataset loaded successfully: {selected_file}"
    )

except Exception as e:

    st.error(f"Error loading dataset: {e}")
    st.stop()


# ==========================================
# 4. SIDEBAR FILTERS
# ==========================================

st.sidebar.title("🔎 Dashboard Filters")

# Region filter
regions = sorted(df["Region"].dropna().unique())

selected_regions = st.sidebar.multiselect(
    "Select Region",
    regions,
    default=regions
)

# Category filter
categories = sorted(df["Category"].dropna().unique())

selected_categories = st.sidebar.multiselect(
    "Select Category",
    categories,
    default=categories
)

# Segment filter
if "Segment" in df.columns:

    segments = sorted(df["Segment"].dropna().unique())

    selected_segments = st.sidebar.multiselect(
        "Select Segment",
        segments,
        default=segments
    )

else:
    selected_segments = []

# Date filter
min_date = df["Order Date"].min()
max_date = df["Order Date"].max()

if pd.notna(min_date) and pd.notna(max_date):

    date_range = st.sidebar.date_input(
        "Select Date Range",
        value=(min_date.date(), max_date.date()),
        min_value=min_date.date(),
        max_value=max_date.date()
    )

else:
    date_range = None


# ==========================================
# 5. APPLY FILTERS
# ==========================================

filtered_df = df.copy()

filtered_df = filtered_df[
    filtered_df["Region"].isin(selected_regions)
]

filtered_df = filtered_df[
    filtered_df["Category"].isin(selected_categories)
]

if "Segment" in filtered_df.columns:
    filtered_df = filtered_df[
        filtered_df["Segment"].isin(selected_segments)
    ]

if date_range and len(date_range) == 2:

    start_date, end_date = date_range

    filtered_df = filtered_df[
        (filtered_df["Order Date"].dt.date >= start_date) &
        (filtered_df["Order Date"].dt.date <= end_date)
    ]


# ==========================================
# 6. KEY PERFORMANCE INDICATORS
# ==========================================

st.subheader("📌 Overall Business Performance")

total_sales = filtered_df["Sales"].sum()

total_profit = filtered_df["Profit"].sum()

total_orders = filtered_df["Order Id"].nunique()

total_quantity = filtered_df["Quantity"].sum() if "Quantity" in filtered_df.columns else 0

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "💰 Total Sales",
    f"${total_sales:,.2f}"
)

col2.metric(
    "📈 Total Profit",
    f"${total_profit:,.2f}"
)

col3.metric(
    "🛒 Total Orders",
    f"{total_orders:,}"
)

col4.metric(
    "📦 Total Quantity",
    f"{total_quantity:,.0f}"
)

st.divider()


# ==========================================
# 7. REGION-WISE SALES
# ==========================================

st.subheader("🌍 Region-wise Sales")

region_sales = (
    filtered_df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

col1, col2 = st.columns(2)

with col1:

    fig, ax = plt.subplots()

    region_sales.plot(
        kind="bar",
        ax=ax
    )

    ax.set_title("Region-wise Sales")
    ax.set_xlabel("Region")
    ax.set_ylabel("Sales")

    plt.xticks(rotation=30)

    st.pyplot(fig)
    plt.close(fig)


# ==========================================
# 8. CATEGORY-WISE SALES
# ==========================================

with col2:

    category_sales = (
        filtered_df.groupby("Category")["Sales"]
        .sum()
    )

    fig, ax = plt.subplots()

    category_sales.plot(
        kind="pie",
        autopct="%1.1f%%",
        ax=ax
    )

    ax.set_title("Category-wise Sales")
    ax.set_ylabel("")

    st.pyplot(fig)
    plt.close(fig)

st.divider()


# ==========================================
# 9. MONTHLY SALES TREND
# ==========================================

st.subheader("📅 Monthly Sales Trend")

monthly_sales = (
    filtered_df.dropna(subset=["Order Date"])
    .set_index("Order Date")
    .resample("ME")["Sales"]
    .sum()
)

fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker="o"
)

ax.set_title("Monthly Sales Trend")
ax.set_xlabel("Month")
ax.set_ylabel("Sales")

ax.grid(True)

plt.xticks(rotation=45)

st.pyplot(fig)
plt.close(fig)

st.divider()


# ==========================================
# 10. TOP 10 PRODUCTS
# ==========================================

st.subheader("🏆 Top 10 Products")

top_products = (
    filtered_df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

fig, ax = plt.subplots(figsize=(12, 6))

top_products.sort_values().plot(
    kind="barh",
    ax=ax
)

ax.set_title("Top 10 Products by Sales")
ax.set_xlabel("Sales")

st.pyplot(fig)
plt.close(fig)

st.dataframe(
    top_products.reset_index(),
    use_container_width=True
)

st.divider()


# ==========================================
# 11. PROFIT ANALYSIS
# ==========================================

st.subheader("💹 Profit Analysis")

profit_category = (
    filtered_df.groupby("Category")["Profit"]
    .sum()
)

fig, ax = plt.subplots()

profit_category.plot(
    kind="bar",
    ax=ax
)

ax.set_title("Category-wise Profit")
ax.set_xlabel("Category")
ax.set_ylabel("Profit")

st.pyplot(fig)
plt.close(fig)

st.divider()


# ==========================================
# 12. DATA TABLE
# ==========================================

st.subheader("📋 Superstore Dataset")

st.write(
    f"Showing {len(filtered_df):,} records"
)

st.dataframe(
    filtered_df,
    use_container_width=True
)


# ==========================================
# 13. DOWNLOAD FILTERED DATA
# ==========================================

csv_data = filtered_df.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="⬇️ Download Filtered Dataset",
    data=csv_data,
    file_name="superstore_filtered.csv",
    mime="text/csv"
)


# ==========================================
# 14. FOOTER
# ==========================================

st.divider()

st.markdown(
    """
    <div style="text-align:center">
        <h4>Superstore Data Analytics Project</h4>
        <p>Developed using Python, Pandas, Matplotlib and Streamlit</p>
        <p>Data Analytics | Data Visualization | Business Intelligence</p>
    </div>
    """,
    unsafe_allow_html=True
)