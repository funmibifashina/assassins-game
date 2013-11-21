from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, ValidationError
from wtforms.validators import Required, Optional, Email, EqualTo
from models import User

def non_duplicate_email(form, field):
    sameEmails = User.query.filter_by(email = field.data)
    if sameEmails.count() > 0:
        raise ValidationError("Duplicate email detected")

def actual_user(form, field):
    usersWithNick = User.query.filter_by(nickname = field.data)
    if usersWithNick.count() < 1:
        raise ValidationError("That's not a user")

class RegisterForm(Form):
    username = TextField("Username", validators = [Required()])
    password = PasswordField("Password", validators = [Required()])
    passwordAgain = PasswordField("Confirm password",
            validators = [Required(), EqualTo("password")])
    email = TextField("Email", validators = [Email(), non_duplicate_email])

class LoginForm(Form):
    username = TextField("Username", validators = [Required()])
    password = PasswordField("Password", validators = [Required()])

class MakeGameForm(Form):
    title = TextField("Title")

class EditGameForm(Form):
    title = TextField("Title", validators = [Optional()])
    userToAdd = TextField("User to add", validators = [Optional(), actual_user])

