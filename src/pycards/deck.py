import random
from collections import MutableSequence
import itertools

RANKS = tuple("ace two three four five six seven \
               eight nine ten jack queen king".split())
SUITS = tuple("hearts diamonds spades clubs".split())


class Card(object):
    """A playing card
    >>> from pycards.game import Game
    >>> from pycards.deck import Card
    >>> g = Game(['a','b'], shuffled=False)
    >>> g.deck.deal(['a','b'],2) # doctest: +NORMALIZE_WHITESPACE
    {'a': [king of clubs, king of diamonds], 'b': [king of spades, king of hearts]}
    >>> len(g.deck)
    48
    >>> Card(suit='clubs',rank='king') not in g.deck
    True
    >>> Card(suit='diamonds',rank='king') not in g.deck
    True
    >>> Card(suit='clubs',rank='nine') not in g.deck
    False
    >>> Card(suit='spades',rank='ace') in g.deck
    True
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
        return (isinstance(other, self.__class__) and
                (self.rank == other.rank) and
                (self.suit == other.suit))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return u'%s of %s' % (self.rank, self.suit)


class Deck(MutableSequence):
    """An object representing a deck of cards
    """

    def __init__(self):
        """Create the unshuffled deck
        """
        self._deck = list()
        for (rank, suit) in itertools.product(RANKS, SUITS):
            self._deck.append(Card(rank, suit))

    def __len__(self):
        return len(self._deck)

    def __getitem__(self, idx):
        return self._deck[idx]

    def __setitem__(self, card, idx):
        self._deck[idx] = card
        return self._deck[idx]

    def __delitem__(self, idx):
        del self._deck[idx]

    def shuffle(self):
        random.shuffle(self._deck)

    def dealone(self):
        card = self._deck.pop()
        return card

    def insert(self, card, idx):
        self._deck.insert(idx, card)

    def deal(self, players, cardcount):
        if len(players) * cardcount > len(self):
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
