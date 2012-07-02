# -*- coding: utf-8 -*-
#
# Copyright 2012 CDNZZ.COM
#

"""
:Author: rebill
"""


class SampleClass(object):
    """
    Summary of class here.

    Longer class information....
    Longer class information....

    :param likes_spam: A boolean indicating if we like SPAM or not.
    """

    def __init__(self, likes_spam=False):
        self.likes_spam = likes_spam
        self.eggs = 0

    def public_method(self):
        """Performs operation blah."""
