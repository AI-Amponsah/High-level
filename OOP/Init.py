""""The __init__ method also know as the constructor is used to create objects and 
executes when an object is created
"""
class Student:
    def __init__(self):
        self.name = "John"
        self.id = "1024587"
    def print_data(self):
        print(self.name, self.id)
person = Student()
person.print_data()