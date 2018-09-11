import uuid
from src.common.database import Database
import time

__author__ = "Roberto Munoz Garcia"

class Cliente(object):

    def __init__(self, campo1, campo2, campo3, campo4, campo5, campo6, campo7, campo8, campo9, campo10, campo11, campo12, campo13, campo14, campo15, fecha_alta=time.strftime("%d/%m/%Y"),_id=None):
        self._id = uuid.uuid4().hex if _id is None else _id
        self.fecha_alta = fecha_alta
        self.campo1 = campo1
        self.campo2 = campo2
        self.campo3 = campo3
        self.campo4 = campo4
        self.campo5 = campo5
        self.campo6 = campo6
        self.campo7 = campo7
        self.campo8 = campo8
        self.campo9 = campo9
        self.campo10 = campo10
        self.campo11 = campo11
        self.campo12 = campo12
        self.campo13 = campo13
        self.campo14 = campo14
        self.campo15 = campo15

    def save_to_mongo(self):
        Database.insert(collection="clientes", data=self.json())

    def json(self):
        return {
            "_id": self._id,
            "fecha_alta": self.fecha_alta,
            "campo1": self.campo1,
            "campo2": self.campo2,
            "campo3": self.campo3,
            "campo4": self.campo4,
            "campo5": self.campo5,
            "campo6": self.campo6,
            "campo7": self.campo7,
            "campo8": self.campo8,
            "campo9": self.campo9,
            "campo10": self.campo10,
            "campo11": self.campo11,
            "campo12": self.campo12,
            "campo13": self.campo13,
            "campo14": self.campo14,
            "campo15": self.campo15,
        }

    def find_clients(self):
        json = self.json()
        filtrado = {key: value for key, value in json.items() if value != '' and key != "_id" and key !="fecha_alta"}
        return [client for client in Database.find(collection="clientes", query=filtrado)]

    def update_clients(self):
        json = self.json()
        for i in range(len(json["_id"])):
            id = {key: value[i] for key, value in json.items() if key == "_id"}
            filtrado = {key: value[i] for key, value in json.items() if key != "_id" and key != "fecha_alta"}
            query = {'$set': filtrado}
            Database.update(collection="clientes", id=id, query=query)

    def remove_client(self):
        json = self.json()
        for i in range(len(json["_id"])):
            id = {key: value[i] for key, value in json.items() if key == "_id"}
            Database.remove(collection="clientes", query=id)
