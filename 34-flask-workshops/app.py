import csv

from flask import Flask, render_template, request

CSV_FILE_PATH = "data/books.csv"

app = Flask(__name__)

history = []


class Book:
    def __init__(self, title, author, book_count):
        self.title = title
        self.author = author
        self.book_count = int(book_count)

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', book_count={self.book_count})"

    def to_dict(self):
        return {"title": self.title, "author": self.author, "book_count": self.book_count}


def load_books():
    books = []
    with open(CSV_FILE_PATH, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            book = Book(title=row["title"], author=row["author"], book_count=row["book_count"])
            books.append(book)

        return books


@app.route("/")
def index():
    history.append("index")
    return render_template("index.html", subtitle = "Home")


@app.route("/add-book", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        title = request.form.get("title")
        author = request.form.get("author")
        book_count = int(request.form.get("book_count"))

        # loading books from a CSV file
        books = load_books()

        # Checking if book exist in library and adding new books
        book_exists = False
        for book in books:
            if book.title == title and book.author == author:
                book_exists = True
                book.book_count += book_count
                break

        if not book_exists:
            books.append(Book(title, author, book_count))

        # print(books)

        # Save books to a file
        with open(CSV_FILE_PATH, "w", encoding="utf-8") as file:
            fieldnames = ["title", "author", "book_count"]
            writer = csv.DictWriter(file, fieldnames = fieldnames)
            writer.writeheader()
            writer.writerows([book.to_dict() for book in books])

        history.append("add book")

    return render_template("add_book.html", subtitle = "Add book")


@app.route("/borrow-book", methods=["GET", "POST"])
def borrow_book():
    if request.method == "POST":
        title = request.form.get("title")
        author = request.form.get("author")
        book_count = int(request.form.get("book_count"))

        searched_book = Book(title, author, book_count)

        print("Searched book:", searched_book)

        with open(CSV_FILE_PATH, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            books = []
            for row in reader:
                print(row)
                if row["title"] == title and row["author"] == author:
                    print("Book was found")
                    available_books = int(row["book_count"])

                    if available_books >= book_count:
                        # enough books to borrow
                        row["book_count"] = str(available_books - book_count)
                    else:
                        print(f"Not enough books of title '{row["title"]}' in the library")
                books.append(row)

        with open(CSV_FILE_PATH, "w", encoding="utf-8") as file:
            fieldnames = ["title", "author", "book_count"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(books)

        history.append("borrow book")

    return render_template("borrow_book.html", subtitle = "Borrow book")


@app.route("/books-list")
def books_list():
    books = load_books()
    history.append("books list")
    return render_template("books_list.html", subtitle="List of available books", books = books)


@app.route("/operations-history")
def operations_history():
    return render_template("operations_history.html", subtitle="Operations history", history = history)


if __name__ == "__main__":
    app.run(debug=True)