import pandas as pd
import matplotlib.pyplot as plt
sales_data = {"Date": ["2025-01-05", "2025-01-20",
                       "2025-02-10", "2025-03-15",
                       "2025-04-05", "2025-05-18",
                       "2025-06-10", "2025-07-25",
                       "2025-08-12", "2025-09-20",
                       "2025-10-15", "2025-11-30"],
            "Category": ["Electronics", "Clothing",
                         "Electronics", "Food",
                         "Clothing", "Food",
                         "Electronics", "Food",
                         "Clothing", "Electronics",
                         "Food", "Clothing"],
            "Sales": [45000, 25000,
                      52000, 30000,
                      35000, 28000,
                      60000, 32000,
                      42000, 65000,
                      38000, 48000]}
df = pd.DataFrame(sales_data)
df["Date"] = pd.to_datetime(df["Date"])
print("Sales Dataset")
print(df)

monthly_sales = df.groupby(df["Date"].dt.to_period("M"))["Sales"].sum()
print("\nMonthly Sales")
print(monthly_sales)
quarterly_sales = df.groupby(df["Date"].dt.to_period("Q"))["Sales"].sum()
print("\nQuarterly Sales")
print(quarterly_sales)

plt.figure(figsize=(10,5))
plt.plot(monthly_sales.index.astype(str),monthly_sales.values,marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales Revenue")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("monthly_sales_trend.png",dpi=300)
plt.show()

plt.figure(figsize=(8,5))
plt.plot(quarterly_sales.index.astype(str),quarterly_sales.values,marker="o")
plt.title("Quarterly Sales Trend")
plt.xlabel("Quarter")
plt.ylabel("Sales Revenue")
plt.grid(True)
plt.tight_layout()
plt.savefig("quarterly_sales_trend.png",dpi=300)
plt.show()

category_sales = df.groupby("Category")["Sales"].sum()
print("\nCategory Wise Sales")
print(category_sales)

plt.figure(figsize=(8,5))
plt.bar(category_sales.index,category_sales.values)
plt.title("Category Wise Sales Comparison")
plt.xlabel("Product Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("category_sales_bar_chart.png",dpi=300)
plt.show()

plt.figure(figsize=(7,7))
plt.pie(category_sales.values,labels=category_sales.index,autopct="%1.1f%%",startangle=90)
plt.title("Sales Contribution by Category")
plt.tight_layout()
plt.savefig("category_sales_pie_chart.png",dpi=300)
plt.show()

best_category = category_sales.idxmax()
highest_sales = category_sales.max()
summary = f"""
SALES ANALYTICS REPORT
------------------------
Total Sales:{df['Sales'].sum()}

Monthly Sales Analysis:
{monthly_sales}

Quarterly Sales Analysis:
{quarterly_sales}

Category Performance:
{category_sales}

Best Performing Category:
{best_category}

Highest Category Sales:
{highest_sales}

Visualization Approach:
------------------------
1. Line Chart:
->Used to identify sales trends over time.
->Suitable for time-series analysis.

2. Bar Chart:
->Used to compare sales performance among categories.
->Helps identify top-performing categories.

3. Pie Chart:
->Used to visualize percentage contribution of each category to total sales.

Formatting Techniques:
-----------------------
- Meaningful chart titles were added.
- X-axis and Y-axis labels were provided.
- Grid lines improve readability.
- Data points were highlighted in line charts.
- Percentage labels were added in pie charts.
"""
with open("sales_analysis_summary.txt","w") as file:
    file.write(summary)
print("\nAnalysis completed successfully!")
print("Charts and summary report generated.")