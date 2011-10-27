class CPilot(object):
    __slot__ = ['__previous', '__sonar', '__inverse', '__culdesac'];

    def __init__(self):
        self.__previous = None
        self.__sonar = {'right' : 0, 'down' : 0, 'left' : 0, 'up' : 0}
        self.__inverse = {'right' : 'left', 'down' : 'up', 'left' : 'right', 'up' : 'down'}
        self.__culdesac = False
        
    def setCulDeSac(self, culdesac):
        self.__culdesac = culdesac == True

    def getCulDeSac(self):
        return self.__culdesac

    def setSonar(self, sonar):
        self.__sonar = sonar

    def isCrossRoad(self):
        if self.__sonar.values().count(True) >= 3:
            return True
        else:
            return False
        
    def moveTo(self, action):
        if not self.__inverse.has_key(action):
            raise ValueError ('Unknown robot action')
        if self.__sonar[action] > 0:
            self.__previous = action
            return action
        else:
            raise ValueError ('Imposible motion')
    def nextMove(self):
        # copiamos el sonar 
        motions = dict(self.__sonar)
        print motions
        #miramos si es el principio, es decir, no hay previo
        if self.__previous != None:
            # si no es el principio ponemos el inverso del previo a False
            motions[self.__inverse[self.__previous]] = False
            # si hay 4 False es obvio, CULDESAC
	if motions.values().count(False) == 4:
	    self.setCulDeSac(True)
	    # asi que volvemos por donde vinimos
	    action = self.__inverse[self.__previous]
	    self.__previous = action;
	    return action
	else:
	    # sino para cada opcion de motions miramos que movimiento podemos hacer
	    for key in motions.keys():
		if motions[key] == True:
		    #action = key
		    self.__previous = key;
		    return key
