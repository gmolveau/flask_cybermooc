# controllers/user.py

from ..database import db
from ..models.user import User


def user_signup(username, email, password):
    if User.query.filter(User.username == username).first() is not None:
        raise Exception("username already taken")
    if User.query.filter(User.email == email).first() is not None:
        raise Exception("email already signed-up")
    new_user = User()
    new_user.username = username
    new_user.email = email
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    return new_user


def user_login(username, password):
    user = User.query.filter(User.username == username).first()
    if user is not None:
        if user.verify_password(password):
            return user
        raise Exception("password incorrect")
    raise Exception("username incorrect")
