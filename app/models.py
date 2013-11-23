import datetime
from app import db
from sqlalchemy import Table, Text, MetaData
from sqlalchemy.orm import backref

# association table to tell which Users are in which Games
game_players = Table("game_players", db.metadata,
        db.Column("game_id", db.Integer, db.ForeignKey("games.id_")),
        db.Column("user_id", db.Integer, db.ForeignKey("users.id_"))
    )

# states for a Game
GAME_NOT_STARTED = 0
GAME_ACTIVE = 1
GAME_ENDED = 2

class Game(db.Model):
    __tablename__ = "games"

    id_ = db.Column(db.Integer, primary_key = True)
    state = db.Column(db.Integer, default = GAME_NOT_STARTED)
    title = db.Column(db.String(32))

    # many to many Game <-> User
    users = db.relationship("User", secondary = game_players, backref = "games")

    def __repr__(self):
        return "<Game #%r '%r'>" % (id_, title)

class User(db.Model):
    __tablename__ = "users"

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

