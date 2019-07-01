#!/usr/bin/python
# -*- coding : utf-8 -*-


"""
*The Abstract Factory design pattern solves problems like:

- How can an application be independent of how its objects are created?
- How can a class be independent of how the objects it requires are created?
- How can families of related or dependent objects be created?

Creating objects directly within the class that requires the objects is inflexible because it commits the class to
particular objects and makes it impossible to change the instantiation later independently from (without having to
change) the class. It stops the class from being reusable if other objects are required, and it makes the class
hard to test because real objects can't be replaced with mock objects.

*The Abstract Factory design pattern describes how to solve such problems:

- Encapsulate object creation in a separate (factory) object. That is, define an interface (AbstractFactory)
  for creating objects, and implement the interface.

- A class delegates object creation to a factory object instead of creating objects directly.

References:
    https://en.wikipedia.org/wiki/Abstract_factory_pattern
    https://www.oodesign.com/abstract-factory-pattern.html
    https://github.com/Leonardofreua/python-patterns/blob/master/creational/abstract_factory.py
"""

import random


class PetShop(object):
    """A pet shop"""

    def __init__(self, animal_factory=None):
        """pet_factory is our abstract factory.  We can set it at will."""

        self.pet_factory = animal_factory

    def show_pet(self):
        """Creates and shows a pet using the abstract factory"""

        pet = self.pet_factory()
        print("We have a lovely {}".format(pet))
        print("It says {}".format(pet.speak()))


class Dog(object):
    def speak(self):
        return "woof"

    def __str__(self):
        return "Dog"


class Cat(object):
    def speak(self):
        return "meow"

    def __str__(self):
        return "Cat"


# Additional factories:

# Create a random animal
def random_animal():
    """Let's be dynamic!"""
    return random.choice([Dog, Cat])()


# Show pets with various factories
if __name__ == "__main__":

    # A Shop that sells only cats
    cat_shop = PetShop(Cat)
    cat_shop.show_pet()
    print("")

    # A shop that sells random animals
    shop = PetShop(random_animal)
    for i in range(3):
        shop.show_pet()
        print("=" * 20)

# ---- OUTPUT: ---- :
#
# We have a lovely Cat
# It says meow
#
# We have a lovely Cat
# It says meow
# ====================
# We have a lovely Cat
# It says meow
# ====================
# We have a lovely Dog
# It says woof
# ====================
