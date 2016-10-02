import random
from collections import MutableSequence
import itertools

RANKS = tuple("ace two three four five six seven \
               eight nine ten jack queen king".split())
SUITS = tuple("hearts diamonds spades clubs".split())


class Card(object):
    """A playing card"""

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
            self.value = 0

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __eq__(self, other):
        return (isinstance(other, self.__class__) and
                (self.value == other.value))

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
        player: The player holding the hand
        from_deck: The Deck object from which the cards are drawn
        """
        self.from_deck = from_deck
        self.player = player

    def __len__(self):
        return len([i for i in self.from_deck if i.tag == self.player.name])

    def discard(self, card, to_location='discard'):
        """Discard one card"""
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

    def __init__(self, shuffle=False, cards=None):
        """Create the unshuffled deck
        """
        self._deck = list()
        self.populate(cards)

    def __len__(self):
        return len([i for i in self._deck if i.tag == 'deck'])

    def __getitem__(self, idx):
        return self._deck[idx]

    def __setitem__(self, idx, card):
        self._deck[idx] = card
        return self._deck[idx]

    def __delitem__(self, idx):
        del self._deck[idx]

    def populate(self, cards=None):
        """Generate a standard Deck or create from a list of Card objects"""
        if cards is not None and len(cards) > 0:
            for card in cards:
                if type(card) == Card:
                    self._deck.append(card)
                else:
                    raise TypeError("%s is not of type Card" % (card,))
        else:
            for (rank, suit) in itertools.product(RANKS, SUITS):
                value = min(RANKS.index(rank) + 1, 10)
                self._deck.append(Card(rank, suit, value))

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
