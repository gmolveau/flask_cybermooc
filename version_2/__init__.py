# __init__.py

from flask import Flask

def create_app():
    app = Flask(__name__)

    from .api_v1 import api_v1_blueprint
    app.register_blueprint(api_v1_blueprint)

    return app
