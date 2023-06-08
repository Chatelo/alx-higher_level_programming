#!/usr/bin/python3.8
"""
This module prints all the names defined by the compiled module hidden_4.pyc
"""

if __name__ == "__main__":
    import hidden_4

    for name in sorted(dir(hidden_4)):
        if name[0:2] != "__":
            print(name)
