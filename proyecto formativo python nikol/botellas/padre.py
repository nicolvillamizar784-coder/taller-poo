# botella.py
# Clase padre Botella

class Botella:
#inicializador de la clase de la botella 
    def _init_(self, capacidad, forma):
#asigna la capacidad de la botella
        self.capacidad = capacidad
#asigna forma de la botella        
        self.forma = forma

    # Método  mostrar información 
    def mostrar_info(self):
        print("Capacidad:", self.capacidad, "ml")
        print("Forma:", self.forma)