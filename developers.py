import sys
import random 
import os
import colorama 
from colorama import Fore


class Card:
    #Attributes of the class Card
    def __init__(self,value,color,symbol):
        self.value = value
        self.color = color
        self.symbol = symbol
  
    #The information method sends the cards with their value, color and symbol.  
    def information(self):
        return Fore.CYAN + f"{self.value} {self.color} {self.symbol}"+ Fore.WHITE

class Deck:
    #Attributes of the class Deck.
    def __init__(self):
      self.cards = []
      self.discard_deck = []

    #Method to fill the deck.
    def fillDeck(self):
        card_list = []
        values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        # symbols = [["Red","Heart"],["Red","Diamond"],["Black","Clover"],["Black","Peak"]]♥ ♦ ♣ ♠
        symbols = [["Red","Heart |♥|"],["Red","Diamond |♦|"],["Black","Clover |♣|"],["Black","Peak |♠|"]]
       
        for s in symbols:
            for v in values:
                card_list.append(Card(v,s[0],s[1]) )
        random.shuffle(card_list)
        self.cards = card_list
        

    def sendCard(self):
        #Take the last card from the DECK.
        return self.cards.pop()

    def sendDiscard(self):
        #Take the last card from DISCARD DECK.
        return self.discard_deck.pop()

    def discardDeck(self,currentPlayer): #cree un parametro
        #Descartar de la
        return self.discard_deck.append(currentPlayer.discarHandCard())
    
    def showLastCard(self):
        #Show the last card of the discard mallet.
        return self.discard_deck[-1]

class Players:
    num_player = 1
    def __init__(self):
        #Attributes of the class Players.
        #HandCard list creation and player method call.
        self.handCard = []
        self.player()
        Players.num_player += 1

    #Call the item deck 5 times to fill the hand.
    def fillHandCard(self, baraja):
        #Fill each player’s deck. 
        for i in range(0,5):
            AddF = baraja.sendCard()
            self.handCard.append(AddF)
            

    def discarHandCard(self):
        return self.handCard.pop()

    def addCard(self,cardToAdd):
        #Adds a card to a player’s hand.
        self.handCard.append(cardToAdd)
        return cardToAdd.information()

    def showCards(self):
        #Filling a String with the 5 cards to print on each player’s data.
        listCard = ""
        for card in self.handCard:
            listCard += card.information() + " | "
        return (listCard)
        

    
    #Method for displaying each player’s data.
    def show(self):
        return f"\t\t\t\t\t    {self.player_num} \n------------------------------------------ ⇥  {self.name} {self.lastName}  ⇤ ----------------------------------------------------------\n{self.showCards()}"

        #return '{} {} {}'.format(self.name,self.lastName,self.player_num)

    #Method that asks for each player’s data.
    def player(self):
        while True:
            self.name = input("\n\t\t\t\tPlayer name: ")
            self.lastName = input("\t\t\t\tPlayer last name: ")
            if self.name == "" or self.lastName == "":
                print(Fore.RED + "\t\t\t\tError, wrong information." + Fore.WHITE)
            else:
                self.player_num = f"Player #{Players.num_player}."
                break
                
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
        # self.turnOfPlayer = self.baraja
        self.turn()
        print("""
        
        """)
        self.choice() 

    def changeTurnOfPlayer(self):
        #Change of player, for shifts.
        self.turnOfPlayer = self.player1 if self.turnOfPlayer == self.player2 else self.player2  

    def shufflingCards(self):
        self.baraja.cards = self.baraja.discard_deck[:-1]
        auxVariable = self.baraja.discard_deck[-1]
        self.baraja.discard_deck = [auxVariable]
        random.shuffle(self.baraja.cards)

    #The choise method asks the player which card he will choose: a card from the deck or a card from the discard deck.
    def choice(self):
        self.changeTurnOfPlayer()
        while True:
            # cleanConsole()
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
                        self.shufflingCards() #agregado 123

                    cardToAdd = self.baraja.sendCard()
                    print (self.turnOfPlayer.addCard(cardToAdd))
                    self.turn()  
                    
                elif choises == "2":
                    #ESTO DEBO REVISARLO
                    cardToAdd = self.baraja.sendDiscard()
                    print(self.turnOfPlayer.addCard(cardToAdd))
                    self.turn()
                    
                # cleanConsole()
                #Changes players turn
                self.changeTurnOfPlayer()

            else:
                print(Fore.RED +"Error, you’ve entered an incorrect number.\nChoose an option of 1-2." + Fore.WHITE)

        if self.winner() == True:
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
                        # print("----- [0] ---- [1] ---- [2] ---- [3] ----[4] ")
                        break
                    else:
                        print( Fore.RED + "Error, digit an incorrect number, you must enter a number of 0-4" + Fore.WHITE)
                break
            else:
                print(Fore.RED +"Error, digit an incorrect character, you must type the letter A or B." +Fore.WHITE)

        

    def winner(self):
        #This method will verify if any of the players have the necessary cards to win.
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


class principalMenu:
    def __init__(self):
        cleanConsole()
        
        print(Fore.RED + "\n\t\t\t" + " ♥  ♦  ♣  ♠  "*4 , Fore.WHITE)
        print(Fore.GREEN + """
        \t\t\t    C A R D  G A M E  3  &  2 
        """ +Fore.WHITE)
        print(Fore.RED + "\t\t\t" + " ♥  ♦  ♣  ♠  "*4 , Fore.WHITE)
        print ("""\n\t\t\t\tC h o o s e   A n   O p t i o n : \n\n\t\t\t\t\t1 -- START. \n\n\t\t\t\t\t2 -- HELP. \n\n\t\t\t\t\t3 -- CLOSE
        """)
    
        num = input("\t\t\t\tA N S W E R : ") 
        if num == "1":
            #Here you must start the game by calling the Players class.
            self.playGame = Game()
            sys.exit()


        if num == "2":
            #After reading must return to the top of the menu.
            cleanConsole() 
            print (Fore.GREEN + "\n\n\t\t\tH O W   T O   P L A Y   I T ?" + Fore.WHITE)
            print(Fore.YELLOW + "\n1- Enter your name.\n\n2- Enter your last name.\n\n3- Several options will appear to be chosen each time it is your turn.\n\n4- You will have the option to keep a card from the deck and exchange it for one of your hand or discard the card from the deck.\n\n5- If you choose to change the card in the deck to one in the hand, your hand will appear:\n\n\t[7 Black Peak, 6 Black Peak, A Red Diamond, 2 Black Peak, 4 Black Peak]\n\n6- You must choose between the 5 cards you have, which you want to change, by typing a position of one of the 0-4 cards.\n\n7- He who has two equal cards of one and three equal cards of another will win.\n" +Fore.WHITE)
            print("-----"*22)
            print("\n\t\t\t\t A -- You want to go back to the menu?\n\n\t\t\t\t B -- Close the game?\n")
            while True:
                num2 = input("\t\t\t\t -- A N S W E R : ").upper()
                if num2 == "A":
                    principalMenu()
                if num2 == "B":
                    cleanConsole()
                    print (Fore.RED + "\t\t\t\t\t《  《  《  《  《  《  》  》  》  》  》  》  " + Fore.WHITE)
                    print("""
            ---- ||  T h e   g a m e   w i l l   c l o s e,   w a i t   a   m o m e n t,   p l e a s e.  ||----
            """)
                    print(Fore.RED + "\t\t\t\t\t《  《  《  《  《  《  》  》  》  》  》  》  " + Fore.WHITE)
                    sys.exit()
                else:
                    print("You have entered an incorrect character.\nChoose an A OR B option.")
        if num == "3":
            #Just present the message that the game is closing and closing.
            
            cleanConsole()
            print (Fore.RED + "\t\t\t\t\t《  《  《  《  《  《  》  》  》  》  》  》  " + Fore.WHITE)
            print("""
            ---- ||  T h e   g a m e   w i l l   c l o s e,   w a i t   a   m o m e n t,   p l e a s e.  ||----
            """)
            print(Fore.RED + "\t\t\t\t\t《  《  《  《  《  《  》  》  》  》  》  》  " + Fore.WHITE)
            sys.exit()

        else:
            print(Fore.RED +"Error, you’ve entered an incorrect number.\nChoose an option of 1-3." + Fore.WHITE)
            time.sleep(0.8)
            principalMenu()
        
principalMenu()
