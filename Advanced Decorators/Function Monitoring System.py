import time 
from functools import wraps

# Logging Decorator
def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"\nThe Function {func.__name__} is called\nargs: {args}\nkwargs: {kwargs}\nResult: {result}\n")
        return result
    return wrapper

#Timer Decorator
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"\nTime take to finish function {end - start : .5f} seconds\n")
        return result
    return wrapper

#Call Counter 
def call_count(func):
    Count = 0
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal Count
        Count += 1
        Result = func(*args, **kwargs)
        print(F"\n The Function {func.__name__} has been called {Count} time(s)\n")
        return Result
    return wrapper 

#Retry Decorator
def retry(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(n):
                try:
                    return func(*args,**kwargs) 
                except Exception:
                    print(f"Retrying.....Attempt {i+1}")
            raise Exception("Function Failed After retires")
        return wrapper
    return decorator


@log
@timer
@call_count
def add(a, b):

    time.sleep(1)
    return a + b


add(5, 7)
add(10, 20)

# Retry Decorator Test
counter = 0

@retry(3)
def unstable():

    global counter
    counter += 1

    if counter < 3:
        raise ValueError("Random failure")

    return "Success"


print(unstable())


                
    