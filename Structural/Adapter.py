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

- Define a separate adapter class that converts the (incompatible) interface of a class (adaptee)
into another interface (target) clients require.
- Work through an adapter to work with (reuse) classes that do not have the required interface.

Reference: https://en.wikipedia.org/wiki/Adapter_pattern
"""


