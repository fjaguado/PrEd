# -*- coding:utf-8  -*-
import inspect
import CNode
import CList

print "Comprovant CQueue:",

# Comprovació de la declaració de la classe:
################################################################################

try:
	CQueue = __import__("CQueue")
	reload(CQueue)
except:
	raise ValueError, """CQueue: No s'ha trobat l'arxiu "CQueue.py" (Comproveu el nom de l'arxiu que ha de ser exactament igual)."""

try:
	if len(inspect.getargspec(CQueue.CQueue.Push)[0]) != 2: raise ValueError, """CQueue: a Push() se li passa un paràmetre, la seva capçalera ha de ser exactament: "def Push(self,valor):" """
except AttributeError:
	raise ValueError, """CQueue: No s'ha trobat la funció Push(). La capçalera d'aquesta ha de ser exactament: "def Push(self,valor):" """

try:
	if len(inspect.getargspec(CQueue.CQueue.Pop)[0]) != 1: raise ValueError, """CQueue: a Pop() no se li passa cap paràmetre, la seva capçalera ha de ser exactament: "def Pop(self):" """
except AttributeError:
	raise ValueError, """CQueue: No s'ha trobat la funció Pop(). La capçalera d'aquesta ha de ser exactament: "def Pop(self):" """

try:
	if len(inspect.getargspec(CQueue.CQueue.__str__)[0]) != 1: raise ValueError, """CQueue: a __str__() no se li passa cap paràmetre, la seva capçalera ha de ser exactament: "def __str__(self):" """
except AttributeError:
	raise ValueError, """CQueue: No s'ha trobat la funció __str__(). La capçalera d'aquesta ha de ser exactament: "def __str__(self):" """

try:
	if len(inspect.getargspec(CQueue.CQueue.__iter__)[0]) != 1: raise ValueError, """CQueue: a __iter__() no se li passa cap paràmetre, la seva capçalera ha de ser exactament: "def __iter__(self):" """
except AttributeError:
	raise ValueError, """CQueue: No s'ha trobat la funció __iter__(). La capçalera d'aquesta ha de ser exactament: "def __iter__(self):" """

try:
	if len(inspect.getargspec(CQueue.CQueue.next)[0]) != 1: raise ValueError, """CQueue: a next() no se li passa cap paràmetre, la seva capçalera ha de ser exactament: "def next(self):" """
except AttributeError:
	raise ValueError, """CQueue: No s'ha trobat la funció next(). La capçalera d'aquesta ha de ser exactament: "def next(self):" """



q=CQueue.CQueue()
try:
    q.First()
    raise ValueError, """CQueue: a First() no s'ha de poder cridar la funció First desde una cua"""
except AttributeError:
    pass
except:
    raise ValueError, """CQueue: a First() al cridar la funció First desde una cua hem de retornar un AttributeError"""
    
try:
    q.Last()
    raise ValueError, """CQueue: a Last() no s'ha de poder cridar la funció Last desde una cua"""
except AttributeError:
    pass
except:
    raise ValueError, """CQueue: a Last() al cridar la funció Last desde una cua hem de retornar un AttributeError"""

try:
    q.Right()
    raise ValueError, """CQueue: a Right() no s'ha de poder cridar la funció Right desde una cua"""
except AttributeError:
    pass
except:
    raise ValueError, """CQueue: a Right() al cridar la funció Right desde una cua hem de retornar un AttributeError"""

try:
    q.Left()
    raise ValueError, """CQueue: a Left() no s'ha de poder cridar la funció Left desde una cua"""
except AttributeError:
    pass
except:
    raise ValueError, """CQueue: a Left() al cridar la funció Left desde una cua hem de retornar un AttributeError"""

try:
    q.getData()
    raise ValueError, """CQueue: a getData() no s'ha de poder cridar la funció getData desde una cua"""
except AttributeError:
    pass
except:
    raise ValueError, """CQueue: a getData() al cridar la funció getData desde una cua hem de retornar un AttributeError"""

try:
    q.getLast() 
    raise ValueError, """CQueue: a getLast() no s'ha de poder cridar la funció getLast desde una cua"""
except AttributeError:
    pass
except:
    raise ValueError, """CQueue: a getLast() al cridar la funció getLast desde una cua hem de retornar un AttributeError"""

try:
    q.getFirst()
    raise ValueError, """CQueue: a getFirst() no s'ha de poder cridar la funció getFirst desde una cua"""
except AttributeError:
    pass
except:
    raise ValueError, """CQueue: a getFirst() al cridar la funció getFirst desde una cua hem de retornar un AttributeError"""

try:
    q.isLast()
    raise ValueError, """CQueue: a isLast() no s'ha de poder cridar la funció isLast desde una cua"""
except AttributeError:
    pass
except:
    raise ValueError, """CQueue: a isLast() al cridar la funció isLast desde una cua hem de retornar un AttributeError"""

try:
    q.isFirst()
    raise ValueError, """CQueue: a isFirst() no s'ha de poder cridar la funció isFirst desde una cua"""
except AttributeError:
    pass
except:
    raise ValueError, """CQueue: a isFirst() al cridar la funció isFirst desde una cua hem de retornar un AttributeError"""

try:
    q.Insert(4,1)
    raise ValueError, """CQueue: a Insert() no s'ha de poder cridar la funció Insert desde una cua"""
except AttributeError:
    pass
except:
    raise ValueError, """CQueue: a Insert() al cridar la funció Insert desde una cua hem de retornar un AttributeError"""

try:
    q.Remove()
    raise ValueError, """CQueue: a Remove() no s'ha de poder cridar la funció Remove desde una cua"""
except AttributeError:
    pass
except:
    raise ValueError, """CQueue: a Remove() al cridar la funció Remove desde una cua hem de retornar un AttributeError"""


# Comprovació del funcionament de la classe:
################################################################################

try:
    q.Push(1)
except:
    raise ValueError, """CQueue: a Push() salta un error al intentar fer un push"""
try:
    q.Push(2)
except:
    raise ValueError, """CQueue: a Push() salta un error al intentar fer un push"""
try:
    q.Push(3)
except:
    raise ValueError, """CQueue: a Push() salta un error al intentar fer un push"""
try:
    q.Push(4)
except:
    raise ValueError, """CQueue: a Push() salta un error al intentar fer un push"""
try:
    w4=q.Pop()
except:
    raise ValueError, """CQueue: a Pop() salta un error al intentar fer un pop"""

try:
    w3=q.Pop()
except:
    raise ValueError, """CQueue: a Pop() salta un error al intentar fer un pop"""

try:
    w2=q.Pop()
except:
    raise ValueError, """CQueue: a Pop() salta un error al intentar fer un pop"""

try:
    w1=q.Pop()
except:
    raise ValueError, """CQueue: a Pop() salta un error al intentar fer un pop"""

if ((w4!=1) or (w3!=2) or (w2!=3) or(w1!=4)): raise ValueError, """CQueue: a Pop() el Pop no retorna l'element esperat"""


try:
    w=q.Pop()
    raise ValueError, """CQueue: a Pop() al intentar treure elements d'una cua buida hem de llançar un IndexError"""
except IndexError:
    pass

try:
    w0=q.Pop()
    raise ValueError, """CQueue: a Pop() al intentar treure elements d'una cua buida hem de llançar un IndexError"""
except IndexError:
    pass



try:
    q.Push(1)
    q.Push('a')
    q.Push(9.4)
    q.Push([1,2,3])
    q.Push((3,4))
except:
    raise ValueError, """CQueue: a Push() salta un error al intentar fer un push"""

if (type(str(q)) != type("")): raise ValueError, """CQueue: La funció __str__ ha de retornar una cadena de caràcters."""

cont=0
l=[1,'a',9.4,[1,2,3],(3,4)]
for i in q:
    if i != l[cont]:
        raise ValueError, """CQueue: El recorregut d'una cua amb un for no funciona com esperat."""
    cont +=1

if cont != 5: raise ValueError, """CQueue: El recorregut d'una cua amb un for no funciona com esperat."""

q2=CQueue.CQueue()
try:
    q2.Push(1)
    q2.Push('a')
    q2.Push(9.4)
    q2.Pop()
    q2.Pop()
    q2.Push(5)
    q2.Push(7)
    q2.Pop()
    q2.Pop()
    q2.Pop()
    q2.Push(1)
    q2.Push('a')
    q2.Push(9.4)
    q2.Push([1,2,3])
    q2.Push((3,4))
except:
    raise ValueError, """CQueue: a Push() salta un error al intentar fer un push"""

cont=0
l=[1,'a',9.4,[1,2,3],(3,4)]
for i in q2:
    if i != l[cont]:
        raise ValueError, """CQueue: El recorregut d'una cua amb un for no funciona com esperat."""
    cont +=1

if cont != 5: raise ValueError, """CQueue: El recorregut d'una cua amb un for no funciona com esperat."""

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
