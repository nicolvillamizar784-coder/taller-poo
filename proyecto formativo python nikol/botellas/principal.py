# principal.py
# Menú principal con CRUD

from botella_vidrio import BotellaVidrio
from botella_plastico import BotellaPlastico
from basedatos import BaseDatos

bd = BaseDatos()

while True:
    print(" MENÚ BOTELLAS ")
    print("1. Agregar botella de vidrio")
    print("2. Agregar botella de plástico")
    print("3. Listar botellas")
    print("4. Actualizar capacidad")
    print("5. Eliminar botella")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        capacidad = int(input("Capacidad (ml): "))
        forma = input("Forma: ")
        reutilizable = input("¿Es reutilizable? (Sí/No): ")
        botella = BotellaVidrio(capacidad, forma, reutilizable)
        bd.agregar(botella)

    elif opcion == "2":
        capacidad = int(input("Capacidad (ml): "))
        forma = input("Forma: ")
        reciclable = input("¿Es reciclable? (Sí/No): ")
        botella = BotellaPlastico(capacidad, forma, reciclable)
        bd.agregar(botella)

    elif opcion == "3":
        bd.listar()

    elif opcion == "4":
        bd.listar()
        index = int(input("Ingrese el índice: "))
        nueva_capacidad = int(input("Nueva capacidad (ml): "))
        bd.actualizar(index, nueva_capacidad)

    elif opcion == "5":
        bd.listar()
        index = int(input("Ingrese el índice a eliminar: "))
        bd.eliminar(index)

    elif opcion == "6":
        print("Programa finalizado.")
        break

    else:
        print("Opción inválida.")