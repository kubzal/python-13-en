# How to print something on the screen?
print("Hello world")

# Diffrent type of variables
a = 1 # integer, int
b = 3.14 # float
c = "text" # string, str
d = True # boolean, bool

# Builtin functions
# - print() <- prints sth on the screen
# - type() <- return the type of the variable

# Comments (this is a comment ;) ) a line that starts wit '#' symbol and it's not executed by Python interpreter

# Greet user

# Option 1: adding strings
name = "Jakub"
msg = "Hello " + name + "!"

print(msg)

# Option 2: format
template = "Hello {}!"
msg = template.format(name)

print(msg)

# Option 3: f'string

print(f"Hello {name}!")

# Mathematical operations
print()
print("-" * 50, "Mathematical operations", "-" * 50)
print()

print("### Basic operations")
print()

number1 = float(input("Please type the first number: "))
number2 = float(input("Please type another number: "))
print()

addition = number1 + number2
print(f"{number1} + {number2} = {addition}")

substract = number1 - number2
print(f"{number1} - {number2} = {substract}")

multiply = number1 * number2
print(f"{number1} * {number2} = {multiply}")

divide = number1 / number2
print(f"{number1} / {number2} = {divide}")

print()
print("### Advanced operations")
print()

power = number1 ** number2
print(f"{number1}^{number2} = {power}")

sqrt_number1 = number1 ** 0.5
print(f"Square root of {number1} = {sqrt_number1}")

# Division with remainder
# 10 / 3 = 3 remainder 1
# 10 / 2 = 5 remainder 0
# 11 / 4 = 2 remainder 3
# 15 / 2 = 7 reminder 1

# Modulo
remainder = number1 % number2
print(f"Reminder of {number1} divided by {number2} is {remainder}")
print(f"( {number1} % {number2} = {remainder} )")

print()
print("-" * 50, "Logical operations", "-" * 50)
print()

print(f"{number1} == {number2}", number1 == number2) # number1 equal to number2
print(f"{number1} != {number2}", number1 != number2) # number1 different from number2
print(f"{number1} > {number2}", number1 > number2) # number1 greater than number2
print(f"{number1} < {number2}", number1 < number2) # number1 lower than number2
print(f"{number1} >= {number2}", number1 >= number2) # number1 greater or equal to number2
print(f"{number1} <= {number2}", number1 <= number2) # number1 lower or qual to number2


is_number1_equal_number2 = number1 == number2
print(f"Is {number1} equal to {number2}?", is_number1_equal_number2, type(is_number1_equal_number2))


