from .constants import KNOWN_COMMANDS

def display_help():
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

def load_books():
    books = dict()
    with open("books.txt", "r") as file:
        for line in file:
            title, quantity = line.strip().split(",")
            books[title] = int(quantity)
    return books

def update_books(books):
    with open("books.txt", "w") as file:
        for title, quantity in books.items():
            file.write(f"{title}, {quantity}\n")

def display_history(history):
    print("Commands history: \n")
    for order, item in enumerate(history):
        print(f"{order + 1}. {item}")

def display_volume_count(books):
    print("Total number of books: \n")
    total_volumes = sum(books.values())
    print(f"Total number of volumes in the library: {total_volumes}")

def display_number_of_unique_titles(books):
    print("Check unique number of all titles.\n")
    unique_count = len(books)
    print(f"Number of unique titles in the library: {unique_count}")

def check_availability(books):
    print("Check if the book is available.\n")
    title = input("Enter the book title: ")
    if title in books:
        print(f'Book "{title}" is available, quantity: {books[title]} pcs.')
    else:
        print(f'Book "{title}" is not available.')

def list_all_books(books):
    if books:
        print("List of books and number of available copies:")
        for title, quantity in books.items():
            print(f' - "{title}": {quantity} pcs.')

def borrow_book(books):
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

    update_books(books)
    return books

def add_book(books):
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

    update_books(books)
    return books

def add_command_to_history(command, history):
    if command in KNOWN_COMMANDS:
        history.append(command)

    return history