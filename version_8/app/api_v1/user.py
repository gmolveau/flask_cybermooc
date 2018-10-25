# app/api_v1/user.py

from flask import (
    jsonify, request
)
from . import api_v1_blueprint
from .decorators import login_required, roles_required
from ..bcrypt import bc
from ..database import db
from ..jwt import generate_jwt
from ..models.token import Token
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
    current_user = User.query.filter(User.username == username).first()
    if current_user is not None:
        if current_user.verify_password(password):
            claims = {'user_id' : current_user.id}
            jwt = generate_jwt(claims)
            token = Token()
            token.hash = jwt
            token.description = "could be location or something idk from request"
            token.user_id = current_user.id
            db.session.add(token)
            db.session.commit()
            return jsonify(token=jwt),200
        return jsonify(err="password incorrect"), 401
    return jsonify(err="username incorrect"), 404


@api_v1_blueprint.route('/logout', methods=['POST'])
@login_required
def logout(current_user):
    for user_token in current_user.tokens:
        if user_token.hash == request.headers['Authorization']:
            db.session.delete(user_token)
            db.session.commit()
            return jsonify(msg="logged out"), 200
    return jsonify(msg="logged out"), 200