from food import Food
from drink import Drink

class Section:
    def __init__(self):
        self.items: list[Food | Drink] = []
    def len(self) -> int:
        return len(self.items)
    def empty(self) -> bool:
        return self.len() == 0
    def clear(self):
        self.items = []
    def add(self, item):
        self.items.append(item)
    def rm(self, item):
        self.items.remove(item)
    def grab(self, i: int) -> Food | Drink | None:
        if i > self.len():
            return None
        return self.items[i]
    def take(self, i: int) -> Food | Drink | None:
        item = self.grab(i)
        if not item:
            return None
        self.items.pop(i)
        return item
    def hasByCost(self, cost: int) -> bool:
        return self.findByCost(cost) is not None
    def hasByRes(self, res: int) -> bool:
        return self.findByRes(res) is not None
    def has(self, res: int, cost: int) -> bool:
        return self.hasByCost(cost) and self.hasByRes(res)
    def findByCost(self, cost: int) -> Food | Drink | None:
        for i in self.items:
            if i.cost <= cost:
                return i
        return None
    def findByRes(self, res: int) -> Food | Drink | None:
        for i in self.items:
            if i.res <= res:
                return i
        return None
    def find(self, res: int, cost: int) -> Food | Drink | None:
        if self.findByRes(res) and self.findByCost(cost):
            for i in self.items:
                if i.res <= res and i.cost <= cost:
                    return i
        return None