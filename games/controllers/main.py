from flask import render_template, Blueprint
from games.models import Game
from games import db


main_blueprint = Blueprint(
    'main',
    __name__,
    template_folder='../templates'
)


@main_blueprint.route("/")
def home():
    new_game = Game("LOL", "arcade")
    db.session.add(new_game)
    new_game = Game("AoE", "battle")
    db.session.add(new_game)
    new_game = Game("PES", "sports")
    db.session.add(new_game)
    db.session.commit()

    return "Created!"

@main_blueprint.route("/gets")
def dbget():
    games = Game.query.all()
    return render_template("index.html", games = games)
