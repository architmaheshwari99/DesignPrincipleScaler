from abc import ABC, abstractmethod


class Shape:
    def draw(self, shape_type):
        if shape_type == "circle":
            print("Drawing a circle")
        elif shape_type == "square":
            print("Drawing a square")


"""
The Shape class is now open for extension (by adding new shapes) but closed for modification. 
New shapes can be added by creating new classes that implement the Shape interface.

"""


class ShapeImproved(ABC):
    @abstractmethod
    def draw(self):
        pass


class Circle(ShapeImproved):
    def draw(self):
        print("Drawing a circle")


class Square(ShapeImproved):
    def draw(self):
        print("Drawing a square")
