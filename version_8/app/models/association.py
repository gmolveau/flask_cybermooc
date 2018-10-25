# app/models/association.py
# http://docs.sqlalchemy.org/en/latest/orm/extensions/declarative/basic_use.html

from ..database import db

user_roles = db.Table('user_roles',
        db.Column('user_id', db.Integer, db.ForeignKey("users.id")),
        db.Column('role_id', db.Integer, db.ForeignKey("roles.id")))
