

number = int(input("Type number: "))

if number % 2 == 0:
    print(f"Number {number} can be divided by 2")

elif number % 3 == 0:
    print(f"Number {number} can be divided by 3")

elif number % 5 == 0:
    print(f"Number {number} can be divided by 5")

else:
    print(f"Number {number} can't be divided by 2 and 3 and 5")