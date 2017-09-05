'''This is a Coding Dojo homework assignment.'''


def odd_even():
    '''This function counts from 1 to 2000, printing each value
    and then specifying if it is an even or odd number.'''
    for i in range(1, 2000):
        if (i % 2 == 0):
            print 'Number is ' + str(i) + '. That is an even number.'
        else:
            print 'Number is ' + str(i) + '. That is an odd number.'


def multiply(my_list, multiplier):
    '''This function iterates through a list and returns a new
    list with each value multiplied by the second argument.'''
    newList = []
    for val in my_list:
        newList.append(val * multiplier)
    return newList


def hackerChallenge(func, args):
    '''This functions takes the multiply function call as an argument.
    It returns the multiplied list as a 2-dimensional list.'''
    newArray = []
    lastArray = []
    for val in args[0]:
        newArray = [1] * (args[1] * val)
        lastArray.append(newArray)
    return lastArray

# Test cases.
print hackerChallenge(multiply, ([2, 4, 5], 3))
# print(odd_even())
