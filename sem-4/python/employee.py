import math

class Shape:
    def __init__(self):
        self.name = ''
        self.area = 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        self.name = "circle"

    def calarea(self):
        self.area = math.pi * self.radius * self.radius
        print(f"Area is {self.area}")

class Triangle(Shape):
    def __init__(self, height, base):
        self.height = height
        self.base = base
        self.name = "triangle"

    def calarea(self):
        self.area = 0.5 * self.base * self.height
        print(f"Area is {self.area}")

n1 = float(input("Enter radius: "))
c = Circle(n1)
c.calarea()

h = float(input("Enter height: "))
b = float(input("Enter base: "))

t = Triangle(h, b)
t.calarea()

