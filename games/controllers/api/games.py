from flask_restful import Resource, reqparse
from games.models import db, Game
from flask import jsonify, abort, json


class GamesAPI(Resource):
    def get(self, game_id=None):
        if game_id:
            # parser = reqparse.RequestParser()
            # parser.add_argument('id', required=False, type=int, location='args')
            # args = parser.parse_args(strict=True)
            # game_id = args.get('id')
            # if game_id is not None:
            #     Game.query.get(game_id)

            return jsonify(Game.query.get_or_404(game_id).to_json())
        else:
            return jsonify([game.to_json() for game in Game.query.all()])


    def post(self, game_id=None):
        if game_id:
            abort(400)
        else:
            # abort_if_no_admin_auth(token) // extract token from url

            new_game = Game()
            db.session.add(new_game)
            db.session.commit()

            return {"result" : new_game.id}, 201


    def put(self, game_id=None):
        if not game_id:
            abort(400)
        else:
            # abort_if_no_admin_auth(token)

            game = Game.query.get_or_404(game_id)
            db.session.commit()

            return {"result" : game.id}, 201


    def delete(self, game_id=None):
        if not game_id:
            abort(400)
        else:
            # abort_if_no_admin_auth(token)

            game = Game.query.get_or_404(game_id)
            db.session.delete(game)
            db.session.commit()

            return "", 204
