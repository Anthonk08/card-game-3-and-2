#clase para crear objeto de mazo.
from add_card import Card
import random

#COMENTA LO QUE HAGAS, POR FAVOR!!!

#Clase encargada de crear la baraja completa
class Deck:
    def __init__(self):
      self.cards = []
    
    #Metodo encargado de llenar la baraja
    def fillDeck(self):
        list = []
        values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        symbols = [["Red","Heart"],["Red","Diamond"],["Black","Clover"],["Black","Peak"]]
        for s in symbols:
            for v in values:
                list.append(Card(v,s[0],s[1]) )
        random.shuffle(list)
        self.cards = list

    def sendCard(self):
        #Toma la ultima carta de la baraja.
        return self.cards.pop()


