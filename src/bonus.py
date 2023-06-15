"""Bonus Exercise:
Create a base class called Shape with the following attributes and methods:
Attributes:
name (string)
Methods:
__init__(self, name): Initializes the name attribute.
area(self): Computes and returns the area of the shape (0 by default).
Create two subclasses, Rectangle and Circle, which inherit from the Shape class.
 Each subclass should override the area method to compute the area specific to the shape.
Additionally, create a function called total_area that takes a list of shapes and calculates
 the total area of all the shapes in the list.
Finally, create instances of the Rectangle and Circle classes, add them to a list, 
and use the total_area function to calculate and print the total area of all the shapes.
Show less"""

import math

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

def total_area(shapes):
    total = 0
    for shape in shapes:
        total += shape.area()
    return total

# Create instances of Rectangle and Circle
rectangle = Rectangle("Rectangle", 5, 3)
circle = Circle("Circle", 4)

# Add shapes to a list
shapes_list = [rectangle, circle]

# Calculate and print the total area of all shapes
total = total_area(shapes_list)
print("Total area:", total)
