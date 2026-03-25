"""
Mini Table Editor
"""
import sys
from utils import welcome_message, load_data, pretty_print, modify_data, save_data

def main(changes):
    print(changes)

    welcome_message()

    # data load
    data = load_data()

    # print current state of the data
    print("\nInitial state:")
    pretty_print(data)

    # modify table
    for row, col, new_value in changes:
        data = modify_data(data = data, row = int(row), col = int(col), new_value = new_value)

    # print modified table
    print("\nAfter modification:")
    pretty_print(data)

    # save modified data
    save_data(data)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        args = sys.argv[1:]
        changes = list()

        for arg in args:
            changes.append(tuple(arg.split(",")))

        main(changes)