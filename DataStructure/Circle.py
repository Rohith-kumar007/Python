import math
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def Calculate_area(self):
        return math.pi*self.radius**2
    def Calculate_perimeter(self):
        return 2*math.pi*self.radius

radius = float(input("Radius of the circle :"))
circle = Circle(radius)
area = circle.Calculate_area()
perimeter = circle.Calculate_perimeter()
print("Area of the Circle : ",area)
print("Perimeter of the Circle : ",perimeter)
