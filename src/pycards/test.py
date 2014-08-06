from unittest import TestCase
from pycards.deck import Card, Deck, RANKS, SUITS
from pycards.game import Hand, Game

class TestHand(TestCase):

    def setUp(self):
        self.deck = Deck()
        self.cards = []
        self.cards.extend([Card(rank='nine',suit='hearts'), Card(rank='ten', suit='diamonds'), Card('ten','spades'),
                           Card(rank='three', suit='clubs')])
        self.instance = Hand(self.cards)

    def test_value(self):
        """Make sure the value of the hand is calculated correctly"""
        self.assertEqual(self.instance.value(), 32)
        
class TestGame(TestCase):

    def setUp(self):
        playerlist = {'a': None,'b': None}
        self.instance = Game(cardcount=2, playerlist=playerlist)

    def test_playerlist(self):
        assert(self.instance.players['a'].name == 'a')

    def test_deal(self):
        """Test that dealing works"""
        playerlist = [self.instance.players[i].name for i in self.instance.players]
        hands = self.instance.deck.deal(playerlist, 2)
        for player in hands:
            self.instance.add_player(player)
        for player in hands:
            self.instance.players[player].hand = Hand(hands[player])
        self.assertEqual(len(self.instance.players['a'].hand), 2)
        
class TestDeck(TestCase):

    def setUp(self):
        self.instance = Deck()

    def test_deck_length(self):
        """Make sure the deck is 52 cards"""
        assert(len(self.instance) == 52)

    def test_card_rank(self):
        """Make sure rank is valid"""
        card = self.instance.dealone()
        assert(card.rank in RANKS)

    def test_card_suit(self):
        """Make sure the suit is valid"""
        card = self.instance.dealone()
        assert(card.suit in SUITS)

    def test_dealone(self):
        """Make sure deck is reduced by one when we deal a card"""
        l1 = len(self.instance)
        self.instance.dealone()
        l2 = len(self.instance)
        assert(l1 - l2 == 1)

    def test_shuffle(self):
        """Make sure the deck is shuffled properly"""
        self.instance.shuffle()
        unshuffled = Deck()
        # testing that at least one card differs. Dumb, but how else to check
        # so that the test doesn't fail randomly?
        assert(not all([self.instance.deck[i] == unshuffled.deck[i] for i in range(52)]))

    def test_no_shuffle(self):
        """Make sure the first card in an unshuffled deck is the king of clubs"""
        assert(self.instance.dealone() == Card('king','clubs'))

    def test_deal_no_shuffle(self):
        """Make sure deal works as expected"""
        kc = Card('king','clubs')
        kd = Card('king','diamonds')
        ks = Card('king','spades')
        kh = Card('king','hearts')
        expected = {'a': [kc, kd], 'b': [ks, kh]}
        actual = self.instance.deal(['a','b'],2)
        assert(actual == expected)

    def test_deal_length_change(self):
        """Deal should reduce the deck length by cardcount parameter"""
        self.instance.deal(['a','b'],2)
        assert(len(self.instance) == 48)

    def test_bad_cardcount_value(self):
        """Raise ValueError if cardcount*players is larger than deck length"""
        self.assertRaises(ValueError, self.instance.deal, ['a','b'], 27)

    def test_some_values(self):
        """Check some card values"""
        self.instance.shuffle()
        for p in self.instance:
            if p.rank == 'ace':
                assert(p.value == 1)
            if p.rank == 'ten':
                assert(p.value == 10)
            if p.rank == 'jack':
                assert(p.value == 10)
