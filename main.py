from os import system
#from cliente.cerrar import Cerrar
from cliente.activar import Activar
from cliente.consultar_atraso import Consultar_atraso
from cliente.consultar_sus import Consultar_sus
from cliente.devolver import Devolver
from cliente.pedir import Pedir

def main():
    while True:
        print("Elija una operacion:")
        print("1. Activar cuenta")
        print("2. Consultar atraso de libro") #Listo
        print("3. Consultar estado de suscripcion") #Listo
        print("4. Devolver un libro")
        print("5. Pedir un libro")
        print("6. Salir")
        try:
            opcion = int(input("Ingrese una opcion: ").strip())
            if opcion == 1:
                print("Ha seleccionado: 1. Activar cuenta")
                x = Activar()
                #system('cls')
            elif opcion == 2:
                print("Ha seleccionado: 2. Consultar atraso de libro")
                x = Consultar_atraso()
                #system('cls')
            elif opcion == 3:
                print("Ha seleccionado: 3. Consultar estado de suscripcion")
                x = Consultar_sus()
                #system('cls')
            elif opcion == 4:
                print("Ha seleccionado: 4. Devolver un libro")
                x = Devolver()
                #system('cls')
            elif opcion == 5:
                print("Ha seleccionado: 5. Pedir un libro")
                x = Pedir()
                #system('cls')
            elif opcion == 6:
                print("Saliendo")
                #system('cls')
                return
            elif opcion == "cerrar":
                #x = cerrar()
                print("Opcion invalida")
        except:
            print("Opcion invalida")

main()