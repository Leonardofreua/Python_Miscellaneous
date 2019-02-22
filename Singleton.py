#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The singleton pattern is a software design pattern that restricts the 
instantiation of a class to one. This is useful when exactly one object 
is needed to coordinate actions across the system. The term comes from 
the mathematical concept of a singleton.

Reference: https://en.wikipedia.org/wiki/Singleton_pattern
"""


class Singleton:
    __instance = None

    @staticmethod
    def getInstance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("This class is a Singleton class.")
        else:
            Singleton.__instance = self


s = Singleton()
print(s)

s = Singleton.getInstance()
print(s)

# ---- OUTPUT: ---- :
#
# <__main__.Singleton object at 0x030E0D90>
# <__main__.Singleton object at 0x030E0D90>