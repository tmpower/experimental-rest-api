from flask_restful import Api

rest_api = Api()

# API Version 1.0
from games.controllers.api.v1.categories import CategoryAPI, CategoriesAPI
rest_api.add_resource( CategoryAPI, '/api/v1.0/categories/<int:id>', endpoint = 'category_v1' )
rest_api.add_resource( CategoriesAPI, '/api/v1.0/categories', endpoint = 'categories_v1' )

from games.controllers.api.v1.games import GameAPI, GamesAPI
rest_api.add_resource( GameAPI, '/api/v1.0/games/<int:id>', endpoint = 'game_v1')
rest_api.add_resource( GamesAPI, '/api/v1.0/games', endpoint = 'games_v1')

from games.controllers.api.v1.users import UserAPI, UsersAPI
rest_api.add_resource( UserAPI, '/api/v1.0/users/<int:id>', endpoint = 'user_v1')
rest_api.add_resource( UsersAPI, '/api/v1.0/users', endpoint = 'users_v1')

from games.controllers.api.v1.auth import TokenAPI
rest_api.add_resource( TokenAPI, '/api/v1.0/auth/token', endpoint = 'token_v1')

# API Version 2.0
from games.controllers.api.v2.categories import CategoryAPI, CategoriesAPI
rest_api.add_resource( CategoryAPI, '/api/v2.0/categories/<int:id>', endpoint = 'category_v2' )
rest_api.add_resource( CategoriesAPI, '/api/v2.0/categories', endpoint = 'categories_v2' )

from games.controllers.api.v2.games import GameAPI, GamesAPI
rest_api.add_resource( GameAPI, '/api/v2.0/games/<int:id>', endpoint = 'game_v2')
rest_api.add_resource( GamesAPI, '/api/v2.0/games', endpoint = 'games_v2')

from games.controllers.api.v2.users import UserAPI, UsersAPI
rest_api.add_resource( UserAPI, '/api/v2.0/users/<int:id>', endpoint = 'user_v2')
rest_api.add_resource( UsersAPI, '/api/v2.0/users', endpoint = 'users_v2')

from games.controllers.api.v2.auth import TokenAPI
rest_api.add_resource( TokenAPI, '/api/v2.0/auth/token', endpoint = 'token_v2')
