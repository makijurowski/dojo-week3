"""This document is a homework assignment for Coding Dojo."""

def first_and_last(my_list):
    """Print the first and last values in a list. Then create
    a new list using the first & last values from the original."""
    print my_list[0]
    print my_list[-1]
    new_list = my_list[0], my_list[-1]
    return new_list

# Test by printing the result.
print first_and_last(["hello", 2, 54, -2, 7, 12, 98, "world"])
