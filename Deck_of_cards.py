import random

class Card:
    def __init__(self, suit, value):
        self._suit = suit
        self._value = value
        self.name = f'{self._value} {self._suit}'

    def __str__(self):
        return self.name

class Deck_of_Cards:

    def __init__(self):
        self._original_deck = []
        for suit in ['Бубен', "Черви", "Пик", "Треф"]:
            for card in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
                self._original_deck.append(Card(suit, card))
        self.deck = self._original_deck.copy()

    def deal(self):
        if not self.deck:
            print('В колоде не осталось карт.')
            return None
        return self.deck.pop()

    def mix(self):
        self.deck = self._original_deck.copy()
        random.shuffle(self.deck)

    def get_deck(self):
        for i in self.deck:
            print(i, end=', ')
        print()
        print(f'В колоде осталось {len(self.deck)} карт.')


test_deck = Deck_of_Cards()
test_deck.get_deck()
print()
test_deck.mix()
test_deck.get_deck()
print()
print(test_deck.deal())
print(test_deck.deal())
print(test_deck.deal())
test_deck.get_deck()
print()
test_deck.mix()
test_deck.get_deck()