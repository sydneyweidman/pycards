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

    def __init__(self, rank, suit, value=None, tag='deck'):
        """Initialize the card with rank and suit

        Arguments:
        - `rank`: The rank of the card
        - `suit`: The suit of the card
        - `value`: The card value
        - `tag`: A tag indicating the area of the card (hand, discard pile etc)
        """
        self.rank = rank
        self.suit = suit
        self.tag = tag
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


class Hand(object):
    """A class representing a hand of cards
    """

    def __init__(self, player=None, from_deck=None):
        """Create the hand

        Arguments:
        player: The cards with which to build the hand
        from_deck: The Deck object from which the cards are drawn
        """
        self.from_deck = from_deck
        self.player = player

    def __len__(self):
        return len([i for i in self.from_deck if i.tag == self.player.name])

    def discard(self, card, to_location='discard'):
        """Discard one or more cards"""
        card.tag = to_location

    def draw(self):
        """Pickup one card"""
        drawn = self.from_deck.dealone(self.player.name)
        return drawn

    def value(self):
        """The numerical value of the hand, if any
        """
        return sum([i.value for i in self.from_deck
                    if i.tag == self.player.name])


class Deck(MutableSequence):
    """An object representing a deck of cards
    """

    def __init__(self, prepopulate=True, shuffle=False):
        """Create the unshuffled deck
        """
        self._deck = list()
        if prepopulate:
            for (rank, suit) in itertools.product(RANKS, SUITS):
                self._deck.append(Card(rank, suit))

    def __len__(self):
        return len([i for i in self._deck if i.tag == 'deck'])

    def __getitem__(self, idx):
        return self._deck[idx]

    def __setitem__(self, card, idx):
        self._deck[idx] = card
        return self._deck[idx]

    def __delitem__(self, idx):
        del self._deck[idx]

    def shuffle(self):
        random.shuffle(self._deck)

    def dealone(self, to_location):
        card = self._deck[len(self) - 1]
        card.tag = to_location
        return card

    def insert(self, card, idx=0):
        self._deck.insert(card, idx)

    def deal(self, players, cardcount):
        if len(players) * cardcount > len(self):
            raise ValueError
        hands = {}
        for p in players:
            hands[p] = []
        for c in xrange(cardcount):
            for p in players:
                hands[p].append(self.dealone(p))
        return hands

if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()
    players = ['fred', 'bill', 'sam', 'eddie']
    hands = deck.deal(players, 5)
    for p in hands:
        print "%s's hand:'" % (p,)
        for card in hands[p]:
            print card
