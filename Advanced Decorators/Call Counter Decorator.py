Count = 0
def count_calls(func):
    def wrapper():
        global Count
        Count += 1
        print(f"Call {Count} of {func.__name__}")
        func()
        print()
    return wrapper

@count_calls
def greet():
    print("Hello")

for i in range(10):
    greet()


