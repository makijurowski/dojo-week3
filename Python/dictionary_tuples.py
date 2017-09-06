'''This is a Coding Dojo homework assignment.'''


def dict_to_tuples(my_dict):
    '''This function's input is a dictionary and output is a list
    of tuples of all the key-value pairs.'''

    newList = []
    for eachKey, eachValue in my_dict.iteritems():
        newTuple = (eachKey, eachValue)
        newList.append(newTuple)

    return newList


# Provided test cases.
my_dict = {
    "Speros": "(555) 555-5555",
    "Michael": "(999) 999-9999",
    "Jay": "(777) 777-7777"
}

# Testing the function.
print(dict_to_tuples(my_dict))
