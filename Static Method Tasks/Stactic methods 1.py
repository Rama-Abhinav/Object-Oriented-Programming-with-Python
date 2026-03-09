class TemperatureConverter:

    @staticmethod
    def celsius_to_fahrenheit(c):
        F = (c*(9/5))+32
        print(F)

    @staticmethod
    def fahrenheit_to_celsius(f):
        C = (f-32)*(5/9)
        print(C)
    
TemperatureConverter.celsius_to_fahrenheit(30)
TemperatureConverter.fahrenheit_to_celsius(86)

