from add_players import Players

#COMENTA LO QUE HAGAS, POR FAVOR!!!

# class Game:
#     def __init__(self,playerTurn):
#         self.playerTurn = playerTurn
#         self.mazodescarga = []
#         self.message = "Ronda: "
    
#     def turn(self):
#         contador = 0
#         contador += 1
#         print ("Ronda: " , contador) 
    
#         while True:
#             if self.playerTurn == nameofFirstPlayer:
#                 handCard.append(list.pop().information())
#                 print ("--" * 32)
#                 print(nameofFirstPlayer.namefirst())
#                 print (handCard)
            
#             while True:
#                 print('''
#                 A -- te quedas con la carta
#                 B -- lanza la misma carta
#             ''')
#                 write = input("Answer: ")
#                 if write == "B":
#                     self.mazodescarga.append(handCard.pop())
#                     return handCard , self.mazodescarga
#                 if write == "A":
#                     print (handCard)
#                     elige = input("Posicion de carta que deseas cambiar: ")
                
#                 option = ["0", "1", "2", "3", "4", "5"]
#                 for i in range(0,6):
#                     if (elige == option[i]):
#                         self.mazodescarga.append(handCard.pop(option[i]))
#                         return self.mazodescarga
#                     else:
#                         print("No se encuentra entre los posibles numeros")
#             else: 
#                 continue

# nameofFirstPlayer = Players(playerTurn)
# game = Game(nameofFirstPlayer)
# print (game.turn())
# nameofSecondPlayer = Players(playerTurn)
# game2 = Game(nameofSecondPlayer)
# print (game2.turn())