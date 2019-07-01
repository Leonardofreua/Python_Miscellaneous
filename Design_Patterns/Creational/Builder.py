#!/usr/bin/python
# -*- coding : utf-8 -*-

"""
*The Builder design pattern solves problems like:

- How can a class (the same construction process) create different 
  representations of a complex object?
- How can a class that includes creating a complex object be simplified?

Creating and assembling the parts of a complex object directly within a 
class is inflexible. It commits the class to creating a particular 
representation of the complex object and makes it impossible to change 
the representation later independently from (without having to change) the class.

*The Builder design pattern describes how to solve such problems:

Encapsulate creating and assembling the parts of a complex object in a 
separate Builder object.
A class delegates object creation to a Builder object instead of creating
the objects directly.
"""

# Abstract Building
class Building(object):
    def __init__(self):
        self.build_floor()
        self.build_size()

    def build_floor(self):
        raise NotImplementedError

    def build_size(self):
        raise NotImplementedError

    def __repr__(self):
        return 'Floor: {0.floor} | Size: {0.size}'.format(self)


# Concrete Buildings
class House(Building):
    def build_floor(self):
        self.floor = 'One'

    def build_size(self):
        self.size = 'Big'


class Flat(Building):
    def build_floor(self):
        self.floor = 'More than One'

    def build_size(self):
        self.size = 'Small'


# App
if __name__ == "__main__":
    house = House()
    flat = Flat()

    print(house)
    print(flat)

# ---- OUTPUT: ---- :
#
# Floor: One | Size: Big
# Floor: More than One | Size: Small