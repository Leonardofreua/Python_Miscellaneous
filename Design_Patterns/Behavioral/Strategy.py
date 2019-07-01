#!/usr/bin/python
# -*- coding : utf-8 -*-


"""
In Strategy pattern, a class behavior or its algorithm can be changed at run time.
This type of design pattern comes under behavior pattern.

In Strategy pattern, we create objects which represent various strategies and a context
object whose behavior varies as per its strategy object. The strategy object changes the
executing algorithm of the context object.

Reference: https://www.tutorialspoint.com/design_pattern/strategy_pattern.htm
"""


class StrategyExecutor(object):

    def __init__(self, strategy=None):
        self.strategy = strategy

    def execute(self, arg1, arg2):
        if self.strategy is None:
            print("Strategy is not implemented ...")
        else:
            self.strategy.execute(arg1, arg2)


class AdditionStrategy(object):

    def execute(self, arg1, arg2):
        print(arg1 + arg2)


class SubtractionStrategy(object):

    def execute(self, arg1, arg2):
        print(arg1 - arg2)


def main():
    no_strategy = StrategyExecutor()
    addition_strategy = StrategyExecutor(AdditionStrategy())
    subtraction_strategy = StrategyExecutor(SubtractionStrategy())
    no_strategy.execute(4, 6)
    addition_strategy.execute(4, 6)
    subtraction_strategy.execute(4, 6)


if __name__ == '__main__':
    main()

# ---- OUTPUT: ---- :
#
# Strategy is not implemented ...
# 10
# -2