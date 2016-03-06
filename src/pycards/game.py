##############################################################################
#
#     Copyright Sydney Weidman, 2014
#     Author: Sydney Weidman <sydney.weidman@gmail.com>
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from deck import Deck


class Player(object):
    """A class representing a player
    """

    def __init__(self, name):
        """Initialize the player

        Arguments:
        - `name`: The player's name'
        """
        self.name = name
        self.hand = None

    def __repr__(self):
        return self.name


class Hand(object):
    """A class representing a hand of cards
    """

    def __init__(self, from_deck):
        """Create the hand

        Arguments:
        - `cards`: The a list of card instances with which to initialize
        the hand
        """
        self.from_deck = from_deck
        self.cards = []

    def __len__(self):
        return len(self.cards)

    def discard(self, card):
        """Discard one or more cards"""
        for c in self.cards:
            if c == card:
                self.cards.remove(c)

    def draw(self):
        """Pickup one card"""
        drawn = self.from_deck.dealone()
        self.cards.append(drawn)
        return drawn

    def value(self):
        """The numerical value of the hand, if any
        """
        return sum([i.value for i in self.cards])


class GameState(object):
    """A list of dictionaries containing the game state. Each
    element of the list represents one turn.
    """

    def __init__(self, saved_game=None):
        """

        Arguments:
        - `saved_game`: A game that was previously saved
        """
        if saved_game:
            self.state = saved_game
        else:
            self.state = []


class Game(object):
    """A card game

    >>> from game import Game # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    >>> g = Game(2,{'a':None,'b':None})
    >>> g.players
    {'a': a, 'b': b}
    >>> g.run()
    >>> g.started
    True
    """

    def __init__(self, cardcount,
                 playerlist={},
                 saved_game=None,
                 shuffled=True):
        """Set up the card game. Save the game state in the "turns" attribute.

        Arguments:
        - `cardcount`:   The initial cardcount
        - `playerlist`:  The players' names in a dict
        - `saved_game`:  A game that was previously saved
        """
        self.players = playerlist
        self.deck = Deck()
        if shuffled:
            self.deck.shuffle()
        for p in self.players:
            self.add_player(p)
        self.cardcount = cardcount
        self.state = GameState(saved_game)
        self.started = False

    def add_player(self, name):
        """Add a player

        Arguments:
        - `name`: The player's name'
        """
        self.players[name] = Player(name)
        self.players[name].hand = Hand(self.deck)

    def run(self):
        "Start the game"
        self.started = True


if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()
    hand = Hand(deck)
    for i in range(5):
        print hand.draw()
    print hand.cards
