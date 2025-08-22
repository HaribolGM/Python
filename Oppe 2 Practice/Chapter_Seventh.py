# 7. Functions in  Python

# Functions help you organize code, avoid repetition, and solve
# problems modularly.


# 1.Defining & Calling a Function

# def greet():
#     print("Hello, welcome to Python!")


# greet()  # calling the function

# 2. Function with Parameters

# def add(a, b):
#     return a + b


# result = add(4, 10)
# print(result)


# 3. Default Arguments

# def greet(name="guest"):
#     print(f"Hello {name}")


# greet("Gaurav")
# greet()


# 4. Keyword Arguments

# def student(name, age):
#     print(f"Name: {name}, Age: {age}")


# student(age=20, name="Guarav")


# 5. Variable Length Arguments

# args -> multiple positional arguments

# def add_all(*nums):
#     return sum(nums)


# print(add_all(1, 2, 3, 4))

# # ** kwargs -> multiple keyword arguments


# def show_info(**data):
#     for k, v in data.items():
#         print(k, ":", v)


# show_info(name="Guarav", course="Python")


# 6. Scope of Variables

# Local variable -> Defined inside a function, used only there.
# Global variable -> Defined outside function, accessible inside(with global keyboard if modifying).


# x = 10  # global


# def test():
#     x = 5   # local
#     print(x)


# test()
# print(x)


# 7. Recursion

# Function calling itself. Example -> factorial.

# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n-1)


# print(factorial(5))


# Mini Exercises

# 1. Write a function that takes two numbers and returns the maximum.
# 2. Write a function is_palindrome(s) that checks if a string is a palindrome.
#     (Example: "madam" -> True, "hello" -> False)
# 3. Write a recursive function to find the sum of numbers from 1 to n.


# 1. Answers

# def maximum(a, b):
#     if a > b:
#         return a
#     else:
#         return b


# result = maximum(4, 10)
# print(result)


# 2. Answers

# Method one

# def is_palindrome(s):
#     return s == s[::-1]


# print(is_palindrome("madam"))
# print(is_palindrome("hello"))

#  Method two

# def is_palindrome(s):
#     for i in range(len(s)//2):
#         if s[i] != s[-(i+1)]:  # compare front & back chars
#             return False
#     return True


# print(is_palindrome("racecar"))
# print(is_palindrome("python"))


# 3. Answers

# def recursive_sum(n):
#     if n == 0:
#         return 0
#     return n + recursive_sum(n-1)


# print(recursive_sum(5))
# print(recursive_sum(10))
