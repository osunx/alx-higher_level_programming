#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """
    Write a function that returns a set of all elements present in only one set.
    """

    rset = set()

    for i in set_1:
        if i not in set_2:
            rset.add(i)
    return rset
