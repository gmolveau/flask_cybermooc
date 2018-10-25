# app/models/token.py

from .base import Base
from ..database import db

class Token(Base):

    __tablename__ = 'tokens'

    hash = db.Column(db.String, nullable=False, unique=True)
    description = db.Column(db.String)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.id'),
                        nullable=False)
