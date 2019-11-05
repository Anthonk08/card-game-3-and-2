#Diseño de la consola.
from add_deck import Deck #lo quite.
#COMENTA LO QUE HAGAS, POR FAVOR!!!#
class Players:
    num_player = 1
    #Creacion de lista handCard y llamada del metodo player
    def __init__(self):
        self.handCard = []
        self.player()
         #X(le falta algo)
        Players.num_player += 1

    #Llena la baraja de cada jugador 
    
    def fillHandCard(self, baraja):
        #Llama el objeto baraja 5 veces para llenar la mano
        for i in range(0,5):
            self.addCard(baraja)

    # def discarHandCard(self):
    #     return self.handCard.pop()
    def discarHandCard(self):
        return self.handCard.pop()

    def addCard(self,baraja):
        #Se encarga de agregar una carta a la mano de un jugador 
        self.handCard.append(baraja.sendCard())

    def showCards(self):
        #Llenado de un String con las 5 cartas para imprimir en los datos de cada jugador
        listCard = ""
        for card in self.handCard:
            listCard += card.information() + " "
        return listCard

    

    #Metodo para mostrar los datos de cada jugador
    def show(self):
        return f"{self.player_num} \n{self.name}  {self.lastName} \n{self.showCards()}"
        #return '{} {} {}'.format(self.name,self.lastName,self.player_num)

    #Metodo que pide los datos de cada jugador
    def player(self):
        self.name = input("\nPlayer name: ")
        self.lastName = input("Player last name: ")
        self.player_num = f"Player #{Players.num_player}."
        #Esto es un ejemplo.
        # a = f"Diga su nombre, por favor :v{self.name}"

   
# baraja = Deck()
# baraja.fillDeck()

# player1 = Players()
# player1.fillHandCard(baraja)
# player1.showCards()
# print(player1.show())

# player2 = Players()
# player2.fillHandCard(baraja)
# player2.showCards()
# print(player2.show())

