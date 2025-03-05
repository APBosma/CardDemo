class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        """Adds a card to the hand."""
        self.cards.append(card)

    def show_hand(self):
        """Displays the cards in the hand."""
        return ', '.join(self.cards) if self.cards else "Hand is empty."

    def card_count(self):
        """Returns the number of cards in the hand."""
        return len(self.cards)

# Example usage:
hand = Hand()
hand.add_card("Ace of Spades")
hand.add_card("10 of Hearts")
print(hand.show_hand())  # Output: Ace of Spades, 10 of Hearts
print(hand.card_count())  # Output: 2
