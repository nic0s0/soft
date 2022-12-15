from os import system
from cliente.activar import activar
from cliente.consultar_atraso import consultar_atraso
from cliente.consultar_sus import consultar_sus
from cliente.devolver import devolver
from cliente.pedir import pedir

def main():
    system("clear")
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
                print("Ha seleccionado: 1. Activar cuenta")
                x = activar()
                system('clear')
            elif opcion == 2:
                print("Ha seleccionado: 2. Consultar atraso de libro")
                x, y = consultar_atraso()
                system('clear')
            if opcion == 3:
                print("Ha seleccionado: 3. Consultar estado de suscripcion")
                x = consultar_sus()
                system('clear')
            if opcion == 4:
                print("Ha seleccionado: 4. Devolver un libro")
                x = devolver()
                system('clear')
            if opcion == 5:
                print("Ha seleccionado: 5. Pedir un libro")
                x = pedir()
                system('clear')            
            elif opcion == 6:
                print("Saliendo")
                system('clear')
                return
            else:
                print("Opcion invalida")
        except:
            print("Opcion invalida")

main()