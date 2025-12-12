class Person:
  def __init__(self, name):
    self.__name = name
    self.__food = 100
    self.__water = 100
  def feed(self, amount: int):
    self.__food += amount
  def starve(self, amount: int):
    self.__food -= amount
  
  def name(self) -> str:
    """
    Returns the name of the person.
    
    :param self: This person.
    :return: The name.
    :rtype: str
    """
    return self.__name
  def food(self) -> int:
    """
    Returns the current percent food level of the person.
    
    :param self: This person.
    :return: The food level.
    :rtype: int
    """
    return self.__food
  def water(self) -> int:
    """
    Returns the current percent water level of the person.
    
    :param self: This person.
    :return: The water level.
    :rtype: int
    """
    return self.__water
