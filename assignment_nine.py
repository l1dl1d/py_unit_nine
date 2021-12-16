import card
import deck
def deal_cards(the_deck):
    hand = []
    for x in range(5):
        hand.append(the_deck.deal())
    return hand
def compare_cards(card1, card2):
    card1 = deal_cards()
    card2 = deal_cards()
    if card1 > card2:
        print("Player One wins the round")
    elif card2 > card1:
        print("player two wins the round")
