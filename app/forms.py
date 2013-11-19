from flask.ext.wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import Required, Email, EqualTo

class RegisterForm(Form):
    username = TextField("Username", validators = [Required()])
    password = PasswordField("Password", validators = [Required()])
    passwordAgain = PasswordField("Confirm password",
            validators = [Required(), EqualTo("password")])
    email = TextField("Email", validators = [Email()])

