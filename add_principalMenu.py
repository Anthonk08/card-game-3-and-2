#Menu de inicio.
import sys

from add_players import Players
class principalMenu:
    def __init__(self):
        print("\nCARD GAME 3 & 2 \nChoose An Option: \n1 -- START. \n2 -- HELP. \n3 -- CLOSE")    
        while True:
            num = input("ANSWER: ") 
            if num == "1":
                #Aqui debe iniciar el juego, llamando a la clase Players.
                Players()

            if num == "2":
                #Despues de leer debe regresar al principio del menu.
                print("\nCOMO JUGAR.\n1-Ingresa tu nombre.\n2-Ingresa tu apellido.\n3-Apareceran varias a opciones a elegir cada vez que sea su turno.\n4-Tendras la opcion de quedarte con una carta de la baraja y cambiarla por una de tu mano o descartar la carta de la baraja.\n5-En caso de que elijas cambiar la carta de la baraja, por una de la mano, aparecera tu mano:\n\t[7 Black Peak, 6 Black Peak, A Red Diamond, 2 Black Peak, 4 Black Peak]\n6-Debes elegir entre las 5 cartas que tienes, cual deseas cambiar, digitando un la posicion de una de las cartas del 1-5.\n7-Ganará aquel que tenga 2 cartas iguales de una y tres cartas iguales de otra.")
                
                print("\nA- Quieres regresar al menu? \nB- Cerrar el juego?")
                while True:
                    num2 = input("ANSWER: ")
                    if num2 == "A":
                        principalMenu()
                    if num2 == "B":
                        print("The game will close, wait a moment, please.")
                        sys.exit()
                    else:
                        print("Ha digitado un caracter incorrecto.\nElija una opcion del A OR B.")
            if num == "3":
                #Solo presenta el mensaje de que el juego esta cerrando y se cierra.
                print("The game will close, wait a moment, please.")
                sys.exit()

            else:
                print("Error, a digitado un numero incorrecto.\nElija una opcion del 1-3.")

principalMenu()