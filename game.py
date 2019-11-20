import sys
import random 
import os
import colorama 
from colorama import Fore
from deck import Deck
from players import Players
import time

#Method responsible for the operation of player handling and shift exchange.
class Game:
    
    #Attributes of the class Game and method call of other classes.
    def __init__(self):
        #cleanConsole used to clean the console.
        cleanConsole()
        print("---"*37)
        self.player1 = Players()
        print("---"*37)
        time.sleep(0.4)
        cleanConsole()
        print("---"*37)
        self.player2 = Players()
        print("---"*37)
        time.sleep(0.4)
        self.PackOfCards = Deck()
        self.PackOfCards.fillDeck()
        self.player1.fillHandCard(self.PackOfCards)
        self.player2.fillHandCard(self.PackOfCards)
        cleanConsole()
        print(self.player1.show())
        print("---"*37)
        
        self.cardToAdd = self.PackOfCards.sendCard()
        print("New Letter Added: ",self.player1.addCard(self.cardToAdd))
        self.turnOfPlayer = self.player1
        self.turn(True)
        self.choice() 
    
    #Change of player, for shifts.
    def changeTurnOfPlayer(self):
        self.turnOfPlayer = self.player1 if self.turnOfPlayer == self.player2 else self.player2  

    #The choise method asks the player which card he will choose: a card from the deck or a card from the discard deck.
    def choice(self):
        
        self.changeTurnOfPlayer()
        while True:
            cleanConsole()
            print("∸∸∸" *37)
            print("\nChoose one of the options: \n1 -- You want a card from the deck. \n2 -- You want a card from the discard deck.")
            print("\nCard in the discard deck: ", self.PackOfCards.showLastCard().information())
            print(self.turnOfPlayer.show())
            print("---"*37)
        
            optionChoices = input("ANSWER: ") 
            #He’s in charge of taking or discarding a letter.
            if optionChoices == "1" or optionChoices == "2":
                if optionChoices == "1":
                    #In this If is checked if the deck is left empty, the discard deck is shuffled and the cards are added back to the deck.
                    if len(self.PackOfCards.cards) == 0:
                        self.PackOfCards.shufflingCards()

                    cardToAdd = self.PackOfCards.sendCard()
                    print (self.turnOfPlayer.addCard(cardToAdd))
                    isNormalDeck = True
                    self.turn(isNormalDeck)
                    
                elif optionChoices == "2":
                    cardToAdd = self.PackOfCards.sendDiscard()
                    print(self.turnOfPlayer.addCard(cardToAdd))
                    isNormalDeck = False
                    self.turn(isNormalDeck)
                         
                cleanConsole()
                #Condition that verifies if the winner method returns true
                if self.winner():
                    break
                #Changes players turn
                self.changeTurnOfPlayer()
            else:
                print(Fore.RED +"Error, you’ve entered an incorrect number.\nChoose an option of 1-2." + Fore.WHITE)
                time.sleep(0.8)

        cleanConsole()
        #If the winner method returns true, this part presents a message with the winner and his deck and presents the You Win message.
        print(self.turnOfPlayer.show())
        print("∺∺∺∺∺" *22)
        print (Fore.GREEN + """
        \t\t\t--- Y O U  W I N ---
        """ + Fore.WHITE) 
        print("∺∺∺∺∺" *22)
        sys.exit()

    #Turn method takes care of the choices made in each player’s hand
    def turn(self,isNormalDeck):
        if isNormalDeck:
            print("\nOptions of the chart: \nA -- you keep the letter. \nB -- throws the same card.")
        while True:
            
            deckOption = input("Answer: ").upper() if isNormalDeck else "A"
            if deckOption == "B":
                self.PackOfCards.discard_deck.append(self.turnOfPlayer.handCard.pop())
                break
            elif deckOption == "A":
                print("")
                print ("---" *37)
                print ("You have this mallet: \n", self.turnOfPlayer.showCards())
                print(" -------- [0] ----------- [1] ------------- [2] ---------------- [3] --------------- [4] ------------ *CARD ADDED*-")

                option = ["0", "1", "2", "3", "4"]
                while True:
                    cardPosition = input("Card position you want to change: ")
                    if cardPosition == "5":
                        print( Fore.RED + "Error, position 5 contains the card to be added." + Fore.WHITE)
                        time.sleep(0.8)
                        cardPosition = input("Card position you want to change: " )
                    elif cardPosition in option:
                        self.PackOfCards.discard_deck.append(self.turnOfPlayer.handCard.pop(int(cardPosition)))
                        print("You kept these cards: ", self.turnOfPlayer.showCards())
                        break
                    else:
                        print( Fore.RED + "Error, digit an incorrect number, you must enter a number of 0-4" + Fore.WHITE)
                        time.sleep(0.8)
                break
            else:
                print(Fore.RED +"Error, digit an incorrect character, you must type the letter A or B." +Fore.WHITE)
                time.sleep(0.8)
        
    #This method will verify if any of the players have the necessary cards to win.
    def winner(self):
        deckOfPlayer = []
        for card in self.turnOfPlayer.handCard:
            deckOfPlayer.append(card.value)
        deckOfPlayer.sort()
        possibility1=[]
        possibility2=[]
        i=0
        while i < len(deckOfPlayer):
            if len(possibility1) == 0 and len(possibility2) == 0:
                possibility1.append(deckOfPlayer[i])
                possibility2.append(deckOfPlayer[-(i+1)])
            else:
                if deckOfPlayer[i] in possibility1:
                    possibility1.append(deckOfPlayer[i])
                if deckOfPlayer[-(i+1)] in possibility2:
                    possibility2.append(deckOfPlayer[-(i+1)])
                if (len(possibility1) == 3 and len(possibility2) == 2) or (len(possibility1) == 2 and len(possibility2) == 3):
                    return True   
            i+=1
        return False

#Function that cleans the console.
def cleanConsole():
    clear = lambda: os.system("cls")
    clear()