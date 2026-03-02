"""Simple Poker Casino Game

A basic poker game where you play against a dealer.
Uses simplified hand strength scoring for game logic.
"""

import random

# ----- Card Setup -----
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
         'J', 'Q', 'K', 'A']

deck = [(rank, suit) for suit in suits for rank in ranks]


# ----- Hand Strength (VERY simplified scoring) -----
def hand_strength(hand):
    """Calculate hand strength based on card values (simplified scoring)"""
    rank_values = {r: i for i, r in enumerate(ranks)}
    values = sorted([rank_values[card[0]] for card in hand], reverse=True)
    return sum(values[:5])  # crude scoring


# ----- Deal Cards -----
def deal_cards(deck, num):
    """Deal a specified number of cards from the deck"""
    cards = random.sample(deck, num)
    for card in cards:
        deck.remove(card)
    return cards


# ----- Game Logic -----
def play_game():
    """Main game loop for Simple Poker Casino"""
    global deck
    deck = [(rank, suit) for suit in suits for rank in ranks]

    player_money = 1000
    pot = 0

    print("\nWelcome to Simple Poker Casino!")
    print("You start with $1000\n")

    while player_money > 0:
        print(f"\nYour balance: ${player_money}")
        bet = int(input("Enter your bet (0 to quit): "))

        if bet == 0:
            break

        if bet > player_money:
            print("Not enough money!")
            continue

        player_money -= bet
        pot = bet * 2  # Dealer matches bet

        # Deal hole cards
        player_hand = deal_cards(deck, 2)
        dealer_hand = deal_cards(deck, 2)

        print(f"\nYour cards: {player_hand}")

        # Flop
        flop = deal_cards(deck, 3)
        print(f"Flop: {flop}")

        # Turn
        turn = deal_cards(deck, 1)
        print(f"Turn: {turn}")

        # River
        river = deal_cards(deck, 1)
        print(f"River: {river}")

        community = flop + turn + river

        # Final hands
        player_final = player_hand + community
        dealer_final = dealer_hand + community

        player_score = hand_strength(player_final)
        dealer_score = hand_strength(dealer_final)

        print("\n--- Showdown ---")
        print(f"Dealer cards: {dealer_hand}")

        if player_score > dealer_score:
            print("You WIN!")
            player_money += pot
        elif player_score < dealer_score:
            print("Dealer wins.")
        else:
            print("It's a tie!")
            player_money += bet  # return bet

        print(f"Pot was: ${pot}")
        pot = 0

    print("\nGame over.")
    print(f"Final balance: ${player_money}")


if __name__ == "__main__":
    play_game()
