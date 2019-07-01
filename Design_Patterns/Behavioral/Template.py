#!/usr/bin/python
# -*- coding : utf-8 -*-


"""
In Template pattern, an abstract class exposes defined way(s)/template(s) to execute its methods.
Its subclasses can override the method implementation as per need but the invocation is to be in the
same way as defined by an abstract class. This pattern comes under behavior pattern category.

Reference: https://www.tutorialspoint.com/design_pattern/template_pattern.htm
https://github.com/faif/python-patterns/blob/master/patterns/behavioral/template.py
"""

ingredients = "spam eggs apple"
line = '-' * 10


# Skeletons
def iter_elements(getter, action):
    """Template skeleton that iterates items"""
    for element in getter():
        action(element)
        print(line)


def rev_elements(getter, action):
    """Template skeleton that iterates items in reverse order"""
    for element in getter()[::-1]:
        action(element)
        print(line)


# Getters
def get_list():
    return ingredients.split()


def get_lists():
    return [list(x) for x in ingredients.split()]


# Actions
def print_item(item):
    print(item)


def reverse_item(item):
    print(item[::-1])


# Makes templates
def make_template(skeleton, getter, action):
    """Instantiate a template method with getter and action"""

    def template():
        skeleton(getter, action)

    return template


if __name__ == '__main__':
    # Create our template functions
    templates = [
        make_template(s, g, a)
        for g in (get_list, get_lists)
        for a in (print_item, reverse_item)
        for s in (iter_elements, rev_elements)
    ]

    # Execute them
    for template in templates:
        template()

# ---- OUTPUT: ---- :
#
# spam
# ----------
# eggs
# ----------
# apple
# ----------
# apple
# ----------
# eggs
# ----------
# spam
# ----------
# maps
# ----------
# sgge
# ----------
# elppa
# ----------
# elppa
# ----------
# sgge
# ----------
# maps
# ----------
# ['s', 'p', 'a', 'm']
# ----------
# ['e', 'g', 'g', 's']
# ----------
# ['a', 'p', 'p', 'l', 'e']
# ----------
# ['a', 'p', 'p', 'l', 'e']
# ----------
# ['e', 'g', 'g', 's']
# ----------
# ['s', 'p', 'a', 'm']
# ----------
# ['m', 'a', 'p', 's']
# ----------
# ['s', 'g', 'g', 'e']
# ----------
# ['e', 'l', 'p', 'p', 'a']
# ----------
# ['e', 'l', 'p', 'p', 'a']
# ----------
# ['s', 'g', 'g', 'e']
# ----------
# ['m', 'a', 'p', 's']
# ----------
