# Creating and reading CSV file without pandas

# Step 1: Create a sample CSV file
file = open("students.csv", "w")

file.write("NAME,AGE,MARKS\n")
file.write("AMIT,20,85\n")
file.write("RIYA,21,90\n")

file.close()


# Step 2: Read CSV file
file = open("students.csv", "r")

lines = file.readlines()

file.close()


# Step 3: Convert data into list of dictionaries
data = []

headers = lines[0].strip().split(",")

for line in lines[1:]:
    values = line.strip().split(",")

    student = {
        headers[0]: values[0],
        headers[1]: int(values[1]),
        headers[2]: int(values[2])
    }

    data.append(student)


# Step 4: Print final data
print("Student Data:")
print(data)


# Bonus: Calculate average marks
total = 0

for student in data:
    total += student["MARKS"]

average = total / len(data)

print("Average Marks:", average)