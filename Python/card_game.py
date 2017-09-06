class Deck(object):
    def __init__(self):
        self.cards = []
        self.BuildDeck()

    def BuildDeck(self):
        self.suits = ['hearts', 'diamonds', 'spades', 'clubs']
        self.val = 0
        self.cardID = ['A', '2', '3', '4', '5', '6',
                       '7', '8', '9', '10', 'J', 'Q', 'K']

        for each in self.suits:
            for i in range(0, len(self.cardID)):
                Card.suit = each
                Card.val = i + 1
                Card.cardID = self.cardID[i]
                self.cards.append(Card)
        return self.cards


class Player(object):
    def __init__(self, name):
        self.name = name


class Card(object):
    def __init__(self, suits, val, cardID):
        self.suits = suits
        self.val = val
        self.cardID = cardID


print Deck()
