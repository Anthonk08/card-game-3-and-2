import colorama 
from colorama import Fore

#Class players responsible for the data of each player and their deck.
class Players:
    numPlayer = 1
    def __init__(self):
        #Attributes of the class Players.
        #HandCard list creation and player method call.
        self.handCard = []
        self.player()
        Players.numPlayer += 1

    #Call the item deck 5 times to fill the hand.
    def fillHandCard(self, PackOfCards):
        #Fill each player’s deck. 
        for i in range(0,5):
            AddF = PackOfCards.sendCard()
            self.handCard.append(AddF)
    
    #Removes a card from the player’s hand.
    def discardHandCard(self):
        return self.handCard.pop()

    #Adds a card to a player’s hand.
    def addCard(self,cardToAdd):
        self.handCard.append(cardToAdd)
        return cardToAdd.information()

    #Filling a String with the 5 cards to print on each player’s data.
    def showCards(self):
        listCard = ""
        for card in self.handCard:
            listCard += card.information() + " | "
        return (listCard)

    #Method for displaying each player’s data.
    def show(self):
        return f"\n\t\t\t\t\t    {self.player_num} \n\n------------------------------------------ ⇥  {self.name} {self.lastName}  ⇤ ----------------------------------------------------------\n{self.showCards()}"

    #Method that asks for each player’s data.
    def player(self):
        validationTool = True
        while validationTool:
            self.name = input("\n\t\t\t\tPlayer name: ")
            self.lastName = input("\t\t\t\tPlayer last name: ")
            if self.name == "" or self.lastName == "":
                print(Fore.RED + "\t\t\t\tError, wrong information." + Fore.WHITE)
            else:
                self.player_num = f"Player #{Players.numPlayer}."
                validationTool = False