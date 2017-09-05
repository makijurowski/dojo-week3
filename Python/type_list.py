"""This is a Coding Dojo homework assignment."""


def type_in_list(my_list):
    """This functions takes in a list and prints a message for
    each element in the list based on it's data type."""
    totalSum = 0
    newStr = ''
    newList = []
    numUndefined = 0
    nextValType = type(my_list[0])
    listType = ''

    for val in my_list:
        if type(val) is nextValType and listType is not 'mixed':
            listType = "'" + str(type(val)) + "'"

        elif type(val) is not nextValType:
            listType = 'mixed'

        if isinstance(val, int) or isinstance(val, float):
            totalSum += val

        elif isinstance(val, str):
            newStr += (val + ' ')
            val_type = 'str'

    if newStr == '':
        newStr = 'absolutely nothing!'

    output = ('The list you entered has ' + str(listType) + ' values.' +
              '\n\nThat makes the total sum of list values ' + str(totalSum) +
              ', and the string of words in your list: \n' + newStr)
    return output

# Provided test cases.
l1 = ['magical unicorns', 19, 'hello', [0, 1, 2], 98.98, 'world']
l2 = [2, 3, 1, 7, 4, 12]
l3 = ['magical', 'unicorns']

# Testing the output.
print type_in_list(l2)
