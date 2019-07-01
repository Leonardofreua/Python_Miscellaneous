#!/usr/bin/python
# -*- coding : utf-8 -*-


"""
The Observer design pattern is one of the twenty-three well-known "Gang of Four" design patterns
that describe how to solve recurring design problems to design flexible and reusable object-oriented
software, that is, objects that are easier to implement, change, test, and reuse.

*What problems can the Observer design pattern solve?

The Observer pattern addresses the following problems:

- A one-to-many dependency between objects should be defined without making the objects tightly coupled.
- It should be ensured that when one object changes state an open-ended number of dependent objects
  are updated automatically.
- It should be possible that one object can notify an open-ended number of other objects.

Defining a one-to-many dependency between objects by defining one object (subject) that updates
the state of dependent objects directly is inflexible because it couples the subject to particular
dependent objects. Tightly coupled objects are hard to implement, change, test, and reuse because they
refer to and know about (how to update) many different objects with different interfaces.

*What solution does the Observer design pattern describe?

- Define Subject and Observer objects.
- so that when a subject changes state, all registered observers are notified and updated automatically.

Reference: https://en.wikipedia.org/wiki/Observer_pattern
"""

import threading
import time


class Downloader(threading.Thread):

    def run(self):
        print('downloading')

        for i in range(1, 5):
            self.i = i
            time.sleep(2)

        print('Hi')

        return 'Hello world'


class Worker(threading.Thread):

    def run(self):
        for i in range(1, 5):
            print('worker running: %i(%i)' % (i, t.i))
            time.sleep(1)
            t.join()
            print('done')


t = Downloader()
t.start()

time.sleep(1)

t1 = Worker()
t1.start()


t2 = Worker()
t2.start()

t3 = Worker()
t3.start()

# ---- OUTPUT: ---- :
#
# downloading
# worker running: 1(1)
# worker running: 1(1)
# worker running: 1(1)
# Hi
# done
# worker running: 2(4)
# done
# worker running: 2(4)
# done
# worker running: 2(4)
# done
# worker running: 3(4)
# done
# worker running: 3(4)
# done
# worker running: 3(4)
# done
# worker running: 4(4)
# done
# worker running: 4(4)
# done
# worker running: 4(4)
# done
# done
# done
