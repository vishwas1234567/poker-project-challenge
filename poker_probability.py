"""Poker Casino with Win Probability Calculator

A poker game that uses Monte Carlo simulations to calculate
your probability of winning at each stage of the game.
"""

import random
import copy

# ----- Card Setup -----
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
         'J', 'Q', 'K', 'A']

deck_template = [(rank, suit) for suit in suits for rank in ranks]

rank_values = {r: i for i, r in enumerate(ranks)}


# ----- Simple Hand Strength -----
def hand_strength(hand):
    """Calculate hand strength based on card values (simplified scoring)"""
    values = sorted([rank_values[card[0]] for card in hand], reverse=True)
    return sum(values[:5])  # crude scoring


# ----- Monte Carlo Win Probability -----
def calculate_win_probability(player_hand, community_cards, simulations=5000):
    """
    Calculate win probability using Monte Carlo simulation.
    
    Args:
        player_hand: List of 2 cards in player's hand
        community_cards: List of community cards (0-5 cards)
        simulations: Number of simulations to run
    
    Returns:
        Probability of winning as a percentage (0-100)
    """
    wins = 0
    ties = 0

    for _ in range(simulations):
        deck = copy.deepcopy(deck_template)

        # Remove known cards
        for card in player_hand + community_cards:
            deck.remove(card)

        # Random dealer hand
        dealer_hand = random.sample(deck, 2)
        for card in dealer_hand:
            deck.remove(card)

        # Complete community cards
        remaining_cards_needed = 5 - len(community_cards)
        simulated_board = community_cards + random.sample(deck, remaining_cards_needed)

        player_score = hand_strength(player_hand + simulated_board)
        dealer_score = hand_strength(dealer_hand + simulated_board)

        if player_score > dealer_score:
            wins += 1
        elif player_score == dealer_score:
            ties += 1

    return (wins + ties * 0.5) / simulations * 100


# ----- Deal Cards -----
def deal_cards(deck, num):
    """Deal a specified number of cards from the deck"""
    cards = random.sample(deck, num)
    for card in cards:
        deck.remove(card)
    return cards


# ----- Game Logic -----
def play_game():
    """Main game loop for Poker Probability Casino"""
    player_money = 1000
    print("\nWelcome to Poker Probability Casino!")
    print("You start with $1000\n")

    while player_money > 0:
        deck = copy.deepcopy(deck_template)
        pot = 0

        print(f"\nYour balance: ${player_money}")
        bet = int(input("Enter your bet (0 to quit): "))

        if bet == 0:
            break

        if bet > player_money:
            print("Not enough money!")
            continue

        player_money -= bet
        pot = bet * 2

        # Deal hole cards
        player_hand = deal_cards(deck, 2)
        print(f"\nYour cards: {player_hand}")

        # Pre-flop probability
        win_prob = calculate_win_probability(player_hand, [])
        print(f"Pre-Flop Win Probability: {win_prob:.2f}%")

        input("Press Enter for Flop...")

        # Flop
        flop = deal_cards(deck, 3)
        print(f"Flop: {flop}")

        win_prob = calculate_win_probability(player_hand, flop)
        print(f"After Flop Win Probability: {win_prob:.2f}%")

        input("Press Enter for Turn...")

        # Turn
        turn = deal_cards(deck, 1)
        print(f"Turn: {turn}")

        win_prob = calculate_win_probability(player_hand, flop + turn)
        print(f"After Turn Win Probability: {win_prob:.2f}%")

        input("Press Enter for River...")

        # River
        river = deal_cards(deck, 1)
        print(f"River: {river}")

        community = flop + turn + river

        win_prob = calculate_win_probability(player_hand, community)
        print(f"Final Win Probability: {win_prob:.2f}%")

        # Dealer hand
        dealer_hand = deal_cards(deck, 2)

        print("\n--- Showdown ---")
        print(f"Dealer cards: {dealer_hand}")

        player_score = hand_strength(player_hand + community)
        dealer_score = hand_strength(dealer_hand + community)

        if player_score > dealer_score:
            print("You WIN!")
            player_money += pot
        elif player_score < dealer_score:
            print("Dealer wins.")
        else:
            print("It's a tie!")
            player_money += bet

        print(f"Pot was: ${pot}")

    print("\nGame over.")
    print(f"Final balance: ${player_money}")


if __name__ == "__main__":
    play_game()
