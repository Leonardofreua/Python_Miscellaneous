#!/usr/bin/env python
# -*- coding: utf-8 -*-


from Design_Patterns.Behavioral.PublishSubscribe import PublishAndSubscribe

pub = PublishAndSubscribe.Publisher()  # Initialized Publisher

"""
    ** Subscribers: **    
    We have initialized 3 subscribers with specified name 
"""
bob = PublishAndSubscribe.Subscriber('Bob')
alice = PublishAndSubscribe.Subscriber('Alice')
john = PublishAndSubscribe.Subscriber('John')

pub.register(bob)
pub.register(alice)
pub.register(john)

pub.dispatch("It's lunchtime!")

pub.unregister(john)
pub.dispatch("Time for dinner ")

# ---- OUTPUT: ---- :
#
# Alice got message "It's lunchtime!"
# Bob got message "It's lunchtime!"
# John got message "It's lunchtime!"
# Alice got message "Time for dinner "
# Bob got message "Time for dinner "
