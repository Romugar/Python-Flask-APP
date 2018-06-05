from flask import Flask


__author__ = "roberto munoz garcia"

app = Flask(__name__)


@app.route("/")
def hello_method():
    return "Hello, world!"


if __name__ == "__main__":
    app.run(debug=app.config['DEBUG'], port=4990)
