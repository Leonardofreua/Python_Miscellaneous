#!/usr/bin/env python
# -*- coding: utf-8 -*-


from ProductModel import ProductModel
from ConsoleView import ConsoleView
from Controller import Controller


if __name__ == '__main__':
    model = ProductModel()
    view  = ConsoleView()

    controller = Controller(model, view)
    controller.show_items()
    controller.show_item_information('cheese')
    controller.show_item_information('eggs')
    controller.show_item_information('milk')
    controller.show_item_information('arepas')
    