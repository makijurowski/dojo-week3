"""This document is a homework assignment for Coding Dojo."""

def max_min_avg(my_list):
    """Calculates the max, min, and average of numbers in a list."""
    new_list = []
    total = 0
    minimum = my_list[0]
    maximum = my_list[0]
    for num in my_list:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num
        total = total + num
    average = total / len(my_list)
    new_list.append(minimum)
    new_list.append(maximum)
    new_list.append(average)
    return new_list

# Test by printing the result.
RESULT = max_min_avg([2, 54, -2, 7, 12, 98])
print RESULT
