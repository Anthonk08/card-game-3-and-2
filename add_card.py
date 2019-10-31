#Creacion de cartas

#COMENTA LO QUE HAGAS, POR FAVOR!!!

class Card:
  #Atributos de la clase card
  def __init__(self,value,color,symbol):
    self.value = value
    self.color = color
    self.symbol = symbol
  
  #Envia las cartas con su valor, color y su simbolo  
  def information(self):
    return f"{self.value} {self.color} {self.symbol}"    
    #return '{} {} {}'.format(self.value,self.color,self.symbol)


        
