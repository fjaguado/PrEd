class CTreeNode:
    __slots__ = ['__data', '__childs']
    def __init__(self, data):
        self.__data = data
        self.__childs = []
    def addChild(self, child):
        for i in self.__childs:
            if i.getData() == child.getData():
	      return 'Aquest fill ja esta'
        self.__childs.append(child)
    def getChilds(self):
        return self.__childs
    def getData(self):
        return self.__data
    def getChild(self, data):
	for i in self.__childs:
	  if i.getData() == data:
	    return i
	return None