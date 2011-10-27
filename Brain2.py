from pyrobot.brain import Brain
import CPilot
reload(CPilot)

class WB(Brain):
  def setup(self):
    self.inverse = {'right' : 'left', 'down' : 'up', 'left' : 'right', 'up' : 'down'}
    self.actions = ['left', 'up', 'up', 'left']
    self.lastaction = None
    self.backtrace = [] #Lista donde guardaremos el mov. que tiene que hacer el robot en cada cruce para volver
    self.pilot = CPilot.CPilot()#CPilot
    self.robot.move('reset')
  def step(self):
    if not(self.robot.getItem('win')):#si el robot no ha llegado a la salida
      self.pilot.setSonar(self.robot.getItem('sonar'))#utilizamos el sonar
      if self.robot.getItem('golds') > 0:#si queda ORO entramos
	if self.pilot.isCrossRoad(): #si nos encontramos un cruce entramos
	  self.backtrace.append(self.inverse[self.lastaction])# insertamos el movimiento inverso para volver
	  #print 'backtrace='+str(self.backtrace)
	  self.lastaction = self.actions.pop()# extraemos el movimiento
	  #print 'actions='+str(self.actions)
	  self.robot.move(self.lastaction)# movemos el robot
	  self.pilot.moveTo(self.lastaction)# actualizamos variables internas CPilot
	else:# sino hay cruce 
	  self.lastaction = self.pilot.nextMove()
	  pos = self.robot.move(self.lastaction)
	  if pos == 'gold': # 
	    self.robot.move('grab')
      else: #si no queda oro
	if self.pilot.isCrossRoad() == True:
	  self.robot.move(self.pilot.moveTo(self.backtrace.pop()))#empezamos a sacar movimientos a la inversa
	else:#y si no esta en un cruce
	  self.lastaction = self.pilot.nextMove()#actualiza la variable lastaction con el movimiento siguiente
	  self.robot.move(self.lastaction)#y lo mueve
	  
def INIT(engine):
	return WB('WB', engine)
