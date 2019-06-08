from flask import render_template, Blueprint, request, abort
from games.models import Game, User
from games import db


main_blueprint = Blueprint(
    'main',
    __name__,
    template_folder='../templates'
)


main_blueprint.rout('/users/<int:user_id>', methods = ['GET', 'PUT', 'POST', 'DELETE'])
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
