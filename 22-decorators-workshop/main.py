class Manager:
    def __init__(self):
        self.methods = {}

    def assign(self, action_name):
        # Decorator that assigns function to the instance of the Manager
        def decorator(func):
            self.methods[action_name.upper()] = func
            return func
        return decorator

    def execute(self, action, library):
        # Method that calls assigned actions
        action = action.upper()
        if action in self.methods:
            return self.methods[action](library)
        else:
            print("Invalid action")


# Library
library = {"Witcher": 3, "Hobbit": 2, "Harry Potter": 5}

# Manager
manager = Manager()

@manager.assign("add")
def add_book(library):
    title = input("Type the book title: ")
    number_of_items = int(input(f"Type the number of '{title}': "))

    if title in library:
        library[title] += number_of_items
    else:
        library[title] = number_of_items

    print(f"Books added: {number_of_items} of '{title}'")

@manager.assign("borrow")
def borrow_book(library):
    title = input("Type the book title: ")
    if title in library and library[title] > 0:
        library[title] -= 1
        print(f"Book '{title}' was borrowed.")
    else:
        print(f"Book '{title}' is not available.")

@manager.assign("list")
def list_all_books(library):
    if not library:
        print("There are no books in the library.")
    else:
        print("Available books:")
        for title, number_of_items in library.items():
            print(f" - '{title}': {number_of_items}")


while True:
    action = input("Type action [add, borrow, list] or 'exit' to stop the application: ").strip().lower()

    if action == "exit":
        print("Exiting the application")
        break
    manager.execute(action, library)

print()
print("End of the program")
