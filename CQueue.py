# -*- coding: cp1252 -*-
from CNode import *
from CList import *

class CQueue(CList):
  def __init__(self):
    CList.__init__(self)
  def Push(self,data):
    node = CNode(data,None,None)
    if self._CList__size == 0:
      # ponemos el primer y ultimo a nuestro nodo
      self._CList__first = self._CList__last = node
    else:
      # apuntamos a la izquierda al ultimo nodo que habia antes
      node.setLeft(self._CList__last)
      # a la derecha no habra nada
      node.setRight(None)
      # al ultimo nodo le asignamos a la derecha el nodo que vamos a añadir
      self._CList__last.setRight(node)
      # finalmente ponemos el nuevo nodo como último nodo
      self._CList__last = node
    # incrementamos size  
    self._CList__size += 1
      
  def Pop(self):
    if self._CList__size == 0:
      raise IndexError, "Queue vacia"
    else:
      data = self._CList__first.getData()
      if self._CList__size == 1:
	# al ser el único elemento, fijamos first y last a None
	self._CList__first = self._CList__last = None
      else:
	# como es una cola, sacamos siempre por delante
	# pillamos el derecho del Nodo a sacar
	rightNode = self._CList__first.getRight()
	# asignamos a None el derecho del nodo a sacar
	self._CList__first.setRight(None)
	# asignamos el que será primero, que es el que era derecho del que sacamos
	self._CList__first = rightNode
	# y por último dejamos a None el left del actual, el primero no tiene nadie a la izquierda
	self._CList__first.setLeft(None)
      
    self._CList__size -= 1
    return data
  def First(self):
    raise AttributeError, "¡Función no definida en CQueue!"
  def Last(self):
    raise AttributeError, "¡Función no definida en CQueue!"
  def Right(self):
    raise AttributeError, "¡Función no definida en CQueue!"
  def Left(self):
    raise AttributeError, "¡Función no definida en CQueue!"
  def getData(self):
    raise AttributeError, "¡Función no definida en CQueue!"
  def getLast(self):
    raise AttributeError, "¡Función no definida en CQueue!"
  def getFirst(self):
    raise AttributeError, "¡Función no definida en CQueue!"
  def isLast(self):
    raise AttributeError, "¡Función no definida en CQueue!"
  def isFirst(self):
    raise AttributeError, "¡Función no definida en CQueue!"
  def Insert(self, data, flag = 1):
    raise AttributeError, "¡Función no definida en CQueue!"
  def Remove(self):
    raise AttributeError, "¡Función no definida en CQueue!"
