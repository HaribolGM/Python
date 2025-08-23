# 9. Inheritance (reusing a class in another class)

# Inheritance means :
# You create a base class (parent).
# Then you make a child class that can reuse all features of the parent and also add new ones.


# ----------------
# Parent class
# ----------------

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return f"{self.name} makes a sound."


# # -----------------------------
# # Child class (inherits from Animal
# # -----------------------------


# class Dog(Animal):
#     def speak(self):  # overriding the parent's speak method
#         return f"{self.name} says Woof!"


# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} says Meow!"


# # -----------------------
# # Using Inheritance
# # -----------------------

# dog = Dog("Tommy")
# cat = Cat("Kitty")

# print(dog.speak())  # Tommy says Woof!
# print(cat.speak())  # Kitty says  Meow !


# Key things happening here:

# 1. Dog and Cat inherit from Animal.
# 2. They reuse __init__ from Animal (so no need to rewrite)
# 3. They override speak() with their own version.


# Mini Exercise for you:

# 1. Create a base class Vehicle with attributes brand and year.
# 2. Create 2 child classes: Car and Bike that inherit from Vehicle.
# 3. Each child should have its own method (car_sound() -> "Vroom", bike_sound()-> "Brrr!")


# 1. Answers

# class Vehicle:

#     def __init__(self, brand, year):

#         self.brand = brand
#         self.year = year

#     def get_brand(self):
#         return f"this is the brand name : {self.brand}"

#     def get_year(self):
#         return f"this is the brand year : {self.year}"


# # object

# car1 = Vehicle("Rolls Royce", 2023)
# car2 = Vehicle("BMW", 2023)


# # method

# print(car1.get_brand())
# print(car1.get_year())


# # 2. Answers

# class Vehicle:
#     def __init__(self, name):
#         self.name = name

#         def speak(self):
#             return f"this is the name {self.name}"


# class Car(Vehicle):
#     def speak(self):
#         return f"this is the car name {self.name}"


# class Bike(Vehicle):
#     def speak(self):
#         return f"this is the car name {self.name}"


# # object


# car = Car("BMW")
# bike = Bike("Ola")


# # method

# print(car.speak())
# print(bike.speak())


# 3. Answer
# Each child should have its own method (car_sound() -> "Vroom", bike_sound()-> "Brrr!")

# class Vehicle:

#     def __init__(self, name):
#         self.name = name

#         def speak(self):
#             return f"this is the sound {self.name}"


# class Car(Vehicle):

#     def car_sound(self):
#         return self.name


# class Bike(Vehicle):

#     def bike_sound(self):
#         return self.name


# # objects
# car = Car("Vroom")
# bike = Bike("Brrr")

# # Method

# print(car.car_sound())
# print(bike.bike_sound())


# Correct Version

# class Vehicle:
#     def __init__(self, brand, year):
#         self.brand = brand
#         self.year = year

#     def info(self):
#         return f"{self.brand}, Year: {self.year}"


# # child class: car

# class Car(Vehicle):
#     def car_sound(self):
#         return "Vroom!"


# # Child class: bike


# class Bike(Vehicle):
#     def bike_sound(self):
#         return "Brrr!"


# # Objects (instances)
# car = Car("BMW", 2023)
# bike = Bike("Ola", 2024)


# # Using Methods

# print(car.info())
# print(bike.info())

# print(car.car_sound())
# print(bike.bike_sound())
