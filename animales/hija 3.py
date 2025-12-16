from animales import Animal

class Pez(Animal):
    def _init_(self, nombre, edad, habitat, tipo_agua):
        Animal._init_(self, nombre, edad, habitat)
        self.tipo_agua = tipo_agua

    def mostrar(self):
        Animal.mostrar(self)
        print("Tipo de agua:", self.tipo_agua)