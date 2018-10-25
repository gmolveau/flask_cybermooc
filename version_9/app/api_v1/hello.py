# api_v1/hello.py

from . import root_blueprint
from .decorators import login_required, roles_required


@root_blueprint.route('/', methods=['GET'])
def hello_world():
    return 'Hello, World!'


@root_blueprint.route('/need_login', methods=['GET'])
@login_required
def route_need_login(current_user):
    return "if you see this, that means your token is valid"


@root_blueprint.route('/admin', methods=['GET'])
@login_required
@roles_required('admin')
def route_admin_only(current_user):
    return "if you see this, that means you are an admin"
