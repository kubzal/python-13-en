from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome at my home page!"

@app.route("/simple_greet/<name>")
def simple_greet(name):
    return f"Hello {name}!"

@app.route("/greet", defaults={"name": "Stranger"})
@app.route("/greet/<name>")
def greet(name):
    return render_template("greeting.html", name=name)

@app.route("/add/<number1>/<number2>")
def add(number1, number2):
    return str(int(number1) + int(number2))


@app.route("/search")
def search():
    query = request.args.get("query")
    return render_template("search.html", query = query)

# @app.route("/search_results")
# def search_results():
#     query = request.args.get("query")
#     return f"You are searching for: {query}"

@app.route("/calculator")
def calculator():
    number1 = request.args.get("number1")
    number2 = request.args.get("number2")
    operation = request.args.get("operation")

    if operation == "+":
        result = str(int(number1) + int(number2))
    elif operation == "-":
        result = str(int(number1) - int(number2))
    elif operation == "*":
        result = str(int(number1) * int(number2))
    elif operation == "/":
        result = str(int(number1) / int(number2))
    else:
        result = ""

    return render_template("calculator.html", result = result)


if __name__ == "__main__":
    app.run(debug=True)