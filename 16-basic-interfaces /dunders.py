class User:
    def __init__(self, name, age, balance, groups):
        self.name = name
        self.age = age
        self.balance = balance
        self.groups = groups

    def __repr__(self):
        return f"User(name='{self.name}', age={self.age}, balance={self.balance}, groups={self.groups})"

    def __str__(self):
        return self.name

    def present_user(self):
        return f"User(name='{self.name}', age={self.age}, balance={self.balance}, groups={self.groups})"

    def __int__(self):
        return self.age

    def __float__(self):
        return self.balance

    def __bool__(self):
        return self.balance > 0

    def __len__(self):
        return len(self.groups)

    def __getitem__(self, group):
        return self.groups[group]

    def __setitem__(self, group, permissions):
        self.groups[group] = permissions

    def __add__(self, other):
        return self.balance + other.balance

    def __sub__(self, other):
        return self.balance - other.balance

    def __mul__(self, other):
        return self.balance * other.balance

    def __rshift__(self, other):
        other.groups = {
            group: perms.copy() for group, perms in self.groups.items()
        }
        print(f"Groups and permissions from {self.name} have been copied to {other.name}")

user1 = User(
    name = "Kuba",
    age = 33,
    balance = 0.75,
    groups = {
        "data_warehouse": ["read", "write"],
        "intranet": ["read"],
        "email": ["send", "receive"],
        "adminpanel": ["full_access"],
    }
)

print(user1)
print(user1.present_user())
print(user1.__repr__())
print(user1.__str__())

user1.__init__(
    name="Jakub",
    age=33,
    balance=0.75,
    groups={
        "data_warehouse": ["read", "write"],
        "intranet": ["read"],
        "email": ["send", "receive"],
        "adminpanel": ["full_access"],
    }
)
print(user1)


print()
text = "100"
print(text, type(text))
text_int = int(text)
print(text_int, type(text_int))

int_user = int(user1)
print(int_user, type(int_user))

str_user = str(user1)
print(user1, type(str_user))

float_user = float(user1)
print(float_user, type(float_user))

bool_user = bool(user1)
print(bool_user, type(bool_user))

print("len: ", len(user1))

## set item and get item
print("get item before change:", user1["adminpanel"])
user1["adminpanel"] = ["view_only"]
print("get item after change:", user1["adminpanel"])


user2 = User(
    name = "Aleksandra",
    age = 30,
    balance = 0.25,
    groups = {
        "data_warehouse": ["read", "write"],
    }
)
print("User 1 balance:", user1.balance)
print("User 2 balance:", user2.balance)
print(user1 + user2)
print(user1 - user2)
print(user1 * user2)

print()
# Use rshift method
print("User 1 groups:", user1.groups)
print("User 2 groups:", user2.groups)

# rshift

user1 >> user2

print("User 1 groups:", user1.groups)
print("User 2 groups:", user2.groups)