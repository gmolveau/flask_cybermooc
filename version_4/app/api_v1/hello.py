# app/api_v1/hello.py

from . import root_blueprint

@root_blueprint.route('/', methods=['GET'])
def hello_world():
    return 'Hello, World!'
