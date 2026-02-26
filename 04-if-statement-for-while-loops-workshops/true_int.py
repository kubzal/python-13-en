value = input("Enter some value: ")

value_float = float(value)
value_int = int(float(value))

if (value_float / value_int) == 1.0:
    print("It's a true int")
else:
    print("It's not a true int")