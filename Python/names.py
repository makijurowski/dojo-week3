'''This is a Coding Dojo homework assignment.'''


def roster(my_list):
    '''This function takes in a list and prints out all
    of its keys and values.'''

    for person in my_list:
        print ' '.join(person.values())


def multiple_rosters(my_dict):
    '''This function takes in a dictionary and prints out all
    of its keys and values.'''
    count = 1

    for eachKey in my_dict:
        print eachKey
        my_list = my_dict[eachKey]
        for person in my_list:
            wholeName = ' '.join(person.values()).upper()
            print ((str(count) + ' - ' + wholeName + ' - ' +
                   str(len(wholeName) - 1)))
            count += 1
        print '\n'
    return 'All finished!'

# Provided test cases.
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
users = {
    'Students': [
        {'first_name':  'Michael', 'last_name': 'Jordan'},
        {'first_name': 'John', 'last_name': 'Rosales'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel'}
    ],
    'Instructors': [
        {'first_name': 'Michael', 'last_name': 'Choi'},
        {'first_name': 'Martin', 'last_name': 'Puryear'}
    ]
}

# Testing for output
multiple_rosters(users)
