'''This is a Coding Dojo homework assignment.'''


def make_dict(arr1, arr2):
    '''This function takes in two lists and outputs a dictionary with
    the longer list providing the keys and the other list providing values.'''

    new_dict = {}
    count = 0

    if len(arr1) > len(arr2):
        key_list = arr1
        value_list = arr2
    elif len(arr1) < len(arr2):
        key_list = arr2
        value_list = arr1
    else:
        key_list = arr1
        value_list = arr2

    if len(key_list) > len(value_list):
        while (len(key_list) - len(value_list)):
            value_list.append('Undefined')

    for each in key_list:
        new_dict[key_list[count]] = value_list[count]
        count += 1
    return new_dict


# Provided test cases.
name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks",
                   "dolphins", "llamas", "dogs"]

# Testing the function.
print(make_dict(name, favorite_animal))
