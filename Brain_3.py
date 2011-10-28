# -*- coding: cp1252 -*-
from pyrobot.brain import Brain
import CList
import CPilot
import CQueue
# recargamos por lo que pueda pasar
reload(CList)
reload(CPilot)
reload(CQueue)

class WB(Brain):
  def setup(self):
    self.counter = 0
    self.inverse = {'right' : 'left', 'down' : 'up', 'left' : 'right', 'up' : 'down'}
    self.actions = CQueue.CQueue()
    self.lastaction = None
    self.backtrace = CList.CList() #Lista donde guardaremos el mov. que tiene que hacer el robot en cada cruce para volver
    self.pilot = CPilot.CPilot()#CPilot
    self.robot.move('reset')
  def step(self):
    # si el robot no ha llegado a la salida
    if not(self.robot.getItem('win')):
      # utilizamos el sonar
      self.pilot.setSonar(self.robot.getItem('sonar'))
      # si aún queda oro por recoger
      if self.robot.getItem('golds') > 0:
	# miramos si estamos en un cruce
	if self.pilot.isCrossRoad():
	  # cogemos la accion que toque de la cola actions
	  pos = self.actions.Pop()
	  self.robot.move(self.pilot.moveTo(pos))
	  # guardamos en la lista el inverso del movimiento que acabamos de hacer
	  self.backtrace.Insert(self.inverse[self.lastaction])
	else:
	  # fijamos la variable lastaction
	  self.lastaction = self.pilot.nextMove()
	  pos = self.robot.move(self.lastaction)
	  if pos == 'gold':
	    # si la posición es oro, lo cogemos y actualizamos el contador de oro
	    self.robot.move('grab')
	    self.counter -= 1
	  if pos == 'wumpus':
	    # si es wumpus hablamos con él
	    wumpus_say = self.robot.move('talk')
	    while ( wumpus_say != "This thing doesn't speak!"):
	      # hasta que no nos diga que no tiene más que decirnos
	      # vamos guardando en nuestra cola lo que nos dice ( indicaciones )
	      self.actions.Push(wumpus_say)
	      # le volvemos a preguntar para actualizar lo que dice
	      wumpus_say = self.robot.move('talk')
      else:# self.robot.getItem
	if self.pilot.isCrossRoad():
	  # fijamos el current en el último elemento
	  self.backtrace.Last()
	  # sacamos de la lista qué tenemos que hacer
	  self.robot.move(self.pilot.moveTo(self.backtrace.getData()))
	  # eliminamos el elemento gastado de la lista
	  self.backtrace.Remove()
	else:
	  # si no es un cruce actualizamos la variable lastaction
	  self.lastaction = self.pilot.nextMove()
	  # y movemos el robot
	  self.robot.move(self.lastaction)
	  
def INIT(engine):
	return WB('WB', engine)

	