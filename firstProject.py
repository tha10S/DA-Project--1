import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate random sales data for 30 days
np.random.seed(42)  # For reproducibility
days = pd.date_range(start='2023-01-01', periods=30, freq='D')
sales = np.random.randint(100, 500, size=30)  # Random sales between 100 and 500

# Create a DataFrame
df = pd.DataFrame({'Date': days, 'Sales': sales})

# Basic analysis
total_sales = df['Sales'].sum()
average_sales = df['Sales'].mean()
max_sales = df['Sales'].max()
min_sales = df['Sales'].min()

print("Sales Analysis for January 2023")
print(f"Total Sales: ${total_sales}")
print(f"Average Daily Sales: ${average_sales:.2f}")
print(f"Maximum Daily Sales: ${max_sales}")
print(f"Minimum Daily Sales: ${min_sales}")

# Visualize the data
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Sales'], marker='o', linestyle='-')
plt.title('Daily Sales for January 2023')
plt.xlabel('Date')
plt.ylabel('Sales ($)')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()