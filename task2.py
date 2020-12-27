from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def cloth_am(self):
        pass


class Coat(Clothes):

    def __init__(self, size):
        self.size = size

    @property
    def cloth_am(self):
        return self.size/6.5 + 0.5


class Costume(Clothes):

    def __init__(self, height):
        self.height = height

    @property
    def cloth_am(self):
        return 2 * self.height + 0.3


coat_a = Coat(52)
costume_a = Costume(1.70)

print(coat_a.cloth_am + costume_a.cloth_am)
