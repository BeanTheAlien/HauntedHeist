class Person:
    def __init__(self, name: str):
        self.name: str = name
        self.hunger: int = 100
        self.thirst: int = 100
        self.bored: int = 0
        self.danger: int = 0
        self.tired: int = 0
        self.alive: bool = True
    def upd(self):
        if self.isDead():
            return
        if self.hunger < 0 or self.thirst < 0:
            self.die()
            return
        if not self.inDanger():
            if self.isHungry() or self.isThirsty():
                pass
            elif self.isTired():
                pass
            elif self.isBored():
                pass
        else:
            pass
    def die(self):
        self.alive = False
    def isHungry(self) -> bool: return self.hunger < 70
    def isThirsty(self) -> bool: return self.thirst < 70
    def isBored(self) -> bool: return self.bored > 40
    def inDanger(self) -> bool: return self.danger > 30
    def isTired(self) -> bool: return self.tired > 60
    def isDead(self) -> bool: return not self.alive

person: Person = Person("John Person")