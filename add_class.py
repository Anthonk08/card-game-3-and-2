#Inicio del programa en esta archivo se crearan las clases que utilizaremos alrededor del tiempo que estemos trabajando con este mini-proyecto.
#Actualizacion de las clases

class Card:
  def __init__(self,value,color,symbol):
    self.value = value
    self.color = color
    self.symbol = symbol
    
  def information(self):
    return '{} {} {}'.format(self.value,self.color,self.symbol)

class Deck1:
    def deckPlay1(self,deck1):
      self.deck1 = deck1

class Deck2:
  def deckPlay2(self,deck2):
    self.deck2 = deck2

class firstPlayer:
    def __init__(self,name,lastName):
      self.name = name
      self.lastName= lastName
   
    def namefirst(self):
      return '{} {}'.format(self.name,self.lastName)
# ##revisar.
# class SegundoJugador:
#     def __init__(self,Nombre,Apellido):
#       self.Nombre = Nombre
#       self.Apellido= Apellido
   
#     def NombreSegundo(self):
#       return '{} {}'.format(self.Nombre,self.Apellido)



import random
list = []
values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
symbols = [["Red","Heart"],["Red","Diamond"],["Black","Clover"],["Black","Peak"]]
for s in symbols:
  for v in values:
    list.append(Card(v,s[0],s[1]) )

random.shuffle(list)

deck1 = []
deck2 = []

name1 = input("First player name: ")
lastName1 = input("First player last name: ")

name2 = input("Second player name: ")
lastName2 = input("Second player last name: ")

nameofFirstPlayer = firstPlayer(name1,lastName1)
nameofSecondPlayer = firstPlayer(name2,lastName2)

print(nameofFirstPlayer.namefirst())
for i in range(0,5):
  deck1.append(list.pop().information())
  
  
objectDeck1 = Deck1()
objectDeck1.deckPlay1(deck1)
print (objectDeck1.deck1)

####################"El Segundo Jugador "###################

print(nameofSecondPlayer.namefirst())
for j in range(0,5):
  # for k in len(ListaSinP):
  #   lista.pop(k)
    deck2.append(list.pop().information())
    
random.shuffle(list)
objectDeck2 = Deck2()
objectDeck2.deckPlay2(deck2)
print (objectDeck2.deck2)

