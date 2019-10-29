#Diseño de la consola.

class Menu:
    def __init__(self, name, lastName, player):
        self.name = name
        self.lastName = lastName
        self.player = player

    def show(self):
        return '{} {} {}'.format(self.name,self.lastName,self.player)

name = input("First player name: ")
lastName = input("First player last name: ")
player = "Player #1"
player1 = Menu(name, lastName, player)
print(player1.show())

name = input("\nSecond player name: ")
lastName = input("Second player last name: ")
player = "Player #2"
player2 = Menu(name, lastName, player)
print(player2.show())