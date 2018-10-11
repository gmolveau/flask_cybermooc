# __init__.py

from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from os import environ as env
    app.config['SQLALCHEMY_DATABASE_URI'] = env.get('DATABASE_URL')

    from .database import db
    db.init_app(app)

    from .bcrypt import bc
    bc.init_app(app)

    from .cli import cli_init_app
    cli_init_app(app)

    from .api_v1 import api_v1_blueprint
    app.register_blueprint(api_v1_blueprint)

    return app