# lists
list1 = []
list2 = list()

print(list1, type(list1))
print(list2, type(list2))

list_of_ints = [1, 2, 4, 7, -1, 10, 123, 2,-1, 0, 1]
print(list_of_ints, type(list_of_ints))

list_of_floats = [1.0, 0.5, 0.25, -0.1, 11.7, 123.456]
print(list_of_floats, type(list_of_floats))

list_of_strings = ["aaa", "Bbb", 'Text', "name", "some value"]
print(list_of_strings, type(list_of_strings))

list_of_booleans = [True, False, True, True]
print(list_of_booleans, type(list_of_booleans))

some_int = 123
some_float = 3.14
some_string = "hello there!"
some_bool = False

list_of_mixed_types = [1, 2.5, "strings are also welcome :)", True, some_int, some_float, some_string, some_bool, [1, 2, 3], list_of_strings]
print(list_of_mixed_types, type(list_of_mixed_types))

print()
print("-- LISTS WITH LOOPS --")

for item in list_of_mixed_types:
    if type(item) == list:
        for inner_element in item:
            print(inner_element, type(inner_element))
    else:
        print(item, type(item))

print()
print("How to display one element of a list?")
another_list = ["Aa", "Bb", "Cc"]

print(another_list)

# To display only one lement we need to use indexes
print("First element has index 0:", another_list[0])
print("Second element has index 1:", another_list[1])
print("Third element has index 2:", another_list[2])

# The n'th element of a list has n-1 index

print()
print("How to display the last element of a list?")

# len() tells you how many elements we have in a list
# elements_in_another_list = len(another_list)
print("Elements in 'another_list':", len(another_list))

print()
print(f"The last element of a list:", another_list[len(another_list)-1])
print(f"Simpler way of displaying the last element of a list:", another_list[-1])
print(f"The second from the end element of a list:", another_list[-2])

# The list with one element
print()
print("The list with one element:")
one_element_list = [1]
print(one_element_list[0])
print(one_element_list[-1])

# empty_list = []
# print(empty_list[0]) # IndexError: list index out of range

print()

# How to go through elements of a list using while loop?

index = 0
while index < len(another_list):
    print(another_list[index])
    index += 1 # index = index + 1

print()

# We can also do this with for loop
for index in range(len(another_list)):
    print(another_list[index])

print()
# How to display both: index and value?
for index in range(len(another_list)):
    print(f"Index: {index}, Value: {another_list[index]}")

print()
for index, value in enumerate(another_list):
    print(f"Index: {index}, Value: {value}")

print()
# How to add elements to a list?
my_list = [100, 200, 300]
print(f"List values: {my_list}, \n  list length: {len(my_list)}, \n  The last element: {my_list[-1]} \n")

my_list.append(400)
print(f"List values: {my_list}, \n  list length: {len(my_list)}, \n The last element: {my_list[-1]} \n")

my_list.insert(2, "Jakub")
print(f"List values: {my_list}, \n  list length: {len(my_list)}, \n The last element: {my_list[-1]} \n")

my_list.pop()
print(f"List values: {my_list}, \n  list length: {len(my_list)}, \n The last element: {my_list[-1]} \n")

my_list.pop(2)
print(f"List values: {my_list}, \n  list length: {len(my_list)}, \n The last element: {my_list[-1]} \n")

# del my_list[2]
# I do not reccomend that method

# Dictionaries
print()
print("-- DICTIONARIES -- ")

dict1 = {} # be careful! why? I will tell you later :)
dict2 = dict()

print(dict1, type(dict1))
print(dict2, type(dict2))

dict3 = {
    "key1": 100,
    "key2": 200,
    "key3": "Some other value",
    "key4": [1, 2, 3.14, True],
    "key5": {"another_key": 100}
}

print(dict3, type(dict3))
print("len:", len(dict3))
print(dict3["key1"])

print()

for key in dict3:
    print(key, dict3[key])

print()

for key in dict3.keys():
    print(key, dict3[key])

print()

for value in dict3.values():
    print(value)

print()

for key, value in dict3.items():
    print(f"Key: {key}, Value: {value}")

    if type(value) == list:
        print("Value is a list:")
        for element in value:
            print("\t", element, type(element))

    if type(value) == dict:
        print("Value is a dictionary:")
        for k, v in value.items():
            print("\t", "Key:", k, "Value:", v)


print()

# How to add element to a dictionary?

my_dict = {
    "first_name": "Jakub",
    "last_name": "Zalewski",
    "age": 33
}

print(my_dict)

my_dict["city"] = "Warsaw"

print(my_dict)

print()

my_dict["first_name"] = "Steven"

print(my_dict)

my_dict["firstname"] = "Jakub"

print(my_dict)

# TUPLES
tuple1 = ()
tuple2 = tuple()

tuple3 = (1, 2, 3, True, "string as well")
tuple4 = 4, 5, 6
tuple5 = 100,

tuple_of_tuples = (tuple1, tuple2, tuple3, tuple4, tuple5)

for tup in tuple_of_tuples:
    print(tup, type(tup), len(tup))

print(tuple3[3])

# we cannnot append tuples
# tuple_of_tuples.append(1)

# we cannot remove any element of a tuple
# tuple4.pop()

for key, value in dict3.items():
    print(f"Key: {key}, Value: {value}")

print()

for tuple_iterator in dict3.items():
    # print(f"Key: {key}, Value: {value}")
    print(tuple_iterator, type(tuple_iterator))

    print(f"Key: {tuple_iterator[0]}, Value: {tuple_iterator[1]}")

    key, value = tuple_iterator
    print(f"Key: {key}, Value: {value}")
    print()

# SETS
set1 = {}
set2 = set()

print(set1, type(set1)) # acctually it's a dictionary
print(set2, type(set2))

set3 = {100, 1, 3, 4, 7, True, "hello", 3.14, 1, 2, 3, True, "hello"}
print(set3, type(set3)) # now it's a set :)

list_of_dupicated_values = [1001, 1002, 1001, 1002, 1001, 1003]

print(list_of_dupicated_values, type(list_of_dupicated_values), len(list_of_dupicated_values))
set_of_values = set(list_of_dupicated_values)
print(set_of_values, type(set_of_values), len(set_of_values))