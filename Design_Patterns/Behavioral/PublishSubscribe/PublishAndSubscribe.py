#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
The observer pattern is a software design pattern in which an object, called the subject,
maintains a list of its dependents, called observers, and notifies them automatically of any
state changes, usually by calling one of their methods.

Reference: https://hackernoon.com/observer-vs-pub-sub-pattern-50d3b27f838c
"""


class Subscriber:

    def __init__(self, name):
        self.name = name

    def update(self, message):
        print('{} got message "{}"'.format(self.name, message))


class Publisher:

    def __init__(self):
        self.subscribers = set()

    def register(self, who):
        self.subscribers.add(who)

    def unregister(self, who):
        self.subscribers.discard(who)

    def dispatch(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)
