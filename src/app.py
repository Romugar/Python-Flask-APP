from flask import Flask, render_template, request, session
from src.common.database import Database
from src.models.cliente import Cliente
from src.models.user import User

__author__ = "roberto munoz garcia"

app = Flask(__name__)
app.secret_key = "dnH0xA50QiPdFex9Vn7zfORN9q6Z4eTs"

@app.route("/")
def login_template():
    session["email"] = None
    return render_template("login.html")


@app.before_first_request
def initialize_database():
    Database.initialize()


@app.route("/home", methods=["GET", "POST"])
def login_user():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if User.login_valid(email, password):
            session["email"] = email
            return render_template("home.html")
        else:
            session["email"] = None
            try_again = "Usuario o contraseña incorrecta"
            return render_template("login.html", mensaje="Usuario o contraseña incorrecta")
    elif request.method == "GET" and session["email"] is not None:
        return render_template("home.html")
    else:
        return render_template("login.html")


@app.route("/nuevo_cliente", methods=["GET", "POST"])
def add_clients():
    if request.method == "POST":
        cif = request.form["cif"]
        direccion = request.form["direccion"]
        poblacion = request.form["poblacion"]
        cp = request.form["cp"]
        provincia = request.form["provincia"]
        diocesis = request.form["diocesis"]
        arciprestazgo = request.form["arciprestazgo"]
        parroquia = request.form["parroquia"]
        razon = request.form["razon"]
        web = request.form["web"]
        responsable = request.form["responsable"]
        cargo = request.form["cargo"]
        dni = request.form["dni"]
        tfno1 = request.form["tfno1"]
        tfno2 = request.form["tfno2"]
        email = request.form["email"]

        add_client = Cliente(cif, direccion, poblacion, cp, provincia, diocesis, arciprestazgo, parroquia, razon, web, responsable, cargo, dni, tfno1, tfno2, email)
        add_client.save_to_mongo()


    elif request.method == "GET" and session["email"] is not None:
        return render_template("add_client.html")
    else:
        return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=app.config['DEBUG'], port=4990)
