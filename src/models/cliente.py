import uuid
from src.common.database import Database
import time

__author__ = "Roberto Munoz Garcia"

class Cliente(object):

    def __init__(self, cif, direccion, poblacion, cp, provincia, parroquia_razon, diocesis, arciprestazgo, web, responsable, cargo, dni, tfno1, tfno2, email, fecha_alta=time.strftime("%d/%m/%Y"),_id=None):
        self._id = uuid.uuid4().hex if _id is None else _id
        self.fecha_alta = fecha_alta
        self.cif = cif
        self.direccion = direccion
        self.poblacion = poblacion
        self.cp = cp
        self.provincia = provincia
        self.parroquia_razon = parroquia_razon
        self.diocesis = diocesis
        self.arciprestazgo = arciprestazgo
        self.web = web
        self.responsable = responsable
        self.cargo = cargo
        self.dni = dni
        self.tfno1 = tfno1
        self.tfno2 = tfno2
        self.email = email

    def save_to_mongo(self):
        Database.insert(collection="clientes", data=self.json())

    def json(self):
        return {
            "_id": self._id,
            "fecha_alta": self.fecha_alta,
            "cif": self.cif,
            "direccion": self.direccion,
            "poblacion": self.poblacion,
            "cp": self.cp,
            "provincia": self.provincia,
            "parroquia_razon": self.parroquia_razon,
            "diocesis": self.diocesis,
            "arciprestazgo": self.arciprestazgo,
            "web": self.web,
            "responsable": self.responsable,
            "cargo": self.cargo,
            "dni": self.dni,
            "tfno1": self.tfno1,
            "tfno2": self.tfno2,
            "email": self.email,
        }

    def find_clients(self):
        json = self.json()
        filtrado = {key: value for key, value in json.items() if value != '' and key != "_id" and key !="fecha_alta"}
        return filtrado
        # return [client for client in Database.find(collection="clientes", query=filtrado)]
