#!/usr/bin/python3

for c in range(90, 64, -1):
    print("{:c}".format(c + 32 * ((c % 2) ^ 1)), end="")
