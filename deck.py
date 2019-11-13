from card import Card 
import random 

#The Deck class contains the elements of creating the cards: their number, suit and logo.
class Deck:
    #Attributes of the class Deck.
    def __init__(self):
      self.cards = []
      self.discard_deck = []

    #Method to fill the deck.
    def fillDeck(self):
        self.cards = []
        values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        symbols = [["Red","Heart |♥|"],["Red","Diamond |♦|"],["Black","Clover |♣|"],["Black","Peak |♠|"]]
       
        for s in symbols:
            for v in values:
                self.cards.append(Card(v,s[0],s[1]) )
        random.shuffle(self.cards)

    #Take the last card from the DECK.
    def sendCard(self):
        return self.cards.pop()

    #Take the last card from DISCARD DECK.
    def sendDiscard(self):
        return self.discard_deck.pop()

    #Method used to discard a card in the discard deck.
    def discardDeck(self,currentPlayer):
        return self.discard_deck.append(currentPlayer.discardHandCard())
    
    #Show the last card of the discard mallet.
    def showLastCard(self):
        return self.discard_deck[-1]
    
    #Method used to shuffle the discard deck and put the cards back into the middle deck.
    def shufflingCards(self):
        self.cards = self.discard_deck[:-1]
        saveCards = self.discard_deck[-1]
        self.discard_deck = [saveCards]
        random.shuffle(self.cards)
        input("CENTRAL DECK HAS BEEN SHUFFLED")
