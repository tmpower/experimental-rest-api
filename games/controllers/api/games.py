from flask_restful import Resource
from games.models import db, Game
from flask import jsonify, abort


class GamesAPI(Resource):
    def get(self, game_id=None):
        if game_id:
            return jsonify(Game.query.get_or_404(game_id).to_dict())
        else:
            return jsonify(Game.query.all())


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
