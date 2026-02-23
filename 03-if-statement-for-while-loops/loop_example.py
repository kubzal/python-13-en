# loops
print ("-- WELCOME --")

# name = "Jakub"
# condition = True
# while condition:
#     print(name)
#
#     again = input("Again? ")
#
#     if again == "yes":
#         condition = True
#     else:
#         condition = False

even = False
odd = False

user_input = input("If you want to see even numbers type 'even', if odd type 'odd', otherwise you will see nothing: ")

if user_input == "even":
    even = True

if user_input == "odd":
    odd = True

number = 0
while number < 10:
    if even:
        if number % 2 == 0:
            print(number)
    if odd:
        if number % 2 != 0:
            print(number)

    number = number + 1

print("-- GOOD BYE --")