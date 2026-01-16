from inv import Inv
from food import Food
from drink import Drink
import random

class Person:
  def __init__(self, name: str):
    self.name: str = name
    self.hunger: int = 100
    self.thirst: int = 100
    self.bored: int = 0
    self.danger: int = 0
    self.tired: int = 0
    self.money: int = 1000
    self.inv: Inv = Inv()
    self.state: int = 1
  
  # main
  def act(self):
    if self.state == 0:
      return
    if self.hunger < 0 or self.thirst < 0:
      self.state = 0
      return
    self.tick()
    # minimal danger level (ignorable)
    if not self.inDanger():
      if self.isHungry() or self.isThirsty():
        if self.inv.len():
          if self.isHungry():
            item = self.inv.findFood(100 - self.hunger)
            if item:
              self.cons(item)
          if self.isThirsty():
            item = self.inv.findDrink(100 - self.thirst)
            if item:
              self.cons(item)
      elif self.isTired():
        self.sleep()
      elif self.isBored():
        pass
    else:
      pass
  def tick(self):
    self.hunger -= 1
    self.thirst -= 1
  
  # actions
  def eat(self, fd: Food):
    self.hunger += fd.res
  def drink(self, dr: Drink):
    self.thirst += dr.res
  def cons(self, item: Food | Drink):
    if isinstance(item, Food):
      self.hunger += item.res
    else:
      self.thirst += item.res
    self.inv.rm(item)
  def sleep(self):
    self.tired -= self.ran(10, 30)
  def fun(self):
    self.bored -= self.ran(10, 30)
  def work(self):
    self.bored += self.ran(10, 30)
  
  # stat checks
  def isHungry(self) -> bool:
    return self.hunger < 70
  def isThirsty(self) -> bool:
    return self.thirst < 70
  def inDanger(self) -> bool:
    return self.danger > 10
  def isTired(self) -> bool:
    return self.tired > 70
  def isBored(self) -> bool:
    return self.bored > 70
  
  # utils
  def ran(self, a: int, b: int) -> int:
    return random.randint(a, b)
  
  def __str__(self):
    return f"-- Person --\nName: \"{self.name}\"\nFood: {self.hunger}\nWater: {self.thirst}"

person = Person("Hello World")