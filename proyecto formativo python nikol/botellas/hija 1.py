# botella_vidrio.py
# Clase hija Botella de Vidrio

from botellas import Botella

class BotellaVidrio(Botella):
    def _init_(self, capacidad, forma, reutilizable):
        super()._init_(capacidad, forma)
        self.reutilizable = reutilizable

    def mostrar_info(self):
        print("Botella de Vidrio")
        super().mostrar_info()
        print("Reutilizable:", self.reutilizable)