class Student:

    def __init__(self,name,marks):
        self.name = name
        self.__marks = marks

    def get_marks(self):        # Getter Method
        return self.__marks
    
S = Student("Ram", 80)

print(S.get_marks())
print(S.__marks)
        