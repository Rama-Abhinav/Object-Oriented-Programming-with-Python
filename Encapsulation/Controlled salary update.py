class Employee:
    
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, value):
        if value <= 0:
            print("Salary cannot be zero or negative !!")
        elif value > (self.__salary/2):
            print("Salary increase cannot exceed 50% in one update")
        else:
            print(f"Setting salary to {value}")
            self.__salary = value

    salary = property(get_salary, set_salary)
        
E = Employee("Rama", 10000)

print(E.salary)

E.salary = 2000000
E.salary = -234
E.salary = 2000
print(E.salary)