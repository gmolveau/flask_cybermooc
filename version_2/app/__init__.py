# app/__init__.py
# application factory

from flask import Flask

def create_app():
    app = Flask(__name__)

    from .api_v1 import root_blueprint
    app.register_blueprint(root_blueprint)

    return app
