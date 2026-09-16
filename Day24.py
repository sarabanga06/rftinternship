import pandas as pd
import matplotlib.pyplot as plt

# Weather data
data = {
    "Date": [
        "2026-09-01", "2026-09-01", "2026-09-01",
        "2026-09-02", "2026-09-02", "2026-09-02",
        "2026-09-03", "2026-09-03", "2026-09-03",
        "2026-09-04", "2026-09-04", "2026-09-04",
        "2026-09-05", "2026-09-05", "2026-09-05"
    ],
    "City": [
        "Delhi", "Mumbai", "Chandigarh",
        "Delhi", "Mumbai", "Chandigarh",
        "Delhi", "Mumbai", "Chandigarh",
        "Delhi", "Mumbai", "Chandigarh",
        "Delhi", "Mumbai", "Chandigarh"
    ],
    "Temperature": [
        32, 29, 27,
        34, 28, 25,
        31, 30, 26,
        35, 29, 24,
        33, 31, 28
    ],
    "Weather": [
        "Sunny", "Rainy", "Sunny",
        "Sunny", "Rainy", "Rainy",
        "Rainy", "Sunny", "Sunny",
        "Sunny", "Rainy", "Rainy",
        "Sunny", "Sunny", "Sunny"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Average temperature of each city
avg = df.groupby("City")["Temperature"].mean()

print("\nAverage Temperature:")
print(avg.round(2))

# Hottest and coldest city
print("\nHottest City:", avg.idxmax())
print("Coldest City:", avg.idxmin())

# Rainy and sunny days
print("\nRainy Days:", (df["Weather"] == "Rainy").sum())
print("Sunny Days:", (df["Weather"] == "Sunny").sum())

# Temperature Trend
plt.plot(df["Date"], df["Temperature"], marker="o")
plt.title("Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Weather Distribution
df["Weather"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)
plt.title("Weather Distribution")
plt.ylabel("")
plt.show()

# Average Temperature per City
avg.plot(kind="bar")
plt.title("Average Temperature per City")
plt.ylabel("Temperature (°C)")
plt.tight_layout()
plt.show()

# Moving average prediction
prediction = df["Temperature"].rolling(3).mean().iloc[-1]

print("\nPredicted Tomorrow's Temperature:",
      round(prediction, 2), "°C")

# Export final report
avg.reset_index().to_csv(
    "weather_report.csv",
    index=False
)

print("\nReport saved successfully!")