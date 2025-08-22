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


Class Vehicle()

    def __init__(self, brand, year)