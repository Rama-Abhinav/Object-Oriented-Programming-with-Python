def admin_login(func):
    def wrapper(*args, **kwargs):
        if kwargs.get("role") == "admin":
            return func(*args, **kwargs)
        else:
            print("ACCESS DENIED")
    return wrapper

@admin_login
def delete_user(role):
    print("Deleting User")

delete_user(role="admin")
delete_user(role="new user")
    


    
