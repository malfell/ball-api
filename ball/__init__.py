# import flask
from flask import Flask

# APPLICATION FACTORY
def create_app():
    # new app instance of Flask
    app = Flask(__name__)

    # index route
    @app.route('/')
    def hello():
        return 'Hello, Ball!'
    
    # return
    return app