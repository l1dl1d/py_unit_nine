class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        return self.rank + " of " + self.suit
    def __gt__(self, other):
        if (self.rank == other.rank):
            return self.suits.index(self.suit) > other.suits.index(other.suit)
        return self.ranks.index(self.rank) > other.ranks.index(other.rank)
