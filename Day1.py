data = [10, None, 20, 10, "", 30, None, 40]

list = list(set(data))
print(list)

final = []
removed_count = 0
for item in list:
    if item != None and item != "":
        final.append(item)
    else:
        removed_count += 1

print("Clean List : ", final)
print("No. of values removed: ", removed_count)

final.sort()
print("Final List: ", final)