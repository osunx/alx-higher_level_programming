#!/usr/bin/python3
def islower(c):
    """Checks if the given character is lowercase"""
    if c >= 'a' and c <= 'z':
        return True
    else:
        return False
# This can also be done using the ASCII values directly
#def islower(letter):
 #   """Checks if the given letter is lowercase"""
 #   if ord(letter) >= 97 and ord(letter) <= 122:
 #       return True
 #   else:
 #       return False
