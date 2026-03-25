import csv
import os

def greet():
    print("Hello")

def welcome_message():
    welcome_mesage = "-"*10 + " Welcome in Mini Table Editor ! " + "-"*10
    welcome_mesage = welcome_mesage.center(110)
    print(welcome_mesage)
    print("version 0.1".center(len(welcome_mesage)))

def load_data(file_name = "employees.csv"):
    file_path = os.path.join("data", file_name)

    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            reader = csv.reader(f)
            data = list(reader)
        return data
    else:
        print("File do not exist")
        return None

def pretty_print(data):
    print("\n")
    max_lengths = list()
    for col in range(len(data[0])):
        max_col_length = 0
        for row in data:
            max_col_length = max(max_col_length, len(row[col]))
        max_lengths.append(max_col_length)
    for row in data:
        text = ""
        for i, cell in enumerate(row):
            text += "\t" + str(cell).ljust(max_lengths[i])
        print(text)

def validate_coordinates(data, row, col):
    if row < 0 or row >= len(data):
        print("Wrong row number")
        return False

    if col < 0 or col >= len(data[0]):
        print("Wrong column number")
        return False

    return True

def modify_data(data, row, col, new_value):
    if validate_coordinates(data, row, col):
        data[row][col] = new_value
    return data


def save_data(data=None, file_path=None):
    if not file_path:
        file_path = os.path.join("data", "employees_modified.csv")
    if data:
        if os.path.exists(os.path.dirname(file_path)):
            with open(file_path, "w") as f:
                writer = csv.writer(f)
                writer.writerows(data)
            print(f"Modified data saved to a file {file_path}")
        else:
            print("Directory doesn't exist")
    else:
        print("Data not provided")
