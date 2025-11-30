# Constructor Class
"""
Constructor as Classes we used to build, construct other informations or store data.
"""
class Employee:
    count = 0

    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
        Employee.count += 1

    def display_profile(self):
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: ${self.salary}", end="\n\n")


# self is used to set called values inside itself, thus being called "self".
# This method shows that you need to use the self argument to access instance attributes within a class.

"""
In this class, you define a class attribute called count and initialize it to 0.
You'll use this attribute as a 'counter' to keep track of the number of Employee instances.
Class attributes like '.count' are common to the class and all its instances.
"""