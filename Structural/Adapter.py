#!/usr/bin/python
# -*- coding : utf-8 -*-


"""
The adapter design pattern is one of the twenty-three well-known GoF design patterns that describe
how to solve recurring design problems to design flexible and reusable object-oriented software,
that is, objects that are easier to implement, change, test, and reuse.

*The adapter design pattern solves problems like:

- How can a class be reused that does not have an interface that a client requires?
- How can classes that have incompatible interfaces work together?
- How can an alternative interface be provided for a class?

Often an (already existing) class can't be reused only because its interface doesn't
conform to the interface clients require.

*The adapter design pattern describes how to solve such problems:

- Define a separate adapter class that converts the (incompatible) interface of a class (adapter)
into another interface (target) clients require.
- Work through an adapter to work with (reuse) classes that do not have the required interface.

Reference: https://en.wikipedia.org/wiki/Adapter_pattern
"""


class EuropeanSocketInterface:

    def voltage(self):
        pass

    def live(self):
        pass

    def neutral(self):
        pass

    def earth(self):
        pass


# Adapter
class Socket(EuropeanSocketInterface):

    def voltage(self):
        return 230

    def live(self):
        return 1

    def neutral(self):
        return -1

    def earth(self):
        return 0


# Target Interface
class USASocketInterface:

    def voltage(self):
        pass

    def live(self):
        pass

    def neutral(self):
        pass


# Adapter
class Adapter(USASocketInterface):
    __socket = None

    def __init__(self, socket):
        self.__socket = socket

    def voltage(self):
        return 110

    def live(self):
        return self.__socket.live()

    def neutral(self):
        return self.__socket.neutral()


# Client
class EletrictKettle:
    __power = None

    def __init__(self, power):
        self.__power = power

    def boil(self):
        if self.__power.voltage() > 110:
            print("Kettle on fire!")
        else:
            if self.__power.live() == 1 and self.__power.neutral() == -1:
                print("Coffee Time!")
            else:
                print("No power")


def main():
    socket = Socket()
    adapter = Adapter(socket)
    kettle = EletrictKettle(adapter)

    # Make Coffee
    kettle.boil()

    return 0


if __name__ == '__main__':
    main()

# ---- OUTPUT: ---- :
#
# Coffee Time!
