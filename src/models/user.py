import uuid
from flask import session
from src.common.database import Database

__author__ = "Roberto Munoz Garcia"


class User(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id


    @classmethod
    def get_by_email(cls, email):
        data = Database.find_one("users", {"email": email})
        if data is not None:
            return cls(**data)


    @staticmethod
    def login_valid(email, password):
        # validar usuario y contraseña
        user = User.get_by_email(email)
        if user is not None:
            # Compara la contraseña
            return user.password == password
        return False


    @staticmethod
    def login(user_email):
        # Login_valid ha sido llamado
        session["email"] = user_email
