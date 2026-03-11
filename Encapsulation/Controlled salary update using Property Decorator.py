class Employee:
    
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    @property
    def salary(self):
        if hasattr(self, "_Employee__salary"):      # Safe Getter method
            return self.__salary
        else:
            return "Salary not set"

    @salary.setter
    def salary(self, value):
        if value <= 0:
            print("Salary cannot be zero or negative !!")
        elif value > (self.__salary/2):
            print("Salary increase cannot exceed 50% in one update")
        else:
            print(f"Setting salary to {value}")
            self.__salary = value

    @salary.deleter
    def salary(self):
        print("Deleting the Salary of employee")
        del self.__salary


    
        
E = Employee("Rama", 10000)

print(E.salary)

E.salary = 2000000
E.salary = -234
E.salary = 2000
print(E.salary)
del E.salary
print(E.salary)