from CTreeNode import *

class CTree:
    __slots__ = ['__root','__labels']
    def __init__(self):
        self.__root = CTreeNode(None)
        self.__labels = ['<tipus>','<catsize>','<domestic>','<tail>','<legs>','<fins>','<venomous>','<breathes>','<backbone>','<toothed>','<predator>','<aquatic>','<airborne>','<milk>','<eggs>','<feathers>','<hair>','<name>']
    def Build (self,filename):
        fileHandle = open(filename, 'r')
        fileList = fileHandle.readlines()
        #print fileList
        maxim = range(len(fileList))
        for i in maxim:
	    #para cada linea quitamos caracteres \r\n
            fileList[i] = fileList[i].rstrip('\r\n')
        self.parser(fileList, 1, 0, self.__root)
    def AddData(self, features):
        self.addDataRecursive(features,0,self.__root)
    def GetDataClass(self, features):
        node_actual = self.__root
        index = 0
        # mientras el nodo al que apunta tenga algo y no hayamos llegado al final de las features
        while ( node_actual != None ) and ( index < len(features)):
            node_actual = node_actual.getChild(features[index])#obtenemos el hijo
            index = index+1 # aumentamos el indice
        if node_actual == None:
            return None # retornem None
        else:
            return node_actual.getChilds()[0].getData() # si hay datos devolvemos los datos a los que hemos llegado
    def parser(self, list,linenum,depth,nodeact):
	# mientras queden elementos en la lista
        while ( (depth < len(self.__labels) ) and ( list[linenum] == self.__labels[depth] ) ):
            dada = list[linenum+1] # el dato es una posicion delante
            node = CTreeNode(dada) # creamos un nuevo nodo del arbol con el dato que hemos cogido
            nodeact.addChild(node) # se lo anyadimos como hijo al nodo actual
            node = nodeact.getChild(dada) # actualiazamos el nodo actual
            linenum = self.parser(list,linenum+2,depth+1,node)+1 #llamamos al parser recursivamente
        return linenum
    def addDataRecursive(self, features, featurenum, nodeact):
        if featurenum < len(features):
            node = CTreeNode(features[featurenum])
            nodeact.addChild(node)
            node = nodeact.getChild(features[featurenum])
            self.addDataRecursive(features, featurenum+1, node)
