# -*- coding:utf-8  -*-
import inspect 

print "Comprovant CPilot2:",
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

try:
	if len(inspect.getargspec(CPilot.CPilot.possibleActions)[0]) != 1: raise ValueError, """CPilot: a possibleActions() no se li ha de passar cap paràmetre, la seva capçalera ha de ser exactament: "def possibleActions(self):" """
except AttributeError:
	raise ValueError, """CPilot: No s'ha trobat la funció possibleActions(). La capçalera d'aquesta ha de ser exactament: "def possibleActions(self):"."""



# Comprovació del funcionament de la classe:
################################################################################
p=CPilot.CPilot()
inverse = {'right' : 'left', 'down' : 'up', 'left' : 'right', 'up' : 'down'}
print ''
for i in inverse.keys():
    for j in inverse.keys():
	s={'right' : 1, 'down' : 1, 'left' : 1, 'up' : 1}
	p.setSonar(s)
	p.moveTo(inverse[i])
	actions = p.possibleActions()
	if actions[0] != (0, i):
            raise ValueError, """ possibleActions ha de retornar (0, direccio de retorn) com a primer element de la llista"""
        l=['right','left','up','down']
        l.pop(l.index(i))
        for k in actions[1:]:
            if k[0]!=1:
                raise ValueError, """ possibleActions ha de retornar (1,direccio) per totes les direccions que no siguin les de retorn"""
            try:
                l.pop(l.index(k[1]))
            except:
                raise ValueError, """possibleActions retorna una acció desconeguda. """                         
        if l != []:
            raise ValueError, """ possibleActions retorna mes coses del compte. """
        s={'right' : 0, 'down' : 0, 'left' : 0, 'up' : 0}
	s[i]=1
	s[j]=1
	p.setSonar(s)
	tmp=p.nextMove()
	msg1 = """CPilot: La funció nextMove no retorna el moviment correcte en el cas d'un sonar """ + str(s) + """ i acabant de fer un '""" + str(inverse[i]) + """', en lloc d'un '""" + str(j) + """' retorna un '""" + str(tmp) + """'."""
	if tmp!=j: raise ValueError, msg1
	if sum(s.values()) == 1 and p.getCulDeSac() != True:
	    raise ValueError, """La funció nextMove no posa la variable __culdesac a True quan arriba a un cul de sac."""
        if i!=j:
            for x in s:
                if s[x] == 0:
                    p.setSonar({'right' : 1, 'down' : 1, 'left' : 1, 'up' : 1})
                    p.moveTo(inverse[i])
                    sn = dict(s)
                    sn[x] = 1
                    p.setSonar(sn)
                    actions = p.possibleActions()
                    if actions[0] != (0, i):
                        raise ValueError, """ possibleActions ha de retornar (0, direccio de retorn) com a primer element de la llista"""
                    l = [i, j, x]
                    l.pop(l.index(i))
                    for k in actions[1:]:
                        if k[0]!=1:
                            raise ValueError, """ possibleActions ha de retornar (1,direccio) per totes les direccions que no siguin les de retorn"""
                        try:
                            l.pop(l.index(k[1]))
                        except:
                            raise ValueError, """possibleActions retorna una acció desconeguda. """                         
                    if l != []:
                        raise ValueError, """ possibleActions retorna mes coses del compte. """

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
