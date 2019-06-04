class Config(object):
    SECRET_KEY = 'XMLZODSHE8N6NFOZDPZA2HULWSIYJU45K6N4ZO9M' # use your own

    ## DB config
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ## e-mail config
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'EMAIL_USER'
    MAIL_PASSWORD = 'EMAIL_PASS'


class DevConfig(Config):
    ## DB config (sqlite)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///restapi.db'

    DEBUG = True

class ProdConfig(Config):
    ## DB config (postgres)
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/restapi'

    DEBUG = False
