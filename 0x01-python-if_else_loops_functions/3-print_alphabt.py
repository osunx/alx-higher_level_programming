#!/usr/bin/python3

# Print the ASCII alphabet in lowercase except for 'e' and 'q'
for char in range(97, 123):
    if chr(char) != 'e' and chr(char) != 'q':
        print("{}".format(chr(char)), end="")
