import matplotlib.pyplot as plt

# Dataset
categories = ["Food", "Travel", "Shopping"]
expenses = [500, 300, 200]

# Highlight highest category
explode = [0.1, 0, 0]

# Create Pie Chart
plt.figure(figsize=(7,7))

plt.pie(
    expenses,
    labels=categories,
    autopct='%1.1f%%',
    explode=explode,
    shadow=True,
    startangle=90
)

# Title
plt.title("Category Breakdown of Expenses")

# Show chart
plt.show()