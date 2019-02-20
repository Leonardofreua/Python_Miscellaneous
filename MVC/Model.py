#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Model(object):
    def __iter__(self):
        raise NotImplementedError

    def get(self, item):
        """Returns an object with a .items() call method
        that iterates over key,value pairs of its information."""
        raise NotImplementedError

    @property
    def item_type(self):
        raise NotImplementedError