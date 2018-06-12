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
        parroquia_razon = request.form["parroquia_razon"]
        diocesis = request.form["diocesis"]
        arciprestazgo = request.form["arciprestazgo"]
        web = request.form["web"]
        responsable = request.form["responsable"]
        cargo = request.form["cargo"]
        dni = request.form["dni"]
        tfno1 = request.form["tfno1"]
        tfno2 = request.form["tfno2"]
        email = request.form["email"]

        add_client = Cliente(cif, direccion, poblacion, cp, provincia, parroquia_razon, diocesis, arciprestazgo, web, responsable, cargo, dni, tfno1, tfno2, email)
        add_client.save_to_mongo()

        return render_template("add_client.html", mensaje="Cliente guardado con éxito")
    elif request.method == "GET" and session["email"] is not None:
        return render_template("add_client.html")
    else:
        return render_template("login.html")


@app.route("/resultado_busqueda", methods=["GET", "POST"])
def find_and_filter_clients():
    if request.method == "POST":
        cif = request.form["cif"]
        direccion = request.form["direccion"]
        poblacion = request.form["poblacion"]
        cp = request.form["cp"]
        provincia = request.form["provincia"]
        parroquia_razon = request.form["parroquia_razon"]
        diocesis = request.form["diocesis"]
        arciprestazgo = request.form["arciprestazgo"]
        web = request.form["web"]
        responsable = request.form["responsable"]
        cargo = request.form["cargo"]
        dni = request.form["dni"]
        tfno1 = request.form["tfno1"]
        tfno2 = request.form["tfno2"]
        email = request.form["email"]

        query_clients = Cliente(cif, direccion, poblacion, cp, provincia, parroquia_razon, diocesis, arciprestazgo, web, responsable, cargo, dni, tfno1, tfno2, email)
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
        cif = request.form.getlist("cif")
        direccion = request.form.getlist("direccion")
        poblacion = request.form.getlist("poblacion")
        cp = request.form.getlist("cp")
        provincia = request.form.getlist("provincia")
        parroquia_razon = request.form.getlist("parroquia_razon")
        diocesis = request.form.getlist("diocesis")
        arciprestazgo = request.form.getlist("arciprestazgo")
        web = request.form.getlist("web")
        responsable = request.form.getlist("responsable")
        cargo = request.form.getlist("cargo")
        dni = request.form.getlist("dni")
        tfno1 = request.form.getlist("tfno1")
        tfno2 = request.form.getlist("tfno2")
        email = request.form.getlist("email")

        clients_to_edit = Cliente(cif, direccion, poblacion, cp, provincia, parroquia_razon, diocesis, arciprestazgo, web,
                                responsable, cargo, dni, tfno1, tfno2, email, fecha_alta, _id)
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
        cif = request.form.getlist("cif")
        direccion = request.form.getlist("direccion")
        poblacion = request.form.getlist("poblacion")
        cp = request.form.getlist("cp")
        provincia = request.form.getlist("provincia")
        parroquia_razon = request.form.getlist("parroquia_razon")
        diocesis = request.form.getlist("diocesis")
        arciprestazgo = request.form.getlist("arciprestazgo")
        web = request.form.getlist("web")
        responsable = request.form.getlist("responsable")
        cargo = request.form.getlist("cargo")
        dni = request.form.getlist("dni")
        tfno1 = request.form.getlist("tfno1")
        tfno2 = request.form.getlist("tfno2")
        email = request.form.getlist("email")

        clients_to_edit = Cliente(cif, direccion, poblacion, cp, provincia, parroquia_razon, diocesis, arciprestazgo, web,
                                responsable, cargo, dni, tfno1, tfno2, email, fecha_alta, _id)
        clients_to_edit.remove_client()

        return render_template("home.html", resultado="Los datos han sido borrados")
    elif request.method == "GET" and session["email"] is not None:
        return render_template("home.html")
    else:
        return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=app.config['DEBUG'], port=4990)
