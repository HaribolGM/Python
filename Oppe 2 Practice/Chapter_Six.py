# 6. Comprehensions (List, Dict, Set)

# Comprehensions are shortcuts to create collections in one line.


# 1. List Comprehension

# Normal way
# squares = []
# for i in range(1, 6):
#     squares.append(i**2)
#     print(squares)


# with Comprehension
# squares = [i**2 for i in range(1, 6)]
# print(squares)  # [1, 4, 9, 16, 25]


# With Condition:
# evens = [i for i in range(1, 11) if i % 2 == 0]
# print(evens)  # [2, 4, 6, 8, 10]


# 2.Dictionary Comprehension

# squares as dictionary
# squares = {i: i**2 for i in range(1, 6)}
# print(squares)


# 3. Set Comprehension

# unique_squares = {i**2 for i in range(1, 6)}
# print(unique_squares)


# Mini Exercises

# 1. Create a list of all odd numbers from 1 to 20 using comprehension.
# 2. Create a dictionary of numbers and their cubes from 1 to 5.
#     Example: {1: 1, 2: 8, 3: 27,....}
# 3. Create a set of all vowels present in string "programming".


# 1. Answers

# odd = [i for i in range(1, 21) if i % 2]
# print(odd)


# 2. Answers

# cubes = {i: i**3 for i in range(1, 6)}
# print(cubes)


# 3. Answers

# vowels = {i for i in "programming" if i in "aeiou"}
# print(vowels)
