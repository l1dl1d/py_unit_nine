import card
import deck


def deal_cards(the_deck):
    hand = []
    for x in range(5):
        hand.append(the_deck.deal())
    return hand


def compare_cards(card1, card2):
    if card1 > card2:
        return "Player One"
    elif card2 > card1:
        return "Player Two"


def main():
    player_one = deal_cards()
    player_two = deal_cards()
