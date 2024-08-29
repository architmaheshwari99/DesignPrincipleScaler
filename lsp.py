class Bird:
    def fly(self):
        return "I can fly!"


class Sparrow(Bird):
    def fly(self):
        return "Sparrow flying!"


class Ostrich(Bird):
    def fly(self):
        raise NotImplementedError("Ostrich can't fly!")


# Function that uses the Bird class
def make_bird_fly(bird: Bird):
    return bird.fly()


# Now let's test it
sparrow = Sparrow()
ostrich = Ostrich()

print(make_bird_fly(sparrow))  # Output: "Sparrow flying!"
print(make_bird_fly(ostrich))  # Output: NotImplementedError

"""
the Ostrich class now adheres to the Liskov Substitution Principle because it 
doesn’t override a method in a way that breaks the expected behavior. 
The design is also improved by introducing a FlyingBird class for birds that can 
fly, allowing Sparrow to inherit from it and Ostrich to remain a subclass of Bird 
without implementing fly

"""


class Bird:
    def move(self):
        return "I can move!"


class FlyingBird(Bird):
    def fly(self):
        return "I can fly!"


class Sparrow(FlyingBird):
    def fly(self):
        return "Sparrow flying!"


class Ostrich(Bird):
    def move(self):
        return "Ostrich running!"


# Function that uses the Bird class
def make_bird_move(bird: Bird):
    return bird.move()


# Function that uses the FlyingBird class
def make_bird_fly(bird: FlyingBird):
    return bird.fly()


# Now let's test it
sparrow = Sparrow()
ostrich = Ostrich()

print(make_bird_move(sparrow))  # Output: "I can move!"
print(make_bird_fly(sparrow))  # Output: "Sparrow flying!"
print(make_bird_move(ostrich))  # Output: "Ostrich running!"
