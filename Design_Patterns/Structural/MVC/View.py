#!/usr/bin/env python
# -*- coding: utf-8 -*-


class View(object):
    def show_item_list(self, item_type, item_list):
        raise NotImplementedError

    def show_item_information(self, item_type, item_name, item_info):
        """Will look for item information by iterating over key,value pairs
        yielded by item_info.items()"""
        raise NotImplementedError

    def item_not_found(self, item_type, item_name):
        raise NotImplementedError
