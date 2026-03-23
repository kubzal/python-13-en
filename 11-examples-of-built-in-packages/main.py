import os
import math
import random
import datetime
import time
import webbrowser

login = os.getlogin()

print(login)

pid = os.getpid()

print(pid)

col, lines = os.get_terminal_size()
print(col, lines)

def print_decorated_text(text):
    text_len = len(text)
    col, lines = os.get_terminal_size()
    decoration_size = (col - text_len - 10) // 2
    print("-"* decoration_size, text, "-"* decoration_size)

print_decorated_text("Hello Future Collars")

print(os.getcwd())
print()

# folder = input("type folder name: ")
#
# if os.path.exists(folder):
#     print(f"Folder '{folder}' already exists")
# else:
#     print(f"Creating folder '{folder}'")
#     os.mkdir(folder)

with open(os.path.join("folder1", "file.txt")) as f:
    text = f.read()
    print(text)

# os.path.isdir(path) <- checks if the path is a directory
print()
print(os.path.basename(os.getcwd()))
print(os.path.abspath("folder1"))

print()

number1 = 2.15
number2 = 3.67

print(round(number1), round(number2))
print(math.floor(number1), math.floor(number2))
print(math.ceil(number1), math.ceil(number2))

number3 = -10
number4 = 11
print(math.fabs(number3), math.fabs(number4))
print(abs(number3), abs(number4))

print(math.log(number2))

print(sum([1, 2, 3]))
print(math.fsum([1, 2, 3]))

# random

print()

print(random.random())
print(random.randint(10, 20))
print(random.choice(["me", "you", "noone"]))
print()

lst = ["a", "b", "c"]
print(lst)

random.shuffle(lst)
print(lst)

current_time = datetime.datetime.now()
print(f"Current time: {current_time}" )
print(f"year: {current_time.year}")
print(f"month: {current_time.month}")
print(f"day: {current_time.day}")
print(f"hour: {current_time.hour}")
print(f"minutes: {current_time.minute}")
print(f"seconds: {current_time.second}")
print(f"miliseconds: {current_time.microsecond}")

# sleep function
# print("\n\n\n")
#
# print("Hello...")
# time.sleep(5)
# print("... who are you?")
# time.sleep(7)
# print("... can I trust you?")
# time.sleep(5)
# print()

webbrowser.open("https://google.com")