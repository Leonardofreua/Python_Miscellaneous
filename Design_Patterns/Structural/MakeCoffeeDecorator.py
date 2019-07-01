#!/usr/bin/python
# -*- coding : utf-8 -*-

from Design_Patterns.Structural import CoffeeShopDecorator

myCoffee = CoffeeShopDecorator.Concrete_Coffee()
print('Ingredients: ' + myCoffee.get_ingredients() + '; Cost' + str(myCoffee.get_cost()) + '; sales tax = ' + str(
    myCoffee.get_tax()))

myCoffee = CoffeeShopDecorator.Milk(myCoffee)
print('Ingredients: ' + myCoffee.get_ingredients() + '; Cost' + str(myCoffee.get_cost()) + ', sales tax = ' + str(
    myCoffee.get_tax()))

myCoffee = CoffeeShopDecorator.Vanilla(myCoffee)
print('Ingredients: ' + myCoffee.get_ingredients() + '; Cost' + str(myCoffee.get_cost()) + ', sales tax = ' + str(
    myCoffee.get_tax()))

myCoffee = CoffeeShopDecorator.Sugar(myCoffee)
print('Ingredients: ' + myCoffee.get_ingredients() + '; Cost' + str(myCoffee.get_cost()) + ', sales tax = ' + str(
    myCoffee.get_tax()))

# ---- OUTPUT: ---- :
#
# Ingredients: coffee; Cost1.0;sales tax = 0.1
# Ingredients: coffee, milk; Cost1.25, sales tax = 0.125
# Ingredients: coffee, milk, vanilla; Cost2.0, sales tax = 0.2
# Ingredients: coffee, milk, vanilla, sugar; Cost2.0, sales tax = 0.2
