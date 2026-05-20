import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample dataset: Student Marks
marks = [45, 50, 55, 60, 62, 65, 67, 70, 72, 75,
         78, 80, 82, 85, 87, 90, 92, 95, 97, 100]

# Create DataFrame
df = pd.DataFrame({"Marks": marks})

# Set plot style
sns.set_style("whitegrid")

# Create histogram with KDE curve
plt.figure(figsize=(8,5))

sns.histplot(df["Marks"],
             bins=8,
             kde=True,
             color="skyblue")

# Title and labels
plt.title("Distribution Analysis of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")

# Show plot
plt.show()

# Identify skewness
skewness = df["Marks"].skew()

print("Skewness of Data:", skewness)

if skewness > 0:
    print("The distribution is Positively Skewed.")
elif skewness < 0:
    print("The distribution is Negatively Skewed.")
else:
    print("The distribution is Symmetric.")