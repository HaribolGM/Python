# 8. Classes &  Objects - Basics

# 1. Define a class, create objects

# class Student:
#     def __init__(self, name, roll):
#         self.name = name  # instance attribute
#         self.roll = roll

#     def info(self):         # instance method
#         return f"{self.name} ({self.roll})"


# s1 = Student("Gaurav", 101)
# print(s1.info())

# 2. self and __init__
# __init__ runs when objects is created.
# self refers to that object.

# 3. __str__ (nice print)

# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amt):
#         self.balance += amt

#     def withdraw(self, amt):
#         if amt <= self.balance:
#             self.balance -= amt
#         else:
#             print("Insufficient funds")

#     def __str__(self):
#         return f"Account({self.owner}, balance={self.balance})"


# acc = BankAccount("Gaurav", 500)
# acc.deposit(200)
# acc.withdraw(300)
# print(acc)  # Account(Gaurav, balance= 400)


# 4. Instance vs Class Variables

# class Car:
#     wheels = 4

#     def __init__(self, brand):
#         self.brand = brand


# c1 = Car("Tata")
# c2 = Car("Mahindra")
# Car.wheels = 5
# print(c1.wheels, c2.wheels)  # 5 5
# print(c1.brand, c2.brand)  # Tata Mahindra


# Mini Exercises (do these)

# # 1.Rectangle

#     Create Rectangle(w, h) with:
#     methods: area(), perimeter()
#     __str__ to show: Rectangle(3x4) area=12 perimeter=14

# # 2.Student

#     Create Student(name, marks_list) with:
#     methods: average() returning average marks
#     __str__ giving: Student(name=..., avg=...)


# # 3.Counter

#     Create Counter(start=0) with:
#     methods: inc(), dec(), value()
#     Try multiple objects and confirm they keep their own counts.


# 1. Rectangle

# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h

#     def area(self):
#         return self.w * self.h

#     def perimeter(self):
#         return 2 * (self.w + self.h)

#     def __str__(self):
#         return f"Rectangle({self.w}x{self.h}) area={self.area()} perimeter={self.perimeter()}"

# # Test


# r = Rectangle(3, 4)
# print(r)


# 2.Student

# class Student:
#     def __init__(self, name, marks_list):
#         self.name = name
#         self.marks_list = marks_list

#     def average(self):
#         return sum(self.marks_list) / len(self.marks_list)

#     def __str__(self):
#         return f"Student(name={self.name}, avg={self.average():.2f})"

# # Test


# s = Student("Gaurav", [80, 90, 75, 85])
# print(s)  # Student(name= Gaurav, avg= 82.50)


# 3. Counter

# class Counter:
#     def __init__(self, start=3):
#         self.count = start

#     def inc(self):
#         self.count += 1

#     def dec(self):
#         self.count -= 1

#     def value(self):
#         return self.count

# # Test


# c1 = Counter(2)
# c2 = Counter(10)

# c1.inc()
# c1.inc()
# c2.dec()


# print(c1.value())
# print(c2.value())


# Key things to notice:

# Each object (like r, s c1, c2) has its own data (self stores it).
# __str__ makes printing pretty.
# Methods just use objects data (self).


# 1) class

# A class is like a blueprint/template.
# It tells Python what an object of this type will look like
# (What data is has + what actions it can do)


# -------------------------
# Class
# -------------------------

class Dog:
    # __init__ is special METHOD
    # It runs automatically when we create a new Dog object.

    def __init__(self, name, age):

        # "self" means "this object itself"
        # self.name and self.age are VARIABLES  that belong to the object
        self.name = name
        self.age = age

        # Method = a function inside a class
        # This method makes the Dog bark

        def bark(self):
            return f"{self.name} says Woof!"

        # Another method: tells dog's age in human years

        def human_age(self):
            return self.age * 7

# -----------------------------
# Object
# -----------------------------
# An object is an actual "thing" create from the class (blueprint).
# Here we create 2 dogs (2 different objects).


dog1 = Dog("Tommy", 3)  # This makes a Dog object with name="Tommy" , age = 3
dog2 = Dog("Sheru", 5)  # Another Dog object with different data


# -----------------------------
# Using Method
# -----------------------------

print(dog1.bark())  # Calls the bark() METHOD -> "Tommy says WOOF!"
print(dog2.bark())

print(dog1.human_age())
print(dog2.human_age())
