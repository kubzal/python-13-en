# 1. shorter form of if/else statement

# in Polish language almost every female first name ends with letter 'a'

firstname = "Adam"
if firstname[-1] == "a":
    gender = "f"
else:
    gender = "m"

print(f"{firstname=} {gender=}")

# shorter form
firstname = "Adam"
gender = "f" if firstname[-1] == "a" else "m"

print(f"{firstname=} {gender=}")

print()

# 2. list comprehension

firstname = "adAm"
print(firstname, firstname.capitalize())

print()

list_of_names = ["adam", "Jessica", "Manolo", "Elena", "jakub", "james", "mIchael"]
list_of_names_converted = []
for firstname in list_of_names:
    list_of_names_converted.append(firstname.capitalize())

print(list_of_names)
print(list_of_names_converted)

print()

# shorter form
list_of_names = ["adam", "Jessica", "Manolo", "Elena", "jakub", "james", "mIchael"]
list_of_names_converted = [firstname.capitalize() for firstname in list_of_names]

print(list_of_names)
print(list_of_names_converted)

print()

list_of_names = ["adam", "Jessica", "Manolo", "Elena", "jakub", "james", "mIchael"]
list_of_names_that_need_conversion = []
for firstname in list_of_names:
    if firstname != firstname.capitalize():
        list_of_names_that_need_conversion.append(firstname.capitalize())

print(list_of_names)
print(list_of_names_that_need_conversion)

print()

# shorter form
list_of_names = ["adam", "Jessica", "Manolo", "Elena", "jakub", "james", "mIchael"]
list_of_names_that_need_conversion = [
    firstname.capitalize()
    for firstname in list_of_names
    if firstname != firstname.capitalize()
]

print(list_of_names)
print(list_of_names_that_need_conversion)

print()

# 3. dict comprehension
list_of_names = ["adam", "Jessica", "Manolo", "Elena", "jakub", "james", "mIchael"]
dict_of_names = {firstname: firstname.capitalize() for firstname in list_of_names}

print(list_of_names)
print(dict_of_names)

# 4. pip = pip install packages
