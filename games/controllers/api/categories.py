from flask_restful import Resource, reqparse, marshal, fields
from games.models import db, Category
from flask import jsonify, abort, json
# from games.controllers.api.games import game_fields

category_fields = {
    'name': fields.String,
    # 'games': fields.List(fields.Nested(game_fields)),
    'uri': fields.Url('category')
}

class CategoriesAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str, required=True, help='No category title provided', location='json')
        self.reqparse.add_argument('game_id', type=int, default=1, location='json')
        super(CategoriesAPI, self).__init__()

    def get(self):
        categories = Category.query.all()
        return jsonify( [ marshal(category, category_fields) for category in categories ] )

    def post(self):
        # abort_if_no_admin_auth(token) // extract token from url
        args = self.reqparse.parse_args(strict=True)
        new_category = Category(args['name'])
        db.session.add(new_category)
        db.session.commit()

        return {"result" : new_category.id}, 201


class CategoryAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str, location='json')
        super(CategoryAPI, self).__init__()

    def get(self, id):
        category = Category.query.get_or_404(id)
        return jsonify( marshal(category, category_fields) )

    def put(self, id):
        # abort_if_no_admin_auth(token)
        category = Category.query.get_or_404(id)
        # edit and update 'game' here..
        db.session.commit()

        return {"result" : category.id}, 201

    def delete(self, id):
        # abort_if_no_admin_auth(token)
        category = Category.query.get_or_404(id)
        db.session.delete(category)
        db.session.commit()

        return "", 204
