from os import system
from cliente.activar import Activar
from cliente.consultar_atraso import Consultar_atraso
from cliente.consultar_sus import Consultar_sus
from cliente.devolver import Devolver
from cliente.pedir import Pedir

def main():
    while True:
        print("Elija una operacion:")
        print("1. Activar cuenta")
        print("2. Consultar atraso de libro")
        print("3. Consultar estado de suscripcion")
        print("4. Devolver un libro")
        print("5. Pedir un libro")
        print("6. Salir")
        try:
            opcion = int(input("Ingrese una opcion: ").strip())
            if opcion == 1:
                print("\nBienvenido a Activar cuenta\n")
                x = Activar()
                #system('cls')
            elif opcion == 2:
                print("\nBienvenido a Consultar atraso de libro\n")
                x = Consultar_atraso()
                #system('cls')
            elif opcion == 3:
                print("\nBienvenido a Consultar estado de suscripcion\n")
                x = Consultar_sus()
                #system('cls')
            elif opcion == 4:
                print("\nBienvenido a Devolver un libro\n")
                x = Devolver()
                #system('cls')
            elif opcion == 5:
                print("\nBienvenido a Pedir un libro\n")
                x = Pedir()
                #system('cls')
            elif opcion == 6:
                print("Saliendo")
                #system('cls')
                return
            else:
                print("Opcion invalida")
        except:
            print("Opcion no habilitada")

main()