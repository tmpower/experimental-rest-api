from flask_restful import Api

rest_api = Api()

from games.controllers.api.games import GamesAPI
rest_api.add_resource(
    GamesAPI,
    '/api/games',
    '/api/games/<int:game_id>',
)

from games.controllers.api.categories import CategoriesAPI
rest_api.add_resource(
    CategoriesAPI,
    '/api/categories',
    '/api/categories/<int:category_id>',
)
