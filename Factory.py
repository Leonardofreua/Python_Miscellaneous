#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The Factory Method design pattern is one of the twenty-three well-known 
"Gang of Four" design patterns that describe how to solve recurring 
design problems to design flexible and reusable object-oriented 
software, that is, objects that are easier to implement, change, 
test, and reuse.

*The Factory Method design pattern solves problems like:
- How can an object be created so that subclasses can redefine which class to instantiate?
- How can a class defer instantiation to subclasses?

*The Factory Method design pattern describes how to solve such problems:

- Define a separate operation (factory method) for creating an object.
- Create an object by calling a factory method.

Reference: https://en.wikipedia.org/wiki/Factory_method_pattern
"""


class Button(object):
    html = ""

class Image(Button):
    html = "<img> </img>"

class Input(Button):
    html = "<input> </input>"

class Flash(Button):
    html = "<obj> </obj>"

class ButtonFactory():
    def create_button(self, type):
        targetClass = type.capitalize()
        return globals()[targetClass]()

button_obj = ButtonFactory()
button = ['image', 'input', 'flash']
for b in button:
    print(button_obj.create_button(b).html)