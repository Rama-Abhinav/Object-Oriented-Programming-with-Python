def log_args(func):
    def wrapper(*args, **kwargs):
        Result = func(*args, **kwargs)
        print(f"Function {func.__name__} called\nargs: {args}\nkwargs: {kwargs}\nResult: {Result}")
    return wrapper

@log_args
def add(a,b):
    return a+b

add(5,10)