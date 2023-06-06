#!/usr/bin/python3
for a in range(0, 10):
    for b in range(a + 1, 10):
        if a != b:
            if a != 8 or b != 9:
                print("{:d}{:d}, ".format(a, b), end="")
            else:
                print("{:d}{:d}".format(a, b))
