"""This document is a homework assignment for Coding Dojo."""


def find_and_replace(words, target):
    """ Using the following input, find and return the index position
        for the word 'day.'
        INPUT: str, OUTPUT int. """
    position = words.find(target)
    print position
    return words.replace(target, " month")

# Test by printing the result.
RESULT = find_and_replace("It's thanksgiving day. It's my birthday, too!", (
    "day"))
print RESULT
