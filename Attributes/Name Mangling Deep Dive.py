class Test:

    def __init__(self, value):
        self.__value = value
    
    def show(self):
        return self.__value

o = Test(10)

print(dir(o))
