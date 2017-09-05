"""This is a Coding Dojo homework assignment."""


def multiples():
    """This function has two parts that consist of other functions."""
    def odds_to_1000():
        """Prints all odd numbers up through 1000."""
        for i in range(1, 1001, 2):
            print i

    def multiples_of_5():
        """Prints all multiples of 5 from 5 to 1,000,000."""
        for i in range(5, 1000001, 5):
            print i
    return odds_to_1000(), multiples_of_5()


def sum_list(my_list):
    "Adds all the numbers in a list, returns a number."""
    total = 0
    for num in my_list:
        total = total + num
    return total


def average_list(my_list):
    "Finds the average value of numbers in a list, returns a number."""
    total = 0
    for num in my_list:
        total = total + num
    average = total / len(my_list)
    return average

# Test cases
# print multiples()
print sum_list([1, 2, 5, 10, 255, 3])
print average_list([1, 2, 5, 10, 255, 3])
