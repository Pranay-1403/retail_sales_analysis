import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration
st.set_page_config(
    page_title="Retail Sales Analytics Dashboard",
    page_icon="🛍️",
    layout="wide"
)

# 2. Data Loading & Preprocessing
@st.cache_data
def load_data():
    df = pd.read_csv("retail_sales.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    df['YearMonth'] = df['Date'].dt.to_period('M').astype(str)
    
    # Age Group Binning
    bins = [17, 25, 35, 50, 100]
    labels = ['18-25', '26-35', '36-50', '50+']
    df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels)
    return df

df = load_data()

# 3. Sidebar Filters
st.sidebar.header("Filter Options")

# Category filter
selected_category = st.sidebar.multiselect(
    "Select Product Category:",
    options=df["Product Category"].unique(),
    default=df["Product Category"].unique()
)

# Gender filter
selected_gender = st.sidebar.multiselect(
    "Select Gender:",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

# Age group filter
selected_age_group = st.sidebar.multiselect(
    "Select Age Group:",
    options=df["Age Group"].unique(),
    default=df["Age Group"].unique()
)

# Apply filters
filtered_df = df[
    (df["Product Category"].isin(selected_category)) &
    (df["Gender"].isin(selected_gender)) &
    (df["Age Group"].isin(selected_age_group))
]

# 4. Header & Top-level KPI Metrics
st.title("🛍️ Retail Sales & Customer Analytics Dashboard")
st.markdown("Interactive performance overview based on transaction records.")

col1, col2, col3, col4 = st.columns(4)

total_revenue = filtered_df["Total Amount"].sum()
total_orders = filtered_df["Transaction ID"].count()
avg_order_value = filtered_df["Total Amount"].mean() if total_orders > 0 else 0
total_units = filtered_df["Quantity"].sum()

col1.metric("Total Revenue", f"${total_revenue:,.2f}")
col2.metric("Total Orders", f"{total_orders:,}")
col3.metric("Avg Order Value", f"${avg_order_value:,.2f}")
col4.metric("Units Sold", f"{total_units:,}")

st.divider()

# 5. Charts Layout (Row 1)
row1_col1, row1_col2 = st.columns(2)

with row1_col1:
    st.subheader("Revenue by Product Category")
    cat_revenue = filtered_df.groupby("Product Category")["Total Amount"].sum().reset_index()
    fig_cat = px.bar(
        cat_revenue,
        x="Product Category",
        y="Total Amount",
        text_auto="$,.0f",
        color="Product Category",
        template="plotly_white"
    )
    fig_cat.update_layout(showlegend=False, yaxis_title="Revenue ($)")
    st.plotly_chart(fig_cat, use_container_width=True)

with row1_col2:
    st.subheader("Monthly Sales Trend")
    monthly_trend = filtered_df.groupby("YearMonth")["Total Amount"].sum().reset_index()
    fig_trend = px.line(
        monthly_trend,
        x="YearMonth",
        y="Total Amount",
        markers=True,
        template="plotly_white"
    )
    fig_trend.update_layout(xaxis_title="Month", yaxis_title="Revenue ($)")
    st.plotly_chart(fig_trend, use_container_width=True)

# 6. Charts Layout (Row 2)
row2_col1, row2_col2 = st.columns(2)

with row2_col1:
    st.subheader("Revenue by Category & Gender")
    gender_cat = filtered_df.groupby(["Product Category", "Gender"])["Total Amount"].sum().reset_index()
    fig_gender = px.bar(
        gender_cat,
        x="Product Category",
        y="Total Amount",
        color="Gender",
        barmode="group",
        template="plotly_white"
    )
    fig_gender.update_layout(yaxis_title="Revenue ($)")
    st.plotly_chart(fig_gender, use_container_width=True)

with row2_col2:
    st.subheader("Total Revenue by Age Group")
    age_trend = filtered_df.groupby("Age Group", observed=True)["Total Amount"].sum().reset_index()
    fig_age = px.bar(
        age_trend,
        x="Age Group",
        y="Total Amount",
        text_auto="$,.0f",
        color="Age Group",
        template="plotly_white"
    )
    fig_age.update_layout(showlegend=False, yaxis_title="Revenue ($)")
    st.plotly_chart(fig_age, use_container_width=True)

# 7. Raw Data Explorer
with st.expander("🔍 View Raw Filtered Data"):
    st.dataframe(filtered_df, use_container_width=True)

