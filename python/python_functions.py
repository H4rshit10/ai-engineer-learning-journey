"""
Python Functions Examples
"""

# simple function
def greet():
    print("Hello, welcome to Python")

greet()

# function with parameters
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)

# function with default parameter
def welcome(name="User"):
    print("Welcome", name)

welcome()
welcome("Harshit")

# function with multiple returns
def calculate(a, b):
    sum_val = a + b
    diff_val = a - b
    return sum_val, diff_val

s, d = calculate(10, 5)
print("Sum:", s, "Difference:", d)

# function calling inside loop
for i in range(3):
    greet()
