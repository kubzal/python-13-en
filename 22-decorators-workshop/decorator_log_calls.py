from datetime import datetime

def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"[{datetime.now()}] Function '{func.__name__}' was executed with args {args} and kwargs {kwargs}")
        result = func(*args, **kwargs)
        print(f"[{datetime.now()}] Function returned result {result}")
        return result
    return wrapper

@log_calls
def add(a, b):
    return a + b

@log_calls
def sub(a, b):
    return a - b

number_1 = int(input("Enter number 1: "))
number_2 = int(input("Enter number 2: "))

result_add = add(number_1, number_2)
print(f"Adding numbers {number_1} and {number_2}. Result is {result_add}")

print()

result_add = add(a = number_1, b = number_2)
print(f"Adding numbers {number_1} and {number_2}. Result is {result_add}")

print()

result_add = add(number_1, b = number_2)
print(f"Adding numbers {number_1} and {number_2}. Result is {result_add}")

result_sub = sub(number_1, number_2)
print(f"Substructing numbers {number_1} and {number_2}. Result is {result_sub}")

print()

result_sub = sub(a = number_1, b = number_2)
print(f"Substructing numbers {number_1} and {number_2}. Result is {result_sub}")

print()

result_sub = sub(number_1, b = number_2)
print(f"Substructing numbers {number_1} and {number_2}. Result is {result_sub}")