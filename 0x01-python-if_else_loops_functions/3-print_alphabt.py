#!/usr/bin/python3

# Print the ASCII alphabet in lowercase except for 'e' and 'q'
for char in range(ord('a'), ord('z') + 1):
    if chr(char) not in ['e', 'q']:
        print(chr(char), end='')
