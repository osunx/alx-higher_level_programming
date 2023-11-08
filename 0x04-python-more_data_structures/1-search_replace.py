#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Write a function that replaces all occurrences of an element by another in a new list."""

    if not my_list:
        return None
    new_list = my_list[:]
    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace
    return new_list

