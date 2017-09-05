'''This is a Coding Dojo homework assignment.'''


def draw_stars(my_list):
    '''This function takes in a list of numbers and prints out the
    corresponding numbers of stars on a new line.'''
    starLine = []
    for val in my_list:
        num = int(val)
        while num > 0:
            starLine.append('* ')
            num -= 1
        print ''.join(starLine)
        starLine = []
    return 'All finished!'


def draw_stars_modified(my_list):
    '''This function takes in a list of numbers AND strings, then prints out
    either the first letter of a str or the number of stars on a new line.'''
    starLine = []
    letterLine = []
    for val in my_list:
        if isinstance(val, int):
            num = int(val)
            while num > 0:
                starLine.append('* ')
                num -= 1
            print ''.join(starLine)
            starLine = []

        elif isinstance(val, str):
            num = len(val)
            while num > 0:
                letterLine.append(val[0] + ' ')
                num -= 1
            print (''.join(letterLine)).lower()
            letterLine = []
    return 'All finished!'


draw_stars_modified([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])
