#Creacion de cartas

class Card:
  def __init__(self,value,color,symbol):
    self.value = value
    self.color = color
    self.symbol = symbol
    
  def information(self):
    return '{} {} {}'.format(self.value,self.color,self.symbol)

