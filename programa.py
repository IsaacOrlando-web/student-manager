import sys
sys.path.append("funciones")

from funciones import *
def main():
    while True:
        print("1.Agregar nuevo estudiante")
        print("2.Mostrar toda la informacion")
        print("3.Salir")
        option = int(input("Ingrese una opción: "))

        if option == 1:
            name = input("Ingrese el Nombre del estudiante: ")
            notas = float(input("Ingrese el promedio: "))
            SaveStudent(name, notas)
            print("Guardado con exito")

if __name__ == "__main__":
    main()