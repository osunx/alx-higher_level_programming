#!/usr/bin/python3

def common_elements(set_1, set_2):
    """
    Write a function that returns a set of common elements in two sets.
    """

    common_elements = set_1.intersection(set_2)

    for item in common_elements:
        return item
