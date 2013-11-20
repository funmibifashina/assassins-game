from flask import render_template, redirect, session, request, url_for, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm
from models import User
from forms import RegisterForm, LoginForm

@app.before_request
def before_request():
    g.user = current_user

@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    return render_template("titleAndMsg.html", title = "Home",
            message = "Welcome to the Home page")

@app.route("/login", methods = ["GET", "POST"])
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(nickname = form.username.data).first()
        if user is not None and form.password.data == user.password:
            login_user(user)
            return redirect(url_for("index"))
    return render_template("login.html", title = "Login", form = form)

@app.route("/register", methods = ["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        newUser = User(nickname = form.username.data,
                password = form.password.data,
                email = form.email.data)
        db.session.add(newUser)
        db.session.commit()
        # TODO: Catch sqlalchemy.exc.IntegrityError when non-unique email
        return redirect(url_for("thanks"))
    return render_template("register.html", title = "Register", form = form)

@app.route("/thanks")
def thanks():
    return render_template("titleAndMsg.html", title = "Thanks!",
            message = ("Thanks for registering! You should get an email to" +
            " confirm or something like that."))

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/users")
@login_required
def users():
    return render_template("viewUsers.html", title = "View users",
            users = User.query.all())

# used by Flask-Login
@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

