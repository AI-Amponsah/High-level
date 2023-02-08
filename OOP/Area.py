"""Defining a class

"""
class Rectangle:
    """Class rectangle"""
    def area(self):
        """Method to find the area of a rectangle"""
        return self.width * self.height
    def print_area(self):
        """Method to print the area of a rectangle"""
        results = self.area()
        print(results)
rectangle = Rectangle()
rectangle.height = 5
rectangle.width = 4
rectangle.print_area()