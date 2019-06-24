from flask_restful import Resource, reqparse
from games.models import User
from flask import jsonify, abort


#pwd: password
#token: eyJhbGciOiJIUzUxMiIsImlhdCI6MTU2MTIwMTY4OCwiZXhwIjoxNTYxMjAyMjg4fQ.eyJpZCI6MX0.asgQCSGrWJb64ULtAoEYQmM_-lyjIWdYGWcM_mY4bg-4v7bcxp9TCagI9hzzGh5P74IJBFrRJhP__Ox2bGNamA
class TokenAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', type=str, required=True, help='No username provided', location='json')
        self.reqparse.add_argument('password', type=str, required=True, help='No password provided', location='json')
        super(TokenAPI, self).__init__()
    
    def post(self):
        args = self.reqparse.parse_args(strict=True)

        username = args['username']
        password = args['password']

        user = User.query.filter_by(username = username).first()
        if not user or not user.verify_password(password):
            abort(401)

        token = user.generate_auth_token()
        return jsonify( {"token" : token.decode("ascii")} )
