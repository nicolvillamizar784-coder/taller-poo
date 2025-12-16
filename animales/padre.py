# padre.py
class Animal:
    def _init_(self, nombre, edad, habitat):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat

    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Hábitat:", self.habitat)