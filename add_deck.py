#clase para crear objeto de mazo.
from add_card import Card
import random
class Deck:
    def __init__(self):
      self.deck = self.fillDeck()
    
    def fillDeck(self):
        list = []
        values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        symbols = [["Red","Heart"],["Red","Diamond"],["Black","Clover"],["Black","Peak"]]
        for s in symbols:
            for v in values:
                list.append(Card(v,s[0],s[1]) )
        random.shuffle(list)
        return list

# de = Deck()
# for card in de.deck:
#     print(card.information())