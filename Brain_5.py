from pyrobot.brain import Brain
import CStack
reload(CStack)
import CPilot
reload(CPilot)
import CTree
reload(CTree)

class WB(Brain):
    def setup(self):
        self.counter = 0
        self.backtrace = []
        self.pilot = CPilot.CPilot()
        self.stack = CStack.CStack()
        self.tree = CTree.CTree()
        self.tree.Build('/home/kserviii/CPilot/db.xml')
        self.newdata = []
        self.robot.move('reset')
        self.door_locations = []
        self.door_keys = []
        
    def step(self):
        if not(self.robot.getItem('win')):
            self.pilot.setSonar(self.robot.getItem('sonar'))
            #if self.robot.getItem('golds') >= 0:
            if self.pilot.isCrossRoad():
                if self.pilot.getCulDeSac() == True and self.stack.isEmpty() != True:
                    accio = self.stack.Pop()
                    #print 'Cul de sac'
                    if accio[0] == True:
                        self.pilot.setCulDeSac(False)
                    accio = self.pilot.moveTo(accio[1])
                else:
                    #print 'Possibles'
                    accions_possibles = self.pilot.possibleActions()
                    for i in accions_possibles:
                        self.stack.Push(i)
                    accio = self.stack.Pop()
                    accio = self.pilot.moveTo(accio[1])
                    self.pilot.setCulDeSac(False)
            else:
                #print 'nextMove'
                accio = self.pilot.nextMove()
            pos = self.robot.move(accio)
            if pos == 'gold':
                self.robot.move('grab')
            elif pos == 'key':
                #self.robot.move('talk')
                nouAnimal = []
                while 1:
                    info = self.robot.move('talk')
                    #print str(info)
                    if info != "This thing doesn't speak!":
                        nouAnimal.append(info)
                    else:
                        break
                if nouAnimal:
                    #print 'NOU ANIMAL:' + str(nouAnimal)
                    self.tree.AddData(nouAnimal)

            elif pos == 'door':
                #self.robot.move('talk')
                #self.robot.getItem('location')
                position = self.robot.getItem('location');
                JaVist = self.JaVisitat(position)
                if not JaVist:
                    atributs = []                    
                    while 1:
                        info=self.robot.move('talk')
                        if info:
                            atributs.append(info)
                        else:
                            break
                else:
                    atributs = JaVist
                animal = self.tree.GetDataClass(atributs)
                if animal:
                    self.robot.move(animal)
                else:
                    self.door_locations.append(position)
                    self.door_keys.append(atributs)

    def JaVisitat(self, position):
        X = range(len(self.door_locations))
        for i in X:
            if self.door_locations[i] == position:
                #print 'JAVIST:' + str(self.door_keys[i])
                return self.door_keys[i]
        return None
                
                        
def INIT(engine):
    return WB('WB', engine)
