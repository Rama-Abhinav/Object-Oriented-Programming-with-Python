from math import pi

class Circle:

    def __init__(self, radius):
        self.radius = radius
        self.__area = round((pi*(self.radius**2)), 2)
    
    def get_area(self):
        return f"A circle of radius {self.radius} has an area {self.__area}"
    
c1 = Circle(10)
print(c1.get_area())
    