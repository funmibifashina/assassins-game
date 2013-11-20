from app import db

class User(db.Model):
    id_ = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(32), index = True, unique = True)
    email = db.Column(db.String(128), index = True, unique = True)
    emailConfirmed = db.Column(db.Boolean())
    dateTimeCreated = db.Column(db.DateTime())
    # Yes, this is bad
    password = db.Column(db.String(128))

    def __repr__(self):
        return "<User %r>" % (self.nickname)

