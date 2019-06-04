from games import db


class Game(db.Model):
    __tablename__ = "game"
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String())

    developer_id = db.Column(db.Integer(), db.ForeignKey('developer.id'))

    category = db.Column(db.String())


    def __init__(self, title, category):
        self.title = title
        self.category = category

    def to_json(self):
        json_post = {
            'title': self.title,
            'category': self.category
        }
        return json_post


class Category(db.Model):
    __tablename__ = "category"
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String())
    category = db.Column(db.String())

    def __init__(self, title, game):
        self.title = title
        self.game = game

    def to_json(self):
        json_post = {
            'title': self.title,
            'game': self.game
        }
        return json_post


class Developer(db.Model):
    __tablename__ = "developer"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())

    games = db.relationship('Game', backref='developer', lazy='dynamic')

    def __init__(self, title, game):
        self.name = title

    def to_json(self):
        json_post = {
            'name': self.name,
            # 'game': self.game
        }
        return json_post
