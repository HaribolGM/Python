# 3. Input & Output (I/O) in Python


# 1. Taking input

# By default , input() takes string.
# name = input("enter your name")
# print("Hello", name)

# if you need number input convert it:
# age = int(input("Enter your age: "))
# print("Next year you will be:", age + 1)


# 2. Printing Output

# Simple print:
# print("Python is fun")

# Multiple values:
# x, y = 10, 20
# print("x =", x, "y =", y)

# f-string formatting(most useful):

# name = "Gaurav"
# marks = 95
# print(f"My name is {name}, I scored {marks}%")


# Controlling separator & end:

# print(1, 2, 3, sep="-")
# print("Hello", end=" ")
# print("World")


# Mini Exercise

# 1. Take your name and age as input, then point:
#     "Hi <name>, you are <age> years old."
# 2. Take two numbers as input and print their sum like this:
#     "The sum of 5 and 10 is 15"


# 1. Answers

# name = input("Enter your name")
# age = input("Enter your age")
# print(f"Hi {name}, you are {age} year old.")

# 2. Answer
# num1 = int(input("Enter First Number"))
# num2 = int(input("Enter Second Number"))
# cal = num1 + num2
# print(f"The sum of the {num1} and {num2} is {cal}")
