from food import Food
from drink import Drink

class Inv:
    def __init__(self):
        self.inv: list[Food | Drink] = []
    def add(self, item: Food | Drink):
        self.inv.append(item)
    def rm(self, item: Food | Drink):
        self.inv.remove(item)
    def len(self) -> bool:
        return len(self.inv) > 0
    def find(self, deg: int) -> Food | Drink | None:
        for i in self.inv:
            if i.res <= deg:
                return i
        return None
    def findFood(self, deg: int) -> Food | None:
        for i in self.inv:
            if isinstance(i, Food):
                if i.res <= deg:
                    return i
        return None
    def findDrink(self, deg: int) -> Drink | None:
        for i in self.inv:
            if isinstance(i, Drink):
                if i.res <= deg:
                    return i
        return None
    def has(self, type: int) -> bool:
        for i in self.inv:
            if type == 0:
                if isinstance(i, Food):
                    return True
            if type == 1:
                if isinstance(i, Drink):
                    return True
        return False