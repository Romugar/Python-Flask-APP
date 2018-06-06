from flask import session, render_template
from src.common.database import Database
from passlib.hash import pbkdf2_sha512

__author__ = "Roberto Munoz Garcia"


class User(object):
    def __init__(self, email, password):
        self.email = email
        self.password = password


    @staticmethod
    def login_valid(email, password):
        # validar usuario y contraseña
        user = Database.find_one("users", {"email": email})
        if user is not None:
            # Compara la contraseña
            return pbkdf2_sha512.verify(password, user["password"])
        else:
            return False

