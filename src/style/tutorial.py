# -*- coding: utf-8 -*-
#
# Copyright 2012 CDNZZ.COM
#

"""
:Author: rebill
"""

import gevent


class Tutorial(object):
    """
    Gevent Tutorial

    A context switch in gevent is done through yielding.
    In this case example we have two contexts which yield
    to each other through invoking **gevent.sleep(0)**.
    """

    def __init__(self):
        gevent.joinall([
            gevent.spawn(self.foo),
            gevent.spawn(self.bar),
        ])

    def foo(self):
        """
        Function foo document
        """
        print('Running in foo')
        gevent.sleep(0)
        print('Explicit context switch to foo again')

    def bar(self):
        """
        Function bar document
        """
        print('Explicit context to bar')
        gevent.sleep(0)
        print('Implicit context switch back to bar')


if __name__ == '__main__':
    t = Tutorial()
