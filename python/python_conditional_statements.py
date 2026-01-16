"""
Python Conditional Statements Examples
"""

# if statement
age = 18
if age >= 18:
    print("You are eligible to vote")

# if-else statement
number = 5
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# if-elif-else statement
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")

# logical operators with conditionals
a = 10
b = 20

if a > 5 and b > 15:
    print("Both conditions are true")

# nested if
x = 15
if x > 10:
    if x < 20:
        print("x is between 10 and 20")
