class Employee:

    company_name = "Google"
    employee_count = 0

    def __init__(self, name):
        
        self.employee_id = Employee.employee_count + 1 #Assign the current count to the new instance's ID
        self.name = name

        Employee.employee_count += 1 # Increment the class attribute for the next object

        print(f"Employee Record:-\tName : {self.name}\tEmployee ID : {self.employee_id}\n")
    
    @classmethod
    def Company_name(cls, new_name):
        cls.company_name = new_name
        


print(Employee.company_name)

emp1 = Employee("Alice")
emp2 = Employee("Bob")
emp3 = Employee("Charlie")

Employee.Company_name("OpenAI Labs")# Company name is modified before printing not during printing 

print(Employee.company_name)
print(emp1.company_name)
print(emp2.company_name)