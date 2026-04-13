
def validate_age(age):
    if age < 0:
        raise ValueError("Age can't be negative!")
    elif age < 18:
        print(f"User is not an adult!")
    else:
        print(f"User is an adult.")


validate_age(25)
try:
    validate_age(-5)
except ValueError as e:
    print(f"Error: {e}")

validate_age(16)