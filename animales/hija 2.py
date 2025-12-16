from animales import Animal

class Cocodrilo(Animal):
    def _init_(self, nombre, edad, habitat, tamaño):
        Animal._init_(self, nombre, edad, habitat)
        self.tamaño = tamaño

    def mostrar(self):
        Animal.mostrar(self)
        print("Tamaño:", self.tamaño)