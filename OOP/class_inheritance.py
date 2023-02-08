"""Class inheritance is a way to extend a class
the new class is known as a child class builds its logic
from the parent class

class Parent:
    def __init__(self) -> None:
        pass
class child(Parent):
    def function_here:
        pass
"""
class Vehicle:
    def insurance(self, year):
        self.year = 0
        return 0
class motor(Vehicle):
    def insurance(self, year):
        return year * 5
class car(Vehicle):
    def insurance(self, year):
        return year * 10
scooter = motor()
print(scooter.insurance(20))
cars = car()
print(cars.insurance(50))