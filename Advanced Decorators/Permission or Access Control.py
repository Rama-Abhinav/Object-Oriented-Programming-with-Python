def admin_only(func):
    def wrapper(*args, **kwargs):
        if kwargs.get("user") == "Admin":
            print("\nAccess Granted, Welcome Admin :-")
            func(*args,**kwargs)
        else :
            print("\nAccess Denied --> ADMIN REQUIRED !!\n")
    return wrapper

@admin_only
def delete_database(user):
    print("Database Deleted\n")

delete_database(user="Admin")
delete_database(user="NotAdmin")

