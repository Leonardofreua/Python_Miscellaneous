#!/usr/bin/python
# -*- coding : utf-8 -*-

"""
The Decorator design pattern is one of the twenty-three well-known GoF design patterns
that describe how to solve recurring design problems to design flexible and reusable object-oriented
software, that is, objects that are easier to implement, change, test, and reuse.

*What problems can the Decorator design pattern solve?

- Responsibilities should be added to (and removed from) an object dynamically at run-time.
- A flexible alternative to subclassing for extending functionality should be provided.
When using subclassing, different subclasses extend a class in different ways. But an extension
is bound to the class at compile-time and can't be changed at run-time.

*What solution does the Decorator design pattern describe?

Define Decorator objects that

- implement the interface of the extended (decorated) object (Component) transparently by forwarding
all requests to it and
- perform additional functionality before/after forwarding a request.
"""

from __future__ import print_function


class TextTag(object):
    """Represents a base text tag"""

    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text


class BoldWrapper(TextTag):
    """Wraps a tag in <b>"""

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return "<b>{}</b>".format(self._wrapped.render())


class ItalicWrapper(TextTag):
    """Wraps a tag in <i>"""

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return "<i>{}</i>".format(self._wrapped.render())


if __name__ == '__main__':
    simple_hello = TextTag("hello, world!")
    special_hello = ItalicWrapper(BoldWrapper(simple_hello))
    print("before:", simple_hello.render())
    print("after:", special_hello.render())

# ---- OUTPUT: ---- :
#
# before: hello, world!
# after: <i><b>hello, world!</b></i>
