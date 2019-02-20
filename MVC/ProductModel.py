#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Model import Model


class ProductModel(Model):
    class Price(float):
        """A polymorphic way to pass a float with a particular
         __str__ functionality."""

        def __str__(self):
            return "{:.2f}".format(self)

    products = {
        'milk': {'price': Price(1.50), 'quantity': 10},
        'eggs': {'price': Price(0.20), 'quantity': 100},
        'cheese': {'price': Price(2.00), 'quantity': 10}
    }

    item_type = 'product'

    def __iter__(self):
        for item in self.products:
            yield item

    def get(self, product):
        try:
            return self.products[product]
        except KeyError as e:
            raise KeyError((str(e) + " not in the model's item list."))