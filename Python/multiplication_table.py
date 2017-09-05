"""This is a Coding Dojo homework assignment."""


def mult_table(num):
    """This function takes in a value and then generates a
    multiplcation table up to that number."""
    y_count = 1

    while y_count <= num:
        newRow = []
        for i in range(1, num + 1):
            newRow.append(str(i * y_count) + '')
        print(' '.join(newRow))
        y_count += 1
    return 'All finished!'

# Testing the output.
print(mult_table(12))
