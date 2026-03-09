# why functions are so important?

def seperator():
    print()
    print("-" * 30)
    print()

print("Hello world")
list_1 = [1, 2, 3, 4, 5]

seperator()

for x in list_1:
    print(x)

seperator()

print("Good bye")

seperator()

def connect_to_db_and_extract_user_info():
    user_info = {
        "first_name": "Jakub",
        "city": "Warsaw"
    }
    return user_info

connect_to_db_and_extract_user_info()