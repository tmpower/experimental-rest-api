from flask_restful import Api

rest_api = Api()

from games.controllers.api.games import GameAPI, GamesAPI
rest_api.add_resource( GameAPI, '/api/games/<int:game_id>', endpoint = 'game')
rest_api.add_resource( GamesAPI, '/api/games', endpoint = 'games')

from games.controllers.api.categories import CategoriesAPI
rest_api.add_resource( CategoriesAPI, '/api/categories', '/api/categories/<int:category_id>' )
