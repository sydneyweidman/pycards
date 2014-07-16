import random
import itertools

RANKS = tuple("ace two three four five six seven eight nine ten jack queen king".split())
SUITS = tuple("hearts diamonds spades clubs".split())

class Card(object):
    """A playing card
    """
    
    def __init__(self, rank, suit, value=None):
        """Initialize the card with rank and suit
        
        Arguments:
        - `rank`: The rank of the card
        - `suit`: The suit of the card
        """
        self.rank = rank
        self.suit = suit
        if value:
            self.value = value
        else:
            self.value = min(RANKS.index(self.rank) + 1, 10)

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __eq__(self, other):
        return (isinstance(other, self.__class__) and (self.rank == other.rank)
                and (self.suit == other.suit))

    def __ne__(self, other):
        return not self.__eq__(other)
        
    def __repr__(self):
        return u'%s of %s' % (self.rank, self.suit)

class Deck(object):
    """An object representing a deck of cards
    """
    
    def __init__(self):
        """Create the unshuffled deck
        """
        self.deck = [Card(rank,suit) for (rank,suit) in itertools.product(RANKS,SUITS)]
        self.idx = 0

    def __len__(self):
        return len(self.deck)
    
    def __iter__(self):
        return self

    def shuffle(self):
        random.shuffle(self.deck)

    def next(self):
        try:
            card = self.deck[self.idx]
            self.idx += 1
            return card
        except IndexError:
            raise StopIteration

    def dealone(self):
        card = self.deck.pop()
        self.idx -= 1
        return card

    def deal(self, players, cardcount):
        if len(players)*cardcount > len(self.deck):
            raise ValueError
        hand = dict()
        for p in players:
            hand[p] = []
        for c in xrange(cardcount):
            for p in players:
                hand[p].append(self.dealone())
        return hand

if __name__ == '__main__':
    deck = Deck()
    for card in deck:
        print card
    deck.shuffle()
    for card in deck:
        print card
        
