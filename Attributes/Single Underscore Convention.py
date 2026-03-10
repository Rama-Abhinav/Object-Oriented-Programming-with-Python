class Employee:

    def __init__(self, name, _salary, __ssn):
        self.name = name
        self._salary = _salary # _ is only a naming convention
        self.__ssn = __ssn     # __ activates name mangling

e = Employee("Ram", 120, 12343)

print(e.name)
print(e._salary)
print(e.__ssn)