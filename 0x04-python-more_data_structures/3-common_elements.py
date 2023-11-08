#!/usr/bin/python3

def common_elements(set_1, set_2):
    """
    Write a function that returns a set of common elements in two sets.
    """

    rset = set()

    for i in set_1:
        if i in set_2:
            rset.add(i)
    return rset
