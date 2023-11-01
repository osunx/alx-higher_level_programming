#!/usr/bin/python3

# Print the ASCII alphabet in lowercase without a new line
for char in range(ord('a'), ord('z') + 1):
    print(chr(char), end='')
# this can also be done like this
#for i in range(97, 123):
#    print(chr(i), end="")
