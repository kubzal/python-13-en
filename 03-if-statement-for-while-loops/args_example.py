import sys

args = sys.argv

# for arg in args:
#     print(arg)

if len(args) > 3:
    first_name = args[1]
    last_name = args[2]

    print(f"First name: {first_name}, Last name: {last_name}")
else:
    print("You probably forget to pass args")