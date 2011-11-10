# -*- coding: cp1252 -*-
from CNode import *
from CList import *

class CQueue(CList):
  def __init__(self):
    CList.__init__(self)
  def Push(self,data):
    if self._CList__size > 0:
      CList.Last(self)
    CList.Insert(self,data,1)
      
  def Pop(self):
    CList.First(self)
    data = CList.getData(self)
    CList.Remove(self)
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
