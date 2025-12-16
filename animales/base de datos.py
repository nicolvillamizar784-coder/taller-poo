# basedatos.py
class BaseDatos:
    def _init_(self):
        self.animales = []

    def agregar(self, animal):
        self.animales.append(animal)
        print("Animal agregado correctamente")

    def listar(self):
        for animal in self.animales:
            print("----------")
            animal.mostrar()

    def eliminar(self, nombre):
        for animal in self.animales:
            if animal.nombre == nombre:
                self.animales.remove(animal)
                print("Animal eliminado")