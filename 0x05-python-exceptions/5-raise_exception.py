#!/usr/bin/python3

def raise_exception():
    """Raise a TypeError exception."""
    try:
        1 + "one"
    except TypeError:
        raise
