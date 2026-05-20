from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SECRET_KEY"] = "your_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"

db = SQLAlchemy(app)

history = []

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(120), nullable = False)
    author = db.Column(db.String(120), nullable = False)
    book_count = db.Column(db.Integer, nullable=False, default=0)

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

        book = Book.query.filter_by(title=title, author=author).first()

        if book:
            book.book_count += book_count
        else:
            book = Book(title=title, author=author, book_count=book_count)
            db.session.add(book)

        db.session.commit()
        history.append("add book")

    return render_template("add_book.html", subtitle = "Add book")


@app.route("/borrow-book", methods=["GET", "POST"])
def borrow_book():
    if request.method == "POST":
        title = request.form.get("title")
        author = request.form.get("author")
        book_count = int(request.form.get("book_count"))

        book = Book.query.filter_by(title = title, author = author).first()

        if book is None:
            print(f"Book '{title}' by {author} was not found")
        elif book.book_count >= book_count:
            book.book_count -= book_count
            db.session.commit()
        else:
            print(f"Not enough books of title '{book.title}' in the library")

        history.append("borrow book")

    return render_template("borrow_book.html", subtitle = "Borrow book")


@app.route("/books-list")
def books_list():
    books = Book.query.all()
    history.append("books list")
    return render_template("books_list.html", subtitle="List of available books", books = books)


@app.route("/operations-history")
def operations_history():
    return render_template("operations_history.html", subtitle="Operations history", history = history)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)