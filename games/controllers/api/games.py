from flask_restful import Resource, reqparse, marshal, fields
from games.models import db, Game
from flask import jsonify, abort, json
from games.controllers.api.categories import category_fields


game_fields = {
    'title': fields.String,
    'developer': fields.String,
    'categories': fields.Nested(category_fields),
    'uri': fields.Url('game')
}


class GamesAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, required=True, help='No game title provided', location='json')
        self.reqparse.add_argument('developer_id', type=int, default=1, location='json')
        self.reqparse.add_argument('category_id', type=int, default=1, location='json')
        super(GamesAPI, self).__init__()

    def get(self):
        games = Game.query.all()
        return jsonify( [ marshal(game, game_fields) for game in games ] )

    def post(self):
        # abort_if_no_admin_auth(token) // extract token from url
        args = self.reqparse.parse_args(strict=True)
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
        super(GameAPI, self).__init__()

    def get(self, id):
        game = Game.query.get_or_404(id)
        return jsonify( marshal(game, game_fields) )

    def put(self, id):
        # abort_if_no_admin_auth(token)
        game = Game.query.get_or_404(id)
        # edit and update 'game' here..
        db.session.commit()

        return {"result" : game.id}, 201

    def delete(self, id):
        # abort_if_no_admin_auth(token)
        game = Game.query.get_or_404(id)
        db.session.delete(game)
        db.session.commit()

        return "", 204
