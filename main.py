from functools import total_ordering
from Tasks.tasks3.test import *


@total_ordering
class Technics:
    __slots__ = ('name', 'price', 'availability')

    def __init__(self, name, price, availability):
        self.name = name
        self.price = price
        self.availability = availability

    @property
    def category(self):
        return "Дорогой" if self.price > 1000 else "Бюджетный"

    def __dir__(self):
        return ['name', 'price', 'availability', 'category']

    def __len__(self):
        return len(self.name)

    def __eq__(self, other):
        return len(self) == len(other)

    def __lt__(self, other):
        return len(self) < len(other)


# Пример для тестирования класса Technics
laptop1 = Technics("Ноутбук", 20000, True)
laptop2 = Technics("Смартфон", 800, True)
print(laptop1.category)
if laptop1 > laptop2:
    print("Название техники", laptop1.name, "длиннее, чем название техники", laptop2.name)
else:
    print("Название техники", laptop2.name, "длиннее, чем название техники", laptop1.name)





