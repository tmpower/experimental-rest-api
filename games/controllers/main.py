from flask import render_template, Blueprint, request, abort
from games.models import Game, User, Category, Developer
from games import db


main_blueprint = Blueprint(
    'main',
    __name__,
    template_folder='../templates'
)


@main_blueprint.route("/put_games")
def put_games():
    category1 = Category.query.get(1)
    category2 = Category.query.get(2)

    new_game = Game("FIFA19")
    new_game.categories.append(category1)
    new_game.categories.append(category2)
    db.session.add(new_game)

    new_game = Game("SubwayRunner")
    new_game.categories.append(category2)
    db.session.add(new_game)

    db.session.commit()

    return "Games Created!"

@main_blueprint.route("/get_games")
def get_games():
    games = Game.query.all()
    return render_template("index.html", games = games)

@main_blueprint.route("/put_categories")
def put_categories():
    new_category = Category("multiplayer")
    db.session.add(new_category)
    new_category = Category("arcade")
    db.session.add(new_category)
    db.session.commit()

    return "Categories Created!"

@main_blueprint.route("/get_categories")
def get_categories():
    categories = Game.query.get(5).categories
    return render_template("index.html", categories = categories)

@main_blueprint.route("/put_developers")
def put_developers():
    game5 = Game.query.get(2)

    new_developer = Developer("EA")
    new_developer.games.append(game5)

    db.session.add(new_developer)
    db.session.commit()

    return "Developers Created!"

@main_blueprint.route("/get_developers")
def get_developers():
    developers = Game.query.get(2).developer
    return render_template("index.html", developers = developers)
