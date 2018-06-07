
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