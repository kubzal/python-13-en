import os

def bordered(callback):
    def retfunc():
        w, h = os.get_terminal_size()
        print("=" * w, end ="\n")
        callback()
        print("=" * w, end = "\n")
        print()
    return retfunc

@bordered
def main_func():
    print("Line 1")
    print("Line 2")

@bordered
def another_func():
    for i in range(1, 10):
        print(i)

main_func()
another_func()