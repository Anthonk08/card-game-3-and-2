#Diseño de la consola.

class Players:
    num_player = 1
    def __init__(self, handCard):
        self.handCard = handCard
        self.player()
        Players.num_player+=1

    def show(self):
        return '{} {} {}'.format(self.name,self.lastName,self.player)

    def player(self):
        self.name = input("First player name: ")
        self.lastName = input("First player last name: ")
        self.player_num = "Player #{}".format(Players.num_player)
        




