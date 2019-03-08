#!/usr/bin/python
# -*- coding : utf-8 -*-


"""
The Command design pattern is one of the twenty-three well-known GoF design patterns that describe
how to solve recurring design problems to design flexible and reusable object-oriented software,
that is, objects that are easier to implement, change, test, and reuse.

*What problems can the Command design pattern solve?

- Coupling the invoker of a request to a particular request should be avoided. That is, hard-wired
requests should be avoided.
- It should be possible to configure an object (that invokes a request) with a request.
Implementing (hard-wiring) a request directly into a class is inflexible because it couples the class
to a particular request at compile-time, which makes it impossible to specify a request at run-time.

*What solution does the Command design pattern describe?

- Define separate (command) objects that encapsulate a request.
- A class delegates a request to a command object instead of implementing a particular request directly.

Reference: https://en.wikipedia.org/wiki/Command_pattern
"""

import os
from os.path import lexists


class MoveFileCommand(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def execute(self):
        self.rename(self.src, self.dest)

    def undo(self):
        self.rename(self.dest, self.src)

    def rename(self, src, dest):
        print(u"renaming %s to %s" % (src, dest))
        os.rename(src, dest)


def main():
    command_stack = []

    # commands are just pushed into the command stack
    command_stack.append(MoveFileCommand('foo.txt', 'bar.txt'))
    command_stack.append(MoveFileCommand('bar.txt', 'baz.txt'))

    # verify that none of the target files exist
    assert not lexists("foo.txt")
    assert not lexists("bar.txt")
    assert not lexists("baz.txt")
    try:
        with open("foo.txt", "w"):  # Creating the file
            pass

        # they can be executed later on
        for cmd in command_stack:
            cmd.execute()

        # and can also be undone at will
        for cmd in reversed(command_stack):
            cmd.undo()
    finally:
        os.unlink("foo.txt")


if __name__ == "__main__":
    main()

# ---- OUTPUT: ---- :
#
# renaming foo.txt to bar.txt
# renaming bar.txt to baz.txt
# renaming baz.txt to bar.txt
# renaming bar.txt to foo.txt
