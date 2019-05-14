#!/usr/bin/python
# -*- coding : utf-8 -*-


"""
The Visitor design pattern is one of the twenty-three well-known GoF design patterns
that describe how to solve recurring design problems to design flexible and reusable object-oriented
software, that is, objects that are easierto implement, change, test, and reuse.

*What problems can the Visitor design pattern solve?

- It should be possible to define a new operation for (some) classes of an object structure without
  changing the classes.
- When new operations are needed frequently and the object structure consists of many unrelated classes,
  it's inflexible to add new subclasses each time a new operation is required because "[..] distributing all
  these operations across the various node classes leads to a system that's hard to understand, maintain, and change."

*What solution does the Visitor design pattern describe?

- Define a separate (visitor) object that implements an operation to be performed on elements of an
  object structure.
- Clients traverse the object structure and call a dispatching operation accept(visitor) on an element —
  that "dispatches" (delegates) the request to the "accepted visitor object". The visitor object then performs
  the operation on the element ("visits the element").

Reference: https://en.wikipedia.org/wiki/Visitor_pattern
           https://github.com/Leonardofreua/python-patterns/blob/master/behavioral/visitor.py
"""


class Node(object):
    pass


class A(Node):
    pass


class B(Node):
    pass


class C(A, B):
    pass


class Visitor(object):

    def visit(self, node, *args, **kwargs):
        meth = None
        for cls in node.__class__.__mro__:
            meth_name = 'visit_' + cls.__name__
            meth = getattr(self, meth_name, None)
            if meth:
                break

        if not meth:
            meth = self.generic_visit
        return meth(node, *args, **kwargs)

    def generic_visit(self, node, *args, **kwargs):
        print('generic_visit ' + node.__class__.__name__)

    def visit_B(self, node, *args, **kwargs):
        print('visit_B ' + node.__class__.__name__)


def main():
    a = A()
    b = B()
    c = C()
    visitor = Visitor()
    visitor.visit(a)
    visitor.visit(b)
    visitor.visit(c)


if __name__ == "__main__":
    main()

# ---- OUTPUT: ---- :
#
