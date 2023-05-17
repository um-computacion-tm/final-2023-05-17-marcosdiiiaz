from dispositivo import Dispositivo


class Database:
    def __init__(self, database_template):
        dispositivos = database_template.get("dispositivos")
        self.database = [Dispositivo(diccionario=dispositivo) for dispositivo in dispositivos]

    def delete_by_id(self, id):
        self.database = [dispositivo for dispositivo in self.database if dispositivo.id != id]

    def add_dispositivo(self, dispositivo=None, diccionario=None):
        if dispositivo:
            self.database.append(dispositivo)
        elif diccionario:
            self.database.append(Dispositivo(diccionario=diccionario))