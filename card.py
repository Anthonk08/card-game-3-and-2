import colorama 
from colorama import Fore

#The Card class its function is to create the cards display each card with its element.
class Card:
    #Attributes of the class Card
    def __init__(self,value,color,symbol):
        self.value = value
        self.color = color
        self.symbol = symbol
  
    #The information method sends the cards with their value, color and symbol.  
    def information(self):
        return Fore.CYAN + f"{self.value} {self.color} {self.symbol}"+ Fore.WHITE
