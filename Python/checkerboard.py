"""This is a Coding Dojo homework assignment."""


def checkerboard():
    """This function prints a checkerboard pattern to the console."""
    checkerboard_rows = 20

    while checkerboard_rows > 0:
        if checkerboard_rows % 2 == 0:
            print "* * * * * * * * * *"
            checkerboard_rows -= 1
        else:
            print " * * * * * * * * * *"
            checkerboard_rows -= 1
    return 'All finished!'

print(checkerboard())
