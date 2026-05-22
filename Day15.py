import pandas as pd
import matplotlib.pyplot as plt

# Sample Dataset
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [120, 150, 170, 160, 210, 250],
    "Profit": [20, 25, 30, 28, 40, 50]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create Subplots
plt.figure(figsize=(15, 5))

# LINE CHART 
plt.subplot(1, 3, 1)
plt.plot(df["Month"], df["Sales"], marker='o')
plt.title("Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

# BAR CHART 
plt.subplot(1, 3, 2)
plt.bar(df["Month"], df["Profit"])
plt.title("Profit Comparison")
plt.xlabel("Month")
plt.ylabel("Profit")

# HISTOGRAM
plt.subplot(1, 3, 3)
plt.hist(df["Sales"], bins=5)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")

# Adjust Layout
plt.tight_layout()

# Show Dashboard
plt.show()

# INSIGHTS
print("INSIGHTS:")
print("1. Sales show an overall increasing trend.")
print("2. Profit is highest in June.")
print("3. Most sales values are between 150 and 250.")
print("4. No major outliers are visible in the dataset.")