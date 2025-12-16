from animales import Animal

class Pato(Animal):
    def _init_(self, nombre, edad, habitat, puede_nadar):
        Animal._init_(self, nombre, edad, habitat)
        self.puede_nadar = puede_nadar

    def mostrar(self):
        Animal.mostrar(self)
        print("Puede nadar:", self.puede_nada)