import pandas as pd
import matplotlib.pyplot as plt

# Sample Dataset
data = {
    'Date': ['2025-05-01', '2025-05-02', '2025-05-03',
             '2025-05-04', '2025-05-05', '2025-05-06',
             '2025-05-07', '2025-05-08', '2025-05-09',
             '2025-05-10'],
    
    'Stock_Price': [100, 102, 101, 105, 107,
                    104, 108, 110, 109, 113]
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Moving Average (3-day)
df['Moving_Average'] = df['Stock_Price'].rolling(window=3).mean()

# Identify Peaks & Drops
df['Change'] = df['Stock_Price'].diff()

print("Stock Data:\n")
print(df)

# Highest and Lowest Price
peak = df['Stock_Price'].max()
drop = df['Stock_Price'].min()

print("\nHighest Price:", peak)
print("Lowest Price:", drop)

# Volatility Detection
volatility = df['Stock_Price'].std()
print("Volatility (Std Dev):", round(volatility, 2))

# Visualization
plt.figure(figsize=(10,5))

# Stock Price Trend
plt.plot(df['Date'], df['Stock_Price'],
         marker='o', label='Stock Price')

# Moving Average Line
plt.plot(df['Date'], df['Moving_Average'],
         linestyle='--', label='Moving Average')

plt.title("Stock Price Time-Series Analysis")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)

plt.show()