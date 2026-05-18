import pandas as pd
import matplotlib.pyplot as plt

# Dataset
data = {
    "Days": ["MON", "TUE", "WED", "THU", "FRI"],
    "Sales": [200, 250, 300, 280, 350]
}

# Create DataFrame
df = pd.DataFrame(data)

# Find highest and lowest sales
highest = df["Sales"].max()
lowest = df["Sales"].min()

highest_day = df[df["Sales"] == highest]["Days"].values[0]
lowest_day = df[df["Sales"] == lowest]["Days"].values[0]

# Plot line chart
plt.plot(df["Days"], df["Sales"], marker='o', linewidth=2)

# Highlight highest and lowest points
plt.scatter(highest_day, highest, color='green', s=100, label='Highest Sale')
plt.scatter(lowest_day, lowest, color='red', s=100, label='Lowest Sale')

# Add labels and title
plt.title("Weekly Sales Trend")
plt.xlabel("Days")
plt.ylabel("Sales")

# Add sales values on graph
for i in range(len(df)):
    plt.text(df["Days"][i], df["Sales"][i] + 5, str(df["Sales"][i]), ha='center')

# Add legend and grid
plt.legend()
plt.grid(True)

# Display graph
plt.show()