class Dispositivo:
    def __init__(self, id=None, nombre=None, marca=None, tipo=None, diccionario=None):
        self.id, self.nombre, self.marca, self.tipo = id, nombre, marca, tipo

        if diccionario:
            self.id = diccionario.get("id", self.id)
            self.nombre = diccionario.get("nombre", self.nombre)
            self.marca = diccionario.get("marca", self.marca)
            self.tipo = diccionario.get("tipo", self.tipo)