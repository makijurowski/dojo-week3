'''This is a Coding Dojo homework assignment.'''


def make_and_read_dict(my_dict):
    '''This function takes in a dictionary and prints out all
    of its keys and values.'''

    for eachKey, eachValue in my_dict.iteritems():
        print ('My ' + eachKey + ' is ' + eachValue + '.')

aboutMe = {'name': 'Maki', 'age': '30', 'country of birth': 'the United States',
           'favorite programming language': 'Python'}

make_and_read_dict(aboutMe)
