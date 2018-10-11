# api_v1/hello.py

from . import api_v1_blueprint
from .decorators import login_required


@api_v1_blueprint.route('/', methods=['GET'])
def hello_world():
    return 'Hello, World!'


@api_v1_blueprint.route('/need_login', methods=['GET'])
@login_required
def route_need_login(current_user):
    return "if you see this, that means your token is valid"
