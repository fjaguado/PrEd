# -*- coding:utf-8  -*-
import inspect

print "Comprovant CTreeNode:",

# Comprovació de la declaració de la classe:
################################################################################
try:
	CTreeNode = __import__("CTreeNode")
except:
	raise ValueError, """CTreeNode: No s'ha trobat l'arxiu "CTreeNode.py" (Comproveu el nom de l'arxiu que ha de ser exactament igual)."""

try:
	if len(inspect.getargspec(CTreeNode.CTreeNode.addChild)[0]) != 2: raise ValueError, """CTreeNode: a addChild() se li passa un paràmetre, la seva capçalera ha de ser exactament: "def addChild(self,child):" """
except AttributeError:
	raise ValueError, """CTreeNode: No s'ha trobat la funció addChild(). La capçalera d'aquesta ha de ser exactament: "def addChild(self,child):" """


try:
	if len(inspect.getargspec(CTreeNode.CTreeNode.getChilds)[0]) != 1: raise ValueError, """CTreeNode: a getChilds()  no se li passa cap paràmetre, la seva capçalera ha de ser exactament: "def getChilds(self):" """
except AttributeError:
	raise ValueError, """CTreeNode: No s'ha trobat la funció getChilds(). La capçalera d'aquesta ha de ser exactament: "def getChilds(self):" """


try:
	if len(inspect.getargspec(CTreeNode.CTreeNode.getChild)[0]) != 2: raise ValueError, """CTreeNode: a getChild()  se li passa un paràmetre, la seva capçalera ha de ser exactament: "def getChild(self,data):" """
except AttributeError:
	raise ValueError, """CTreeNode: No s'ha trobat la funció getChild(). La capçalera d'aquesta ha de ser exactament: "def getChild(self,data):" """


try:
	if len(inspect.getargspec(CTreeNode.CTreeNode.getData)[0]) != 1: raise ValueError, """CTreeNode: a getData()  no se li passa cap paràmetre, la seva capçalera ha de ser exactament: "def getData(self):" """
except AttributeError:
	raise ValueError, """CTreeNode: No s'ha trobat la funció getData(). La capçalera d'aquesta ha de ser exactament: "def getData(self):" """

    
# Comprovació del funcionament de la classe:
################################################################################

t = CTreeNode.CTreeNode('juan')
if (t.getData() != 'juan'): raise ValueError, """CNODE: No es poden recollir les dades al fer "getData()"."""
t2=CTreeNode.CTreeNode('josep')
t3=CTreeNode.CTreeNode('pere')
t4=CTreeNode.CTreeNode('marta')
t5=CTreeNode.CTreeNode('cristina')
t6=CTreeNode.CTreeNode('pere')
try:
    t.addChild(t2);
except:
    raise ValueError, """CTreeNode: addChild no funciona correctament"""
try:
    t.addChild(t3);
except:
    raise ValueError, """CTreeNode: addChild no funciona correctament"""
try:
    t.addChild(t4);
except:
    raise ValueError, """CTreeNode: addChild no funciona correctament"""
try:
    t.addChild(t5);
except:
    raise ValueError, """CTreeNode: addChild no funciona correctament"""
try:
    t.addChild(t6);
except:
    raise ValueError, """CTreeNode: addChild no funciona correctament"""

if (len(t.getChilds())!=4): raise ValueError, """CTreeNode: addChild no funciona correctament, inserta valors repetits com a fills diferents"""
if (t.getChilds()[0].getData() != 'josep'): raise ValueError, """CCTreeNode: "getChilds()" no retorna el valor correcte."""
if (t.getChilds()[1].getData() != 'pere'): raise ValueError, """CTreeNode: "getChilds()" no retorna el valor correcte."""
if (t.getChilds()[2].getData() != 'marta'): raise ValueError, """CTreeNode: "getChilds()" no retorna el valor correcte."""
if (t.getChilds()[3].getData() != 'cristina'): raise ValueError, """CTreeNode: "getChilds()" no retorna el valor correcte."""
if (t.getChild('laia')!=None): raise ValueError, """CTreeNode: "getChild()" no retorna el valor correcte."""
if (t.getChild('marta').getData().count('marta')!=1): raise ValueError, """CTreeNode: "getChild()" no retorna el valor correcte."""

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
