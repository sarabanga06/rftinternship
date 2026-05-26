import pandas as pd
import matplotlib.pyplot as plt

# Dataset
data = {
    "Customer_ID": [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    "Age": [21, 34, 29, 42, 25, 37, 31, 48, 27, 39],
    "Spending": [2500, 9500, 4200, 15000, 3000, 7200, 11000, 1800, 5300, 8700],
    "Visits": [4, 18, 9, 25, 5, 12, 20, 2, 10, 16]
}

# Create DataFrame
df = pd.DataFrame(data)

# Function for customer segmentation
def segment_customer(spending):
    if spending >= 9000:
        return "High"
    elif spending >= 4000:
        return "Medium"
    else:
        return "Low"

# Apply segmentation
df["Segment"] = df["Spending"].apply(segment_customer)

# Display dataset
print("Updated Customer Segmentation Data:\n")
print(df)

# High-value customers
high_value = df[df["Segment"] == "High"]

# Low-engagement users
low_engagement = df[df["Visits"] < 6]

print("\nHigh-Value Customers:\n")
print(high_value)

print("\nLow-Engagement Customers:\n")
print(low_engagement)

# Visualization 1 - Spending Distribution
plt.figure(figsize=(8,5))
plt.hist(df["Spending"], bins=6)
plt.title("Customer Spending Distribution")
plt.xlabel("Spending Amount")
plt.ylabel("Number of Customers")
plt.show()

# Visualization 2 - Customer Segments
segment_counts = df["Segment"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(segment_counts,
        labels=segment_counts.index,
        autopct='%1.1f%%')
plt.title("Customer Segments")
plt.show()

# Business Strategy Suggestions
print("\nBusiness Strategies:")
print("- Give loyalty rewards to high-value customers.")
print("- Send discount offers to low-engagement users.")
print("- Encourage medium customers with personalized deals.")