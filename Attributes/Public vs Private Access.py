class Person:

    def __init__(self, name, __age):

        self.name = name
        self.__age = __age

    def display_info(self):
        print(f"Hi, {self.name}\n Age is {self.__age}")

p = Person("Ram", 20)

print(p.name)          # Public Attributes are directly accessible
print(p._Person__age)  # Here the private attributes can be accessed using the mangled name 
print(p.__age)         # Here the private attribute is protected and return an attribute error



