class Student:

    def __init__(self, name, marks):

        self.name = name
        self.marks = marks

    def add_marks(self, marks):
        self.marks += marks
        return self.marks
    
    
    def display(self):
        print (f"Name : {self.name}\nMarks : {self.marks}\n\n")
    
s1 = Student("Ram",40)
print(s1.display())
s1.add_marks(10)
print(s1.display())
