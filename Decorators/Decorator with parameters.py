# The decorated function should run three times

def repeat(n):

    def decorator(func):

        def wrapper(*args, **kwargs):

            for i in range(n):
                func(*args, **kwargs)

        return wrapper
    return decorator

@repeat(3)
def hello():
    print("Hello")

hello()

    