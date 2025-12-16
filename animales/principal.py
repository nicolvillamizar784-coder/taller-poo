from caballo import Caballo
from cocodrilo import Cocodrilo
from pez import Pez
from escarabajo import Escarabajo
from pato import Pato
from basedatos import BaseDatos

bd = BaseDatos()

while True:
    print("MENÚ ANIMALES ")
    print("1. Agregar Caballo")
    print("2. Agregar Cocodrilo")
    print("3. Agregar Pez")
    print("4. Agregar Escarabajo")
    print("5. Agregar Pato")
    print("6. Listar animales")
    print("7. Eliminar animal")
    print("8. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        edad = int(input("Edad: "))
        habitat = input("Hábitat: ")
        color = input("Color: ")
        obj = Caballo("Caballo", edad, habitat, color)
        bd.agregar(obj)

    elif opcion == "2":
        edad = int(input("Edad: "))
        habitat = input("Hábitat: ")
        tamanio = input("Tamaño: ")
        obj = Cocodrilo("Cocodrilo", edad, habitat, tamanio)
        bd.agregar(obj)

    elif opcion == "3":
        edad = int(input("Edad: "))
        habitat = input("Hábitat: ")
        tipo_agua = input("Tipo de agua (Dulce/Salada): ")
        obj = Pez("Pez", edad, habitat, tipo_agua)
        bd.agregar(obj)

    elif opcion == "4":
        edad = int(input("Edad: "))
        habitat = input("Hábitat: ")
        vuela = input("¿Vuela? (Sí/No): ")
        obj = Escarabajo("Escarabajo", edad, habitat, vuela)
        bd.agregar(obj)

    elif opcion == "5":
        edad = int(input("Edad: "))
        habitat = input("Hábitat: ")
        nada = input("¿Nada? (Sí/No): ")
        obj = Pato("Pato", edad, habitat, nada)
        bd.agregar(obj)

    elif opcion == "6":
        bd.listar()

    elif opcion == "7":
        nombre = input("Nombre del animal a eliminar: ")
        bd.eliminar(nombre)

    elif opcion == "8":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida")