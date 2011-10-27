# -*- coding: cp1252 -*-
from CNode import *

class CList(object):
  __slots__=['__size', '__first', '__last', '__current', '__iter']
  # Constructor
  def __init__(self):
    self.__size = 0
    self.__first = None
    self.__last = None
    self.__current = None
    self.__iter = None
  # Recollir dades de la llista
  def getData(self):
    if self.__size == 0:
      raise IndexError, "Lista vacia"
    else:
      return self.__current.getData()
      
  def getSize(self):
    return self.__size
  def getLast(self):
    if self.__last == None or self.__size == 0:
      raise IndexError, "No hay elemento final"
    else:
      return self.__last.getData()
      
  def getFirst(self):
    if self.__first == None or self.__size == 0:
      raise IndexError, "No hay primer elemento"
    else:
      return self.__first.getData()
  # Funcions per moure el __current
  def First(self):
    if self.__size == 0: 
      raise IndexError, "Lista vacia, no se puede ir al principio"
    elif self.__first == self.__current:
      print "Ya estamos al principio de la lista"
    else:
      self.__current = self.__first
      
  def Last(self):
    if self.__size == 0:
      raise IndexError, "Lista vacia, no se puede ir al final"
    elif self.__last == self.__current:
      print "Ya estamos al final"
    else:
      self.__current = self.__last
      
  def Left(self):
    if self.__size == 0:
      raise IndexError, "Lista vacia, no se puede ir a la izquierda"
    elif self.__current == self.__first:
      raise IndexError, "Estamos al principio, no se puede ir a la izquierda"
    else:
      self.__current = self.__current.getLeft()
        
  def Right(self):
    if self.__size == 0:
      raise IndexError, "Lista vacia, no se puede ir a la derecha"
    elif self.__current == self.__last:
      raise IndexError, "Estamos al final. No podemos ir a la derecha"
    else:
      self.__current = self.__current.getRight()
  # Funcions per comprovar l'estat de la llista.
  def isLast(self):
    if self.__current == self.__last:
      return True
    else:
      return False
      
  def isFirst(self):
    if self.__current == self.__first:
      return True
    else:
      return False
      
  def isEmpty(self):
    if self.__size == 0:
      return True
    else:
      return False
  # Funcions d'inserció/esborrat de dades
  def Insert(self, data, flag = 1):
    node = CNode(data,None,None)
    if self.__size == 0:
      self.__current = self.__first = self.__last = node
      self.__size += 1
    elif flag == 0:
      self.__size += 1
      #####################
      #add a la izquierda #
      #####################
      #como insertamos a izquierda, el nodo derecho sera current
      node.setRight(self.__current)
      #cogemos el nodo izquierdo a current
      if self.__current != self.__first:
	leftApunt = self.__current.getLeft()
	#se lo asignamos al node
	node.setLeft(leftApunt)
	#asignamos node al que antes era nodo izquierdo de current
	leftApunt.setRight(node)
      #asignamos node como nodo a la izquierda de current
      self.__current.setLeft(node)
      #y asignamos current al nuevo node
      if self.__current == self.__first:
	self.__current = node
	self.__first = self.__current
      else:
	self.__current = node
    elif flag == 1:
      self.__size += 1
      #####################
      #add a la derecha   #
      #####################
      #como insertamos a la derecha, el nodo izquierdo sera current
      node.setLeft(self.__current)
      if self.__last != self.__current:
	rightApunt = self.__current.getRight()
	#se lo asignamos a node
	node.setRight(rightApunt)
	#asignamos node al que antes era nodo derecho de current
	rightApunt.setLeft(node)
      #asignamos node como nodo a la derecha de current
      self.__current.setRight(node)
      #y asignamos current al nuevo node
      if self.__current == self.__last:
	self.__current = node
	self.__last = self.__current
      else:
	self.__current = node
    else:
      print 'Flag erroneo'
      
  def Remove(self):
    if self.__size == 0:
            raise IndexError, "Lista vacia"
    elif self.__size == 1:
      # si solo hay 1 elemento, lo borramos y decrementamos size
      self.__current.setData(None)
      self.__current = None
      self.__size -= 1
    #si hay mas de 2 elementos se pueden dar 3 situaciones
    elif self.__size >= 2:
      # que sea el primer elemento, por lo tanto no tiene nodo a la izquierda del que preocuparse
      if self.__current == self.__first:
	self.__size -= 1
	# cogemos el que tenemos a la derecha que acabara siendo el first
	rightApunt = self.__current.getRight()
	# borramos los datos y apuntadores del current
	self.__current.setRight(None)
	self.__current.setData(None)
	# eliminamos el apuntador que apunta a nuestro current
	rightApunt.setLeft(None)
	# cambiamos el current por su elemento de la derecha
	self.__current = rightApunt
	# y asignamos como primero el que acabamos de convertir en current
	self.__first = self.__current
      # que sea el ultimo elemento, por lo tanto no tiene nodo a la derecha del que preocuparse
      elif self.__current == self.__last:
	self.__size -= 1
	# cogemos el que tenemos a la izquierda que acabara siendo el last
	leftApunt = self.__current.getLeft()
	# borramos los datos y apuntadores del current
	self.__current.setLeft(None)
	self.__current.setData(None)
	# eliminamos el apuntador que apunta a nuestro current
	leftApunt.setRight(None)
	# cambiamos el current por su elemento de la izquierda
	self.__current = leftApunt
	# y asignamos como last el que acabamos de convertir en current
	self.__last = self.__current
      else:
	#elemento de por el medio
	self.__size -= 1
	# cogemos los apuntadores de derecha e izquierda
	leftApunt = self.__current.getLeft()
	rightApunt = self.__current.getRight()
	# eliminamos datos y apuntadores
	self.__current.setLeft(None)
	self.__current.setRight(None)
	self.__current.setData(None)
	# hacemos que se apunten mutuamente los de derecha <-> izquierda saltando el nodo que hemos borrado
	leftApunt.setRight(rightApunt)
	rightApunt.setLeft(leftApunt)
	# y ponemos como current el nodo de la izquierda
	self.__current = leftApunt;
  # Iteradors
  def __iter__(self):
    self.__iter = self.__first
    return self
    
  def next(self):
    try:
      aux = self.__iter
      self.__iter = self.__iter.getRight()
      return aux.getData()
    except:
      raise StopIteration

    # Funció per convertir la llista en una cadena de caracters.
  def __str__(self):
    if self.__size == 0:
      text = 'Lista vacia'
    else:
      text = ''
      for x in self:
	text += str(x)
    return text
