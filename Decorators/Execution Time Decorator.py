import time

def timer(func):

    def wrapper():

        start = time.time()

        func()

        end = time.time()

        print(f"Execution Time = {end - start:.2f} seconds")

    return wrapper 
    
@timer
def slow_function():
    time.sleep(5)

slow_function()