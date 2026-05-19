import matplotlib.pyplot as plt
import numpy as np

# Dataset
students = ["Amit", "Riya", "John"]

math_marks = [85, 92, 78]
science_marks = [88, 95, 80]

# Position of bars
x = np.arange(len(students))
width = 0.35

# Create grouped bar chart
plt.figure(figsize=(8, 5))

plt.bar(x - width/2, math_marks, width,
        label="Math", color="skyblue")

plt.bar(x + width/2, science_marks, width,
        label="Science", color="orange")

# Labels and Title
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Performance Dashboard")
plt.xticks(x, students)
plt.ylim(0, 100)

# Show legend
plt.legend()

# Display values on bars
for i in range(len(students)):
    plt.text(x[i] - width/2, math_marks[i] + 1,
             str(math_marks[i]), ha='center')

    plt.text(x[i] + width/2, science_marks[i] + 1,
             str(science_marks[i]), ha='center')

# Show chart
plt.show()