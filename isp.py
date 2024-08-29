from abc import ABC, abstractmethod


class Worker:
    def work(self):
        pass

    def eat(self):
        pass


class Workable(ABC):
    @abstractmethod
    def work(self):
        pass


class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass


class Human(Workable, Eatable):
    def work(self):
        print("Human is working")

    def eat(self):
        print("Human is eating")


class Robot(Workable):
    def work(self):
        print("Robot is working")


"""
Separate interfaces (Workable and Eatable) ensure that classes only implement what they need, 
following ISP.
"""
