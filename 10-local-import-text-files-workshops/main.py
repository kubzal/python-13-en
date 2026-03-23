# Task: Program managing a simple library
#
# Allows adding books, borrowing, checking availability,
# displaying the book list, and action history.
# The program runs in a loop, allowing the user to enter commands
# such as:
# 1. ADD - Add new books to the library
# 2. BORROW - Borrow books from the library
# 3. BOOKS - Display all books and the number of available copies
# 4. AVAILABILITY - Check if a given book is available in the library
# 5. UNIQUE - Display the number of unique titles in the library
# 6. COUNT - Display the total number of books (volumes) in the library
# 7. HISTORY - Display the history of all book operations
# 8. HELP - Display available commands
# 9. EXIT - End the program

from utils.functions import (
    display_help,
    display_history,
    display_volume_count,
    display_number_of_unique_titles,
    check_availability,
    list_all_books,
    borrow_book,
    add_book,
    load_books,
    add_command_to_history
)

books = load_books()
history = list()  # other option of setting up an empty list --> []

while True:
    print()
    command = input("Enter command: ").upper()

    history = add_command_to_history(command, history)

    print(f"Typed command: {command} \n")

    if command == "EXIT":
        print("Ending the program.")
        break

    elif command == "ADD":
        books = add_book(books)

    elif command == "BORROW":
        books = borrow_book(books)

    elif command == "BOOKS":
        list_all_books(books)

    elif command == "AVAILABILITY":
        check_availability(books)

    elif command == "UNIQUE":
        display_number_of_unique_titles(books)

    elif command == "COUNT":
        display_volume_count(books)

    elif command == "HISTORY":
        display_history(history)

    elif command == "HELP":
        display_help()

    else:
        print("Unknown command. Type 'HELP' to display the list of commands.")

print("The end of the program.")