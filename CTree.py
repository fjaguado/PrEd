from CTreeNode import *

class CTree:
    __slots__ = ['__root','__labels']
    def __init__(self):
        self.__root = CTreeNode(None)
        self.__labels = ['<tipus>','<catsize>','<domestic>','<tail>','<legs>','<fins>','<venomous>','<breathes>','<backbone>','<toothed>','<predator>','<aquatic>','<airborne>','<milk>','<eggs>','<feathers>','<hair>','<name>']
    def Build (self,filename):
        fileHandle = open(filename, 'r')
        fileList = fileHandle.readlines()
        print fileList
        #self.parser(fileList, 1, 0, self.__root)
        maxim = range(len(fileList))
        for i in maxim:
	    #print fileList[i][-2:]
            #if fileList[i][-2:] == '\n':
            fileList[i] = fileList[i].rstrip('\r\n')
            #print fileList[i]
        self.parser(fileList, 1, 0, self.__root)
    def AddData(self, features):
        self.addDataRecursive(features,0,self.__root)
    def GetDataClass(self, features):
        node_actual = self.__root
        index = 0
        print "========"
        while ( node_actual != None ) and ( index < len(features)):
	    print node_actual.getData()
            node_actual = node_actual.getChild(features[index])
            index = index+1
        if node_actual == None:
            return None
        else:
            return node_actual.getChilds()[0].getData()
    def parser(self, list,linenum,depth,nodeact):
        while ( (depth < len(self.__labels) ) and ( list[linenum] == self.__labels[depth] ) ):
            dada = list[linenum+1]
            node = CTreeNode(dada)
            nodeact.addChild(node)
            node = nodeact.getChild(dada)
            linenum = self.parser(list,linenum+2,depth+1,node)+1
        return linenum
    def addDataRecursive(self, features, featurenum, nodeact):
        if featurenum < len(features):
            node = CTreeNode(features[featurenum])
            nodeact.addChild(node)
            node = nodeact.getChild(features[featurenum])
            self.addDataRecursive(features, featurenum+1, node)
