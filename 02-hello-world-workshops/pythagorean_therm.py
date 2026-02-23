
# a^2 + b^2 = c^2

print("Hello! I'm a Python program that helps you to calculate the lenght of your hypotenuse in any right triangle.")
print()

a = float(input("Enter the length of the first leg: "))
b = float(input("Enter the length of the second leg: "))

c_squared = a**2 + b**2
c = c_squared ** 0.5

print(f"Length of your hypotenunse is {c}")