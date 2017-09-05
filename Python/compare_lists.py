"""This is a Coding Dojo homework assignment."""


def compare_two_lists(list_one, list_two):
    """This function takes in two lists and compares them. It then
    returns a print statement identifying whether they are the same."""

    if len(list_one) is not len(list_two):
        return "The lists are not the same."
    else:
        while len(list_one) > 0:
            if list_one[0] is not list_two[0]:
                return "The lists are not the same."
            else:
                del list_one[0]
                del list_two[0]
    return "The lists are the same!"

# Provided test cases.
list_one = [1, 2, 5, 6, 2, 3]
list_two = [1, 2, 5, 6, 2, 3]
# list_one = [1, 2, 5, 6, 5]
# list_two = [1, 2, 5, 6, 5, 3]
# list_one = [1, 2, 5, 6, 5, 16]
# list_two = [1, 2, 5, 6, 5]
# list_one = ['celery', 'carrots', 'bread', 'milk']
# list_two = ['celery', 'carrots', 'bread', 'milk']

print compare_two_lists(list_one, list_two)
