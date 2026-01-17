"""
Python Loops Examples
"""

# for loop using range
for i in range(1, 6):
    print("Number:", i)

# for loop with string
for char in "Python":
    print(char)

# while loop
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

# break statement
for i in range(1, 10):
    if i == 5:
        break
    print("Break example:", i)

# continue statement
for i in range(1, 6):
    if i == 3:
        continue
    print("Continue example:", i)

# nested loop
for i in range(1, 4):
    for j in range(1, 3):
        print(f"i={i}, j={j}")
