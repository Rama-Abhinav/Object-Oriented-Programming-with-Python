def log_argument(func):
    def wrapper(*args):
        function_name = func.__name__
        print(f"Function {function_name} is called\n Arguments are ({args})")
        print("\nFunction Analysed")
    return wrapper

@log_argument
def multiply(a, b):
    return a * b    

multiply(3,4)