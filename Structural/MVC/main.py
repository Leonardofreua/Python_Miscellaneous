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

# ---- OUTPUT: ---- :
#
# PRODUCT LIST:
# milk
# eggs
# cheese
# 
# PRODUCT INFORMATION:
# Name: cheese, Price: 2.00, Quantity: 10
#
# PRODUCT INFORMATION:
# Name: eggs, Price: 0.20, Quantity: 100# 

# PRODUCT INFORMATION:
# Name: milk, Price: 1.50, Quantity: 10
#
# That product "arepas" does not exist in the records