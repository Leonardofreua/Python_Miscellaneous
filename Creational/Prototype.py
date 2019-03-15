#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
*The Prototype design pattern solves problems like:

-How can objects be created so that which objects to create can be specified at run-time?
-How can dynamically loaded classes be instantiated?

Creating objects directly within the class that requires (uses) the objects is inflexible 
because it commits the class to particular objects at compile-time and makes it impossible 
to specify which objects to create at run-time.

*The Prototype design pattern describes how to solve such problems:

- Define a Prototype object that returns a copy of itself.
- Create new objects by copying a Prototype object.

Reference: https://en.wikipedia.org/wiki/Prototype_pattern
"""

import copy


class Prototype(object):

    value = 'default'

    def clone(self, **attrs):
        obj = self.__class__()
        obj.__dict__.update(attrs)
        return obj


class PrototypeDispatcher(object):
    def __init__(self):
        self._objects = {}

    def get_objects(self):
        """Get all objects"""
        return self._objects

    def register_object(self, name, obj):
        """Register an object"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """Unregister an object"""
        del self._objects[name]


def main():
    dispatcher = PrototypeDispatcher()
    prototype = Prototype()

    x = prototype.clone()
    y = prototype.clone(value='y-value', category='y')
    z = prototype.clone(value='z-value', is_checked=True)
    dispatcher.register_object('Object(x)', x)
    dispatcher.register_object('Object(y)', y)
    dispatcher.register_object('Default', z)
    print([{n: p.value} for n, p in dispatcher.get_objects().items()])

if __name__ == '__main__':
    main()

# ---- OUTPUT: ---- :
#
# [{'Object(x)': 'default'}, {'Object(y)': 'y-value'}, {'Default': 'z-value'}]