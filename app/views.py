from flask import render_template, redirect
from app import app
from forms import RegisterForm

@app.route("/")
@app.route("/home")
def index():
    return render_template("titleAndMsg.html", title = "Home",
            message = "Welcome to the Home page")

@app.route("/register", methods = ["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect("/thanks")
    return render_template("register.html", title = "Register", form = form)

@app.route("/thanks")
def thanks():
    return render_template("titleAndMsg.html", title = "Thanks!",
            message = ("Thanks for registering! You should get an email to" +
            "confirm or something like that."))

