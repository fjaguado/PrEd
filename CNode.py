class CNode(object):
  __slots__ = ['__data', '__left', '__right']
  def __init__(self, data, left, right):
    self.__data = data
    self.__left = left
    self.__right = right
  def __str__(self):
    if self.__data is None:
      return '(EmptyNode)'
    else:
      return '(' + str(self.__data) + ')'
  def getData(self):
    return self.__data
  def setData(self,data):
    self.__data = data
  def getLeft(self):
    return self.__left
  def setLeft(self,left):
    self.__left = left
  def getRight(self):
    return self.__right
  def setRight(self,right):
    self.__right = right
