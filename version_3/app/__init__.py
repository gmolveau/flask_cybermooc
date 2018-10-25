# app/__init__.py
# application factory

from flask import Flask

def create_app():
    app = Flask(__name__)

    from os import environ as env
    app.config['SQLALCHEMY_DATABASE_URI'] = env.get('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from .database import db
    db.init_app(app)

    from .cli import cli_init_app
    cli_init_app(app)

    from .api_v1 import root_blueprint
    app.register_blueprint(root_blueprint)

    return app
