#Inicio del programa en esta archivo se crearan las clases que utilizaremos alrededor del tiempo que estemos trabajando con este mini-proyecto.

class Carta:
  def __init__(self,valor,color,simbolo):
    self.valor = valor
    self.color = color
    self.simbolo = simbolo
    
  def devolver(self):
    return '{} {} {}'.format(self.valor,self.color,self.simbolo)

class Mazo:
    def MazoJugar(self,MazoAA):
      self.MazoAA = MazoAA

class Mazo2:
  def MazoJugar2(self,MazoAA2):
    self.MazoAA2 = MazoAA2

class PrimerJugador:
    def __init__(self,Nombre,Apellido):
      self.Nombre = Nombre
      self.Apellido= Apellido
   
    def NombrePrimer(self):
      return '{} {}'.format(self.Nombre,self.Apellido)
##revisar.
class SegundoJugador:
    def __init__(self,Nombre,Apellido):
      self.Nombre = Nombre
      self.Apellido= Apellido
   
    def NombreSegundo(self):
      return '{} {}'.format(self.Nombre,self.Apellido)



import random
lista=[]
valores = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
simbolos = [["Rojo","Corazon"],["Rojo","Diamante"],["Negra","Trebol"],["Negra","Pico"]]
for s in simbolos:
  for v in valores:
    lista.append( Carta(v,s[0],s[1]) )
# print (lista[1].color)
random.shuffle(lista)
# for i in lista:
MazoA=0
MazoA2 = 0
ListaSinP=[]
Nombre1 = input('Nombre del jugador: ')
Apellido1 = input('Apellido del jugador: ')
  
NombreDelPrimerJugador= PrimerJugador(Nombre1,Apellido1)
print(NombreDelPrimerJugador.NombrePrimer())
for i in range(0,5):
  MazoA= (lista[i].devolver())
  ListaSinP.append(MazoA)
  
  ObjetoMazo = Mazo()
  ObjetoMazo.MazoJugar(MazoA)
  print (ObjetoMazo.MazoAA)
####################"El Segundo Jugador "###################
def NoRepetir(self):
    for l in lista:
      for p in ListaSinP: 
        if lista[l].find(ListaSinP[p]):
          contador = lista.pop(ListaSinP[p])
def El(self):
    print( '{}'.format(self.contador))
    
Nombre2 = input('Nombre del segundo jugador: ')
Apellido2 = input('Apellido del segundo jugador: ')
NombreDelSegundoJugador= SegundoJugador(Nombre2,Apellido2)

print(NombreDelSegundoJugador.NombreSegundo())
for j in range(0,5):
  # for k in len(ListaSinP):
  #   lista.pop(k)
    MazoA2 = lista[j].devolver()
    random.shuffle(lista)
    ObjetoMazo2 = Mazo2()
    ObjetoMazo2.MazoJugar2(MazoA2)
    print (ObjetoMazo2.MazoAA2)

