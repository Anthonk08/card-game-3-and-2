#Inicio del programa en esta archivo se crearan las clases que utilizaremos alrededor del tiempo que estemos trabajando con este mini-proyecto.
#Actualizacion de las clases



# class Card:
#   def __init__(self,value,color,symbol):
#     self.value = value
#     self.color = color
#     self.symbol = symbol
    
#   def information(self):
#     return '{} {} {}'.format(self.value,self.color,self.symbol)


# class Deck:
#     def deckPlay1(self,deck):
#       self.deck = deck

# class Deck2:
#   def deckPlay2(self,deck2):
#     self.deck2 = deck2

# class Player:
#     def __init__(self,name,lastName):
#       self.name = name
#       self.lastName= lastName
   
#     def namefirst(self):
#       return '{} {}'.format(self.name,self.lastName)
# ##revisar.
# class SegundoJugador:
#     def __init__(self,Nombre,Apellido):
#       self.Nombre = Nombre
#       self.Apellido= Apellido
   
#     def NombreSegundo(self):
#       return '{} {}'.format(self.Nombre,self.Apellido)

# import random
# list = []
# values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
# symbols = [["Red","Heart"],["Red","Diamond"],["Black","Clover"],["Black","Peak"]]
# for s in symbols:
#   for v in values:
#     list.append(Card(v,s[0],s[1]) )

# random.shuffle(list)

# deck1 = []
# deck2 = []

# print("\nData of the first player.")
# name1 = input("First player name: ")
# lastName1 = input("First player last name: ")

# print("\nData of the second player.")
# name2 = input("Second player name: ")
# lastName2 = input("Second player last name: ")

# nameofFirstPlayer = Player(name1,lastName1)
# nameofSecondPlayer = Player(name2,lastName2)

# print(nameofFirstPlayer.namefirst())
# for i in range(0,5):
#   deck1.append(list.pop().information())

  
# objectDeck1 = Deck()
# objectDeck1.deckPlay1(deck1)
# print (objectDeck1.deck)

####################"El Segundo Jugador "###################

# print(nameofSecondPlayer.namefirst())
# for j in range(0,5):
#   # for k in len(ListaSinP):
#   #   lista.pop(k)
#     deck2.append(list.pop().information())
    
# random.shuffle(list)
# objectDeck2 = Deck()
# objectDeck2.deckPlay1(deck2)
# print (objectDeck2.deck)
# #Probando menu
# class Game:
#   def __init__(self,playerTurn):
#     self.playerTurn = playerTurn
#     self.mazodescarga = []
#     self.message = "Ronda: "
  
#   def Turn1(self):
#     contador = 0
#     contador += 1
#     print ("Ronda: " , contador) 
  
#     while True:
#         if self.playerTurn == nameofFirstPlayer:
#             deck1.append(list.pop().information())
#             print ("--" * 32)
#             print(nameofFirstPlayer.namefirst())
#             print (deck1)
        
#         while True:
#             print('''
#             A -- te quedas con la carta
#             B -- lanza la misma carta
#         ''')
#             write = input("respuesta: ")
#             if write == "B":
#                 self.mazodescarga.append(deck1.pop())
#                 return deck1 , self.mazodescarga
#             if write == "A":
#                 print (deck1)
#                 elige = input("Posicion de carta que deseas cambiar: ")
#             if elige == "0":
#                 self.mazodescarga.append(deck1.pop(0))
#                 return self.mazodescarga
#             elif elige == "1":
#                 self.mazodescarga.append(deck1.pop(1))
#                 return self.mazodescarga
#             elif elige == "2":
#                 self.mazodescarga.append(deck1.pop(2))
#                 return self.mazodescarga
#             elif elige == "3":
#                 self.mazodescarga.append(deck1.pop(3))
#                 return self.mazodescarga
#             elif elige == "4":
#                 self.mazodescarga.append(deck1.pop(4))
#                 return self.mazodescarga
#             elif elige == "5":
#                 self.mazodescarga.append(deck1.pop(5))
#                 return self.mazodescarga
#             else:
#                 print("No se encuentra entre los posibles numeros")

#         else: 
#             continue
        
#         # for descargajugadoruno in list:
#         #   for mazoquetiene in deck1:
#         #     if list[descargajugadoruno] != deck1[mazoquetiene]:
#         #       self.mazodescarga.append(list.pop)
        
#         #agregar una funcion que sea turno.
        
#     else:
#         deck2.append(list.pop().information())
#         print ("--" * 32)
#         print(nameofSecondPlayer.namefirst())
#         print (deck2)
        
#         while True:
#             print('''
#             A -- te quedas con la carta
#             B -- lanza la misma carta
#         ''')
#             write = input("respuesta: ")
#             if write == "B":
#                 self.mazodescarga.append(deck1.pop())
#                 return deck1 , self.mazodescarga
#             if write == "A":
#                 print (deck1)
#                 elige = input("Posicion de carta que deseas cambiar: ")
#             if elige == "0":
#                 self.mazodescarga.append(deck2.pop(0))
#                 return self.mazodescarga
#             elif elige == "1":
#                 self.mazodescarga.append(deck2.pop(1))
#                 return self.mazodescarga
#             elif elige == "2":
#                 self.mazodescarga.append(deck2.pop(2))
#                 return self.mazodescarga
#             elif elige == "3":
#                 self.mazodescarga.append(deck2.pop(3))
#                 return self.mazodescarga
#             elif elige == "4":
#                 self.mazodescarga.append(deck2.pop(4))
#                 return self.mazodescarga
#             elif elige == "5":
#                 self.mazodescarga.append(deck2.pop(5))
#                 return self.mazodescarga
#             else:
#                 print("No se encuentra entre los posibles numeros")

        
     
            


# nameofFirstPlayer = Player(name1,lastName1)
# game = Game(nameofFirstPlayer)
# print (game.Turn1())
# nameofSecondPlayer = Player(name2,lastName2)
# game2 = Game(nameofSecondPlayer)
# print (game2.Turn1())

from add_card import Card 
from add_deck import Deck
from add_players import Players
from add_game import Game