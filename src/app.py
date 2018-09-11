from flask import Flask, render_template, request, session
from src.common.database import Database
from src.models.cliente import Cliente
from src.models.user import User

__author__ = "roberto munoz garcia"

app = Flask(__name__)
app.secret_key = "aqui la secret key"

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
            return render_template("login.html", mensaje="Usuario o contraseña incorrecta")
    elif request.method == "GET" and session["email"] is not None:
        return render_template("home.html")
    else:
        return render_template("login.html")


@app.route("/nuevo_cliente", methods=["GET", "POST"])
def add_clients():
    if request.method == "POST":
        campo1 = request.form["campo1"]
        campo2 = request.form["campo2"]
        campo3 = request.form["campo3"]
        campo4 = request.form["campo4"]
        campo5 = request.form["campo5"]
        campo6 = request.form["campo6"]
        campo7 = request.form["campo7"]
        campo8 = request.form["campo8"]
        campo9 = request.form["campo9"]
        campo10 = request.form["campo10"]
        campo11 = request.form["campo11"]
        campo12 = request.form["campo12"]
        campo13 = request.form["campo13"]
        campo14 = request.form["campo14"]
        campo15 = request.form["campo15"]

        add_client = Cliente(campo1, campo2, campo3, campo4, campo5, campo6, campo7, campo8, campo9, campo10, campo11, campo12, campo13, campo14, campo15)
        add_client.save_to_mongo()

        return render_template("add_client.html", mensaje="Cliente guardado con éxito")
    elif request.method == "GET" and session["email"] is not None:
        return render_template("add_client.html")
    else:
        return render_template("login.html")


@app.route("/resultado_busqueda", methods=["GET", "POST"])
def find_and_filter_clients():
    if request.method == "POST":
        campo1 = request.form["campo1"]
        campo2 = request.form["campo2"]
        campo3 = request.form["campo3"]
        campo4 = request.form["campo4"]
        campo5 = request.form["campo5"]
        campo6 = request.form["campo6"]
        campo7 = request.form["campo7"]
        campo8 = request.form["campo8"]
        campo9 = request.form["campo9"]
        campo10 = request.form["campo10"]
        campo11 = request.form["campo11"]
        campo12 = request.form["campo12"]
        campo13 = request.form["campo13"]
        campo14 = request.form["campo14"]
        campo15 = request.form["campo15"]

        query_clients = Cliente(campo1, campo2, campo3, campo4, campo5, campo6, campo7, campo8, campo9, campo10, campo11, campo12, campo13, campo14, campo15)
        result = query_clients.find_clients()

        return render_template("find_clients.html", result=result)
    elif request.method == "GET" and session["email"] is not None:
        return render_template("home.html")
    else:
        return render_template("login.html")


@app.route("/editar_clientes/<path:result>", methods=["GET", "POST"])
def edit_clients(result):
    if request.method == "GET" and session["email"] is not None:
        data = eval(result)
        return render_template("edit_clients.html", data=data)
    else:
        return render_template("login.html")

@app.route("/guardar_edicion", methods=["GET", "POST"])
def save_edition():
    if request.method == "POST":
        _id = request.form.getlist("_id")
        fecha_alta = request.form.getlist("fecha_alta")
        campo1 = request.form.getlist("campo1")
        campo2 = request.form.getlist("campo2")
        campo3 = request.form.getlist("campo3")
        campo4 = request.form.getlist("campo4")
        campo5 = request.form.getlist("campo5")
        campo6 = request.form.getlist("campo6")
        campo7 = request.form.getlist("campo7")
        campo8 = request.form.getlist("campo8")
        campo9 = request.form.getlist("campo9")
        campo10 = request.form.getlist("campo10")
        campo11 = request.form.getlist("campo11")
        campo12 = request.form.getlist("campo12")
        campo13 = request.form.getlist("campo13")
        campo14 = request.form.getlist("campo14")
        campo15 = request.form.getlist("campo15")

        clients_to_edit = Cliente(campo1, campo2, campo3, campo4, campo5, campo6, campo7, campo8, campo9,
                                  campo10, campo11, campo12, campo13, campo14, campo15, fecha_alta, _id)
        clients_to_edit.update_clients()

        return render_template("home.html", resultado="Edición guardada con éxito")
    elif request.method == "GET" and session["email"] is not None:
        return render_template("home.html")
    else:
        return render_template("login.html")

@app.route("/borrar_clientes/<path:result>", methods=["GET", "POST"])
def remove_clients(result):
    if request.method == "GET" and session["email"] is not None:
        data = eval(result)
        return render_template("confirmacion.html", data=data)
    else:
        return render_template("login.html")

@app.route("/confirmar_borrado", methods=["GET", "POST"])
def confirm_remove():
    if request.method == "POST":
        _id = request.form.getlist("_id")
        fecha_alta = request.form.getlist("fecha_alta")
        campo1 = request.form.getlist("campo1")
        campo2 = request.form.getlist("campo2")
        campo3 = request.form.getlist("campo3")
        campo4 = request.form.getlist("campo4")
        campo5 = request.form.getlist("campo5")
        campo6 = request.form.getlist("campo6")
        campo7 = request.form.getlist("campo7")
        campo8 = request.form.getlist("campo8")
        campo9 = request.form.getlist("campo9")
        campo10 = request.form.getlist("campo10")
        campo11 = request.form.getlist("campo11")
        campo12 = request.form.getlist("campo12")
        campo13 = request.form.getlist("campo13")
        campo14 = request.form.getlist("campo14")
        campo15 = request.form.getlist("campo15")

        clients_to_remove = Cliente(campo1, campo2, campo3, campo4, campo5, campo6, campo7, campo8, campo9,
                                    campo10, campo11, campo12, campo13, campo14, campo15, fecha_alta, _id)
        clients_to_remove.remove_client()

        return render_template("home.html", resultado="Los datos han sido borrados")
    elif request.method == "GET" and session["email"] is not None:
        return render_template("home.html")
    else:
        return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=app.config['DEBUG'], port=4990)
