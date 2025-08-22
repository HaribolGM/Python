# 5. Loops (for, while)

# Loops are used to repeat actions.

# 1. for loop

# Used to loop over a sequence (List, string,range, etc)

# for i in range(5):
#     print(i)

# fruits = ["apple", "banana", "mango"]
# for f in fruits:
#     print(f)


# 2. while loop
# Repeats while condition is true.


# n = 1
# while n <= 5:
#     print(n)
#     n += 1


# 3. Loop Control Statements

# break exit the loop completely

# for i in range(10):
#     if i == 5:
#         break
#     print(i)


# continue skip current iteration

# for i in range(5):
#     if i == 2:
#         continue
#     print(i)


# # pass do nothing (Placeholder)
# for i in range(3):
#     pass
#     print(i)


# 4. else with loop

# Runs when loop finishes normally (not by break.)

# for i in range(5):
#     print(i)
# else:
#     print("Loop finished")


# Mini Exercise

# 1. Print numbers from 1 to 10 using a while loop.
# 2. Print all even numbers between 1 and 20 using a for loop.
# 3. Write a program that asks for a number and prints its multiplication table (up to 10)

# 1. Answers

# n = 1
# while n <= 10:
#     print(n)
#     n += 1


# 2. Answers

# for i in range(1, 20):
#     if i % 2 == 0:
#         print(i)


# 3. Answer

# num = int(input("Enter a number: "))

# for i in range(1, 11):
#     result = i * num
#     print(result)
