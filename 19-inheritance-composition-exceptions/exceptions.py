def division(num1, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
        result = num1 / num2
        print(f"Division result: {result}")

    except ZeroDivisionError:
         print("Error: You can't divide by zero!")

    except ValueError:
        print("Error: Values must be integers or floats!")

    else:
        print("Division succeed!")

    finally:
        print("Program ends.")


num1 = input("Type num1: ")
num2 = input("Type num2: ")
division(num1, num2)

# ZeroDivisionError:
# ValueError: