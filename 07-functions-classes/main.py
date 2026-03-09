# # Examples of functions that we already know:
# print("Hello world")
# val = input("Enter value: ")
# print(type(val))
#
# list1 = ["A", "B", "C"]
#
# for index, value in enumerate(list1):
#     print(index, value)

def greet(first_name):
    print(f"Hello {first_name}")

greet("Jakub")
greet("Eleonora")

def sum_two_numbers(number1, number2):
    result = number1 + number2
    print(f"The sum of two numbers: {number1} and {number2} is {result}")
    return result

sum1 = sum_two_numbers(1, 2)
print(sum1)

def display_n_numbers(n, even=True, odd=True):
    for number in range(n):
        if even:
            if number % 2 == 0:
                print(number)

        if odd:
            if number % 2 != 0:
                print(number)


# print()
# display_n_numbers(10, odd=False)
#
# print()
# display_n_numbers(15, even=False)


def get_smallest_even_or_odd_number(list_numbers, even):
    list_numbers = sorted(list_numbers)

    for number in list_numbers:
        if even:
            if number % 2 == 0:
                return number
        else:
            if number % 2 != 0:
                return number

list_numbers_1 = [100, 101, 11, 3, 7, 14, 16, 8, 2]
smallest_odd = get_smallest_even_or_odd_number(list_numbers = list_numbers_1, even = False)
print("Smallest odd:", smallest_odd)

print()

smallest_even = get_smallest_even_or_odd_number(list_numbers = list_numbers_1, even = True)
print("Smallest even:", smallest_even)

def foo():
    a = 1 + 2

    return a

    # that part is unreachable
    b = 2 + 3

    return b

print()
print(foo())


def funtion_multiple_args(*args):
    print(f"Sum of arguments/parameters: {sum(args)}")

    for arg in args:
        print(arg)

funtion_multiple_args(1, 2, 4)
funtion_multiple_args(1, 2, 4, 100, 111)
funtion_multiple_args(1)
funtion_multiple_args()

def function_kwargs(**kwargs):
    for key, value in kwargs.items():
        if key == "first_name":
            print(value)

function_kwargs(first_name="Jakub", aa= 1, bb=3)
function_kwargs(aa= 1, bb=3)
function_kwargs()
function_kwargs(1, 2, 3)