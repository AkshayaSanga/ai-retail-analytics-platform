import pandas as pd

# Load dataset
df = pd.read_csv("sales.csv")

# Remove missing values
df = df.dropna()

# Convert Date column (change column name if needed)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Remove invalid dates
df = df.dropna(subset=['Date'])

# Create new columns
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year

# Save cleaned data
df.to_csv("cleaned_sales.csv", index=False)

print("✅ Data Cleaning Completed")