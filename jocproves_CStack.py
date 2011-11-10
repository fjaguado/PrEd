# -*- coding:utf-8  -*-
import inspect
print "Comprovant CStack:",

import CNode
import CList

# Comprovació de la declaració de la classe:
################################################################################

try:
	CStack = __import__("CStack")
	reload(CStack)
except:
	raise ValueError, """CSTACK: No s'ha trobat l'arxiu "CStack.py" (Comproveu el nom de l'arxiu que ha de ser exactament igual)."""

try:
	if len(inspect.getargspec(CStack.CStack.Push)[0]) != 2: raise ValueError, """CSTACK: a Push() se li passa un paràmetre, la seva capçalera ha de ser exactament: "def Push(self,valor):" """
except AttributeError:
	raise ValueError, """CSTACK: No s'ha trobat la funció Push(). La capçalera d'aquesta ha de ser exactament: "def Push(self,valor):" """

try:
	if len(inspect.getargspec(CStack.CStack.Pop)[0]) != 1: raise ValueError, """CSTACK: a Pop() no se li passa cap paràmetre, la seva capçalera ha de ser exactament: "def Pop(self):" """
except AttributeError:
	raise ValueError, """CSTACK: No s'ha trobat la funció Pop(). La capçalera d'aquesta ha de ser exactament: "def Pop(self):" """

try:
	if len(inspect.getargspec(CStack.CStack.__str__)[0]) != 1: raise ValueError, """CSTACK: a __str__() no se li passa cap paràmetre, la seva capçalera ha de ser exactament: "def __str__(self):" """
except AttributeError:
	raise ValueError, """CSTACK: No s'ha trobat la funció __str__(). La capçalera d'aquesta ha de ser exactament: "def __str__(self):" """

try:
	if len(inspect.getargspec(CStack.CStack.__iter__)[0]) != 1: raise ValueError, """CSTACK: a __iter__() no se li passa cap paràmetre, la seva capçalera ha de ser exactament: "def __iter__(self):" """
except AttributeError:
	raise ValueError, """CSTACK: No s'ha trobat la funció __iter__(). La capçalera d'aquesta ha de ser exactament: "def __iter__(self):" """

try:
	if len(inspect.getargspec(CStack.CStack.next)[0]) != 1: raise ValueError, """CSTACK: a next() no se li passa cap paràmetre, la seva capçalera ha de ser exactament: "def next(self):" """
except AttributeError:
	raise ValueError, """CSTACK: No s'ha trobat la funció next(). La capçalera d'aquesta ha de ser exactament: "def next(self):" """



s=CStack.CStack()
try:
    s.First()
    raise ValueError, """CSTACK: a First() no s'ha de poder cridar la funció First desde una pila"""
except AttributeError:
    pass
except:
    raise ValueError, """CSTACK: a First() al cridar la funció First desde una pila hem de retornar un AttributeError"""
    
try:
    s.Last()
    raise ValueError, """CSTACK: a Last() no s'ha de poder cridar la funció Last desde una pila"""
except AttributeError:
    pass
except:
    raise ValueError, """CSTACK: a Last() al cridar la funció Last desde una pila hem de retornar un AttributeError"""

try:
    s.Right()
    raise ValueError, """CSTACK: a Right() no s'ha de poder cridar la funció Right desde una pila"""
except AttributeError:
    pass
except:
    raise ValueError, """CSTACK: a Right() al cridar la funció Right desde una pila hem de retornar un AttributeError"""

try:
    s.Left()
    raise ValueError, """CSTACK: a Left() no s'ha de poder cridar la funció Left desde una pila"""
except AttributeError:
    pass
except:
    raise ValueError, """CSTACK: a Left() al cridar la funció Left desde una pila hem de retornar un AttributeError"""

try:
    s.getData()
    raise ValueError, """CSTACK: a getData() no s'ha de poder cridar la funció getData desde una pila"""
except AttributeError:
    pass
except:
    raise ValueError, """CSTACK: a getData() al cridar la funció getData desde una pila hem de retornar un AttributeError"""

try:
    s.getLast() 
    raise ValueError, """CSTACK: a getLast() no s'ha de poder cridar la funció getLast desde una pila"""
except AttributeError:
    pass
except:
    raise ValueError, """CSTACK: a getLast() al cridar la funció getLast desde una pila hem de retornar un AttributeError"""

try:
    s.getFirst()
    raise ValueError, """CSTACK: a getFirst() no s'ha de poder cridar la funció getFirst desde una pila"""
except AttributeError:
    pass
except:
    raise ValueError, """CSTACK: a getFirst() al cridar la funció getFirst desde una pila hem de retornar un AttributeError"""

try:
    s.isLast()
    raise ValueError, """CSTACK: a isLast() no s'ha de poder cridar la funció isLast desde una pila"""
except AttributeError:
    pass
except:
    raise ValueError, """CSTACK: a isLast() al cridar la funció isLast desde una pila hem de retornar un AttributeError"""

try:
    s.isFirst()
    raise ValueError, """CSTACK: a isFirst() no s'ha de poder cridar la funció isFirst desde una pila"""
except AttributeError:
    pass
except:
    raise ValueError, """CSTACK: a isFirst() al cridar la funció isFirst desde una pila hem de retornar un AttributeError"""

try:
    s.Insert(4,1)
    raise ValueError, """CSTACK: a Insert() no s'ha de poder cridar la funció Insert desde una pila"""
except AttributeError:
    pass
except:
    raise ValueError, """CSTACK: a Insert() al cridar la funció Insert desde una pila hem de retornar un AttributeError"""

try:
    s.Remove()
    raise ValueError, """CSTACK: a Remove() no s'ha de poder cridar la funció Remove desde una pila"""
except AttributeError:
    pass
except:
    raise ValueError, """CSTACK: a Remove() al cridar la funció Remove desde una pila hem de retornar un AttributeError"""


# Comprovació del funcionament de la classe:
################################################################################

try:
    s.Push(1)
except:
    raise ValueError, """CSTACK: a Push() salta un error al intentar fer un push"""
try:
    s.Push(2)
except:
    raise ValueError, """CSTACK: a Push() salta un error al intentar fer un push"""
try:
    s.Push(3)
except:
    raise ValueError, """CSTACK: a Push() salta un error al intentar fer un push"""
try:
    s.Push(4)
except:
    raise ValueError, """CSTACK: a Push() salta un error al intentar fer un push"""
try:
    w4=s.Pop()
except:
    raise ValueError, """CSTACK: a Pop() salta un error al intentar fer un pop"""

try:
    w3=s.Pop()
except:
    raise ValueError, """CSTACK: a Pop() salta un error al intentar fer un pop"""

try:
    w2=s.Pop()
except:
    raise ValueError, """CSTACK: a Pop() salta un error al intentar fer un pop"""

try:
    w1=s.Pop()
except:
    raise ValueError, """CSTACK: a Pop() salta un error al intentar fer un pop"""

if ((w4!=4) or (w3!=3) or (w2!=2) or(w1!=1)): raise ValueError, """CSTACK: a Pop() el Pop no retorna l'element esperat"""


try:
    w=s.Pop()
    raise ValueError, """CSTACK: a Pop() al intentar treure elements d'una pila buida hem de llançar un IndexError"""
except IndexError:
    pass

try:
    w0=s.Pop()
    raise ValueError, """CSTACK: a Pop() al intentar treure elements d'una pila buida hem de llançar un IndexError"""
except IndexError:
    pass



try:
    s.Push(1)
    s.Push('a')
    s.Push(9.4)
    s.Push([1,2,3])
    s.Push((3,4))
except:
    raise ValueError, """CSTACK: a Push() salta un error al intentar fer un push"""

if (type(str(s)) != type("")): raise ValueError, """CStack: La funció __str__ ha de retornar una cadena de caràcters."""

cont=0
l=[(3,4),[1,2,3],9.4,'a',1]
for i in s:
    if i != l[cont]:
        raise ValueError, """CStack: El recorregut d'una pila amb un for no funciona com esperat."""
    cont +=1

if cont != 5: raise ValueError, """CStack: El recorregut d'una pila amb un for no funciona com esperat."""

s2=CStack.CStack()
try:
    s2.Push(1)
    s2.Push('a')
    s2.Push(6)
    s2.Push(6)
    s2.Pop()
    s2.Push(9)
    s2.Pop()
    s2.Pop()
    s2.Push(9.4)
    s2.Push([1,2,3])
    s2.Push(5)
    s2.Pop()
    s2.Pop()
    s2.Push([1,2,3])    
    s2.Push((3,4))
except:
    raise ValueError, """CSTACK: a Push() salta un error al intentar fer un push"""

cont=0
l=[(3,4),[1,2,3],9.4,'a',1]
for i in s2:
    if i != l[cont]:
        raise ValueError, """CStack: El recorregut d'una pila amb un for no funciona com esperat."""
    cont +=1

if cont != 5: raise ValueError, """CStack: El recorregut d'una pila amb un for no funciona com esperat."""

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
