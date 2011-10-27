# -*- coding:utf-8  -*-
import inspect 
import CNode
print "Comprovant CList:"

# Comprovació de la declaració de la classe:
################################################################################
print "	1.- Comprovant capçaleres"
try:
        CList = __import__("CList")
        reload(CList)
except:
        raise ValueError, """CLIST: No s'ha trobat l'arxiu "CList.py" (Comproveu el nom de l'arxiu que ha de ser exactament igual)."""

if len(inspect.getargspec(CList.CList.__init__)[0]) != 1: raise ValueError, """CLIST: El constructor de CList no se li passa cap paràmetre, la seva capçalera ha de ser "def __init__(self):" """
try:
        if len(inspect.getargspec(CList.CList.getData)[0]) != 1: raise ValueError, """CLIST: a getData() no se li passa cap paràmetre, la seva capçalera ha de ser exactament: "def getData(self):" """
except AttributeError:
        raise ValueError, """CLIST: No s'ha trobat la funció getData(). La capçalera d'aquesta ha de ser exactament: "def getData(self):"."""
try:
        if len(inspect.getargspec(CList.CList.getSize)[0]) != 1: raise ValueError, """CLIST: a getSize() no se li passa cap paràmetre, la seva capçalera ha de ser exactament: "def getSize(self):" """
except AttributeError:
        raise ValueError, """CLIST: No s'ha trobat la funció getSize(). La capçalera d'aquesta ha de ser exactament: "def getSize(self):"."""
try:
        if len(inspect.getargspec(CList.CList.getLast)[0]) != 1: raise ValueError, """CLIST: a getLast() no se li passa cap paràmetre, la seva capçalera ha de ser exactament: "def getLast(self):" """
except AttributeError:
        raise ValueError, """CLIST: No s'ha trobat la funció getLast(). La capçalera d'aquesta ha de ser exactament: "def getLast(self):"."""
try:
        if len(inspect.getargspec(CList.CList.getFirst)[0]) != 1: raise ValueError, """CLIST: a getSizgetFirste() no se li passa cap paràmetre, la seva capçalera ha de ser exactament: "def getFirst(self):" """
except AttributeError:
        raise ValueError, """CLIST: No s'ha trobat la funció getFirst(). La capçalera d'aquesta ha de ser exactament: "def getFirst(self):"."""
try:
        if len(inspect.getargspec(CList.CList.First)[0]) != 1: raise ValueError, """CLIST: a First() no se li passa cap paràmetre, la seva capçalera ha de ser exactament: "def First(self):" """
except AttributeError:
        raise ValueError, """CLIST: No s'ha trobat la funció First(). La capçalera d'aquesta ha de ser exactament: "def First(self):"."""
try:
        if len(inspect.getargspec(CList.CList.Last)[0]) != 1: raise ValueError, """CLIST: a Last() no se li passa cap paràmetre, la seva capçalera ha de ser exactament: "def Last(self):" """
except AttributeError:
        raise ValueError, """CLIST: No s'ha trobat la funció Last(). La capçalera d'aquesta ha de ser exactament: "def Last(self):"."""
try:
        if len(inspect.getargspec(CList.CList.Left)[0]) != 1: raise ValueError, """CLIST: a Left() no se li passa cap paràmetre, la seva capçalera ha de ser exactament: "def Left(self):" """
except AttributeError:
        raise ValueError, """CLIST: No s'ha trobat la funció Left(). La capçalera d'aquesta ha de ser exactament: "def Left(self):"."""
try:
        if len(inspect.getargspec(CList.CList.Right)[0]) != 1: raise ValueError, """CLIST: a Right() no se li passa cap paràmetre, la seva capçalera ha de ser exactament: "def Right(self):" """
except AttributeError:
        raise ValueError, """CLIST: No s'ha trobat la funció Right(). La capçalera d'aquesta ha de ser exactament: "def Right(self):"."""
try:
        if len(inspect.getargspec(CList.CList.isLast)[0]) != 1: raise ValueError, """CLIST: a isLast() no se li passa cap paràmetre, la seva capçalera ha de ser exactament: "def isLast(self):" """
except AttributeError:
        raise ValueError, """CLIST: No s'ha trobat la funció isLast(). La capçalera d'aquesta ha de ser exactament: "def isLast(self):"."""
try:
        if len(inspect.getargspec(CList.CList.isFirst)[0]) != 1: raise ValueError, """CLIST: a isFirst() no se li passa cap paràmetre, la seva capçalera ha de ser exactament: "def isFirst(self):" """
except AttributeError:
        raise ValueError, """CLIST: No s'ha trobat la funció isFirst(). La capçalera d'aquesta ha de ser exactament: "def isFirst(self):"."""
try:
        if len(inspect.getargspec(CList.CList.isEmpty)[0]) != 1: raise ValueError, """CLIST: a isEmpty() no se li passa cap paràmetre, la seva capçalera ha de ser exactament: "def isEmpty(self):" """
except AttributeError:
        raise ValueError, """CLIST: No s'ha trobat la funció isEmpty(). La capçalera d'aquesta ha de ser exactament: "def isEmpty(self):"."""
try:
        if len(inspect.getargspec(CList.CList.__str__)[0]) != 1: raise ValueError, """CLIST: a __str__() no se li passa cap paràmetre, la seva capçalera ha de ser exactament: "def __str__(self):" """
except AttributeError:
        raise ValueError, """CLIST: No s'ha trobat la funció __str__(). La capçalera d'aquesta ha de ser exactament: "def __str__(self):"."""
try:
        if len(inspect.getargspec(CList.CList.Insert)[0]) != 3: raise ValueError, """CLIST: a Insert() no se li passa cap paràmetre, la seva capçalera ha de ser exactament: "def Insert(self, data, flag = 1):" """
        if inspect.getargspec(CList.CList.Insert)[2] != None: raise ValueError, """CLIST: a Insert() no se li passa cap paràmetre, la seva capçalera ha de ser exactament: "def Insert(self, data, flag = 1):" """
        if inspect.getargspec(CList.CList.Insert)[3] != (1,): raise ValueError, """CLIST: a Insert() no se li passa cap paràmetre, la seva capçalera ha de ser exactament: "def Insert(self, data, flag = 1):" """
except AttributeError:
        raise ValueError, """CLIST: No s'ha trobat la funció Insert(). La capçalera d'aquesta ha de ser exactament: "def Insert(self, data, flag = 1):"."""
try:
        if len(inspect.getargspec(CList.CList.Remove)[0]) != 1: raise ValueError, """CLIST: a Remove() no se li passa cap paràmetre, la seva capçalera ha de ser exactament: "def Remove(self):" """
except AttributeError:
        raise ValueError, """CLIST: No s'ha trobat la funció Remove(). La capçalera d'aquesta ha de ser exactament: "def Remove(self):"."""
try:
        if len(inspect.getargspec(CList.CList.__iter__)[0]) != 1: raise ValueError, """CLIST: a __iter__() no se li passa cap paràmetre, la seva capçalera ha de ser exactament: "def __iter__(self):" """
except AttributeError:
        raise ValueError, """CLIST: No s'ha trobat la funció __iter__(). La capçalera d'aquesta ha de ser exactament: "def __iter__(self):"."""
try:
        if len(inspect.getargspec(CList.CList.next)[0]) != 1: raise ValueError, """CLIST: a next() no se li passa cap paràmetre, la seva capçalera ha de ser exactament: "def next(self):" """
except AttributeError:
        raise ValueError, """CLIST: No s'ha trobat la funció next(). La capçalera d'aquesta ha de ser exactament: "def next(self):"."""


# Comprovació del funcionament de la classe:
################################################################################
print "	2.- Comprovacions amb llista buida"
try:
        l = CList.CList()
except:
        raise ValueError, """CLIST: El constructor de CList fa una exceptció."""

        # Comprovacions per una llista buida
if l.getSize() != 0: raise ValueError, """CLIST: La mida d'una llista buida ha de ser zero."""
if not l.isEmpty(): raise ValueError, """CLIST: isEmpty() no retorna True quan la llista és buida."""
try:
        a = l.getData()
        raise ValueError, """CLIST: fer getData() d'una llista buida ha de generar una excepció del tipus IndexError."""
except IndexError:
        pass
except:
        raise ValueError, """CLIST: fer getData() d'una llista buida ha de generar una excepció del tipus IndexError."""
try:
        a = l.getLast()
        raise ValueError, """CLIST: fer getLast() d'una llista buida ha de generar una excepció del tipus IndexError."""
except IndexError:
        pass
except:
        raise ValueError, """CLIST: fer getLast() d'una llista buida ha de generar una excepció del tipus IndexError."""
try:
        a = l.getFirst()
        raise ValueError, """CLIST: fer getFirst() d'una llista buida ha de generar una excepció del tipus IndexError."""
except IndexError:
        pass
except:
        raise ValueError, """CLIST: fer getFirst() d'una llista buida ha de generar una excepció del tipus IndexError."""
try:
        l.Left()
        raise ValueError, """CLIST: fer Left() d'una llista buida ha de generar una excepció del tipus IndexError."""
except IndexError:
        pass
except:
        raise ValueError, """CLIST: fer Left() d'una llista buida ha de generar una excepció del tipus IndexError."""
try:
        l.Right()
        raise ValueError, """CLIST: fer Right() d'una llista buida ha de generar una excepció del tipus IndexError."""
except IndexError:
        pass
except:
        raise ValueError, """CLIST: fer Right() d'una llista buida ha de generar una excepció del tipus IndexError."""
try:
        if type(str(l)) != type(''): raise ValueError, """CLIST: la funció __str__ sempre ha de retornar una cadena de caràcters, encara que la llista sigui buida."""
except:
        raise ValueError, """CLIST: la funció __str__ d'una llista buida ha generat una excepció. Aquesta funció sempre ha de generar una cadena de caràcters."""
try:
        for x in l:
                pass
except:
        raise ValueError, """CLIST: Error a __iter__()/next(). Recorrer una llista buida genera un error."""
try:
        l.Remove()
        raise ValueError, """CLIST: Un remove en una llista buida ha de generar un IndexError."""
except IndexError:
        pass
except:
        raise ValueError, """CLIST: Un remove en una llista buida ha de generar un IndexError."""
# ------------------------------------------------------------------------------
print "	3.- Comprovacions amb una llista d'un element"
l.Insert(-1)
try:
        d = l.getData()
except:
        raise ValueError, """CLIST: al fer getData() d'una llista amb un element és genera un excepció."""
d = l.getData()
if type(d) == type(CNode.CNode): raise ValueError, """CLIST: Al fer getData() és retorna un CNode, s'ha de retornar el contingut del CNode."""
if d != -1: raise ValueError, """CLIST: Al fer getData() no es pot recuperar el valor que s'hi havia guardat."""
try:
        d = l.getFirst()
except:
        raise ValueError, """CLIST: al fer getFirst() d'una llista amb un element és genera un excepció."""
d = l.getFirst()
if type(d) == type(CNode.CNode): raise ValueError, """CLIST: Al fer getFirst() és retorna un CNode, s'ha de retornar el contingut del CNode."""
if d != -1: raise ValueError, """CLIST: Al fer getFirst() no es pot recuperar el valor que s'hi havia guardat."""
try:
        d = l.getLast()
except:
        raise ValueError, """CLIST: al fer getLast() d'una llista amb un element és genera un excepció."""
d = l.getLast()
if type(d) == type(CNode.CNode): raise ValueError, """CLIST: Al fer getLast() és retorna un CNode, s'ha de retornar el contingut del CNode."""
if d != -1: raise ValueError, """CLIST: Al fer getLast() no es pot recuperar el valor que s'hi havia guardat."""
try:
        if not l.isLast(): raise ValueError, """CLIST: isLast() no funciona correctament per una llista amb un element."""
except:
        raise ValueError, """CLIST: isLast() genera una excepció quan es comprova una llista amb un element."""
try:
        if not l.isFirst(): raise ValueError, """CLIST: isFirst() no funciona correctament per una llista amb un element."""
except:
        raise ValueError, """CLIST: isFirst() genera una excepció quan es comprova una llista amb un element."""
if l.getSize() != 1: raise ValueError, """CLIST: La mida d'una llista amb un element ha de ser 1."""
if l.isEmpty(): raise ValueError, """CLIST: isEmpty() retorna True quan hi ha només un element."""
try:
        if type(str(l)) != type(''): raise ValueError, """CLIST: la funció __str__ sempre ha de retornar una cadena de caràcters."""
except:
        raise ValueError, """CLIST: la funció __str__ ha generat una excepció."""
try:
        for x in l:
                pass
except:
        raise ValueError, """CLIST: Error a __iter__()/next(). S'ha generat una excepció al intentar fer un bucle de la llista."""
try:
        l.Left()
        raise ValueError, """CLIST: fer Left() d'una amb un element ha de generar una excepció del tipus IndexError."""
except IndexError:
        pass
except:
        raise ValueError, """CLIST: fer Left() d'una amb un element ha de generar una excepció del tipus IndexError."""
try:
        l.Right()
        raise ValueError, """CLIST: fer Right() d'una amb un element ha de generar una excepció del tipus IndexError."""
except IndexError:
        pass
except:
        raise ValueError, """CLIST: fer Right() d'una amb un element ha de generar una excepció del tipus IndexError."""
try:
        l.Remove()
except:
        raise ValueError, """CLIST: fer un Remove() d'una llista amb un element ha generat una excepció."""
print "	4.- Comprovacions desprès d'eliminar aquest element."
# ------------------------------------------------------------------------------
if l.getSize() != 0: raise ValueError, """CLIST: La mida d'una llista buida ha de ser zero."""
if not l.isEmpty(): raise ValueError, """CLIST: isEmpty() no retorna True quan la llista és buida."""
try:
        a = l.getData()
        raise ValueError, """CLIST: fer getData() d'una llista buida ha de generar una excepció del tipus IndexError."""
except IndexError:
        pass
except:
        raise ValueError, """CLIST: fer getData() d'una llista buida ha de generar una excepció del tipus IndexError."""
try:
        a = l.getLast()
        raise ValueError, """CLIST: fer getLast() d'una llista buida ha de generar una excepció del tipus IndexError."""
except IndexError:
        pass
except:
        raise ValueError, """CLIST: fer getLast() d'una llista buida ha de generar una excepció del tipus IndexError."""
try:
        a = l.getFirst()
        raise ValueError, """CLIST: fer getFirst() d'una llista buida ha de generar una excepció del tipus IndexError."""
except IndexError:
        pass
except:
        raise ValueError, """CLIST: fer getFirst() d'una llista buida ha de generar una excepció del tipus IndexError."""
try:
        l.Left()
        raise ValueError, """CLIST: fer Left() d'una llista buida ha de generar una excepció del tipus IndexError."""
except IndexError:
        pass
except:
        raise ValueError, """CLIST: fer Left() d'una llista buida ha de generar una excepció del tipus IndexError."""
try:
        l.Right()
        raise ValueError, """CLIST: fer Right() d'una llista buida ha de generar una excepció del tipus IndexError."""
except IndexError:
        pass
except:
        raise ValueError, """CLIST: fer Right() d'una llista buida ha de generar una excepció del tipus IndexError."""
try:
        if type(str(l)) != type(''): raise ValueError, """CLIST: la funció __str__ sempre ha de retornar una cadena de caràcters, encara que la llista sigui buida."""
except:
        raise ValueError, """CLIST: la funció __str__ d'una llista buida ha generat una excepció. Aquesta funció sempre ha de generar una cadena de caràcters."""
try:
        for x in l:
                pass
except:
        raise ValueError, """CLIST: Error a __iter__()/next(). Recorrer una llista buida genera un error."""
try:
        l.Remove()
        raise ValueError, """CLIST: Un remove en una llista buida ha de generar un IndexError."""
except IndexError:
        pass
except:
        raise ValueError, """CLIST: Un remove en una llista buida ha de generar un IndexError."""
#-------------------------------------------------------------------------------
print "	5.- Comprovacions amb n elements"

try:
        for x in range(20):
                l.Insert(x)
except:
        raise ValueError, """CLIST: Error al fer Insert de 20 elements amb el flag a 1"""
value = 0
if l.getFirst() != 0: raise ValueError, """CLIST: getFirst() no retorna el valor correcte."""
if l.getLast() != 19: raise ValueError, """CLIST: getLast() no retorna el valor correcte."""
if l.getData() != 19: raise ValueError, """CLIST: getData() no retorna el valor correcte."""
l.First()
if l.getFirst() != 0: raise ValueError, """CLIST: getFirst() no retorna el valor correcte."""
l.Last()
if l.getData() != 19: raise ValueError, """CLIST: getData() no retorna el valor correcte."""
l.First()
for x in range(19):
        if l.getData() != x: raise ValueError, """CLIST: getData() no retorna el valor correcte."""
        l.Right()
if l.getData() != 19: raise ValueError, """CLIST: getData() no retorna el valor correcte."""
try:
        l.Right()
        raise ValueError, """CLIST: Right no genera un error quan s'arriba al final de la llista."""
except IndexError:
        pass
except:
        raise ValueError, """CLIST: Right no genera un error quan s'arriba al final de la llista."""
for x in range(19, 0, -1):
        if l.getData() != x: raise ValueError, """CLIST: getData() no retorna el valor correcte."""
        l.Left()
if l.getData() != 0: raise ValueError, """CLIST: getData() no retorna el valor correcte."""
try:
        l.Left()
        raise ValueError, """CLIST: Right no genera un error quan s'arriba al final de la llista."""
except IndexError:
        pass
except:
        raise ValueError, """CLIST: Right no genera un error quan s'arriba al final de la llista."""
l.First()
if l.isLast(): raise ValueError, """CLIST: isLast() retorna True quan no estem al final de la llista."""
if not l.isFirst(): raise ValueError, """CLIST: isFirst() no retorna True quan estem al principi de la llista."""
l.Right()
l.Right()
if l.getData() != 2: raise ValueError, """CLIST: Al posar-nos al principi d'una llista i fer dos Right()'s, la llista no retorna el valor correcte."""
if l.isLast(): raise ValueError, """CLIST: isLast() retorna True quan no estem al final de la llista."""
if l.isFirst(): raise ValueError, """CLIST: isFirst() retorna True quan no estem al principi de la llista."""

l.Last()
if not l.isLast(): raise ValueError, """CLIST: isLast() no retorna True quan estem al final de la llista."""
if l.isFirst(): raise ValueError, """CLIST: isFirst() retorna True quan no estem al principi de la llista."""
l.Left()
l.Left()
if l.getData() != 17: raise ValueError, """CLIST: Al posar-nos al final d'una llista i fer dos Left()'s, la llista no retorna el valor correcte."""
if l.isLast(): raise ValueError, """CLIST: isLast() retorna True quan no estem al final de la llista."""
if l.isFirst(): raise ValueError, """CLIST: isFirst() retorna True quan no estem al principi de la llista."""

l.First()
l.Right()
l.Right()
l.Right()
l.Remove()
if l.getData() != 2: raise ValueError, """CLIST: Error al esborrar el 3er element, el current hauria d'apuntar al segon però no ho fa."""
l.Last()
l.Left()
l.Left()
l.Remove()
if l.getData() != 16: raise ValueError, """CLIST: Error al esborrar el 18è element, el current hauria d'apuntar al 17è però no ho fa."""

l.First()
l.Remove()
if l.getData() != 1: raise ValueError, """CLIST: Error al esborrar el 1er element, el current hauria d'apuntar al segon però no ho fa."""
l.Last()
l.Remove()
if l.getData() != 18: raise ValueError, """CLIST: Error al esborrar el últim element, el current hauria d'apuntar al penúltim però no ho fa."""
resulting_list = [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18]
l.First()
for x in resulting_list:
        if x != l.getData(): raise ValueError, """CLIST: Error al esborrar, hi ha un """ + str(l.getData()) + " quan hi hauria d'haver un " + str(x)
        try: l.Right()
        except: pass

if len(str(l)) < len(resulting_list): raise ValueError, "Error al convertir la llista a un str (funció __str__)."
if type(str(l)) != type(''): raise ValueError, "Una llista ha de retornar una cadena de caracters."

index = 0
for x in l:
        if x != resulting_list[index]: raise ValueError, """Error al recorrer la llista (funcions __iter__/next())."""
        index += 1

l.First()
l.Right()
l.Right()
l.Right()
l.Right()
l.Right()
error_remove = False
try:
        while l.getSize() > 0 and not l.isEmpty():
                try:
                        l.Remove()
                except:
                        error_remove = True
                        raise ValueError
except:
        if error_remove: raise ValueError, "Error al intentar fer un remove"
        else:
                try:
                        l.getSize()
                except:
                        raise ValueError, "Error al intentar calcular la mida amb getSize()."
                try:
                        l.isEmpty()
                except:
                        raise ValueError, "Error al intentar calcular la mida amb getSize()."
print "	6.- Comprovacions al acabar de buidar la llista."
# ------------------------------------------------------------------------------
if l.getSize() != 0: raise ValueError, """CLIST: La mida d'una llista buida ha de ser zero."""
if not l.isEmpty(): raise ValueError, """CLIST: isEmpty() no retorna True quan la llista és buida."""
try:
        a = l.getData()
        raise ValueError, """CLIST: fer getData() d'una llista buida ha de generar una excepció del tipus IndexError."""
except IndexError:
        pass
except:
        raise ValueError, """CLIST: fer getData() d'una llista buida ha de generar una excepció del tipus IndexError."""
try:
        a = l.getLast()
        raise ValueError, """CLIST: fer getLast() d'una llista buida ha de generar una excepció del tipus IndexError."""
except IndexError:
        pass
except:
        raise ValueError, """CLIST: fer getLast() d'una llista buida ha de generar una excepció del tipus IndexError."""
try:
        a = l.getFirst()
        raise ValueError, """CLIST: fer getFirst() d'una llista buida ha de generar una excepció del tipus IndexError."""
except IndexError:
        pass
except:
        raise ValueError, """CLIST: fer getFirst() d'una llista buida ha de generar una excepció del tipus IndexError."""
try:
        l.Left()
        raise ValueError, """CLIST: fer Left() d'una llista buida ha de generar una excepció del tipus IndexError."""
except IndexError:
        pass
except:
        raise ValueError, """CLIST: fer Left() d'una llista buida ha de generar una excepció del tipus IndexError."""
try:
        l.Right()
        raise ValueError, """CLIST: fer Right() d'una llista buida ha de generar una excepció del tipus IndexError."""
except IndexError:
        pass
except:
        raise ValueError, """CLIST: fer Right() d'una llista buida ha de generar una excepció del tipus IndexError."""
try:
        if type(str(l)) != type(''): raise ValueError, """CLIST: la funció __str__ sempre ha de retornar una cadena de caràcters, encara que la llista sigui buida."""
except:
        raise ValueError, """CLIST: la funció __str__ d'una llista buida ha generat una excepció. Aquesta funció sempre ha de generar una cadena de caràcters."""
try:
        for x in l:
                pass
except:
        raise ValueError, """CLIST: Error a __iter__()/next(). Recorrer una llista buida genera un error."""
try:
        l.Remove()
        raise ValueError, """CLIST: Un remove en una llista buida ha de generar un IndexError."""
except IndexError:
        pass
except:
        raise ValueError, """CLIST: Un remove en una llista buida ha de generar un IndexError."""
#-------------------------------------------------------------------------------
print "	7.- Tornar a omplir la llista (canviant el valor del flag)."
for x in range(40):
        l.Insert(x, x % 2)

resulting_list = range(0, 40, 2) + range(39, 0, -2)
l.First()
for x in resulting_list:
        if l.getData() != x: raise ValueError, "CLIST: Error al insertar en una llista fent servir el flag a zero."
        try: l.Right()
        except: pass

print "CList: [Correcte]"

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
