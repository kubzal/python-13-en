import os

def bordered(callback):
    w, h = os.get_terminal_size()
    print("=" * w, end ="\n")
    callback()
    print("=" * w, end = "\n")
    print()

def main_func():
    print("Line 1")
    print("Line 2")

def another_func():
    for i in range(1, 10):
        print(i)

bordered(main_func)
bordered(another_func)