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
        if not self.alive:
            return
        if self.hunger < 0 or self.thirst < 0:
            self.die()
            return
    def die(self):
        self.alive = False

person: Person = Person("John Person")