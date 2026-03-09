class Rectangle:

    def __init__(self, length, width):#Avoid Built-in Name Shadowing --> NO len, str, int .....etc.,

        self.length = length
        self.width = width
#Python uses snake_case for naming methods --> Method names should be area(), perimeter() not Area()
    def area(self):
        return f"area : {self.length*self.width}"
    
    def perimeter(self):
        return f"perimeter : {2*(self.length+self.width)}"
    
    def display(self):
        print(f"\n\nRectangle : lengthgth = {self.length} & Breadth = {self.width}")
        print(self.area())
        print(self.perimeter())


r1 = Rectangle(10, 5)
r1.display()
