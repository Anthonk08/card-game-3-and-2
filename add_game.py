class Game:
      def __init__(self,playerTurn):
    self.playerTurn = playerTurn
    self.mazodescarga = []
    self.message = "Ronda: "
  
  def turn(self):
    contador = 0
    contador+=1
    print ("Ronda: " , contador) 
  
    while True:
        if self.playerTurn == nameofFirstPlayer:
            deck1.append(list.pop().information())
            print ("--" * 32)
            print(nameofFirstPlayer.namefirst())
            print (deck1)
        
        while True:
            print('''
            A -- te quedas con la carta
            B -- lanza la misma carta
        ''')
            write = input("respuesta: ")
            if write == "B":
                self.mazodescarga.append(deck1.pop())
                return deck1 , self.mazodescarga
            if write == "A":
                print (deck1)
                elige = input("Posicion de carta que deseas cambiar: ")
            
            option = ["0", "1", "2", "3", "4", "5"]
            for(i = 0; i < 6; i++):
                if (elige == option[i]):
                    self.mazodescarga.append(deck1.pop(option[i]))
                    return self.mazodescarga
                else:
                    print("No se encuentra entre los posibles numeros")
        else: 
            continue