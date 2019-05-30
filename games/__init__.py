from flask import Flask

# import Blueprints here
from games.controllers.main import main_blueprint

# import APIs here
from games.controllers.api import rest_api
from games.controllers.api.games import GamesAPI
# from games.controllers.api.categories import CategoriesAPI


def create_app():
    app = Flask(__name__)

    # register your APIs here
    rest_api.add_resource(
        GamesAPI,
        '/api/games',
        '/api/games/<int:game_id>',
    )

    # rest_api.add_resource(
    #     CategoriesAPI,
    #     '/api/categories',
    #     '/api/categories/<int:category_id>',
    # )

    rest_api.init_app(app)

    # register your Blueprints here
    app.register_blueprint(main_blueprint)
    
    return app
