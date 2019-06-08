from games import db
from passlib.apps import custom_app_context as pwd_context


categories = db.Table(
    'game_categories',
    db.Column('game_id', db.Integer, db.ForeignKey('game.id')),
    db.Column('category_id', db.Integer, db.ForeignKey('category.id'))
)


class Game(db.Model):
    __tablename__ = "game"

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String())

    developer_id = db.Column(db.Integer(), db.ForeignKey('developer.id'))

    categories = db.relationship('Category', secondary=categories, backref=db.backref('games', lazy='dynamic'), lazy='dynamic')

    def __init__(self, title):
        self.title = title

    # def to_json(self):
    #     json_game = {
    #         'title': self.title,
    #         # 'developer_id': self.developer_id
    #     }
    #     return json_game


class Category(db.Model):
    __tablename__ = "category"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())

    def __init__(self, name):
        self.name = name


class Developer(db.Model):
    __tablename__ = "developer"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())

    games = db.relationship('Game', backref='developer', lazy='dynamic')

    def __init__(self, name):
        self.name = name


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(32), index = True)
    password_hash = (db.String(64))

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)