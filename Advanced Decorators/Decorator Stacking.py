import time
import functools

def timer(func):
    def wrapper(*args,**kwargs):
        start = time.perf_counter()
        rv = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"\nThe time taken to execute {func.__name__} is {end - start:5f}\n")
        return rv
    return wrapper

def log_args(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"\nThe Function {func.__name__} has been called\nArgs: {args}\nkwargs: {kwargs}\nResult: {result}")
        return result
    return wrapper

@timer
@log_args
def multiply(a,b):
    return a*b

multiply(5,10)