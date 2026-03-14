import time 

def timer(func):
    def wrapper():
        print(f"Function {func.__name__} started")
        start = time.time()
        func()
        end = time.time()
        print(f"Function {func.__name__} finished in {end - start:.2f}")
    return wrapper

@timer
def slow_function():
    time.sleep(2)

slow_function()
