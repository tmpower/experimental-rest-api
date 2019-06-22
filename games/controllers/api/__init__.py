from flask_restful import Api

rest_api = Api()

from games.controllers.api.categories import CategoryAPI, CategoriesAPI
rest_api.add_resource( CategoryAPI, '/api/categories/<int:id>', endpoint = 'category' )
rest_api.add_resource( CategoriesAPI, '/api/categories', endpoint = 'categories' )

from games.controllers.api.games import GameAPI, GamesAPI
rest_api.add_resource( GameAPI, '/api/games/<int:id>', endpoint = 'game')
rest_api.add_resource( GamesAPI, '/api/games', endpoint = 'games')

from games.controllers.api.users import UserAPI, UsersAPI
rest_api.add_resource( UserAPI, '/api/users/<int:id>', endpoint = 'user')
rest_api.add_resource( UsersAPI, '/api/users', endpoint = 'users')

from games.controllers.api.auth import TokenAPI
rest_api.add_resource( TokenAPI, '/api/auth/token', endpoint = 'token')
