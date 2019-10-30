#Diseño de la consola.

class Players:
    num_player = 1
    def __init__(self, handCard):
        self.handCard = handCard

    def show(self):
        return '{} {} {}'.format(self.name,self.lastName,self.player)

    def player(self, name, lastName, player,):
        self.name = name
        self.lastName = lastName
        self.player = player
        name = input("First player name: ")
        lastName = input("First player last name: ")
        player_num = "Player #{}".format(num_player)
        info_player = Players(name, lastName, player_num)
        print(info_player())





