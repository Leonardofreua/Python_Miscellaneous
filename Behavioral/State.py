#!/usr/bin/python
# -*- coding : utf-8 -*-


"""
The state design pattern is one of the twenty-three design patterns designed by the Gang of Four
that describe how to solve recurring design problems. Such problems cover the design of flexible
and reusable object-oriented software, such as objects that are easy to implement, change, test, and reuse.

*The state pattern is set to solve two main problems:

- An object should change it's behavior when it's internal state changes.
- State-specific behavior should be defined independently. That is, adding new states should not affect
the behavior of existing states.

*Implementing state-specific behavior directly within a class is inflexible because it commits the
 class to a particular behavior and makes it impossible to add a new state or change the behavior
 of an existing state later independently from (without changing) the class. In this, the pattern
 describes two solutions:

- Define separate (state) objects that encapsulate state-specific behavior for each state.
That is, define an interface (state) for performing state-specific behavior, and define classes that
implement the interface for each state.
- A class delegates state-specific behavior to it's current state object instead of implementing
state-specific behavior directly.

Reference: https://en.wikipedia.org/wiki/State_pattern
"""


class State(object):

    def scan(self):
        """Scan the dial to the next station"""
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0
        print(u"Scanning... Station is %s %s" % (self.stations[self.pos], self.name))


class AmState(State):

    def __init__(self, radio):
        self.radio = radio
        self.stations = ["1250", "1380", "1510"]
        self.pos = 0
        self.name = "AM"

    def toggle_amfm(self):
        print(u"Switching to FM")
        self.radio.state = self.radio.fmstate


class FmState(State):

    def __init__(self, radio):
        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.pos = 0
        self.name = "FM"

    def toggle_amfm(self):
        print(u"Switching to AM")
        self.radio.state = self.radio.amstate


class Radio(object):
    """ A radio.
        It has a scan button, and an AM/FM toggle switch
    """

    def __init__(self):
        """We have an AM state and an FM state"""
        self.amstate = AmState(self)
        self.fmstate = FmState(self)
        self.state = self.amstate

    def toggle_amfm(self):
        self.state.toggle_amfm()

    def scan(self):
        self.state.scan()


def main():
    radio = Radio()
    actions = [radio.scan] * 2 + [radio.toggle_amfm] + [radio.scan] * 2
    actions *= 2

    for action in actions:
        action()


if __name__ == '__main__':
    main()

# ---- OUTPUT: ---- :
#
# Scanning... Station is 1380 AM
# Scanning... Station is 1510 AM
# Switching to FM
# Scanning... Station is 89.1 FM
# Scanning... Station is 103.9 FM
# Scanning... Station is 81.3 FM
# Scanning... Station is 89.1 FM
# Switching to AM
# Scanning... Station is 1250 AM
# Scanning... Station is 1380 AM
