"""Poker Casino Games with Probability Calculations

This module provides both simple poker and poker with Monte Carlo
probability calculations.
"""

import random
import copy
from typing import List, Tuple, Dict


# Card Setup
SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

RANK_VALUES = {r: i for i, r in enumerate(RANKS)}
DECK_TEMPLATE = [(rank, suit) for suit in SUITS for rank in RANKS]


# ----- Hand Strength Calculation -----
def hand_strength(hand: List[Tuple[str, str]]) -> int:
    """
    Calculate hand strength based on card values (simplified scoring).

    Args:
        hand: List of cards (rank, suit)

    Returns:
        Integer score representing hand strength
    """
    values = sorted([RANK_VALUES[card[0]] for card in hand], reverse=True)
    return sum(values[:5])


# ----- Monte Carlo Win Probability -----
def calculate_win_probability(
    player_hand: List[Tuple[str, str]],
    community_cards: List[Tuple[str, str]],
    simulations: int = 5000,
) -> float:
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
        deck = copy.deepcopy(DECK_TEMPLATE)

        # Remove known cards
        for card in player_hand + community_cards:
            if card in deck:
                deck.remove(card)

        # Random dealer hand
        dealer_hand = random.sample(deck, 2)
        for card in dealer_hand:
            deck.remove(card)

        # Complete community cards
        remaining_cards_needed = 5 - len(community_cards)
        if remaining_cards_needed > 0 and len(deck) >= remaining_cards_needed:
            simulated_board = community_cards + random.sample(
                deck, remaining_cards_needed
            )
        else:
            simulated_board = community_cards

        player_score = hand_strength(player_hand + simulated_board)
        dealer_score = hand_strength(dealer_hand + simulated_board)

        if player_score > dealer_score:
            wins += 1
        elif player_score == dealer_score:
            ties += 1

    return (wins + ties * 0.5) / simulations * 100


# ----- Deal Cards -----
def deal_cards(deck: List[Tuple[str, str]], num: int) -> List[Tuple[str, str]]:
    """
    Deal a specified number of cards from the deck.

    Args:
        deck: Current deck of cards
        num: Number of cards to deal

    Returns:
        List of dealt cards
    """
    cards = random.sample(deck, min(num, len(deck)))
    for card in cards:
        if card in deck:
            deck.remove(card)
    return cards


# ----- Game Logic -----
def play_poker_simple(is_colab: bool = False) -> None:
    """
    Play Simple Poker Casino game.

    Args:
        is_colab: Whether running in Google Colab
    """
    player_money = 1000
    pot = 0

    print("\n" + "=" * 60)
    print("SIMPLE POKER CASINO".center(60))
    print("=" * 60)
    print("You start with $1000")
    print("=" * 60 + "\n")

    hand_count = 0
    while player_money > 0:
        deck = copy.deepcopy(DECK_TEMPLATE)
        pot = 0
        hand_count += 1

        print(f"\nHand #{hand_count} | Balance: ${player_money}")
        print("-" * 40)

        try:
            if is_colab:
                bet = int(input("Enter your bet (0 to quit): "))
            else:
                bet = int(input("Enter your bet (0 to quit): "))
        except (ValueError, EOFError):
            if is_colab:
                print("Quitting game...")
                break
            continue

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

        print(f"Your cards: {format_cards(player_hand)}")

        # Flop
        flop = deal_cards(deck, 3)
        print(f"Flop: {format_cards(flop)}")

        # Turn
        turn = deal_cards(deck, 1)
        print(f"Turn: {format_cards(turn)}")

        # River
        river = deal_cards(deck, 1)
        print(f"River: {format_cards(river)}")

        community = flop + turn + river

        # Final hands
        player_final = player_hand + community
        dealer_final = dealer_hand + community

        player_score = hand_strength(player_final)
        dealer_score = hand_strength(dealer_final)

        print("\n" + "-" * 40)
        print("SHOWDOWN")
        print("-" * 40)
        print(f"Dealer cards: {format_cards(dealer_hand)}")

        if player_score > dealer_score:
            print("YOU WIN!")
            player_money += pot
        elif player_score < dealer_score:
            print("Dealer wins.")
        else:
            print("It's a tie!")
            player_money += bet  # return bet

        print(f"Pot: ${pot}")

    print("\n" + "=" * 60)
    print("GAME OVER".center(60))
    print(f"Final balance: ${player_money}".center(60))
    print("=" * 60 + "\n")


def play_poker_probability(is_colab: bool = False) -> None:
    """
    Play Poker with live probability calculations.

    Args:
        is_colab: Whether running in Google Colab
    """
    player_money = 1000
    print("\n" + "=" * 60)
    print("POKER WITH PROBABILITY ANALYSIS".center(60))
    print("=" * 60)
    print("You start with $1000")
    print("=" * 60 + "\n")

    hand_count = 0
    while player_money > 0:
        deck = copy.deepcopy(DECK_TEMPLATE)
        pot = 0
        hand_count += 1

        print(f"\nHand #{hand_count} | Balance: ${player_money}")
        print("-" * 40)

        try:
            if is_colab:
                bet = int(input("Enter your bet (0 to quit): "))
            else:
                bet = int(input("Enter your bet (0 to quit): "))
        except (ValueError, EOFError):
            if is_colab:
                print("Quitting game...")
                break
            continue

        if bet == 0:
            break

        if bet > player_money:
            print("Not enough money!")
            continue

        player_money -= bet
        pot = bet * 2

        # Deal hole cards
        player_hand = deal_cards(deck, 2)
        print(f"\nYour cards: {format_cards(player_hand)}")

        # Pre-flop probability
        win_prob = calculate_win_probability(player_hand, [])
        print(f"Pre-Flop Win Probability: {win_prob:.2f}%")

        if not is_colab:
            input("Press Enter for Flop...")
        else:
            print("[Flop coming...]")

        # Flop
        flop = deal_cards(deck, 3)
        print(f"Flop: {format_cards(flop)}")

        win_prob = calculate_win_probability(player_hand, flop)
        print(f"After Flop Win Probability: {win_prob:.2f}%")

        if not is_colab:
            input("Press Enter for Turn...")
        else:
            print("[Turn coming...]")

        # Turn
        turn = deal_cards(deck, 1)
        print(f"Turn: {format_cards(turn)}")

        win_prob = calculate_win_probability(player_hand, flop + turn)
        print(f"After Turn Win Probability: {win_prob:.2f}%")

        if not is_colab:
            input("Press Enter for River...")
        else:
            print("[River coming...]")

        # River
        river = deal_cards(deck, 1)
        print(f"River: {format_cards(river)}")

        community = flop + turn + river

        win_prob = calculate_win_probability(player_hand, community)
        print(f"Final Win Probability: {win_prob:.2f}%")

        # Dealer hand
        dealer_hand = deal_cards(deck, 2)

        print("\n" + "-" * 40)
        print("SHOWDOWN")
        print("-" * 40)
        print(f"Dealer cards: {format_cards(dealer_hand)}")

        player_score = hand_strength(player_hand + community)
        dealer_score = hand_strength(dealer_hand + community)

        if player_score > dealer_score:
            print("YOU WIN!")
            player_money += pot
        elif player_score < dealer_score:
            print("Dealer wins.")
        else:
            print("It's a tie!")
            player_money += bet

        print(f"Pot: ${pot}")

    print("\n" + "=" * 60)
    print("GAME OVER".center(60))
    print(f"Final balance: ${player_money}".center(60))
    print("=" * 60 + "\n")


def format_cards(cards: List[Tuple[str, str]]) -> str:
    """Format cards for display."""
    return ", ".join([f"{rank}{suit[0]}" for rank, suit in cards])


if __name__ == "__main__":
    play_poker_probability()
