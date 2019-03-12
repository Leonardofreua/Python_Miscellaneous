#!/usr/bin/python
# -*- coding : utf-8 -*-

"""
The Proxy design pattern is one of the twenty-three well-known GoF design patterns
that describe how to solve recurring design problems to design flexible and reusable
object-oriented software, that is, objects that are easier to implement, change, test, and reuse.

*What problems can the Proxy design pattern solve?

- The access to an object should be controlled .
- Additional functionality should be provided when accessing an object.

When accessing sensitive objects, for example, it should be possible to
check that clients have the needed access rights.

*What solution does the Proxy design pattern describe?

Define a separate Proxy object that

- can be used as substitute for another object (Subject) and
- implements additional functionality to control the access to this subject.

Reference: https://en.wikipedia.org/wiki/Proxy_pattern
"""

from abc import ABCMeta, abstractmethod


NOT_IMPLEMENTED = "You should implement this."


class AbstractCar:
    __metaclass__ = ABCMeta

    @abstractmethod
    def drive(self):
        raise NotImplementedError(NOT_IMPLEMENTED)


class Car(AbstractCar):
    def drive(self):
        print("Car has been driven!")


class Driver(object):
    def __init__(self, age):
        self.age = age


class ProxyCar(AbstractCar):
    def __init__(self, driver):
        self.car = Car()
        self.driver = driver

    def drive(self):
        if self.driver.age <= 16:
            print("Sorry, the driver is too young to drive.")
        else:
            self.car.drive()


if __name__ == '__main__':
    driver = Driver(16)
    car = ProxyCar(driver)
    car.drive()

    driver = Driver(25)
    car = ProxyCar(driver)
    car.drive()

# ---- OUTPUT: ---- :
#
