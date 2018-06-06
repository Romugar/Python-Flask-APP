from flask import Flask, render_template, request, session
from src.common.database import Database
from src.models.user import User

__author__ = "roberto munoz garcia"

app = Flask(__name__)
app.secret_key = "dnH0xA50QiPdFex9Vn7zfORN9q6Z4eTs"

@app.route("/")
def login_template():
    return render_template("login.html")


@app.before_first_request
def initialize_database():
    Database.initialize()


@app.route("/auth/login", methods=["POST"])
def login_user():
    email = request.form["email"]
    password = request.form["password"]

    if User.login_valid(email, password):
        session["email"] = email
        # return render_template("home.html", email=session["email"])
    else:
        session["email"] = None
        try_again = "Usuario o contraseña incorrecta"
        return render_template("login.html", mensaje=try_again)


if __name__ == "__main__":
    app.run(debug=app.config['DEBUG'], port=4990)
