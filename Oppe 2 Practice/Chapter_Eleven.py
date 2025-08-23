# 11. Encapsulation (Access Modifiers)

# Encapsulation = Hiding the details inside a class and controlling who can access them.
# In Python, we usually do this with:

# 1. Public -> can be accessed anywhere

# self.name  # normal

# 2. Protected (_) -> meant to be internal, but still accessible if needed

# self._age

# 3. Private(__) -> strictly internal, not directly accessible

# self.__salary


# Example:


# class Employee:
#     def __init__(self, name, salary):
#         self.name = name            # Public
#         self._role = "Engineer"     # Protected
#         self.__salary = salary      # Private

#     # Public method to

#     def get_salary(self):
#         return f"Salary: {self.__salary}"

#     # Public method to update private variable safely

#     def set_salary(self, amount):
#         if amount > 0:
#             self.__salary = amount
#         else:
#             print("Invalid salary!")


# # objects

# emp = Employee("Alice", 50000)

# print(emp.name)     # Public -> Accessible
# print(emp._role)   # Protected  -> Accessible but not recommended

# print(emp.get_salary())

# emp.set_salary(60000)
# print(emp.get_salary())


# This is encapsulation: hiding data(__salary) and controlling access through methods.

# Mini exercise idea:

# Create a BankAccount class with:

# Private variable: __balance
# Methods: deposit(amount) and withdraw(amount)(with checks for negative balance).
# Method: get_balance()


# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance  # private variable

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount

#         else:
#             print("Invalid deposit amount")

#     def withdraw(self, amount):
#         if amount > 0 and amount <= self.__balance:
#             self.__balance -= amount

#         else:
#             print("Insufficient balance")

#     def get_balance(self):
#         return self.__balance   # Returns current balance


# # objects
# acc = BankAccount(4000)
# acc.deposit(200)
# acc.withdraw(210)

# print(acc.get_balance())
