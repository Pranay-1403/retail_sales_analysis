# Retail Sales & Customer Analytics Dashboard

An end-to-end data analysis and interactive web application built with Python, Pandas, Plotly, and Streamlit to uncover retail revenue drivers and customer demographics.

---

## 📌 Table of Contents
1. [Project Overview](#project-overview)
2. [Dataset Description](#dataset-description)
3. [Tech Stack](#tech-stack)
4. [Project Workflow](#project-workflow)
5. [Key Insights & Visualizations](#key-insights--visualizations)
6. [Business Recommendations](#business-recommendations)
7. [Interactive Web Dashboard (Streamlit)](#interactive-web-dashboard-streamlit)
8. [Installation & Setup](#installation--setup)

---

## 🔍 Project Overview
Retailers require precise visibility into buying habits, product turnover, and customer segmentation to optimize inventory and marketing budgets. This project analyzes transaction-level data to evaluate:
- Sales trends and seasonality over a full annual cycle.
- Product demand across Clothing, Electronics, and Beauty categories.
- Demographic spending patterns by age cohort and gender.

---

## 📊 Dataset Description
- *Records*: 1,000 retail transactions
- *Features*: Transaction ID, Date, Customer ID, Gender, Age, Product Category, Quantity, Price per Unit, Total Amount
- *Data Quality*: Clean dataset with zero null or missing values across all columns.

---

## 🛠️ Tech Stack
- *Data Analysis & Processing*: Python 3.x, pandas
- *Static Visualizations (Jupyter)*: matplotlib, seaborn
- *Interactive Visualizations*: plotly
- *Web App Framework*: streamlit
- *Environment*: Jupyter Notebook / VS Code

---

## ⚙️ Project Workflow
1. *Data Ingestion & Integrity Checks*:
   - Inspected structural metadata using df.info() and verified absence of null values.
2. *Feature Engineering*:
   - Converted date strings into pandas datetime objects (dt.to_period('M')).
   - Binned customer ages into distinct cohorts (18-25, 26-35, 36-50, 50+).
3. *Exploratory Data Analysis*:
   - Grouped sales volume and revenue by product line.
   - Evaluated monthly time-series performance.
   - Cross-tabulated gender spending across product categories.
4. *Data Visualization*:
   - Built an integrated 4-panel dashboard highlighting all key metrics.

---

## 📈 Key Insights & Visualizations
Insert your dashboard image here (sales_performance_dashboard.png)

- *Revenue Drivers*: Electronics and Clothing represent the top revenue channels, with Beauty trailing closely behind.
- *Seasonality Peaks*: Sharp revenue spikes observed in May, October, and December.
- *Demographic Split*: Customers aged 36–50 represent the highest-volume spending segment, while younger shoppers (18–25) generate the highest ticket size per purchase.

---

## 💡 Business Recommendations
1. *Inventory Management*: Ramp up stock allocation in April and September ahead of historical spikes in May and Q4.
2. *Segmented Marketing*: Run targeted campaigns featuring Beauty and Clothing products to female segments, and emphasize premium Electronics to male segments.
3. *VIP Loyalty Programs*: Introduce loyalty rewards for the 36+ age demographic to maximize lifetime value and sustain the primary revenue base.

---

## 💻 Interactive Web Dashboard (app.py)
​The project features an interactive Streamlit application enabling real-time slicing and metric evaluation:

1. *​Dynamic KPI Cards*: Instant calculations of Total Revenue, Total Orders, Average Order Value (AOV), and Units Sold based on selected filters.
2. *​Multi-attribute Filtering*: Filter simultaneously by Product Category, Gender, and Age Group via the sidebar.
3. *Interactive Visuals*: Plotly-powered charts for category performance, monthly revenue trends, demographic cross-tabs, and cohort distributions.
4. *​Raw Data Inspector*: Embedded expandable table to view and inspect underlying filtered rows.


---


## 🚀 Installation & Setup
1. Clone the repository:

   git clone https://github.com/Pranay-1403/retail_sales_analysis.git

   cd retail-sales-analysis

2. Install dependencies:
    
    pip install pandas matplotlib seaborn plotly streamlit

3. Run the notebook:
    jupyter notebook Sales.ipynb

4. Launch the Streamlit Web Application
    Streamlit run app.py
   