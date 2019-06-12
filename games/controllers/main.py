from flask import render_template, Blueprint, request, abort
from games.models import Game, User, Category
from games import db


main_blueprint = Blueprint(
    'main',
    __name__,
    template_folder='../templates'
)


@main_blueprint.route('/users/<int:user_id>', methods = ['GET', 'PUT', 'POST', 'DELETE'])
def users(user_id = None):
    if request.method == 'POST':
        if user_id is None:
            username = request.json.get('username')
            password = request.json.get('password')

            if username is None or password is None:
                abort(400) # empty fields
            if User.query.filter_by(username = username).first() is not None:
                abort(400) # existing username

            user = User(username = username)
            user.hash_password(password)
            db.session.add(user)
            db.session.commit()

            return {"username" : user.username}, 201


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
    categories = Category.query.all()
    return render_template("index.html", categories = categories)
