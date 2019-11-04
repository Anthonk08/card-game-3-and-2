from add_players import Players
from add_deck import Deck

# #COMENTA LO QUE HAGAS, POR FAVOR!!!

# class Game:
#     def __init__(self):
#         self.player1 = Players()
#         self.deck = Deck()
#         self.date.fillHandCard()
#         self.date.show()
        

# game1 = Game()
# print (game1)
class Game:
    def __init__(self):
        self.player1 = Players()
        self.baraja = Deck()
        self.baraja.fillDeck()
        self.player1.fillHandCard(self.baraja) #porsiaca'
        self.choice()
        self.turn() #X(le falta algo)

    #El metodo choise, se encarga de preguntar al jugador, que carta eligira: una de la baraja o una de la baraja de descarte.
    def choice(self):
        print("\nElige una de las opciones: \n1 -- Deseas una carta de la baraja. \n2 -- Deseas una carta de la baraja de descarte.")
        while True:
            choises = input("ANSWER: ")    
            if choises == "1":
                self.turn()
            if choises == "2":
                #ESTO DEBO REVISARLO
                discardDeck()
            else:
                print("Error, a digitado un numero incorrecto.\nElija una opcion del 1-2.")

    def turn(self):
        print("\nOpciones de la carta: \nA -- te quedas con la carta \nB -- lanza la misma carta")
        write = input("Answer: ")
        if write == "B":
            print (self.player1.handCard.pop().information())
        if write == "A":
            print (self.player1.showCards())
            option = ["0", "1", "2", "3", "4", "5"]
            while True:
                elige = input("Posicion de carta que deseas cambiar: ")
                if elige in option:
                    self.baraja.discard_deck.append(self.player1.handCard.pop(int(elige)))
                    print(self.baraja.showCards())
                    break
                else:
                    print("incorrecto")


    def winner(self):
        #Este metodo verificará si alguno d elos jugadores tiene las cartas necesarias para ganar
        Mazodeljugador ='BBAAA'
        Ganador = []
        mensaje = "Ganaste"
        for i in Mazodeljugador:
            if Ganador:
                if i != Ganador[-1]:
                    Ganador.append(i)
                    if len(Ganador) == 2:
                        print(mensaje)
            else:
                Ganador.append(i)
        print(Ganador)


Game()



            # for i in range(0,len(option)):
            #     try:
            #         if elige == option[i]:
            #             self.baraja.discard_deck.append(self.player1.handCard.pop(int(option[i])))
            #             print (self.baraja.showCards())
            #     except:
            #         print('ESTUPIDO') 
                
                    



#         # self.playerTurn = playerTurn
#         # self.mazodescarga = []
#         # self.message = "Ronda: "
#         self.handCard = handCard.addCard()
    
#     def turn(self):
#         # contador = 0
#         # contador += 1
#         # print ("Ronda: " , contador) 
    
#         while True:
#             if self.playerTurn == nameofFirstPlayer:
#                 Players.handCard.append(list.pop().information())
#                 print ("--" * 32)
#                 print(nameofFirstPlayer.namefirst())
#                 print (handCard)
            
#             while True:
#                 print('''
#                 A -- te quedas con la carta
#                 B -- lanza la misma carta
#             ''')
#                 write = input("Answer: ")
#                 if write == "B":
#                     self.mazodescarga.append(handCard.pop())
#                     return handCard , self.mazodescarga
#                 if write == "A":
#                     print (handCard)
#                     elige = input("Posicion de carta que deseas cambiar: ")
                
#                 option = ["0", "1", "2", "3", "4", "5"]
#                 for i in range(0,6):
#                     if (elige == option[i]):
#                         self.mazodescarga.append(handCard.pop(option[i]))
#                         return self.mazodescarga
#                     else:
#                         print("No se encuentra entre los posibles numeros")
#             else: 
#                 continue

# nameofFirstPlayer = Players(playerTurn)
# game = Game(nameofFirstPlayer)
# print (game.turn())
# nameofSecondPlayer = Players(playerTurn)
# game2 = Game(nameofSecondPlayer)
# print (game2.turn())
