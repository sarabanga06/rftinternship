import pandas as pd
import matplotlib.pyplot as plt

# Read CSV
df = pd.read_csv("employee_performance.csv")
print(df.columns)

# Department average
avg = df.groupby("Department")["Performance"].mean()
print("\nDepartment Average:\n", avg.round(2))

# Top 10 performers
top10 = df.nlargest(10, "Performance")
print("\nTop 10 Performers:\n",
      top10[["Employee", "Performance"]])

# Attendance below 75%
low = df[df["Attendance"] < 75]
print("\nAttendance Below 75%:\n",
      low[["Employee", "Attendance"]])

# Performance chart
avg.plot(kind="bar", title="Department Performance")
plt.ylabel("Average Performance")
plt.tight_layout()
plt.show()

# Attendance trend
plt.plot(df["Employee_Name"], df["Attendance"], marker="o")
plt.axhline(75, linestyle="--")
plt.title("Attendance Trend")
plt.xticks(rotation=60)
plt.ylabel("Attendance %")
plt.tight_layout()
plt.show()

# Department distribution
df["Department"].value_counts().plot(
    kind="pie", autopct="%1.1f%%"
)
plt.title("Department Distribution")
plt.ylabel("")
plt.show()

# Export report
pd.concat([top10, low]).to_csv(
    "final_employee_report.csv", index=False
)

print("\nReport saved successfully!")