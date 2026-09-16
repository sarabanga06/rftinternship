import pandas as pd
import matplotlib.pyplot as plt

# Transaction data
data = {
    "Date": [
        "01-09","01-09","01-09","02-09","02-09",
        "03-09","03-09","04-09","04-09","05-09",
        "05-09","06-09","06-09","07-09","07-09",
        "08-09","08-09","09-09","09-09","10-09"
    ],
    "Account": [
        "A101","A102","A101","A103","A104",
        "A101","A105","A102","A103","A101",
        "A106","A107","A101","A108","A102",
        "A103","A101","A109","A104","A101"
    ],
    "Category": [
        "Shopping","Food","Shopping","Travel","Bills",
        "Food","Shopping","Bills","Travel","Shopping",
        "Food","Entertainment","Shopping","Food","Travel",
        "Bills","Shopping","Entertainment","Food","Shopping"
    ],
    "Amount": [
        2500,800,2500,12000,1500,
        700,15000,2200,11000,13500,
        900,1800,2500,750,13000,
        2100,2500,16000,950,14500
    ]
}

df = pd.DataFrame(data)

# Duplicate transactions
duplicates = df[df.duplicated(
    ["Account", "Category", "Amount"], keep=False
)]

print("\nDuplicate Transactions:")
print(duplicates)

# High-value transactions
high = df[df["Amount"] > 10000]

print("\nHigh-Value Transactions:")
print(high)

# Frequent accounts
count = df["Account"].value_counts()
frequent = count[count >= 3]

print("\nFrequent Accounts:")
print(frequent)

# Risk score
df["Risk_Score"] = 0

df.loc[df["Amount"] > 10000, "Risk_Score"] += 50
df.loc[df.duplicated(
    ["Account", "Category", "Amount"], keep=False
), "Risk_Score"] += 30
df.loc[df["Account"].isin(frequent.index), "Risk_Score"] += 20

print("\nRisk Scores:")
print(df[["Account", "Amount", "Risk_Score"]])

# Transaction Category Chart
df["Category"].value_counts().plot(kind="bar")
plt.title("Transaction Category")
plt.xlabel("Category")
plt.ylabel("Number of Transactions")
plt.show()

# Daily Transaction Trend
df.groupby("Date")["Amount"].sum().plot(marker="o")
plt.title("Daily Transaction Trend")
plt.xlabel("Date")
plt.ylabel("Total Amount")
plt.xticks(rotation=45)
plt.show()

# Top 10 Highest Transactions
df.nlargest(10, "Amount").plot(
    x="Account", y="Amount", kind="bar"
)
plt.title("Top 10 Highest Transactions")
plt.xlabel("Account")
plt.ylabel("Amount")
plt.show()

# Export suspicious transactions
suspicious = df[df["Risk_Score"] >= 50]
suspicious.to_csv(
    "suspicious_transactions.csv",
    index=False
)

print("\nSuspicious transactions exported successfully!")