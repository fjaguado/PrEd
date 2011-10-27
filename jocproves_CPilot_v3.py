# -*- coding:utf-8  -*-
import inspect 

print "Comprovant CPilot:",
# Primer de tots s'hauria de comprovar si l'arxiu existeix o no...

try:
	CPilot = __import__("CPilot")
	reload(CPilot)
except:
	raise ValueError, """CPilot: No s'ha trobat l'arxiu "CPilot.py" (Comproveu el nom de l'arxiu que ha de ser exactament igual)."""

# Comprovació de la declaració de la classe:
################################################################################
if len(inspect.getargspec(CPilot.CPilot.__init__)[0]) != 1: raise ValueError, """CPilot: El constructor de CPilot ha de tenir exactament la següent capçalera: "def __init__(self):" """

try:
	if len(inspect.getargspec(CPilot.CPilot.setSonar)[0]) != 2: raise ValueError, """CPilot: a setSonar() se li passa un paràmetre, la seva capçalera ha de ser exactament: "def setSonar(self, sonar):" """
except AttributeError:
	raise ValueError, """CPilot: No s'ha trobat la funció setSonar(). La capçalera d'aquesta ha de ser exactament: "def setSonar(self, sonar):"."""
try:
	if len(inspect.getargspec(CPilot.CPilot.isCrossRoad)[0]) != 1: raise ValueError, """CPilot: a isCrossRoad() no se li passa cap paràmetre, la seva capçalera ha de ser exactament: "def isCrossRoad(self):" """
except AttributeError:
	raise ValueError, """CPilot: No s'ha trobat la funció isCrossRoad(). La capçalera d'aquesta ha de ser exactament: "def isCrossRoad(self):"."""
try:
	if len(inspect.getargspec(CPilot.CPilot.getCulDeSac)[0]) != 1: raise ValueError, """CPilot: a getCulDeSac() no se li passa cap paràmetre, la seva capçalera ha de ser exactament: "def getCulDeSac(self):" """
except AttributeError:
	raise ValueError, """CPilot: No s'ha trobat la funció getCulDeSac(). La capçalera d'aquesta ha de ser exactament: "def getCulDeSac(self):"."""
try:
	if len(inspect.getargspec(CPilot.CPilot.setCulDeSac)[0]) != 2: raise ValueError, """CPilot: a setCulDeSac() se li passa un paràmetre, la seva capçalera ha de ser exactament: "def setCulDeSac(self, culdesac):" """
	if inspect.getargspec(CPilot.CPilot.setCulDeSac)[3] != None: raise ValueError, """CPilot: als paràmetres de setCulDeSac() no se'ls hi pot passar cap paràmetre per defecte, la seva capçalera ha de ser exactament: "def setCulDeSac(self, culdesac):" """
except AttributeError:
	raise ValueError, """CPilot: No s'ha trobat la funció setCulDeSac(). La capçalera d'aquesta ha de ser exactament: "def setCulDeSac(self, culdesac):"."""
try:
	if len(inspect.getargspec(CPilot.CPilot.moveTo)[0]) != 2: raise ValueError, """CPilot: a moveTo() se li ha de passar un paràmetre, la seva capçalera ha de ser exactament: "def moveTo(self, action):" """
	if inspect.getargspec(CPilot.CPilot.moveTo)[3] != None: raise ValueError, """CPilot: als paràmetres de moveTo() no se'ls hi pot passar cap paràmetre per defecte, la seva capçalera ha de ser exactament: "def moveTo(self, action):" """
except AttributeError:
	raise ValueError, """CPilot: No s'ha trobat la funció moveTo(). La capçalera d'aquesta ha de ser exactament: "def moveTo(self, action):"."""
try:
	if len(inspect.getargspec(CPilot.CPilot.nextMove)[0]) != 1: raise ValueError, """CPilot: a nextMove() no se li ha de passar cap paràmetre, la seva capçalera ha de ser exactament: "def nextMove(self):" """
except AttributeError:
	raise ValueError, """CPilot: No s'ha trobat la funció nextMove(). La capçalera d'aquesta ha de ser exactament: "def nextMove(self):"."""



# Comprovació del funcionament de la classe:
################################################################################
msg2 = """CPilot: La funció nextMove no actualitza correctament la variable membre 'self.__previous'."""
msg3 = """CPilot: La funció nextMove ha de posar a True la variable membre 'self.__culdesac' quan el robot arriba a un cul de sac."""
p=CPilot.CPilot()
inverse = {'right' : 'left', 'down' : 'up', 'left' : 'right', 'up' : 'down'}
for i in inverse.keys():
    for j in inverse.keys():
        s={'right' : 1, 'down' : 1, 'left' : 1, 'up' : 1}
        p.setSonar(s)
        p.moveTo(inverse[i])
        s={'right' : 0, 'down' : 0, 'left' : 0, 'up' : 0}
        s[i]=1
        s[j]=1
        p.setSonar(s)
        tmp=p.nextMove()
        msg1 = """CPilot: La funció nextMove no retorna el moviment correcte en el cas d'un sonar """ + str(s) + """ i acabant de fer un '""" + str(inverse[i]) + """', en lloc d'un '""" + str(j) + """' retorna un '""" + str(tmp) + """'."""
        if tmp!=j: raise ValueError, msg1
        if p._CPilot__previous != tmp: raise ValueError, msg2
        s[p._CPilot__previous] = 0
        if s.values().count(True) == 0 and p._CPilot__culdesac != True: raise ValueError, msg3


#raise ValueError, """CPilot: No es poden recollir les dades al fer "getData()"."""
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
