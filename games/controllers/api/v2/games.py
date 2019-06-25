from flask_restful import Resource, reqparse, marshal_with, fields
from games.models import db, Game
from flask import jsonify, abort
from games.utils import abort_if_no_auth #, ratelimit
from games.controllers.api.v2.categories import category_fields


developer_fields = {
    'id': fields.Integer,
    'name': fields.String
}

game_fields = {
    'title': fields.String,
    'developer': fields.Nested(developer_fields),
    'categories': fields.List(fields.Nested(category_fields)),
    'uri': fields.Url('game_v2')
}


class GamesAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, required=True, help='No game title provided', location='json') #location='args'
        self.reqparse.add_argument('developer_id', type=int, default=1, location='json')
        self.reqparse.add_argument('category_id', type=int, default=1, location='json')
        self.reqparse.add_argument('token', type=str, location='json')
        super(GamesAPI, self).__init__()

    @marshal_with(game_fields) # will need to switch back to marshal
    def get(self):
        return Game.query.all()

    # @ratelimit(requests=100, window=60)
    def post(self):
        args = self.reqparse.parse_args(strict=True)
        abort_if_no_auth(args['token'])

        new_game = Game(args['title'])
        db.session.add(new_game)
        db.session.commit()

        return {"result" : new_game.id}, 201


class GameAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, location='json')
        self.reqparse.add_argument('developer_id', type=int, location='json')
        self.reqparse.add_argument('category_id', type=int, location='json')
        self.reqparse.add_argument('token', type=str, location='json')
        super(GameAPI, self).__init__()

    @marshal_with(game_fields)
    def get(self, id):
        return Game.query.get_or_404(id)

    def put(self, id):
        args = self.reqparse.parse_args(strict=True)
        abort_if_no_auth(args['token'])

        game = Game.query.get_or_404(id)
        game.developer_id = args['developer_id']
        db.session.commit()

        return {"result" : game.id}, 201

    def delete(self, id):
        args = self.reqparse.parse_args(strict=True)
        abort_if_no_auth(args['token'])

        game = Game.query.get_or_404(id)
        db.session.delete(game)
        db.session.commit()

        return "", 204
