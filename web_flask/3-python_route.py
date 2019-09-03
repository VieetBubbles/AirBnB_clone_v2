#!/usr/bin/python3
# Write a script that starts a Flask web application

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hello_slash():
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def heelo_c(text):
    input_c = text.replace("_", " ")
    return ("C {}".format(input_c))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_ro(text="is cool"):
    return ("Python {}".format(text.replace("_", " ")))

if __name__ is "__main__":
    app.run(host="0.0.0.0", port=5000)
