import sys
import random 
import os
class Card:

    #Attributes of the class Card
    def __init__(self,value,color,symbol):
        self.value = value
        self.color = color
        self.symbol = symbol
  
    #The information method sends the cards with their value, color and symbol.  
    def information(self):
        return f"{self.value} {self.color} {self.symbol}"   

class Deck:
    #Attributes of the class Deck.
    def __init__(self):
      self.cards = []
      self.discard_deck = []

    #Method to fill the deck.
    def fillDeck(self):
        card_list = []
        values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        symbols = [["Red","Heart"],["Red","Diamond"],["Black","Clover"],["Black","Peak"]]
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
    #Attributes of the class Players.
    num_player = 1
    #HandCard list creation and player method call.
    def __init__(self):
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
            listCard += card.information() + " "
        return (listCard)

    
    #Method for displaying each player’s data.
    def show(self):
        return f"           {self.player_num} \n--------- ⇥  {self.name} {self.lastName}  ⇤ ---------\n{self.showCards()}"

        #return '{} {} {}'.format(self.name,self.lastName,self.player_num)

    #Method that asks for each player’s data.
    def player(self):
        self.name = input("\nPlayer name: ")
        self.lastName = input("Player last name: ")
        self.player_num = f"Player #{Players.num_player}."

class Game:
    #Attributes of the class Game and method call of other classes.
    def __init__(self):
        #cleanConsole used to clean the console.
        cleanConsole()
        print("---"*32) #design
        self.player1 = Players()
        print("---"*32) #design
        cleanConsole()
        print("---"*32)
        self.player2 = Players()
        print("---"*32)
        print("---"*32)
        self.baraja = Deck()
        self.baraja.fillDeck()
        self.player1.fillHandCard(self.baraja)
        self.player2.fillHandCard(self.baraja)
        cleanConsole()
        print(self.player1.show())
        print("---"*32)
        self.cardToAdd = self.baraja.sendCard()
        print("Nueva Carta Agregada: ",self.player1.addCard(self.cardToAdd))
        self.turnOfPlayer = self.player1
        # self.turnOfPlayer = self.baraja
        self.turn()
        print("""
        
        """)
        self.choice() 

        self.winner()
        
        #X(le falta algo)
        self.winner()
        cleanConsole()

    #The choise method asks the player which card he will choose: a card from the deck or a card from the discard deck.
    def choice(self):
        
        while True:
            # cleanConsole()
            print("∸∸∸∸∸∸∸∸" *20)
            print("\nChoose one of the options: \n1 -- You want a card from the deck. \n2 -- You want a card from the discard deck.")
            print("\nCard in the discard deck: ", self.baraja.showLastCard().information())
            #Change of player, for shifts.
            self.turnOfPlayer = self.player1 if self.turnOfPlayer == self.player2 else self.player2
            print(self.turnOfPlayer.show())
            print("-----"*10)
            choises = input("ANSWER: ") 
            if choises == "1": 
                cardToAdd = self.baraja.sendCard()
                print (self.turnOfPlayer.addCard(cardToAdd))
                self.turn()
            elif choises == "2":
                #ESTO DEBO REVISARLO
                cardToAdd = self.baraja.sendDiscard()
                # print (self.baraja.discardDeck(cardToAdd))
                print(self.turnOfPlayer.addCard(cardToAdd))
                # self.baraja.discardDeck()
                self.turn()
            else:
                print("Error, you’ve entered an incorrect number.\nChoose an option of 1-2.")

            # if num_player == "1":
            #     return num_player == "2"
            # else:
            #     return num_player == "1"
            
    def turn(self):
        
        print("\nOptions of the chart: \nA -- you keep the letter. \nB -- throws the same card.")
        write = input("Answer: ")
        if write == "B":
            self.baraja.discard_deck.append(self.turnOfPlayer.handCard.pop())
            
        elif write == "A":
            print("")
            print ("You have this mallet: " , self.turnOfPlayer.showCards())
            option = ["0", "1", "2", "3", "4", "5"]
            while True:
                elige = input("Card position you want to change: ")
                if elige in option:
                    self.baraja.discard_deck.append(self.turnOfPlayer.handCard.pop(int(elige)))
                    print("--You kept these cards: ", self.turnOfPlayer.showCards())
                    break
                else:
                    print("Error, digit an incorrect number, you must enter a number of 1-5")
        else:
            print("Error, digit an incorrect character, you must type the letter A or B.")

        

    def winner(self):
        #This method will verify if any of the players have the necessary cards to win.
        Mazodeljugador = self.player1.handCard
        # print(Mazodeljugador[0].value)
        Mazodeljugador.sort()
        g=[]
        c=[]
        x=0
        mensaje = "-----YOU WIN------"
        # Ganador = []
        while x < len(Mazodeljugador):
          if len(g)==0 and len(c)==0:
            g.append(Mazodeljugador[x].value)
            c.append(Mazodeljugador[-(x+1)].value)
            print (mensaje = "no has ganado")
          else:
            if Mazodeljugador[x].value in g:
              g.append(Mazodeljugador[x].value)
            if Mazodeljugador[-(x+1)].value in c:
              c.append(Mazodeljugador[-(x+1)].value)
            if len(g)==3 and len(c)==2 or len(g)==2 and len(c)==3:
              print (mensaje)
          x+=1

#Function that cleans the console.
def cleanConsole():
    clear = lambda: os.system("cls")
    clear()


class principalMenu:
    def __init__(self):
        cleanConsole()
        print("\nCARD GAME 3 & 2 \nChoose An Option: \n1 -- START. \n2 -- HELP. \n3 -- CLOSE")    
        while True:
            num = input("ANSWER: ") 

            if num == "1":
                #Here you must start the game by calling the Players class.
                self.playGame = Game()
                break


            if num == "2":
                #After reading must return to the top of the menu.
                print("\nHOW TO PLAY IT?\n1-Enter your name.\n2-Enter your last name.\n3-Several options will appear to be chosen each time it is your turn.\n4-You will have the option to keep a card from the deck and exchange it for one of your hand or discard the card from the deck.\n5-If you choose to change the card in the deck to one in the hand, your hand will appear:\n\t[7 Black Peak, 6 Black Peak, A Red Diamond, 2 Black Peak, 4 Black Peak]\n6-You must choose between the 5 cards you have, which you want to change, by typing a position of one of the 0-4 cards.\n7-He who has two equal cards of one and three equal cards of another will win.")
                
                print("\nA- You want to go back to the menu? \nB- Close the game?")
                while True:
                    num2 = input("ANSWER: ")
                    if num2 == "A":
                        principalMenu()
                    if num2 == "B":
                        print("The game will close, wait a moment, please.")
                        sys.exit()
                    else:
                        print("You have entered an incorrect character.\nChoose an A OR B option.")
            if num == "3":
                #Just present the message that the game is closing and closing.
                print("The game will close, wait a moment, please.")
                sys.exit()

            else:
                print("Error, you’ve entered an incorrect number.\nChoose an option of 1-3.")
        
principalMenu()
