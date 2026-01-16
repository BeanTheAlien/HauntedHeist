from food import Food
from drink import Drink
from malwart_section import Section

class Malwart:
    def __init__(self):
        self.secs: list[Section] = []
    def add(self, sec: Section):
        self.secs.append(sec)
    def rm(self, sec: Section):
        self.secs.remove(sec)
    def has(self, sec: Section) -> bool:
        return sec in self.secs
    def len(self) -> int:
        return len(self.secs)
    def at(self, i: int) -> Section | None:
        if i > self.len():
            return None
        return self.secs[i]
    def findByRes(self, res: int) -> Food | Drink | None:
        for i in self.secs:
            if i.hasByRes(res):
                return i.findByRes()
        return None
    def findByCost(self, cost: int) -> Food | Drink | None:
        for i in self.secs:
            if i.hasByCost(cost):
                return i.findByCost(cost)
        return None
    def find(self, res: int, cost: int) -> Food | Drink | None:
        for i in self.secs:
            if i.has(res, cost):
                return i.find(res, cost)
        return None
    def findInByRes(self, sec: Section, res: int) -> Food | Drink | None:
        if sec.hasByRes(res):
            return sec.findByRes(res)
        return None
    def findInByCost(self, sec: Section, cost: int) -> Food | Drink | None:
        if sec.hasByCost(cost):
            return sec.findByCost(cost)
        return None
    def findIn(self, sec: Section, res: int, cost: int) -> Food | Drink | None:
        if sec.has(res, cost):
            return sec.find(res, cost)
        return None