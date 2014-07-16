##############################################################################
##
##     Copyright University of Winnipeg, 2014
##     Author: Sydney Weidman <s.weidman@uwinnipeg.ca>
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

class Hand(object):
    """A class representing a hand of cards
    """
    
    def __init__(self, cards):
        """Create the hand
        
        Arguments:
        - `cards`: The a list of card instances with which to initialize the hand
        """
        self.cardcount = len(cards)
        self.cards = cards

    def discard(self, cards):
        """Discard one or more cards"""
        for card in cards:
            self.cards.remove(card)

    def pickup(self, cards):
        """Pickup one or more cards"""
        self.cards.extend(cards)

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
    """
    
    def __init__(self, players, rules, saved_game):
        """Set up the card game. Save the game state in the "turns" attribute.
        
        Arguments:
        - `players`: A list of Player instances
        - `rules`: A set of rules describing the game
        - `saved_game`: A game that was previously saved
        """
        self.players = players
        self.deck = Deck()
        self.turns = GameState()

    def run(self):
        "Start the game"
        pass

        


