from animales import Animal

class Escarabajo(Animal):
    def _init_(self, nombre, edad, habitat, vuela):
        Animal._init_(self, nombre, edad, habitat)
        self.vuela = vuela

    def mostrar(self):
        Animal.mostrar(self)
        print("Vuela:", self.vuela)