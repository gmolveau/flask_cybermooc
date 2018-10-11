# api_v1/user.py

from flask import (
    jsonify, request
)
from . import api_v1_blueprint
from ..controllers.user import user_signup, user_login
from ..database import db

@api_v1_blueprint.route('/users/signup', methods=['POST'])
def signup():
    datas = request.get_json()
    username = datas.get('username','')
    if username is '':
        return jsonify(error="username is empty"),400
    # we could add some filters to our username
    email = datas.get('email','')
    if email is '':
        return jsonify(error="email is empty"),400
    # we could verify that this email is valid
    password = datas.get('password','')
    if password is '':
        return jsonify(error="password is empty"),400
    try:
        new_user = user_signup(username, email, password)
        return jsonify(msg="welcome :-)"),200
    except Exception as err:
        return jsonify(err=str(err)),401


@api_v1_blueprint.route('/users/login', methods=['POST'])
def login():
    datas = request.get_json()
    username = datas.get('username','')
    if username is '':
        return jsonify(error="username is empty"),400
    password = datas.get('password','')
    if password is '':
        return jsonify(error="password is empty"),400
    try:
        connected_user = user_login(username, password)
        return jsonify(msg="welcome :-)"),200
    except Exception as err:
        return jsonify(err=str(err)),401
