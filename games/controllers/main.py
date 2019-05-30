from flask import render_template, Blueprint
# from games.models import db, Game


main_blueprint = Blueprint(
    'main',
    __name__,
    template_folder='../templates'
)


@main_blueprint.route("/")
def home():
    # games = Game.query.all()
    return render_template("index.html")
