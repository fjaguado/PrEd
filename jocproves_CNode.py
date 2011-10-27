# -*- coding:utf-8  -*-
import inspect

print "Comprovant CNode:",
# Primer de tots s'hauria de comprovar si l'arxiu CNode.py existeix o no...

try:
	CNode = __import__("CNode")
	reload(CNode)
except:
	raise ValueError, """CNODE: No s'ha trobat l'arxiu "CNode.py" (Comproveu el nom de l'arxiu que ha de ser exactament igual)."""

# Comprovació de la declaració de la classe:
################################################################################
if len(inspect.getargspec(CNode.CNode.__init__)[0]) != 4: raise ValueError, """CNODE: El constructor de CNode ha de tenir exactament la següent capçalera: "def __init__(self, data, left, right):" """
if inspect.getargspec(CNode.CNode.__init__)[3] != None: raise ValueError, """CNODE: Als paràmetres del constructor de CNode no se'ls hi pot passar un paràmetre per defecte. El constructor ha de tenir exactament la següent capçalera: "def __init__(self, data, left, right):" """

try:
	if len(inspect.getargspec(CNode.CNode.getData)[0]) != 1: raise ValueError, """CNODE: a getData() no se li passa cap paràmetre, la seva capçalera ha de ser exactament: "def getData(self):" """
except AttributeError:
	raise ValueError, """CNODE: No s'ha trobat la funció getData(). La capçalera d'aquesta ha de ser exactament: "def getData(self):"."""
try:
	if len(inspect.getargspec(CNode.CNode.getLeft)[0]) != 1: raise ValueError, """CNODE: a getLeft() no se li passa cap paràmetre, la seva capçalera ha de ser exactament: "def getLeft(self):" """
except AttributeError:
	raise ValueError, """CNODE: No s'ha trobat la funció getLeft(). La capçalera d'aquesta ha de ser exactament: "def getLeft(self):"."""
try:
	if len(inspect.getargspec(CNode.CNode.getRight)[0]) != 1: raise ValueError, """CNODE: a getRight() no se li passa cap paràmetre, la seva capçalera ha de ser exactament: "def getRight(self):" """
except AttributeError:
	raise ValueError, """CNODE: No s'ha trobat la funció getRight(). La capçalera d'aquesta ha de ser exactament: "def getRight(self):"."""
try:
	if len(inspect.getargspec(CNode.CNode.__str__)[0]) != 1: raise ValueError, """CNODE: a __str__() no se li passa cap paràmetre, la seva capçalera ha de ser exactament: "def __str__(self):" """
except AttributeError:
	raise ValueError, """CNODE: No s'ha trobat la funció __str__(). La capçalera d'aquesta ha de ser exactament: "def __str__(self):"."""
try:
	if len(inspect.getargspec(CNode.CNode.setData)[0]) != 2: raise ValueError, """CNODE: a setData() no se li ha de passar un paràmetre, la seva capçalera ha de ser exactament: "def setData(self, data):" """
	if inspect.getargspec(CNode.CNode.setData)[3] != None: raise ValueError, """CNODE: als paràmetres de setData() no se'ls hi pot passar cap paràmetre per defecte, la seva capçalera ha de ser exactament: "def setData(self, data):" """
except AttributeError:
	raise ValueError, """CNODE: No s'ha trobat la funció setData(). La capçalera d'aquesta ha de ser exactament: "def setData(self, data):"."""
try:
	if len(inspect.getargspec(CNode.CNode.setLeft)[0]) != 2: raise ValueError, """CNODE: a setLeft() no se li ha de passar un paràmetre, la seva capçalera ha de ser exactament: "def setLeft(self, left):" """
	if inspect.getargspec(CNode.CNode.setLeft)[3] != None: raise ValueError, """CNODE: als paràmetres de setLeft() no se'ls hi pot passar cap paràmetre per defecte, la seva capçalera ha de ser exactament: "def setLeft(self, left):" """
except AttributeError:
	raise ValueError, """CNODE: No s'ha trobat la funció setLeft(). La capçalera d'aquesta ha de ser exactament: "def setLeft(self, left):"."""
	if len(inspect.getargspec(CNode.CNode.setRight)[0]) != 2: raise ValueError, """CNODE: a setRight() no se li ha de passar un paràmetre, la seva capçalera ha de ser exactament: "def setRight(self, right):" """
	if inspect.getargspec(CNode.CNode.setRight)[3] != None: raise ValueError, """CNODE: als paràmetres de setRight() no se'ls hi pot passar cap paràmetre per defecte, la seva capçalera ha de ser exactament: "def setRight(self, right):" """
except AttributeError:
	raise ValueError, """CNODE: No s'ha trobat la funció setRight(). La capçalera d'aquesta ha de ser exactament: "def setRight(self, right):"."""

# Comprovació del funcionament de la classe:
################################################################################
c = CNode.CNode(20, None, None)
if (c.getData() != 20): raise ValueError, """CNODE: No es poden recollir les dades al fer "getData()"."""
if (c.getLeft() != None): raise ValueError, """CNODE: "getLeft()" no retorna el valor correcte."""
if (c.getRight() != None): raise ValueError, """CNODE: "getRight()" no retorna el valor correcte."""
c.setData(30)
if (c.getData() != 30): raise ValueError, """CNODE: La funcio setData() no canvia el valor de __data del node."""
c.setLeft(10)
if (c.getLeft() != 10): raise ValueError, """CNODE: La funcio setLeft() no canvia el valor de __left del node."""
c.setRight(15)
if (c.getRight() != 15): raise ValueError, """CNODE: La funcio setRight() no canvia el valor de __right del node."""
c = CNode.CNode(15, 7, 9)
if (c.getLeft() != 7): raise ValueError, """CNODE: El constructor no inicialitza correctament __left."""
if (c.getRight() != 9): raise ValueError, """CNODE: El constructor no inicialitza correctament __right."""
if (c.getData() != 15): raise ValueError, """CNODE: El constructor no inicialitza correctament __data."""

if (type(str(c)) != type("")): raise ValueError, """CNODE: La funció __str__ ha de retornar una cadena de caràcters."""
print "[Correcte]"


#///////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////#////////////////////////////////////////
#/////////////////////////////////////###///////////////////////////////////////
#////////////////////////////////////#####//////////////////////////////////////
#///////////////////////////////////#######/////////////////////////////////////
#//////////////////////////////////#########////////////////////////////////////
#/////////////////////////////////###########///////////////////////////////////
#////////////////////////////////////#####//////////////////////////////////////
#////////////////////////////////////#####//////////////////////////////////////
#////////////////////////////////////#####//////////////////////////////////////
#/////////////////////////////////###########///////////////////////////////////
#//////////////////////////////////#########////////////////////////////////////
#///////////////////////////////////#######/////////////////////////////////////
#////////////////////////////////////#####//////////////////////////////////////
#/////////////////////////////////////###///////////////////////////////////////
#//////////////////////////////////////#////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////
