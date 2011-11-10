# -*- coding: cp1252 -*-
from CNode import *
from CList import *

class CStack(CList):
  def __init__(self):
    CList.__init__(self)
  def Push(self,data):
    if self._CList__size > 0:
      CList.Last(self)
    CList.Insert(self,data,1)
      
  def Pop(self):
    if self._CList__size == 0:
      raise IndexError, "Cola vacía"
    else:
      #CList.First(self)
      data = CList.getData(self)
      CList.Remove(self)
      return data  
  
  def __str__(self):
    text = ''
    for x in self:
      text += str(x)
    return str(text)
  def __iter__(self):
      # Ponemos iter en la primera posición de la pila
      self._CList__iter = self._CList__last
      # Devolvemos la lista entera, es decir, self. 
      return self
  def next(self):
    try:
      # Guardamos iter en una variable auxiliar
      aux = self._CList__iter
      # Movemos iter una posición a la derecha
      self._CList__iter = aux.getLeft()
      # devuelve en contenido del apuntador aux
      return aux.getData()
    except:
      raise StopIteration
    
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