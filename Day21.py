# 1. Function to check whether a number is prime
def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

# 2. Function using *args to find the largest number
def largest(*args):
    return max(args)

# 3. Function using **kwargs to print student information
def student_info(**kwargs):
    print("\nStudent Information:")
    for key, value in kwargs.items():
        print(key, ":", value)

# 4. Challenge: maximum, minimum, average and sum
def calculate(numbers):
    maximum = max(numbers)
    minimum = min(numbers)
    average = sum(numbers) / len(numbers)
    total = sum(numbers)

    return maximum, minimum, average, total

# ---------------- MAIN PROGRAM ----------------
print("===== PYTHON FUNCTIONS - DAY 21 =====")

# Prime number
num = int(input("\nEnter a number to check whether it is prime: "))

if is_prime(num):
    print(num, "is a Prime Number")
else:
    print(num, "is Not a Prime Number")

# *args
print("\n===== *args Example =====")

numbers = [10, 25, 7, 45, 18, 32]
print("Numbers:", numbers)
print("Largest Number:", largest(*numbers))

# **kwargs
print("\n===== **kwargs Example =====")

student_info(
    name="Sara",
    age=20,
    branch="CSE-AIML",
    college="UIET Kurukshetra"
)

# Challenge
print("\n===== List Calculation =====")

numbers = [10, 20, 30, 40, 50]
maximum, minimum, average, total = calculate(numbers)

print("Numbers:", numbers)
print("Maximum:", maximum)
print("Minimum:", minimum)
print("Average:", average)
print("Sum:", total)