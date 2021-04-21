from abc import ABC, abstractmethod

class Tela(ABC):
  @abstractmethod
  def __init__(self, controlador):
    self.__controlador = controlador
    self.__window = None

  @property
  def window(self):
    return self.__window #verificar

  @abstractmethod
  def tela_opcoes(self):
    pass

  @property
  def controlador(self):
    return self.__controlador
