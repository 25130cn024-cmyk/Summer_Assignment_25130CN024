# Find Duplicates in Array

arr = [10, 20, 10, 30, 20, 40]

for i in arr:
    if arr.count(i) > 1:
        print(i)