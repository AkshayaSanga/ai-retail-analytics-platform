import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("cleaned_sales.csv")

# ---- Monthly Sales Trend ----
monthly_sales = df.groupby('Month')['Sales'].sum()

plt.figure()
plt.plot(monthly_sales)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# ---- Category-wise Sales ----
category_sales = df.groupby('Category')['Sales'].sum()

plt.figure()
category_sales.plot(kind='bar')
plt.title("Category-wise Sales")
plt.show()

# ---- Region-wise Profit ----
region_profit = df.groupby('Region')['Profit'].sum()

plt.figure()
region_profit.plot(kind='bar')
plt.title("Region-wise Profit")
plt.show()