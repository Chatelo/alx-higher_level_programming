#!/usr/bin/python3
# 11-delete_at.py


def delete_at(my_list=[], idx=0):
    """
    Deletes the item at a specific position in a list.

    Args:
        my_list: A list of integers.
        idx: The index of the item to delete.

    Returns:
        The updated list.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        del my_list[idx]
        return my_list
