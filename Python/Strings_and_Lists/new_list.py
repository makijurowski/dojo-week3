"""This document is a homework assignment for Coding Dojo."""

def new_list(my_list):
    """Given a list, sort and then split in two halves. Push the list
    created from the first half onto the list created from the second
    half, starting at position 0. Will return a list within a list."""
    half = len(my_list) // 2
    my_list.sort()
    first_half = my_list[:half]
    second_half = my_list[half:]
    second_half.insert(0, first_half)
    return second_half

# Test by printing the result.
print new_list([19, 2, 54, -2, 7, 12, 98, 32, 10, -3, 6])
