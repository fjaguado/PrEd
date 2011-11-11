# -*- coding: cp1252 -*-
from pyrobot.brain import Brain
import CPilot
import CStack
# recargamos por lo que pueda pasar

reload(CPilot)
reload(CStack)

class WB(Brain):
  def setup(self):
    self.counter = 0
    self.inverse = {'right' : 'left', 'down' : 'up', 'left' : 'right', 'up' : 'down'}
    #self.actions = CQueue.CQueue()
    self.lastaction = None
    #self.backtrace = CList.CList() #Lista donde guardaremos el mov. que tiene que hacer el robot en cada cruce para volver
    self.stack = CStack.CStack()
    self.pilot = CPilot.CPilot()#CPilot
    self.robot.move('reset')
  def step(self):
    # si el robot aún no ha llegado a la salida
    if not(self.robot.getItem('win')): 
      self.pilot.setSonar(self.robot.getItem('sonar')) # utilizamos el sonar
      if self.pilot.isCrossRoad():# si estamos en un cruce
	# si es un CulDeSac y la pila no está vacía
	if self.pilot.getCulDeSac() == True and self.stack.isEmpty() != True:
	  # sacamos un movimiento de la pila del estilo ( true, 'right')
	  accio = self.stack.Pop()
	  # miramos si el primer valor de la tupla es True 
	  if accio[0] == True: 
	    self.pilot.setCulDeSac(False) # ponemos CulDeSac a false
	  accio = self.pilot.moveTo(accio[1]) # cogemos el 2o valor de la tupla como próximo movimiento
	  
	else:# sino es un CulDeSac o la pila está vacía
	  #print 'Possibles'
	  # miramos los posibles movimientos
	  accions_possibles = self.pilot.possibleActions()# guardamos todos los posibles en la pila
	  for i in accions_possibles:
	    self.stack.Push(i) 
	  accio = self.stack.Pop() # sacamos un movimiento de la pila
	  accio = self.pilot.moveTo(accio[1])# movemos nuestro robot 
	  self.pilot.setCulDeSac(False)# ponemos CulDeSac a False
      else:#sino es un cruce
	  #print 'nextMove'
	  # movemos al robot al próximo movimiento
	  accio = self.pilot.nextMove()
      # miramos si es oro y lo cogemos
      pos = self.robot.move(accio)
      if pos == 'gold':
	  self.robot.move('grab')
	  
def INIT(engine):
	return WB('WB', engine)

	