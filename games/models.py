from games import db


class Game(db.Model):
    __tablename__ = "game"
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String())
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
