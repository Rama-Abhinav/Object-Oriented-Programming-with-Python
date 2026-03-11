#Always use snake_case for attributes and methods.

class Battery:

    def __init__(self, capacity):
        self.capacity = capacity
        self.__charge = 0           #Always initialize internal state safely.

    @property
    def charge(self):
        return f"The Current Charge of the battery is {self.__charge}"
    
    @charge.setter
    def charge(self, value):
        if value < 0 :
            print("Charge cannot be negative!!")
        elif value > self.capacity:
            self.__charge = self.capacity
            print("Maximum Capacity Reached , Cannot charge more than this !!!")
        else:
            self.__charge = value

    @property
    def battery_percentage(self):
        return f" Battery Percentage = {round(((int(self.__charge)/int(self.capacity))*100), 3)}%"

B = Battery(140)

print(B.charge)

B.charge = 2000
B.charge = -10

B.charge = 120
print(B.charge)
print(B.battery_percentage)
