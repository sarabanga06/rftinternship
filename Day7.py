import pandas as pd

# Creating the dataset
data = {
    "NAME": ["AMIT", "RIYA", "JOHN"],
    "MATH": [80, 90, 60],
    "SCIENCE": [70, 88, 65],
    "ENGLISH": [85, 92, 70]
}

# Creating DataFrame
df = pd.DataFrame(data)

# Calculate average marks per student
df["AVERAGE"] = (df["MATH"] + df["SCIENCE"] + df["ENGLISH"]) / 3

# Find topper
topper = df.loc[df["AVERAGE"].idxmax()]

# Count students above overall average
overall_average = df["AVERAGE"].mean()
above_average_count = (df["AVERAGE"] > overall_average).sum()

# Add grade column
def grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 75:
        return "A"
    elif avg >= 60:
        return "B"
    else:
        return "C"

df["GRADE"] = df["AVERAGE"].apply(grade)

# Subject-wise average
subject_average = df[["MATH", "SCIENCE", "ENGLISH"]].mean()

# Display DataFrame
print("Student Performance Dashboard\n")
print(df)

# Display topper
print("\nTopper:")
print(topper["NAME"], "with average marks =", round(topper["AVERAGE"], 2))

# Display students above average
print("\nNumber of students above overall average:", above_average_count)

# Display subject-wise averages
print("\nSubject-wise Average:")
print(subject_average)