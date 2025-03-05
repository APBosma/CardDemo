import random

class Deck:
    def __init__(self):
        self.cards = []
        self.build_deck()

    def build_deck(self):
        """Generates a full deck of 52 cards."""
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.cards = [f"{rank} of {suit}" for suit in suits for rank in ranks]

    def shuffle(self):
        """Shuffles the deck."""
        random.shuffle(self.cards)

    def draw_card(self):
        """Draws a card from the deck. If the deck is empty, returns None."""
        return self.cards.pop() if self.cards else None

# Example usage:
deck = Deck()
deck.shuffle()
print(deck.draw_card())