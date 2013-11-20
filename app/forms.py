from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, ValidationError
from wtforms.validators import Required, Email, EqualTo
from models import User

def non_duplicate_email(form, field):
    sameEmails = User.query.filter_by(email = field.data)
    if sameEmails.count() > 0:
        raise ValidationError("Duplicate email detected")

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

