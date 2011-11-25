class CTreeNode:
    __slots__ = ['__data', '__childs']
    def __init__(self, data):
        self.__data = data
        self.__childs = []
    def addChild(self, child):
        for i in self.__childs:
            if i.getData() == child.getData():#si ya tenemos este valor guardado
	      return 'Aquest fill ja esta'
        self.__childs.append(child) # sino anyadimos el hijo
    def getChilds(self):
        return self.__childs
    def getData(self):
        return self.__data
    def getChild(self, data):
	for i in self.__childs:
	  if i.getData() == data: # si tenemos el dato guardado
	    return i # devolvemos el hijo que lo tiene
	return None # sino devolvemos None