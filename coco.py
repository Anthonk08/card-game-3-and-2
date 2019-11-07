import sys
import random 
import os
class Card:

    #Atributos de la clase card
    def __init__(self,value,color,symbol):
        self.value = value
        self.color = color
        self.symbol = symbol
  
    #Envia las cartas con su valor, color y su simbolo  
    def information(self):
        return f"{self.value} {self.color} {self.symbol}"   

class Deck:
    def __init__(self):
      self.cards = []
      self.discard_deck = []

    #Metodo encargado de llenar la baraja
    def fillDeck(self):
        card_list = []
        values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        symbols = [["Red","Heart"],["Red","Diamond"],["Black","Clover"],["Black","Peak"]]
        for s in symbols:
            for v in values:
                card_list.append(Card(v,s[0],s[1]) )
        random.shuffle(card_list)
        self.cards = card_list
        

    def sendCard(self):
        #Toma la ultima carta de la baraja.
        return self.cards.pop()

    def sendDiscard(self):
        #toma la ultima carta de baraja de descarte.
        return self.discard_deck.pop()

    def discardDeck(self,currentPlayer): #cree un parametro
        #Descartar de la
        return self.discard_deck.append(currentPlayer.discarHandCard())
    
    def showLastCard(self):
        #Muestra la ultima carta del mazo de descarte.
        return self.discard_deck[-1]

class Players:
    num_player = 1
    #Creacion de lista handCard y llamada del metodo player
    def __init__(self):
        self.handCard = []
        self.player()
        Players.num_player += 1

    #Llena la baraja de cada jugador 
    def fillHandCard(self, baraja):
        #Llama el objeto baraja 5 veces para llenar la mano
        for i in range(0,5):
            AddF = baraja.sendCard()
            self.handCard.append(AddF)
            
            
    # def discarHandCard(self):
    #     return self.handCard.pop()
    def discarHandCard(self):
        return self.handCard.pop()

    def addCard(self,cardToAdd):
        #Se encarga de agregar una carta a la mano de un jugador 
        # lastCard = cardToAdd.sendCard()
        self.handCard.append(cardToAdd)
        return cardToAdd.information()

    def showCards(self):
        #Llenado de un String con las 5 cartas para imprimir en los datos de cada jugador
        listCard = ""
        for card in self.handCard:
            listCard += card.information() + " "
        return (listCard)

    
    #Metodo para mostrar los datos de cada jugador
    def show(self):
        return f"        {self.player_num} \n--------- ⇥  {self.name} {self.lastName}  ⇤ ---------\n{self.showCards()}"

        #return '{} {} {}'.format(self.name,self.lastName,self.player_num)

    #Metodo que pide los datos de cada jugador
    def player(self):
        self.name = input("\nPlayer name: ")
        self.lastName = input("Player last name: ")
        self.player_num = f"Player #{Players.num_player}."
        #Esto es un ejemplo.
        # a = f"Diga su nombre, por favor :v{self.name}"

class Game:
    def __init__(self):
    
        cleanConsole()
        print("---"*32) #diseno
        self.player1 = Players()
        print("---"*32) #diseno
        cleanConsole()
        print("---"*32)
        self.player2 = Players()
        print("---"*32)
        print("---"*32)
        
        self.baraja = Deck()
        self.baraja.fillDeck()
        self.player1.fillHandCard(self.baraja)
        self.player2.fillHandCard(self.baraja)
        cleanConsole()
        print(self.player1.show())
        
        print("---"*32)
        self.cardToAdd = self.baraja.sendCard()
       
        print("Nueva Carta Agregada: ",self.player1.addCard(self.cardToAdd))
        
        self.turnOfPlayer = self.player1
        
        # self.turnOfPlayer = self.baraja
        
        self.turn()
        print("""
        
        """)
        self.choice() #agregado por rita.
        self.winner()
        
        #X(le falta algo)
        
        cleanConsole()

    #El metodo choise, se encarga de preguntar al jugador, que carta eligira: una de la baraja o una de la baraja de descarte.
    def choice(self):
        
        while True:
            # cleanConsole()
            print("∸∸∸∸∸∸" *20)
            print("\nElige una de las opciones: \n1 -- Deseas una carta de la baraja. \n2 -- Deseas una carta de la baraja de descarte.")
            print("\nCarta en la baraja de descarte: ", self.baraja.showLastCard().information())
            #Cambio de jugador, para los turnos.
            self.turnOfPlayer = self.player1 if self.turnOfPlayer == self.player2 else self.player2
            print(self.turnOfPlayer.show())
            print("----"*10)
            choises = input("ANSWER: ")
            if choises == "1": 
                cardToAdd = self.baraja.sendCard()
                print (self.turnOfPlayer.addCard(cardToAdd))
                self.turn()
            elif choises == "2":
                #ESTO DEBO REVISARLO
                cardToAdd = self.baraja.sendDiscard()
                # print (self.baraja.discardDeck(cardToAdd))
                print(self.turnOfPlayer.addCard(cardToAdd))
                # self.baraja.discardDeck()
                self.turn()
            else:
                print("Error, a digitado un numero incorrecto.\nElija una opcion del 1-2.")

            # if num_player == "1":
            #     return num_player == "2"
            # else:
            #     return num_player == "1"
            
    def turn(self):
        
        print("\nOpciones de la carta: \nA -- te quedas con la carta \nB -- lanza la misma carta")
        write = input("Answer: ")
        if write == "B":
            self.baraja.discard_deck.append(self.turnOfPlayer.handCard.pop())
            
        elif write == "A":
            print("")
            print ("Tines este mazo: " , self.turnOfPlayer.showCards())
            option = ["0", "1", "2", "3", "4", "5"]
            while True:
                elige = input("Posicion de carta que deseas cambiar: ")
                if elige in option:
                    self.baraja.discard_deck.append(self.turnOfPlayer.handCard.pop(int(elige)))
                    print("--Te has quedado con estas cartas: ", self.turnOfPlayer.showCards())
                    break
                else:
                    print("Error, digito un numero incorrecto, debe digitar un numero del 1-5")
        else:
            print("Error, digito un caracter incorrecto, debe digitar la letra A o B")

        

    def winner(self):
        #Este metodo verificará si alguno d elos jugadores tiene las cartas necesarias para ganar
        Mazodeljugador = self.player1.handCard
        print(Mazodeljugador)
        Mazodeljugador.sort()
        g=[]
        c=[]
        x=0
        mensaje = "Ganaste"
        # Ganador = []
        while x < len(Mazodeljugador):
          if len(g)==0 and len(c)==0:
            g.append(Mazodeljugador[x])
            c.append(Mazodeljugador[-(x+1)])
            print (mensaje = "no has ganado")
          else:
            if Mazodeljugador[x] in g:
              g.append(Mazodeljugador[x])
            if Mazodeljugador[-(x+1)] in c:
              c.append(Mazodeljugador[-(x+1)])
            if len(g)==3 and len(c)==2 or len(g)==2 and len(c)==3:
              print (mensaje)
          x+=1

    #Metodo que limpia la consola.
def cleanConsole():
    clear = lambda: os.system("cls")
    clear()


class principalMenu:
    def __init__(self):
        cleanConsole()
        print("\nCARD GAME 3 & 2 \nChoose An Option: \n1 -- START. \n2 -- HELP. \n3 -- CLOSE")    
        while True:
            num = input("ANSWER: ") 

            if num == "1":
                #Aqui debe iniciar el juego, llamando a la clase Players.
                self.playGame = Game()
                break


            if num == "2":
                #Despues de leer debe regresar al principio del menu.
                print("\nCOMO JUGAR.\n1-Ingresa tu nombre.\n2-Ingresa tu apellido.\n3-Apareceran varias a opciones a elegir cada vez que sea su turno.\n4-Tendras la opcion de quedarte con una carta de la baraja y cambiarla por una de tu mano o descartar la carta de la baraja.\n5-En caso de que elijas cambiar la carta de la baraja, por una de la mano, aparecera tu mano:\n\t[7 Black Peak, 6 Black Peak, A Red Diamond, 2 Black Peak, 4 Black Peak]\n6-Debes elegir entre las 5 cartas que tienes, cual deseas cambiar, digitando un la posicion de una de las cartas del 0-4.\n7-Ganará aquel que tenga 2 cartas iguales de una y tres cartas iguales de otra.")
                
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
# baraja = Players()
# Deck()
