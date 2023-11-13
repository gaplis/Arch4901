# 3) Переписать код в соответствии с Interface Segregation Principle:
# Подсказка: круг не объемная фигура и этому классу не нужен метод volume().

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class ICube(ABC):
    @abstractmethod
    def volume(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 2 * math.pi * self.radius


class Cube(Shape, ICube):
    def __init__(self, edge):
        self.edge = edge

    def area(self):
        return 6 * self.edge * self.edge

    def volume(self):
        return self.edge * self.edge * self.edge
