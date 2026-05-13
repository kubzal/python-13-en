import csv

from flask import Flask, render_template, request

CSV_FILE_PATH = "data/books.csv"

app = Flask(__name__)

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

    return render_template("add_book.html", subtitle = "Add book")

@app.route("/books-list")
def books_list():
    books = load_books()
    return render_template("books_list.html", subtitle="List of available books", books = books)

if __name__ == "__main__":
    app.run(debug=True)