#!/usr/bin/python3
# Print the ASCII alphabet in reverse order,
# alternating lowercase and uppercase

i = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - i)), end="")
    i = 32 if i == 0 else 0
