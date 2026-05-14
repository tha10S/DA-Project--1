import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("=" * 50)
print("      SALES DATA ANALYSIS PROGRAM")
print("=" * 50)

# Ask user for inputs
try:
    num_days = int(input("Enter number of days to generate sales data for: "))
    min_sales_range = int(input("Enter minimum possible sales amount: R"))
    max_sales_range = int(input("Enter maximum possible sales amount: R"))

    # Validate inputs
    if min_sales_range >= max_sales_range:
        print("Error: Minimum sales must be less than maximum sales.")
        exit()

except ValueError:
    print("Invalid input! Please enter numbers only.")
    exit()

# Optional random seed for reproducibility
use_seed = input("Would you like to use a fixed random seed? (yes/no): ").lower()

if use_seed == "yes":
    try:
        seed_value = int(input("Enter seed value: "))
        np.random.seed(seed_value)
    except ValueError:
        print("Invalid seed. Using default random generation.")
else:
    np.random.seed(None)

# Generate dates and sales data
start_date = input("Enter start date (YYYY-MM-DD): ")

try:
    days = pd.date_range(start=start_date, periods=num_days, freq='D')
except:
    print("Invalid date format. Using default date 2023-01-01.")
    days = pd.date_range(start='2023-01-01', periods=num_days, freq='D')

sales = np.random.randint(min_sales_range, max_sales_range + 1, size=num_days)

# Create DataFrame
df = pd.DataFrame({
    'Date': days,
    'Sales': sales
})

# Perform analysis
total_sales = df['Sales'].sum()
average_sales = df['Sales'].mean()
max_sales = df['Sales'].max()
min_sales = df['Sales'].min()

# Find best and worst sales days
best_day = df.loc[df['Sales'].idxmax()]
worst_day = df.loc[df['Sales'].idxmin()]

# Display analysis
print("\n" + "=" * 50)
print("             SALES ANALYSIS REPORT")
print("=" * 50)

print(f"\nTotal Sales: R{total_sales}")
print(f"Average Daily Sales: R{average_sales:.2f}")
print(f"Highest Daily Sales: R{max_sales}")
print(f"Lowest Daily Sales: R{min_sales}")

print("\nBest Sales Day:")
print(f"Date: {best_day['Date'].date()}")
print(f"Sales: R{best_day['Sales']}")

print("\nWorst Sales Day:")
print(f"Date: {worst_day['Date'].date()}")
print(f"Sales: R{worst_day['Sales']}")

# Ask if user wants to see raw data
view_data = input("\nWould you like to view the full sales table? (yes/no): ").lower()

if view_data == "yes":
    print("\nSales Data Table:")
    print(df)

# Plot graph
print("\nGenerating sales graph...")

plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Sales'], marker='o', linestyle='-', linewidth=2)

plt.title('Daily Sales Report', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Sales (R)', fontsize=12)

plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)

# Add average sales line
plt.axhline(
    average_sales,
    color='red',
    linestyle='--',
    label=f'Average Sales (R{average_sales:.2f})'
)

plt.legend()
plt.tight_layout()

plt.show()

print("\nThank you for using the Sales Data Analysis Program!")