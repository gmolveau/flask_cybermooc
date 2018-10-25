# app/api_v1/__init__.py

from flask import Blueprint

root_blueprint =  Blueprint('root', __name__)

# Import any endpoints here to make them available
from . import hello