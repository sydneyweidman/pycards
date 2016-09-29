from unittest import TestCase
from pycards.deck import Card, Deck, RANKS, SUITS
from pycards.game import Game


class TestGame(TestCase):

    def setUp(self):
        self.cardcount = 5
        playerlist = {'a': None, 'b': None}
        self.instance = Game(cardcount=self.cardcount, playerlist=playerlist)

    def test_playerlist(self):
        assert(self.instance.players['a'].name == 'a')


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

    def test_card_value(self):
        """Make sure the value is applied to the card"""
        card = Card(rank='king', suit='spades', value=42)
        self.assertEqual(card.value, 42)

    def test_card_comparator_lt(self):
        card1 = Card('two', 'hearts', value=11)
        card2 = Card('two', 'hearts', value=12)
        assert card1 < card2

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
        assert(not all([self.instance.deck[i] == unshuffled.deck[i]
                        for i in range(52)]))

    def test_no_shuffle(self):
        """Make sure the first card in an unshuffled deck is the king
        of clubs"""
        assert(self.instance.dealone() == Card('king', 'clubs'))

    def test_deal_no_shuffle(self):
        """Make sure deal works as expected"""
        kc = Card('king', 'clubs')
        kd = Card('king', 'diamonds')
        ks = Card('king', 'spades')
        kh = Card('king', 'hearts')
        expected = {'a': [kc, kd], 'b': [ks, kh]}
        actual = self.instance.deal(['a', 'b'], 2)
        assert(actual == expected)

    def test_deal_length_change(self):
        """Deal should reduce the deck length by cardcount parameter"""
        self.instance.deal(['a', 'b'], 2)
        assert(len(self.instance) == 48)

    def test_bad_cardcount_value(self):
        """Raise ValueError if cardcount*players is larger than deck length"""
        self.assertRaises(ValueError, self.instance.deal, ['a', 'b'], 27)

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
