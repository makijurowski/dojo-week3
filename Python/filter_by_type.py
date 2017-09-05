"""This is a Coding Dojo homework assignment."""


def test_a_value(val):
    """Given a value, return what type it is."""
    if type(val) is int:
        print "This is an integer, and... "
        if val >= 100:
            return "It's a really big number!"
        else:
            return "It's not a very big number."
    elif type(val) is str:
        print "This is a string, and... "
        if len(val) >= 50:
            return "It's a long sentence."
        else:
            return "It's a pretty short sentence."
    elif type(val) is list:
        print "This is a list, and... "
        if len(val) >= 10:
            return "Wow, what a big list!"
        else:
            return "Aww, it's not a very big list."
    else:
        return "I don't know what this is!"

# Provided test cases.
sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1, 7, 4, 21]
mL = [3, 5, 7, 34, 3, 2, 113, 65, 8, 89]
lL = [4, 34, 22, 68, 9, 13, 3, 5, 7, 9, 2, 12, 45, 923]
eL = []
spL = ['name', 'address', 'phone number', 'social security number']

# Testing a test case.
print test_a_value(mI)
