# Operators in Python


# 1. Arithmetic Operators
# a, b = 10, 3
# print(a + b) # 13 (Addition)
# print(a - b) # 7 (Minus)
# print(a * b) # 30 (Multiplication)
# print(a / b) # 3.333 (Division -float)
# print(a // b) # 3 (FLoor Division -int)
# print(a % b) # 1 (Remainder)
# print(a ** b) # 1000 (Power : 10^3)


# 2. Comparison (Relational) Operators
# a, b = 10, 3
# print(a == b) # False
# print(a !=b ) # True
# print(a > b) # True
# print(a < b) # False
# print(a >= b) #True
# print(a <= b) #False


# # 3. Logical Operators
# x, y = True, False
# print(x and y)  # False
# print(x or y)  # True
# print(not x)  # False
# print(not y)  # False


# 4. Assignment Operators
# n = 5
# n += 3  # n = n + 3 => 8
# n *= 2  # n = 8*2 => 16
# print(n)

# 5. Membership Operators

# list1 = [1, 2, 3]
# print(2 in list1)  # True
# print(5 not in list1)  # True


# # 6. Identity Operators
# x = [1, 2, 3]
# y = x
# z = [1, 2, 3]

# print(x is y)  # True (same object in memory)
# print(x is z)  # False (same values, but diff objects)
# print(x == z)  # True (values equal)


# 7. Type casting

# changing one data type into another

# a = "100"
# b = int(a)  # string to int
# c = float(b)  # int to float
# d = str(c)  # float to string

# print(type(a), (a))
# print(type(b), (b))
# print(type(c), (c))
# print(type(d), (d))

# Exercise : Write a code that takes "25" as a string, converts
# it into int, adds 10, and prints result.
# =>

# a = "25"
# b = int(a)
# c = b + 10
# print(c)


# Exercise: Check whether "Python" is in the list ["Java", "Python", "C++"].

# list = ["Java", "Python", "C++"]
# list = "Python" in list
# print(list)
