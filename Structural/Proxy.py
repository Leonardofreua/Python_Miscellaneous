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


class Image:

    def __init__(self, fileName):
        self._fileName = fileName

    def load_image_from_disk(self):
        print('loading ' + self._fileName)

    def display_image(self):
        print('display ' + self._fileName)


class Proxy:

    def __init__(self, subject):
        self._subject = subject
        self._proxyState = None


class ProxyImage(Proxy):

    def display_image(self):
        if self._proxyState is None:
            self._subject.load_image_from_disk()
            self._proxyState = 1

        print("display " + self._subject._fileName)


proxy_image1 = ProxyImage(Image("HiRes_10MB_Photo"))
proxy_image2 = ProxyImage(Image("Hello_5MB_Photo2"))

proxy_image1.display_image()
proxy_image1.display_image()
proxy_image2.display_image()
proxy_image2.display_image()

# ---- OUTPUT: ---- :
#
# loading HiRes_10MB_Photo
# display HiRes_10MB_Photo
# display HiRes_10MB_Photo
# loading Hello_5MB_Photo2
# display Hello_5MB_Photo2
# display Hello_5MB_Photo2
