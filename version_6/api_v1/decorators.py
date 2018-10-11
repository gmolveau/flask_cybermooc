# api_v1/decorators.py

from functools import wraps
from flask import (
    jsonify, request
)
from ..jwt import load_jwt
from ..models.user import User


def login_required(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        if 'Authorization' not in request.headers:
            return jsonify(err="no Authorization header found"),400
        try:
            jwt = request.headers['Authorization']
            claims = load_jwt(jwt)
        except Exception as err:
            return jsonify(err=str(err)),401
        if 'user_id' not in claims:
            return jsonify(err="token is not valid"),400
        current_user = User.query.get(claims['user_id'])
        if current_user is None:
            return jsonify(err="404 User not found"),400
        return fn(current_user=current_user, *args, **kwargs)
    return wrapped
