# app/api_v1/user.py

from flask import (
    jsonify, request
)
from . import api_v1_blueprint
from ..database import db
from ..models.user import User


@api_v1_blueprint.route('/signup', methods=['POST'])
def signup():
    datas = request.get_json()
    username = datas.get('username','')
    if username is '':
        return jsonify(error="username is empty"),422
    email = datas.get('email','')
    if email is '':
        return jsonify(error="email is empty"),422
    # we could verify that this email is valid
    password = datas.get('password','')
    if password is '':
        return jsonify(error="password is empty"),422
    if User.query.filter(User.username == username).first() is not None:
        return jsonify(err="username already taken"), 409
    if User.query.filter(User.email == email).first() is not None:
        return jsonify(err="email already signed-up"), 409
    new_user = User()
    new_user.username = username
    new_user.email = email
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify(msg="welcome :-)"), 200


@api_v1_blueprint.route('/login', methods=['POST'])
def login():
    datas = request.get_json()
    username = datas.get('username','')
    if username is '':
        return jsonify(error="username is empty"),422
    password = datas.get('password','')
    if password is '':
        return jsonify(error="password is empty"),422
    user = User.query.filter(User.username == username).first()
    if user is not None:
        if user.verify_password(password):
            return jsonify(msg="welcome"), 200
        return jsonify(err="password incorrect"), 401
    return jsonify(err="username incorrect"), 404
