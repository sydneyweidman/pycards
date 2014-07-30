##############################################################################
##
##     Copyright Sydney Weidman, 2014
##     Author: Sydney Weidman <sydney.weidman@gmail.com>
##
##     This program is free software: you can redistribute it and/or modify
##     it under the terms of the GNU General Public License as published by
##     the Free Software Foundation, either version 3 of the License, or
##     (at your option) any later version.
##
##     This program is distributed in the hope that it will be useful,
##     but WITHOUT ANY WARRANTY; without even the implied warranty of
##     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##     GNU General Public License for more details.
##
##     You should have received a copy of the GNU General Public License
##     along with this program.  If not, see <http://www.gnu.org/licenses/>.
##
##############################################################################
from pycards.deck import Deck

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
    
    def __init__(self, cards=[]):
        """Create the hand
        
        Arguments:
        - `cards`: The a list of card instances with which to initialize the hand
        """
        self.cardcount = len(cards)
        self.cards = cards

    def __len__(self):
        return len(self.cards)
    
    def discard(self, cards):
        """Discard one or more cards"""
        for card in cards:
            self.cards.remove(card)

    def draw(self, cards):
        """Pickup one or more cards"""
        self.cards.extend(cards)
        
    def value(self):
        """The numerical value of the hand, if any
        """
        return sum([i.value for i in self.cards])

class GameState(object):
    """A list of dictionaries containing the game state. Each element of the list represents one turn.
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

    >>> from pycards.game import Game # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    >>> g = Game(2,{'a':None,'b':None})
    >>> g.players
    {'a': a, 'b': b}
    >>> g.run()
    >>> g.started
    True
    """
    
    def __init__(self, cardcount, playerlist={}, saved_game=None):
        """Set up the card game. Save the game state in the "turns" attribute.
        
        Arguments:
        - `cardcount`:   The initial cardcount
        - `playerlist`:  The players' names in a dict
        - `saved_game`:  A game that was previously saved
        """
        self.players = playerlist
        for p in self.players:
            self.add_player(p)
        self.cardcount = cardcount
        self.deck = Deck()
        self.state = GameState(saved_game)
        self.started = False

    def add_player(self, name):
        """Add a player
        
        Arguments:
        - `name`: The player's name'
        """
        self.players[name] = Player(name)
        self.players[name].hand = Hand()
         
    def run(self):
        "Start the game"
        self.started = True

        


