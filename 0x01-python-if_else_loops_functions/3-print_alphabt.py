#!/usr/bin/python3

# Print the ASCII alphabet in lowercase except for 'e' and 'q'
for char in range(97, 123):
    if chr(char) not in ['e', 'q']:
        print(chr(char), end='')
