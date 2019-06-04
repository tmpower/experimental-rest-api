from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config) # load cofigurations from config.py
    db.app = app
    db.init_app(app)

    ## import Blueprints here
    ## register your Blueprints here
    from games.controllers.main import main_blueprint
    app.register_blueprint(main_blueprint)

    ## import rest api here only once
    ## register your resp_api here
    from games.controllers.api import rest_api
    rest_api.init_app(app)

    return app
