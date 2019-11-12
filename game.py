import sys
import random 
import os
import colorama 
from colorama import Fore
from deck import Deck
from players import Players
import time

class Game:
    
    #Attributes of the class Game and method call of other classes.
    def __init__(self):
        #cleanConsole used to clean the console.
        cleanConsole()
        print("---"*37) #design
        self.player1 = Players()
        print("---"*37) #design
        time.sleep(0.4)
        cleanConsole()
        print("---"*37)
        self.player2 = Players()
        print("---"*37)
        time.sleep(0.4)
        self.baraja = Deck()
        self.baraja.fillDeck()
        self.player1.fillHandCard(self.baraja)
        self.player2.fillHandCard(self.baraja)
        cleanConsole()
        print(self.player1.show())
        print("---"*37)
        
        self.cardToAdd = self.baraja.sendCard()
        print("New Letter Added: ",self.player1.addCard(self.cardToAdd))
        self.turnOfPlayer = self.player1
        self.turn()
        self.choice() 
    
    #Change of player, for shifts.
    def changeTurnOfPlayer(self):
        self.turnOfPlayer = self.player1 if self.turnOfPlayer == self.player2 else self.player2  

    #The choise method asks the player which card he will choose: a card from the deck or a card from the discard deck.
    def choice(self):
        self.changeTurnOfPlayer()
        
        while not self.winner():
            print("∸∸∸" *37)
            print("\nChoose one of the options: \n1 -- You want a card from the deck. \n2 -- You want a card from the discard deck.")
            print("\nCard in the discard deck: ", self.baraja.showLastCard().information())
            print(self.turnOfPlayer.show())
            print("---"*37)
        
            choises = input("ANSWER: ") 
            if choises == "1" or choises == "2":
                if choises == "1":
                    #In this If is checked if the deck is left empty, the discard deck is shuffled and the cards are added back to the deck.
                    if len(self.baraja.cards) == 0:
                        self.baraja.shufflingCards() #agregado 123

                    cardToAdd = self.baraja.sendCard()
                    print (self.turnOfPlayer.addCard(cardToAdd))
                    self.turn()  
                    
                elif choises == "2":
                    cardToAdd = self.baraja.sendDiscard()
                    print(self.turnOfPlayer.addCard(cardToAdd))
                    self.turn()     
                cleanConsole()
                if self.winner():
                    break
                #Changes players turn
                self.changeTurnOfPlayer()
            else:
                print(Fore.RED +"Error, you’ve entered an incorrect number.\nChoose an option of 1-2." + Fore.WHITE)

        cleanConsole()
        print("∺∺∺∺∺" *22)
        print (Fore.GREEN + """
        \t\t\t--- Y O U  W I N ---
        """ + Fore.WHITE) 
        print("∺∺∺∺∺" *22)
        sys.exit()

    def turn(self):
        print("\nOptions of the chart: \nA -- you keep the letter. \nB -- throws the same card.")
        while True:
            write = input("Answer: ").upper()
            if write == "B":
                self.baraja.discard_deck.append(self.turnOfPlayer.handCard.pop())
                break
            elif write == "A":
                print("")
                print ("---" *37)
                print ("You have this mallet: \n", self.turnOfPlayer.showCards())
                print(" -------- [0] ----------- [1] ------------- [2] ---------------- [3] --------------- [4] ------------ *CARD ADDED*-")

                option = ["0", "1", "2", "3", "4"]
                while True:
                    elige = input("Card position you want to change: ")
                    if elige == "5":
                        print( Fore.RED + "Error, position 5 contains the card to be added." + Fore.WHITE)
                        elige = input("Card position you want to change: " )
                    elif elige in option:
                        self.baraja.discard_deck.append(self.turnOfPlayer.handCard.pop(int(elige)))
                        print("You kept these cards: ", self.turnOfPlayer.showCards())
                        break
                    else:
                        print( Fore.RED + "Error, digit an incorrect number, you must enter a number of 0-4" + Fore.WHITE)
                break
            else:
                print(Fore.RED +"Error, digit an incorrect character, you must type the letter A or B." +Fore.WHITE)

        
    #This method will verify if any of the players have the necessary cards to win.
    def winner(self):
        Mazodeljugador = self.turnOfPlayer.handCard
        g=[]
        c=[]
        x=0
        while x < len(Mazodeljugador):
          if len(g)==0 and len(c)==0:
            g.append(Mazodeljugador[x].value)
            c.append(Mazodeljugador[-(x+1)].value)
          else:
            if Mazodeljugador[x].value in g:
              g.append(Mazodeljugador[x].value)
            if Mazodeljugador[-(x+1)].value in c:
              c.append(Mazodeljugador[-(x+1)].value)
            if (len(g)==3 and len(c)==2) or (len(g)==2 and len(c)==3):
              return True   
          x+=1
        return False

#Function that cleans the console.
def cleanConsole():
    clear = lambda: os.system("cls")
    clear()