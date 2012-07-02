# -*- coding: utf-8 -*-
#
# Copyright 2012 CDNZZ.COM
#

"""
:Author: rebill
"""

def foo(a, b=None):
    """
    You can specify values for variables at the end of a function's parameter list.
    Calling code must use named values for arguments with a default value.
    This helps document the code somewhat and helps prevent and
    detect interface breakage when more arguments are added.

    **Yes:**
       >>> foo(1)
       >>> foo(1, b=2)

    **No:**
       >>> foo(1, 2)
    """
    if b is None:
        b = 0
    return a + b

def main():
    """
    Python Style Guide Main Function Document
    """
    # Define long string
    x = ('This will build a very long long '
         'long long long long long long string')
    print x
    # Function Call
    c = foo(1, b=2)
    print c
    # Use loops instead when things get more complicated.
    result = []
    for x in range(10):
        for y in range(5):
            if x * y > 10:
                result.append((x, y))
    print result


if __name__ == '__main__':
    main()    