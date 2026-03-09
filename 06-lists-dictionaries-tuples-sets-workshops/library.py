# Task: A program handling a simple library
#
# Enables entering books, borrowing, checking availability,
# displaying the list of books and the history of actions.
# The program runs in a loop, allowing the user to enter commands
# such as:
# [v] ADD - Adding new books to the library
# [v] BORROW - Borrowing books from the library
# [v] BOOKS - Displaying all books and the number of available copies
# [v] AVAILABILITY - Checking if a given book is available in the library
# [v] UNIQUE - Displaying the number of unique titles in the library
# [v] COUNT - Displaying the total number of books (volumes) in the library
# [v] HISTORY - Displaying the history of all operations on books
# [v] HELP - Displaying available commands
# [v]  - Ending the program

KNOWN_COMMANDS = [
    "ADD",
    "BORROW",
    "AVAILABILITY",
    "UNIQUE",
    "COUNT",
    "HISTORY",
    "HELP",
    "EXIT",
]

books = {
    "Harry Potter": 3,
    "The Lord of the Rings": 5,
    "The Witcher": 10,
    "The Catcher in the Rye": 4,
    "Glucose Revolution": 2,
}

history = list()  # other option of setting up an empty list --> []

while True:
    print()
    command = input("Enter command: ").upper()

    if command in KNOWN_COMMANDS:
        history.append(command)

    print(f"Typed command: {command} \n")

    if command == "EXIT":
        print("Ending the program.")
        break

    elif command == "ADD":
        print("Add a book.\n")
        title = input("Enter book title: ")
        quantity = int(input("Enter quantity: "))

        if quantity > 0:
            if title in books:
                # book already exisits
                books[title] += quantity
            else:
                # new book
                books[title] = quantity
        else:
            print("The quantity should be greater than 0.")

    elif command == "BORROW":
        print("Borrow a book.\n")
        title = input("Enter book title: ")
        quantity = int(input("Enter the quantity to borrow: "))

        if title in books and books[title] >= quantity:
            # we can borrow the book
            books[title] -= quantity
            print(f'Borrowed book: "{title}", quantity: {quantity}')
        else:
            print(
                f'Not enough copies of the book "{title}" or it is not in the library.'
            )

    elif command == "BOOKS":
        if books:
            print("List of books and number of available copies:")
            for title, quantity in books.items():
                print(f' - "{title}": {quantity} pcs.')

    elif command == "AVAILABILITY":
        print("Check if the book is available.\n")
        title = input("Enter the book title: ")
        if title in books:
            print(f'Book "{title}" is available, quantity: {books[title]} pcs.')
        else:
            print(f'Book "{title}" is not available.')

    elif command == "UNIQUE":
        print("Check unique number of all titles.\n")
        unique_count = len(books)
        print(f"Number of unique titles in the library: {unique_count}")

    elif command == "COUNT":
        print("Total number of books: \n")
        total_volumes = sum(books.values())
        print(f"Total number of volumes in the library: {total_volumes}")

    elif command == "HISTORY":
        print("Commands history: \n")
        for order, item in enumerate(history):
            print(f"{order+1}. {item}")

    elif command == "HELP":
        print("""List of available commands:
        1. ADD - Adding new books to the library
        2. BORROW - Borrowing books from the library
        3. BOOKS - Displaying all books and the number of available copies
        4. AVAILABILITY - Checking if a given book is available in the library
        5. UNIQUE - Displaying the number of unique titles in the library
        6. COUNT - Displaying the total number of books (volumes) in the library
        7. HISTORY - Displaying the history of all operations on books
        8. HELP - Displaying available commands
        9. EXIT - Ending the program
        """)

    else:
        print("Unknown command. Type 'HELP' to display the list of commands.")

print("The end of the program.")
