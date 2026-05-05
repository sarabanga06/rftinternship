MARKS = [78, 85, 90, 67, 85, 92, 78]

avg = sum(MARKS) / len(MARKS)
print("Average : ", avg)

highest = max(MARKS)
lowest = min(MARKS)
print("Highest Marks : ", highest)
print("Lowest Marks : ", lowest)

count = 0
for num in MARKS:
    if num > avg:
        count += 1
print("Marks above average : ", count)

print("GRADE DISTRIBUTION : ")
for m in MARKS:
    if m >= 90:
        print(f"Grade for {m} : 'A'")
    elif m >= 75:
        print(f"Grade for {m} : 'B'")
    elif m >= 60:
        print(f"Grade for {m} : 'C'")
    else:
        print(f"Grade for {m} : 'FAIL'")
