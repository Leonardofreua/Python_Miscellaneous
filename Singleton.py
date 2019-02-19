#!/usr/bin/env python
# -*- coding: utf-8 -*-

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