import card
import deck
new_card = card.Card("9", "Hearts")
print(type(new_card))
other_card = card.Card("5", "Clubs")
print(other_card)
if new_card > other_card:
    print("first card was bigger")
else:
    print("second card was bigger")
new_deck = deck.Deck()
new_deck.shuffle()
print(new_deck.cards[0])