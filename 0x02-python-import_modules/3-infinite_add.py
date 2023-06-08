#!/usr/bin/python3
import sys

def infinite_add(args):
    total = 0
    for arg in args:
        total += int(arg)
    return total

if __name__ == "__main__":
    args = sys.argv[1:]
    result = infinite_add(args)
    print(result)

