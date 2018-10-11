# api_v1/hello.py

from . import api_v1_blueprint

@api_v1_blueprint.route('/', methods=['GET'])
def hello_world():
    return 'Hello, World!'
