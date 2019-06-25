from flask_restful import Resource, reqparse, marshal_with, fields
from games.models import db, Category
from flask import jsonify, abort
from games.utils import abort_if_no_auth


category_fields = {
    'name': fields.String,
    'uri': fields.Url('category_v1')
    # 'games': fields.List(fields.Nested(game_fields)),
}


class CategoriesAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str, required=True, help='No category title provided', location='json')
        self.reqparse.add_argument('game_id', type=int, default=1, location='json')
        self.reqparse.add_argument('token', type=str, location='json')
        super(CategoriesAPI, self).__init__()

    @marshal_with(category_fields)
    def get(self):
        return Category.query.all()

    def post(self):
        args = self.reqparse.parse_args(strict=True)
        abort_if_no_auth(args['token'])

        new_category = Category(args['name'])
        db.session.add(new_category)
        db.session.commit()

        return {"result" : new_category.id}, 201


class CategoryAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str, location='json')
        self.reqparse.add_argument('token', type=str, location='json')
        super(CategoryAPI, self).__init__()

    @marshal_with(category_fields)
    def get(self, id):
        return Category.query.get_or_404(id)

    def put(self, id):
        args = self.reqparse.parse_args(strict=True)
        abort_if_no_auth(args['token'])

        category = Category.query.get_or_404(id)
        if args['name']:
            category.name = args['name']
        db.session.commit()

        return {"result" : category.id}, 201

    def delete(self, id):
        args = self.reqparse.parse_args(strict=True)
        abort_if_no_auth(args['token'])

        category = Category.query.get_or_404(id)
        db.session.delete(category)
        db.session.commit()

        return "", 204
