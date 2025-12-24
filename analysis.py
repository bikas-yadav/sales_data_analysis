# ----------------------------------------
# Sales Data Analysis Using Python
# ----------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the dataset
file_name = "sales_data.csv"
df = pd.read_csv(file_name)

print("===== First 5 Rows of Data =====")
print(df.head())

# 2. Basic information
print("\n===== Dataset Info =====")
print(df.info())

# 3. Data Cleaning
print("\n===== Checking Missing Values =====")
print(df.isnull().sum())

# Convert Date column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Create Total Sales column
df['Total_Sales'] = df['Quantity'] * df['Price']

print("\n===== Data After Cleaning =====")
print(df.head())

# 4. Business Analysis

# Total revenue
total_revenue = df['Total_Sales'].sum()
print("\nTotal Revenue:", total_revenue)

# Revenue by Region
revenue_by_region = df.groupby('Region')['Total_Sales'].sum()
print("\nRevenue by Region:")
print(revenue_by_region)

# Revenue by Product
revenue_by_product = df.groupby('Product')['Total_Sales'].sum()
print("\nRevenue by Product:")
print(revenue_by_product)

# Best-selling product (by quantity)
best_selling_product = df.groupby('Product')['Quantity'].sum().idxmax()
print("\nBest Selling Product (by quantity):", best_selling_product)

# Best performing region
best_region = revenue_by_region.idxmax()
print("Best Performing Region:", best_region)

# 5. Monthly Sales Trend
df['Month'] = df['Date'].dt.month
monthly_sales = df.groupby('Month')['Total_Sales'].sum()

print("\nMonthly Sales:")
print(monthly_sales)

# 6. Visualization

# Revenue by Region
plt.figure()
revenue_by_region.plot(kind='bar')
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Total Revenue")
plt.tight_layout()
plt.show()

# Revenue by Product
plt.figure()
revenue_by_product.plot(kind='bar')
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Total Revenue")
plt.tight_layout()
plt.show()

# Monthly Sales Trend
plt.figure()
monthly_sales.plot(marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Revenue")
plt.tight_layout()
plt.show()

# 7. Save Summary Report
summary = {
    "Total Revenue": total_revenue,
    "Best Selling Product": best_selling_product,
    "Best Performing Region": best_region
}

summary_df = pd.DataFrame(list(summary.items()), columns=["Metric", "Value"])
summary_df.to_csv("sales_summary_report.csv", index=False)

print("\nSummary report saved as sales_summary_report.csv")

print("\n===== Analysis Completed Successfully =====")
