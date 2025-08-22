# course = "python programming"
# print(len(course))
# print(course[0])
# print(course[-1])
# print(course[0:3])
# print(course[0:])
# print(course[:3])
# print(course[:])


# \ ""

# course = "python \nprogramming"
# print(course)


# first = "Mosh"
# last = "hamedani"
# full = f"{len(first)} {2+2}"
# print(full)


# course = "  Python Programming"
# print(course.upper())
# print(course)
# print(course.lower())
# print(course.title())
# print(course.strip())
# print(course.rstrip())
# print(course.find("Pro"))
# print(course.replace("P", "j"))
# print("Pro" in course)
# print("swift" not in course)


# print(10+3)
# print(10-3)
# print(10*3)
# print(10/3)
# print(10//3)
# print(10 % 3)
# print(10 ** 3)


# x = 10
# x = x + 3
# x += 3

# import math

# # print(round(2.9))
# # print(abs(-2.9))

# print(math.ceil(25.1))


# x = input("x: ")

# y = int(x) + 1
# print(f"x: {x}, y: {y}")

# int(x)
# float(x)
# bool(x)
# str(x)


# Falsy
# ""
# 0
# None


# fruit = "Apple"
# print(fruit[1:-1])

# x = 10 % 3
# print(x)

# print(bool("False"))


# Comparison operators
# ==


# print(ord("A"))

# temperature = 15
# if temperature > 30:
#     print("It's warm")
#     print("Drink Water")
# elif temperature > 35:
#     print("It's a nice day")
# else:
#     print("It's cold")
# print("Done")


# age = 12
# message = "Eligible" if age >= 18 else "Not Eligible" #ternary operator
# print(message)


# and
# or
# not


# high_income = False
# good_credit = True
# student = True


# if high_income or good_credit or not student:
#     print("Eligible")


# age should be between 18 and 65
# age = 12
# if 18 <= age < 65:
#     print("Eligible")
# else:
#     print("Not Eligible")


#  Quiz
# if 10 == "10":
#     print("a")
# elif "bag" > "apple" and "bag" > "cat":
#     print("b")
# else:
#     print("c")


# For Loops

# for number in range(1, 10, 2):
#     print("Attempt", number, number * ".")

# successful = True
# for number in range(3):
#     print("Attempt")
#     if successful:
#         print("Successful")
#         break
# else:
#     print("Attempted 3 times and failed")


# Nested Loops

# for x in range(5):
#     for y in range(3):
#         print(f"({x}, {y})")


# Iterables

# print(type(5))
# print(type(range(5)))

# for item in shopping_cart:
#     print(item)


# number = 100
# while number > 0:
#     print(number)
#     number //= 2

# command = ""
# while command.lower() != "quit":
#     command = input(">")
#     print("ECHO", command)


# infinite loops

# while True:
#     command = input(">")
#     print("ECHO", command)
#     if command.lower() == "quit":
#         break


# Exercise

# display even numbers from 1 to 10

# count = 0
# for number in range(1, 10):
#     if number % 2 == 0:
#         count += 1
#         print(number)
# print(f"we have {count} even numbers")


# Functions

# def greet():
#     print("Hi There")
#     print("welcome aboard")


# greet()


# Arguments

# def greet(first_name, last_name):
#     print(f"Hi {first_name} {last_name} ")
#     print("Welcome aboard")


# greet("Most", "Hamedani")
# greet("Gaurav", "Mali" )


# Types of Functions

# def greet(name):
#     print(f"Hi {name}")


# def get_greeting(name):
#     return f"Hi {name}"


# message = get_greeting("Mosh")
# file = open("content.txt," "w")
# file.write(message)

# def greet(name):
#     print(f"Hi {name}")
#     # return "..."


# print(greet("Mosh"))


# Keyword Arguments

# def increment(number, by):
#     return number + by


# print(increment(2, by=2))


# Default Arguments

# def increment(number, by=4):
#     return number + by


# print(increment(2, 5))


# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total


# print(multiply(2, 3, 4, 5))
