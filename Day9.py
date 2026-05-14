import pandas as pd

# Dataset
data = {
    "Name" : ["A", "B", "C", "D", "E", "F"],
    "Age" : [34, 28, 26, 32, 31, 29],
    "Salary" : [45700, 52500, 53000, 55000, 47800, 50200]
    }

# Create Dataframe
df = pd.DataFrame(data)

print("Original Data :\n", df)

# Filter Conditions
# Age < 30 & Salary > 50000
filtered = df[(df["Salary"] > 50000) & (df["Age"] < 30)]

print("Filtered Data :\n", filtered)

#Bonus
filtered.to_csv("filtered.csv", index = False)

print("\n Filtered data saved to 'filered.csv'") 