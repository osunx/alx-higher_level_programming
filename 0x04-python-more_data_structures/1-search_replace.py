#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Write a function that replaces all occurrences of an element by another in a new list."""

    if not my_list:
        return []
    else:
        for i, item in enumerate(my_list):
            if item == search:
                my_list[i] = replace
    return my_list
