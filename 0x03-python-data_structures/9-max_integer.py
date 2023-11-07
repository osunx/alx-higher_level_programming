#!/usr/bin/python3

def max_integer(my_list=[]):
    """Finds the biggest integer of a list"""
    if len(my_list) == 0:
        return None
    else:
        firstVal = my_list[0]
        for val in range(len(my_list)):
            if my_list[val] > firstVal:
                maxVal = my_list[val]
                firstVal = maxVal
        return maxVal
