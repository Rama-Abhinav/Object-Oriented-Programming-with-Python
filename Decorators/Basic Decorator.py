def announce(func):
    def wrapper():
        print("Starting Function...\n")
        func()
        print("\nFunction Finished !!")
    return wrapper

@announce # Decorator Call
def Greet():
    print("Hello, How is the function ?")

Greet()