from games import db
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired
from flask import current_app


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

    def __init__(self, title, developer_id = 1, categories = []):
        self.title = title


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

    def __init__(self, name, games = []):
        self.name = name


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(32), index = True)
    password_hash = (db.String(64))

    ## password handling
    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    ## token handling
    def generate_auth_token(self, expiration = 600):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in = expiration)
        return s.dumps( {"id": self.id} )

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None # valid token, but expired
        except BadSignature:
            return None # invalid token
        
        user = User.query.get(data['id'])
        return user
    