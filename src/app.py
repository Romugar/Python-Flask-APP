from flask import Flask, render_template

__author__ = "roberto munoz garcia"

app = Flask(__name__)
app.secret_key = "dnH0xA50QiPdFex9VnfzfORN9q6Z4eTs"

@app.route("/")
def login_template():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=app.config['DEBUG'], port=4990)
