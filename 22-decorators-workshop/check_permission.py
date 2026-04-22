class User:
    def __init__(self, name, permission_level):
        self.name = name
        self.permission_level = permission_level

def check_permissions(required_permission_level):
    def decorator(function):
        def wrapper(*args, **kwargs):
            user = kwargs.get("user") # kwargs["user"]
            if isinstance(user, User) and user.permission_level == required_permission_level:
                print()
                print(f"User {user.name} has sufficient permission level to {function.__name__}: {user.permission_level}")
                return function(*args, **kwargs)
            else:
                print()
                print(f"User {user.name} has insufficient permission level to {function.__name__}: {user.permission_level} [Required: {required_permission_level}]")
        return wrapper
    return decorator

@check_permissions("admin")
def show_user_data(user):
    print(f"User data: {user.name}, Permission level: {user.permission_level}")

@check_permissions("moderator")
def delete_comment(user, comment_id):
    print(f"Comment with ID {comment_id} was deleted by {user.name}")

# User 1: User with "admin" permissions
user_1 = User("Jakub", "admin")

show_user_data(user = user_1)
delete_comment(user = user_1, comment_id = 42)

print("-" * 20)

# User 2: User without any permissions
user_2 = User("Aleksandra", "user")

show_user_data(user = user_2)
delete_comment(user = user_2, comment_id = 42)

print("-" * 20)

# User 3: User with "moderator" permissions
user_3 = User("Cathrine", "moderator")

show_user_data(user = user_3)
delete_comment(user = user_3, comment_id = 42)