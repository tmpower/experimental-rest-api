from flask_restful import Api

rest_api = Api()

# API Version 1.0
from games.controllers.api.v1.categories import CategoryAPI, CategoriesAPI
rest_api.add_resource( CategoryAPI, '/api/v1.0/categories/<int:id>', endpoint = 'category' )
rest_api.add_resource( CategoriesAPI, '/api/v1.0/categories', endpoint = 'categories' )

from games.controllers.api.v1.games import GameAPI, GamesAPI
rest_api.add_resource( GameAPI, '/api/v1.0/games/<int:id>', endpoint = 'game')
rest_api.add_resource( GamesAPI, '/api/v1.0/games', endpoint = 'games')

from games.controllers.api.v1.users import UserAPI, UsersAPI
rest_api.add_resource( UserAPI, '/api/v1.0/users/<int:id>', endpoint = 'user')
rest_api.add_resource( UsersAPI, '/api/v1.0/users', endpoint = 'users')

from games.controllers.api.v1.auth import TokenAPI
rest_api.add_resource( TokenAPI, '/api/v1.0/auth/token', endpoint = 'token')

# API Version 2.0
from games.controllers.api.v2.categories import CategoryAPI, CategoriesAPI
rest_api.add_resource( CategoryAPI, '/api/v2.0/categories/<int:id>', endpoint = 'category' )
rest_api.add_resource( CategoriesAPI, '/api/v2.0/categories', endpoint = 'categories' )

from games.controllers.api.v2.games import GameAPI, GamesAPI
rest_api.add_resource( GameAPI, '/api/v2.0/games/<int:id>', endpoint = 'game')
rest_api.add_resource( GamesAPI, '/api/v2.0/games', endpoint = 'games')

from games.controllers.api.v2.users import UserAPI, UsersAPI
rest_api.add_resource( UserAPI, '/api/v2.0/users/<int:id>', endpoint = 'user')
rest_api.add_resource( UsersAPI, '/api/v2.0/users', endpoint = 'users')

from games.controllers.api.v2.auth import TokenAPI
rest_api.add_resource( TokenAPI, '/api/v2.0/auth/token', endpoint = 'token')
