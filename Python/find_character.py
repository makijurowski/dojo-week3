"""This is a Coding Dojo homework assignment."""


def find_char(my_list, char):
    """This function takes in a list of strings and a character to find,
    it returns a list with the words that contain the found character."""
    new_list = []

    for string in my_list:
        if char in string:
            new_list.append(string)
    return new_list

# Provided test case.t
word_list = ['hello', 'world', 'my', 'name', 'is', 'Anna']
char = 'o'

# Expected output:
# new_list = ['hello', 'world']
print find_char(word_list, char)
