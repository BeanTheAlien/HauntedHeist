class Person:
  def __init__(self, name: str):
    self.name: str = name
    self.food: int = 100
    self.water: int = 100
    self.bored: int = 0
    self.danger: int = 0
    self.tired: int = 0
    self.money: int = 1000

    self.Food = self.attrib("food")
    self.Water = self.attrib("water")
    self.Bored = self.attrib("bored")
    self.Danger = self.attrib("danger")
    self.Tired = self.attrib("tired")
    self.Money = self.attrib("money")

    self.eat = self.act("eat", lambda: self.food <= 70, "food", 10)
  
  def attrib(self, attName: str):
    return lambda amt = None : self.att(attName, amt if amt else 0)
  def att(self, attName: str, amt: int):
    self.apnd(attName, amt)
    return self.get(attName)
  
  def act(self, nm: str, cond, prop: str, amt: int):
    self.set(nm, cond)
    self.set(nm.title(), lambda: self.apnd(prop, amt))
  
  def add(self, attName: str, amt: int):
    self.apnd(attName, amt)
    self.clamp(attName, 100)
  
  def get(self, attName: str):
    return getattr(self, attName)
  def set(self, attName: str, val):
    setattr(self, attName, val)
  def apnd(self, attName: str, val):
    self.set(attName, self.get(attName) + val)
  def clamp(self, attName: str, lim: int):
    v = self.get(attName)
    self.set(attName, lim if v > lim else v)
  
  def __str__(self):
    return f"-- Person --\nName: \"{self.name}\"\nFood: {self.food}\nWater: {self.water}"

person = Person("Hello World")
print(person)
person.Food(2)
print(person.Food())