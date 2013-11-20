import secrets_s
import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "app.db")

CSRF_ENABLED = True
SECRET_KEY = secrets_s.SECRET_WTFORMS_KEY

