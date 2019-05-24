from flask_restful import Resource
from games.models import db, Category
from flask import jsonify, abort


class CategoriesAPI(Resource):
    def get(self, category_id=None):
        if category_id:
            return jsonify(Category.query.get_or_404(category_id).to_dict())
        else:
            return jsonify(Category.query.all())


    def post(self, category_id=None):
        if category_id:
            abort(400)
        else:
            new_category = Category()
            db.session.add(new_category)
            db.session.commit()

            return {"result" : new_category.id}, 201


    def put(self, category_id=None):
        if not category_id:
            abort(400)
        else:
            category = Category.query.get_or_404(category_id)
            db.session.commit()

            return {"result" : category.id}, 201


    def delete(self, category_id=None):
        if not category_id:
            abort(400)
        else:
            category = Category.query.get_or_404(category_id)
            db.session.delete(category)
            db.session.commit()

            return "", 204
