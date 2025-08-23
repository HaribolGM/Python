# 10. Polymorphism & Method Overriding

# This is the natural next step after inheritance.
# It means:

# Same method name, but different behavior depending on the class.

# Example:

# class Animal:

#     def speak(self):
#         return "Some sound"


# class Dog(Animal):
#     def speak(self):
#         return "Woof!"


# class Cat(Animal):
#     def speak(self):
#         return "Meow!"


# animals = [Dog(), Cat(), Animal()]

# for a in animals:
#     print(a.speak())


# Here:

# speak() exists in all classes,
# but Dog overrides it to "Woof!",
# Cat overrides it to "Meow!",
# Animal keeps its default "Some sound".

# This is Polymorphism = Many Forms.

#  It's used a lot in real project (e.g., one function name, different behaviors depending on object type).


# Mini Exercise: (Polymorphism & Overriding)
# 1. Create a base class Bird with a method sound() that returns "some bird sound".
# 2. Create two child classes:
#     Parrot -> sound() returns "Squawk"
#     Crow  -> sound() returns "Caw Caw!"
# 3. Make a list of birds ([Parrot(), Crow(), Bird()]) and loop through them, calling .sound().
#     Each should print its own version of sound.

# Solution:


# class Bird:
#     def sound(self):
#         return "some bird sound"


# class Parrot(Bird):
#     def sound(self):
#         return "Squawk"


# class Crow(Bird):
#     def sound(self):
#         return "Caw Caw!"


# # object
# bird = [Parrot(), Crow(), Bird()]

# for a in bird:
#     print(a.sound())


# 📝 Mini Exercise:

# Create a base class Animal with an attribute name (use __init__).

# Add a method speak() in Animal → returns "Some generic animal sound".

# Create two child classes: Dog and Cat.

# Dog’s speak() → "Woof! My name is <name>"

# Cat’s speak() → "Meow! My name is <name>"

# Create objects of Dog and Cat with names and print their sounds using a loop.


# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return "Some generic animal sound"


# class Dog(Animal):
#     def speak(self):
#         return f"Woof! My name is {self.name}"


# class Cat(Animal):
#     def speak(self):
#         return f"Meow! My name is {self.name}"

# # object


# animal = [Dog("Bruno"), Cat("Kitty"), Animal("")]

# for a in animal:
#     print(a.speak())
