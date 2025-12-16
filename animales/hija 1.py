from animales import Animal

class Caballo(Animal):
    def _init_(self, nombre, edad, habitat, color):
        Animal._init_(self, nombre, edad, habitat)
        self.color = color

    def mostrar(self):
        Animal.mostrar(self)
        print("Color:", self.color)