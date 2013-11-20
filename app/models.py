import datetime
from app import db

class User(db.Model):
    id_ = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(32), index = True, unique = True)
    email = db.Column(db.String(128), index = True, unique = True)
    emailConfirmed = db.Column(db.Boolean(), default = False)
    dateTimeCreated = db.Column(db.DateTime(), default = datetime.datetime.now())
    # Yes, this is bad
    password = db.Column(db.String(128))

    # these next 4 are required by Flask-Login
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id_)

    def __repr__(self):
        return "<User %r>" % (self.nickname)

