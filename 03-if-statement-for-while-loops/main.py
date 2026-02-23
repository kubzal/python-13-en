
# Contants
ADULTS_AGE = 18
CURRENT_YEAR = 2026
THE_OLDEST_PERSON_AGE = 150

# calcualting the year of birth of the oldes person
yob_of_the_oldest_person = CURRENT_YEAR - THE_OLDEST_PERSON_AGE

# welcome message
print("This application is only for adult users (18+)")

# getting the input from the user
yob = int(input("What is your year of birth?: "))
print()

# calcualting the user age
user_age = CURRENT_YEAR - yob

# checking if yob is correct
if (yob > CURRENT_YEAR) | (yob < yob_of_the_oldest_person):
    # if year of birth is greater than current year we should
    # ask user if he/she is sure about this value
    print(f"Are you sure that {yob} is your year of birth?")

# if (yob < CURRENT_YEAR) & (yob > yob_of_the_oldest_person):
else:
    # checkin the age of the user
    if user_age >= ADULTS_AGE:
        # user is old enough
        print(f"You are {user_age} years old! It's enough to see that content ;) ")
        print("Welcome to the adults only site!")

    # if user_age < ADULTS_AGE:
    else:
        # user is not old enough
        print(f"You are {user_age} years old! It's not enough to see that content :(")
        print("Sorry! You are not old enough to enter this site!")
        print(f"Come back to us in {ADULTS_AGE-user_age} year(s)! :)")

print()
print("Good bye! See you again!")