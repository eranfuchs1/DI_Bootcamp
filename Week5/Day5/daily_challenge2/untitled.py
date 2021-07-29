from random import shuffle

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def __str__(self):
        return f"{self.suit} {self.value}"

class Cards:
    def __init__(self):
        self.cards = [Card(suit, value) for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades'] for value in ['A'] + list(range(2,11)) + ['J','Q','K']]
    def stack_card(self, card):
        self.cards.append(card)

class Deck(Cards):
    def shuffle(self):
        if len(self.cards) == 52:
            shuffle(self.cards)
        else:
            raise ValueError
    def deal(self):
        return self.cards.pop()


if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()
    for _ in range(10):
        print(deck.deal())
