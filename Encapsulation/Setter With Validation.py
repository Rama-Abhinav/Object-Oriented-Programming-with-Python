class Temperature:

    def __init__(self, celsius):
        self.__celsius = celsius

    def get_temp(self):         # Getter Methods
        return self.__celsius
    
    def set_temp(self, value):  # Setter Methods
        if value < -273.15:
            print("Temperature should not be less than -273.17 degree Celsius")
            return
        self.__celsius = value

X = Temperature(20)

print(X.get_temp())

print(X.set_temp(-500))

X.set_temp(-120)
print(X.get_temp())
