from flask_restful import Resource, reqparse, fields, marshal_with
from games.models import db, User
from flask import jsonify, abort


user_fields = {
    'username': fields.String,
    'uri': fields.Url('user')
}

class UsersAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', type=str, required=True, help='No username provided', location='json')
        self.reqparse.add_argument('password', type=str, required=True, help='No password provided', location='json')
        super(UsersAPI, self).__init__()

    @marshal_with(user_fields)
    def get(self):
        return User.query.all()

    def post(self):
        # abort_if_no_admin_auth(token) // extract token from url
        args = self.reqparse.parse_args(strict=True)
        if User.query.filter_by(username = args['username']).first() is not None:
            abort(400) # username exists
        new_user = User( username = args['username'] )
        new_user.hash_password( args['password'] )
        db.session.add(new_user)
        db.session.commit()

        return {"result" : new_user.id}, 201


class UserAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', type=str, location='json')
        self.reqparse.add_argument('password', type=str, location='json')
        super(UserAPI, self).__init__()

    @marshal_with(user_fields)
    def get(self, id):
        return User.query.get_or_404(id)

    def put(self, id):
        # abort_if_no_admin_auth(token)
        args = self.reqparse.parse_args(strict=True)
        user = User.query.get_or_404(id)
        if args['username']:
            user.username = args['username']
        if args['password']:
            user.hash_password( str(args['password']) )
        db.session.commit()

        return {"result" : user.id}, 201

    def delete(self, id):
        # abort_if_no_admin_auth(token)
        user = User.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()

        return "", 204
