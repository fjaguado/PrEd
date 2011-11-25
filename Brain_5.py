from pyrobot.brain import Brain
import CStack
reload(CStack)
import CPilot
reload(CPilot)
import CTree
reload(CTree)

class WB(Brain):
    def setup(self):
        self.pilot = CPilot.CPilot()
        self.stack = CStack.CStack()
        self.tree = CTree.CTree()
        self.tree.Build('/home/kserviii/CPilot/db.xml')
        self.robot.move('reset')
        self.door_locations = []
        self.door_keys = []
        
    def step(self):
        if not(self.robot.getItem('win')):
            self.pilot.setSonar(self.robot.getItem('sonar'))
            # si esta en un cruce
            if self.pilot.isCrossRoad():
		# si es un CulDeSac y la pila no esta vacia
                if self.pilot.getCulDeSac() == True and not self.stack.isEmpty():
                    accio = self.stack.Pop()# cogemos la accion de la pila
                    if accio[0] == True:
                        self.pilot.setCulDeSac(False)# ponemos a falso el CulDeSac
                    accio = self.pilot.moveTo(accio[1])
                else:
                    accions_possibles = self.pilot.possibleActions()# sino miramos las acciones posibles
                    for i in accions_possibles:# metemos en la pila las acciones posibles
                        self.stack.Push(i)
                    accio = self.stack.Pop()# como ya tenemos movimentos en la pila, cogemos uno
                    accio = self.pilot.moveTo(accio[1])
                    self.pilot.setCulDeSac(False)
            else:
                accio = self.pilot.nextMove()# si no es un cruce, nextMove
            pos = self.robot.move(accio)# cogemos la accion del robot
            if pos == 'gold':# si es oro, lo cogemos
                self.robot.move('grab')
            elif pos == 'key': # si es llave, hablamos y guardamos la informacion
                #self.robot.move('talk')
                nouAnimal = []
                while 1:
                    info = self.robot.move('talk')
                    if info != "This thing doesn't speak!":
                        nouAnimal.append(info)
                    else:
                        break
                if nouAnimal:
                    self.tree.AddData(nouAnimal)# guardamos el nuevo animal en el arbol

            elif pos == 'door':# si estamos ante una puerta
                position = self.robot.getItem('location');
                JaVist = self.JaVisitat(position)# comprobamos si ya hemos visitado la puerta
                if not JaVist:#si no hemos visitado la puerta antes, hablamos con ella
                    atributs = []                    
                    while 1:
                        info=self.robot.move('talk')
                        if info:
                            atributs.append(info)# guardamos los atributos nuevos
                        else:
                            break
                else:
                    atributs = JaVist
                animal = self.tree.GetDataClass(atributs)# recuperamos el dato
                if animal:
                    self.robot.move(animal)# si hay animal, realizamos la accion
                else:
                    self.door_locations.append(position)# sino, guardamos la posicion de la puerta
                    self.door_keys.append(atributs)# y los atributos de la misma

    def JaVisitat(self, position):
        X = range(len(self.door_locations))
        for i in X:
            if self.door_locations[i] == position:
                return self.door_keys[i]
        return None
                
                        
def INIT(engine):
    return WB('WB', engine)
