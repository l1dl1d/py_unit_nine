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
    new_deck = deck.Deck()
    player_one = deal_cards(new_deck)
    player_two = deal_cards(new_deck)
    for x in range(5):
        card1 = player_one[x]
        card2 = player_two[x]
        print(compare_cards(card1, card2))
main()
