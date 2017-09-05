'''This is a Coding Dojo homework assignment.'''

import random


def coin_toss(n):
    '''This function takes in a number and then simulates flipping a coin
    n times, keeping track of how many heads and tails appear.'''
    coinHeads = 0
    coinTails = 0
    thisFlip = ''

    for i in range(0, n):
        print 'Attempt #' + str(i + 1) + ': Throwing a coin...'
        randChance = random.randint(0, 100)
        if randChance > 50:
            coinHeads += 1
            thisFlip = 'head'
        else:
            coinTails += 1
            thisFlip = 'tail'
        print ("It's a " + thisFlip + "! You've flipped " + str(coinHeads) +
               " head(s) and " + str(coinTails) + " tail(s) so far.")
    return 'All finished!'

coin_toss(5000)
