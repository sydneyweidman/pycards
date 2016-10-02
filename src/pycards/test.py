from unittest import TestCase
from pycards.deck import Card, Deck, Hand, RANKS, SUITS
from pycards.game import Game, Player, GameState


class TestGameState(TestCase):

    def setUp(self):
        self.saved = [{'foo': 'bar'}, ]
        self.instance = GameState(saved_game=self.saved)

    def test_saved_game(self):
        """Make sure we can load a saved game"""
        self.assertEqual(self.instance.state, self.saved)


class TestHand(TestCase):

    def setUp(self):
        self.deck = Deck()
        self.deck.populate()
        self.hand = Hand(player=Player('Fred'), from_deck=self.deck)

    def test_hand_draw(self):
        self.hand.draw()
        self.assertEqual(len(self.hand), 1)

    def test_hand_discard(self):
        card = self.hand.draw()
        self.hand.discard(card)
        self.assertEqual(len(self.hand), 0)

    def test_hand_value(self):
        card1 = self.hand.draw()
        card2 = self.hand.draw()
        self.assertEqual(self.hand.value(), card1.value + card2.value)


class TestPlayer(TestCase):

    def setUp(self):
        self.instance = Player('Fred')

    def test_player_repr(self):
        """Make sure __repr__ returns name"""
        self.assertEqual(self.instance.__repr__(), self.instance.name)


class TestGame(TestCase):

    def setUp(self):
        self.cardcount = 5
        playerlist = ['a', 'b']
        self.instance = Game(cardcount=self.cardcount, playerlist=playerlist)

    def test_playerlist(self):
        assert(self.instance.players[0].name == 'a')

    def test_game_run(self):
        """calling game.run should set game.started to true"""
        self.assertFalse(self.instance.started)
        self.instance.run()
        self.assertTrue(self.instance.started)


class TestDeck(TestCase):

    def setUp(self):
        self.instance = Deck()

    def test_deck_length(self):
        """Make sure the deck is 52 cards"""
        assert(len(self.instance) == 52)

    def test_card_rank(self):
        """Make sure rank is valid"""
        card = self.instance.dealone(to_location='discard')
        assert(card.rank in RANKS)

    def test_card_suit(self):
        """Make sure the suit is valid"""
        card = self.instance.dealone(to_location='discard')
        assert(card.suit in SUITS)

    def test_card_value(self):
        """Make sure the value is applied to the card"""
        card = Card(rank='king', suit='spades', value=42)
        self.assertEqual(card.value, 42)

    def test_card_comparator_lt(self):
        """Does __lt__ work as expected?"""
        card1 = Card('two', 'hearts', 2)
        card2 = Card('three', 'spades', 3)
        assert card1 < card2

    def test_card_comparator_gt(self):
        """Does __gt__ work as expected"""
        card1 = Card('two', 'hearts', value=11)
        card2 = Card('two', 'hearts', value=12)
        self.assertGreater(card2, card1)

    def tests_card_operator_ne(self):
        """Does __ne__ work as expected?"""
        card1 = Card('two', 'hearts', value=11)
        card2 = Card('two', 'hearts', value=12)
        self.assertTrue(card2 != card1)

    def test_deck_repr(self):
        """Repr should return a descriptive string"""
        card = Card('two', 'hearts', value=2)
        self.assertEqual(u'two of hearts', card.__repr__())

    def test_deck_setitem(self):
        """Can we insert cards into the deck?"""
        card = Card('ace', 'fudgeos', 10)
        self.instance[3] = card
        self.assertIn(Card('ace', 'fudgeos', 10), self.instance)

    def test_dealone(self):
        """Make sure deck is reduced by one when we deal a card"""
        l1 = len(self.instance)
        self.instance.dealone('discard')
        l2 = len(self.instance)
        assert(l1 - l2 == 1)

    def test_shuffle(self):
        """Make sure the deck is shuffled properly"""
        self.instance.shuffle()
        unshuffled = Deck()
        # testing that at least one card differs. Dumb, but how else to check
        # so that the test doesn't fail randomly?
        assert(not all([self.instance[i] == unshuffled[i]
                        for i in range(52)]))

    def test_no_shuffle(self):
        """Make sure the first card in an unshuffled deck is the king
        of clubs"""
        assert(self.instance.dealone('discard') == Card('king', 'clubs', 10))

    def test_deal_no_shuffle(self):
        """Make sure deal works as expected"""
        kc = Card('king', 'clubs', 10)
        kd = Card('king', 'diamonds', 10)
        ks = Card('king', 'spades', 10)
        kh = Card('king', 'hearts', 10)
        expected = {'a': [kc, kd], 'b': [ks, kh]}
        actual = self.instance.deal(players=['a', 'b'], cardcount=2)
        assert(actual == expected)

    def test_deal_length_change(self):
        """Deal should reduce the deck length by cardcount parameter"""
        self.instance.deal(['a', 'b'], 2)
        assert(len(self.instance) == 48)

    def test_bad_cardcount_value(self):
        """Raise ValueError if cardcount*players is larger than deck length"""
        self.assertRaises(ValueError, self.instance.deal, ['a', 'b'], 27)

    def test_non_card_raises_type_error(self):
        """Raise TypeError if the 'cards' argument to populate contains
        non-cards"""
        deck = Deck()
        cards = [Card('king', 'spades'), Card(
            'king', 'diamonds'), Card('ace', 'hearts'), 8]
        self.assertRaises(TypeError, deck.populate, cards)

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
