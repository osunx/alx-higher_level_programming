#!/usr/bin/python3

# Print the ASCII alphabet in lowercase without a new line
# the ASCII value can also be used "for char in range(97, 123)"
for char in range(ord('a'), ord('z') + 1):
    print(chr(char), end='')
