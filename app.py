from flask import Flask

# __name__ = "main"
app = Flask(__name__)

@app.route("/tasks")
def hello_world():
    return "Hello world!"

@app.route("/about")
def about():
    return "About"

# modo de executar manual (dev local), __name__ sempre sera main
if __name__ == "__main__":
    app.run(debug=True)