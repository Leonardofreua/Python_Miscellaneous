#!/usr/bin/python
# -*- coding : utf-8 -*-


"""
Some programs require a large number of objects that have some shared state among them. Consider for example a
game of war, were there is a large number of soldier objects; a soldier object maintain the graphical representation
of a soldier, soldier behavior such as motion, and firing weapons, in addition soldiers health and location on the
war terrain. Creating a large number of soldier objects is a necessity however it would incur a huge memory cost.
Note that although the representation and behavior of a soldier is the same their health and location can vary greatly.

Reference: https://www.oodesign.com/flyweight-pattern.html
"""


import abc


class FlyweightFactory:
    """
    Create and manage flyweight objects.
    Ensure that flyweights are shared properly. When a client requests a
    flyweight, the FlyweightFactory object supplies an existing instance
    or creates one, if none exists.
    """

    def __init__(self):
        self._flyweights = {}

    def get_flyweight(self, key):
        try:
            flyweight = self._flyweights[key]
        except KeyError:
            flyweight = ConcreteFlyweight()
            self._flyweights[key] = flyweight
        return flyweight


class Flyweight(metaclass=abc.ABCMeta):
    """
    Declare an interface through which flyweights can receive and act on
    extrinsic state.
    """

    def __init__(self):
        self.intrinsic_state = None

    @abc.abstractmethod
    def operation(self, extrinsic_state):
        pass


class ConcreteFlyweight(Flyweight):
    """
    Implement the Flyweight interface and add storage for intrinsic
    state, if any. A ConcreteFlyweight object must be sharable. Any
    state it stores must be intrinsic; that is, it must be independent
    of the ConcreteFlyweight object's context.
    """

    def operation(self, extrinsic_state):
        pass


def main():
    flyweight_factory = FlyweightFactory()
    concrete_flyweight = flyweight_factory.get_flyweight("key")
    concrete_flyweight.operation(None)


if __name__ == "__main__":
    main()

# ---- OUTPUT: ---- :
#
