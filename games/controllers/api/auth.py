from flask_restful import Resource, reqparse, marshal, fields
from games.models import db, User
from flask import jsonify, abort, json
from flask_httpauth import HTTPBasicAuth
from flask import g

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username_or_token, password):
    user = User.verify_auth_token(username_or_token)
    if not user:
        user = User.query.filter_by(username = username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True


class AuthAPI(Resource):
    def get(self):
        token = g.generate_auth_token
        return jsonify( {"token" : token.decode("ascii")} )


class LoginApi(Resource):
    def get(self):
        pass
    
    def put(self):
        pass
