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
"""

class Expr(object):

    def accept(self, visitor):
        method_name = 'visit_{}'.format(self.__class__.__name__.lower())
        visit = getattr(visitor, method_name)
        return visit(self)


class Int(Expr):

    def __init__(self, value):
        self.value = value


class Add(Expr):

    def __init__(self, left, right):
        self.left = left
        self.right = right


class Mul(Expr):

    def __init__(self, left, right):
        self.left = left
        self.right = right

        
class Visitor(object):
    pass


class Eval(Visitor):

    def visit_init(self, i):
        return i.value

    def visit_add(self, a):
        return a.left.accept(self) + a.right.accept(self)

    def visit_mul(self, a):
        return a.left.accept(self) * a.right.accept(self)


class Print(Visitor):

    def visit_init(self, i):
        return i.value

    def visit_add(self, a):
        return '{+{} {}}'.format(a.left.accept(self), a.right.accept(self))

    def visit_mul(self, a):
        return '{+{} {}}'.format(a.left.accept(self), a.right.accept(self))


def main():
    expr = Add(
            Add(Int(4), Int(3)), 
            Mul(Int(10), Add(Int(1), Int(1)))
        )
    print(expr.accept(Print()))
    print(expr.accept(Eval()))


if __name__ == "__main__":
    main()

    
# ---- OUTPUT: ---- :
#
