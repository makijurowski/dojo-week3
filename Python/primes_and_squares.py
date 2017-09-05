"""This is a Coding Dojo homework assignment."""


def foobar(minVal, maxVal):
    """This function checks each num between the min and max
    values, and prints 'Foo' for prime numbers and 'Bar' for
    perfect squares. If neither, it prints FooBar."""

    for x in range(minVal, maxVal):
        # print 'My current num is: ' + str(x)

        for n in range(2, x):
            if n**n == x:
                print 'Bar'  # Perfect square
                break
            elif x % n == 0:
                print 'FooBar'  # Neither prime or perfect square
                break

        print 'Foo'  # Prime number
    return 'All finished!'

foobar(100, 1000000)
