#set 1 
# >>>>>>>>>>>>>
#problem one(1)
# def sum_squares_abs_diff_squares(a: 1, b: 2) -> tuple:


#     sum_of_squares = a**2 + b**2
#     abs_diff_squares = abs(a**2 - b**2)
#     return(sum_of_squares, abs_diff_squares) 

# # result = sum_squares_abs_diff_squares(5,3)
# # print(result)


#problem 2 (2)

# def is_odd_length_palindrome(s: str) -> bool:

#     return len(s) % 2 == 1 and s == s[::-1]





#problem 3 (3)
# def remove_elements_at_two_indices(l: list, i1: int, i2: int):
#     for idx in sorted([i1, i2], reverse=True):
#         l.pop(idx)



#problem 4 (4)
#Sum of Squares of Even Numbers

# def sum_of_squares_of_even(nums: list) -> int:
#     return sum(x**2 for x in nums if x % 2 == 0)







#section 2 - problem 2 
# Upper case only Vowels

# Write a program that takes a passage with n lines of text as input
# for each line, convert all vowels ( a, e, i, o,u) to uppercase and all other
#     characters to lowercase.

# Read the number of lines
# n = int(input())

# # Define a set of vowels for quick lookup
# vowels = {'a', 'e', 'i', 'o', 'u'}

# # Process each line
# for _ in range(n):
#     line = input()
#     new_line = ''
#     for char in line:
#         if char.lower() in vowels:
#             new_line += char.upper()
#         else:
#             new_line += char.lower()
#     print(new_line)








#section-3 problem 1
# Students Marks Filter

# Given the data of student marks in the format of list of tupples of format 
# (rollno:str, marks:int), write a function to filter student roll numbers based on the following cretieria.

# 1. 'above_average': Students with marks above or equal to the average.
# 2. 'below_average': Students with marks below the average.
# 3. 'fail': Students with marks less than 40.
# 4. 'toppers': Students with marks 90 or above.
# 5. None: Return all roll numbers.
# 6. Any other value should return None.

# def get_roll_nos(data:list, criteria = None):

#     #Extract marks for average calculations
#     marks = [entry[1] for entry in data]
#     avg = sum(marks) / len(marks) if marks else 0
    
#     #Helper Filters based on the criteria 
#     if criteria is None:
#         # Return all roll numbers in order 
#         return [entry[0] for entry in data]
#     elif criteria == 'above_average':
#         return [entry[0] for entry in data if entry[1] >= avg]
#     elif criteria == 'below_average':
#         return [entry[0] for entry in data if entry[1] < avg]
#     elif criteria == 'fail':
#         return [entry[0] for entry in data if entry [1] < 40]
#     elif criteria == "toppers":
#         return [entry[0] for entry in data if entry [1] >= 90]
#     elif criteria == "None":
#         return [entry[0] for entry in data]
    
#     else: 
#         # Any other value should return None

#         return None







#section 3 - problem2 

# Print pattern V

# Given an integer n (where n > 0),print a "V" shaped pattern with n rows. The pattern should use 
# backslashes (\) and forward shalshes (/) for each row, with the v character at the bottom. There should be 
#              no spaces to the right of the pattern.

# n = int(input())
# for i in range(n-1):
#     print(' ' * i + '\\' + ' ' * (2*(n-i-1)-1) + '/')
# print(' ' * (n-1) + 'v')




