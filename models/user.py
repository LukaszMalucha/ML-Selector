import os
# import env
from models.confirmation import ConfirmationModel
from flask_login import UserMixin
from db import db


class UserModel(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80))  # can't be nullable=false for github oauth

    confirmation = db.relationship("ConfirmationModel",
                                   lazy="dynamic",  # allows attaching confirmation to the user created previously
                                   cascade="all, delete-orphan")

    @property
    def most_recent_confirmation(self):
        """get most recent confirmation that belongs to the user"""
        return self.confirmation.order_by(db.desc(ConfirmationModel.expire_at)).first()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
