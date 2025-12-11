class Person:
  def __init__(self, name):
    self.__name = name
    self.__food = 100
    self.__water = 100
  def feed(self, amount):
    self.__food += amount
  def starve(self, amount):
    self.__food -= amount
  def name(self):
    return self.__name
  def food(self):
    return self.__food
  def water(self):
    return self.__water
