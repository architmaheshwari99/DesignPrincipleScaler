from abc import abstractmethod, ABC


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


def print_area(rectangle):
    rectangle.width = 5
    rectangle.height = 10
    print(rectangle.area())


rect = Rectangle(2, 3)
print_area(rect)  # Outputs: 6

sq = Square(4)
print_area(sq)  # This will output: 50, which is incorrect for a square.


class ShapeImproved(ABC):
    @abstractmethod
    def area(self):
        pass


class RectangleImproved(ShapeImproved):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class SquareImproved(ShapeImproved):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


def print_area_improved(shape):
    print(shape.area())


"""
Both Rectangle and Square implement the Shape interface, 
ensuring they can be used interchangeably without violating expected behavior.

"""
