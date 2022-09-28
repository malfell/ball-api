# import flask
from flask import Flask

# APPLICATION FACTORY
def create_app():
    # new app instance of Flask
    app = Flask(__name__)

    # SQL Alchemy stuff
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/ball'
    # set modifications on app's config object to false
    # if True, it tracks modifications of objects--feature isn't needed
    # if left unset, the value defaults to None, which takes extra memory--BAD
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # model import
    from . import models
    models.db.init_app(app)

    # index route
    @app.route('/')
    def hello():
        return 'Hello, Ball!'
    
    # return
    return app