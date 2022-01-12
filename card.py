class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        return self.rank + " of " + self.suit
    def __gt__(self, other):
        if (self.rank == other.rank):
            return self.suits[(self.suit)] > other.suits[(other.suit)]
        return self.ranks[(self.rank)] > other.ranks[(other.rank)]
