from flask import render_template
from app import app
from forms import RegisterForm

@app.route("/")
def index():
    return render_template("index.html", title = "Title", message = "Message")

@app.route("/register", methods = ["GET", "POST"])
def register():
    form = RegisterForm()
    return render_template("register.html", title = "Register", form = form)

