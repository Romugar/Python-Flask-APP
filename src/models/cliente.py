import uuid
from src.common.database import Database

__author__ = "Roberto Munoz Garcia"

class Cliente(object):

    def __init__(self, cif, direccion, poblacion, cp, provincia, diocesis, arciprestazgo, parroquia, razon, web, responsable, cargo, dni, tfno1, tfno2, email, _id=None):
        self.cif = cif
        self.direccion = direccion
        self.poblacion = poblacion
        self.cp = cp
        self.provincia = provincia
        self.diocesis = diocesis
        self.arciprestazgo = arciprestazgo
        self.parroquia = parroquia
        self.razon = razon
        self.web = web
        self.responsable = responsable
        self.cargo = cargo
        self.dni = dni
        self.tfno1 = tfno1
        self.tfno2 = tfno2
        self.email = email
        self._id = uuid.uuid4().hex if _id is None else _id

    def save_to_mongo(self):
        Database.insert(collection="clientes", data=self.json())

    def json(self):
        return {
            "_id": self._id,
            "cif": self.cif,
            "direccion": self.direccion,
            "poblacion": self.poblacion,
            "cp": self.cp,
            "provincia": self.provincia,
            "diocesis": self.diocesis,
            "arciprestazgo": self.arciprestazgo,
            "parroquia": self.parroquia,
            "razon": self.razon,
            "web": self.web,
            "responsable": self.responsable,
            "cargo": self.cargo,
            "dni": self.dni,
            "tfno1": self.tfno1,
            "tfno2": self.tfno2,
            "email": self.email,
        }