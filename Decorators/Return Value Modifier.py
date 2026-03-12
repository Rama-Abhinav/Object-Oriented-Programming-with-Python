def double_result(func):
    def wrapper(*args):
        result = func(*args)
        return result*2
    return wrapper

    
@double_result
def get_number(n):
    return n

print(get_number(100))

