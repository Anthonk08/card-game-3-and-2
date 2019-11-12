from card import Card 
import random 
class Deck:
    #Attributes of the class Deck.
    def __init__(self):
      self.cards = []
      self.discard_deck = []

    #Method to fill the deck.
    def fillDeck(self):
        card_list = []
        values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        symbols = [["Red","Heart |♥|"],["Red","Diamond |♦|"],["Black","Clover |♣|"],["Black","Peak |♠|"]]
       
        for s in symbols:
            for v in values:
                card_list.append(Card(v,s[0],s[1]) )
        random.shuffle(card_list)
        self.cards = card_list

    #Take the last card from the DECK.
    def sendCard(self):
        return self.cards.pop()

    #Take the last card from DISCARD DECK.
    def sendDiscard(self):
        return self.discard_deck.pop()

    #Descartar de la
    def discardDeck(self,currentPlayer):
        return self.discard_deck.append(currentPlayer.discarHandCard())
    
    #Show the last card of the discard mallet.
    def showLastCard(self):
        return self.discard_deck[-1]
    
    #Method used to shuffle the discard deck and put the cards back into the middle deck.
    def shufflingCards(self):
        self.cards = self.discard_deck[:-1]
        auxVariable = self.discard_deck[-1]
        self.discard_deck = [auxVariable]
        random.shuffle(self.cards)
        input("CENTRAL DECK HAS BEEN SHUFFLED")
