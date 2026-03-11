

# users = list()
# user1 = {
#     "first_name": "Jakub",
#     "last_name": "Zalewski",
#     "age": 32,
#     "city": "Warsaw",
#     "country": "Poland",
#     "username": "jakub.zalewski",
# }
#
# user2 = {
#     "first_name": "John",
#     "last_name": "Doe",
#     "age": 40,
#     "city": "New York",
#     "country": "US",
# }
#
# user1["sity"] = "Gdansk"
#
# users = [user1, user2]
#
# for user in users:
#     print(user)

def foo():
    print("bar")

class User:
    def __init__(self, first_name, last_name, age, city, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.country = country

    def print_user_details(self):
        print(f"First_name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"City: {self.city}")
        print(f"Country: {self.country}")
        print()

    def print_hello(self):
        print(f"Hello {self.first_name}!")

    def print_bye(self):
        print(f"Bye {self.first_name} {self.last_name}!")


user1 = User("Jakub", "Zalewski", "32", "Warsaw", "Poland")
user2 = User("John", "Doe", "40", "New York", "US")

def print_user_details(user):
    print(f"First_name: {user.first_name}")
    print(f"Last name: {user.last_name}")
    print(f"Age: {user.age}")
    print(f"City: {user.city}")
    print(f"Country: {user.country}")
    print()


print(user1.first_name)
print()

print_user_details(user1)

user1.print_user_details()

print()

user2.print_hello()
user2.print_bye()

class ProductPiece:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self, quantity):
        print(f"{quantity}x pieces of {self.name} cost {quantity*self.price}")


iphone = ProductPiece("iPhone 17", 1000)
macbook = ProductPiece("MacBook Pro 14", 4090)

iphone.get_price(10)
macbook.get_price(1)

print(type(iphone))


class Dog:
    def __init__(self, name):
        self.name = name

    def make_noise(self):
        print(f"Dog {self.name} is barking!")

class Cat:
    def __init__(self, name):
        self.name = name

    def make_noise(self):
        print(f"Cat {self.name} is meowing!")

torvi = Dog("Torvi")
nyx = Cat("Nyx")

torvi.make_noise()
nyx.make_noise()