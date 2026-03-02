#!/usr/bin/env python3
"""
Examples of using the probability_games package in your own code.

This script demonstrates how to import and use the games and simulations
directly in Python applications.
"""

import sys
import os

# Add project root to path for local development
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from probability_games.games.monty_hall import (
    simulate_monty_hall,
    run_monty_hall_analysis,
    display_monty_hall_results,
)
from probability_games.games.poker import (
    calculate_win_probability,
    hand_strength,
    format_cards,
)


def example_1_monty_hall_basic():
    """Example 1: Run basic Monty Hall simulation."""
    print("\n" + "=" * 60)
    print("EXAMPLE 1: Basic Monty Hall Simulation")
    print("=" * 60 + "\n")

    # Simulate 10,000 trials where we switch
    win_rate_switch = simulate_monty_hall(10000, switch_choice=True)
    print(f"Win rate when switching: {win_rate_switch:.4f} ({win_rate_switch*100:.2f}%)")

    # Simulate 10,000 trials where we stay
    win_rate_stay = simulate_monty_hall(10000, switch_choice=False)
    print(f"Win rate when staying: {win_rate_stay:.4f} ({win_rate_stay*100:.2f}%)")

    print(f"\nDifference: {(win_rate_switch - win_rate_stay)*100:.2f}%")


def example_2_monty_hall_analysis():
    """Example 2: Run complete analysis with formatted output."""
    print("\n" + "=" * 60)
    print("EXAMPLE 2: Monty Hall Complete Analysis")
    print("=" * 60)

    results = run_monty_hall_analysis(100000)
    display_monty_hall_results(results)


def example_3_custom_trials():
    """Example 3: Run with different numbers of trials."""
    print("\n" + "=" * 60)
    print("EXAMPLE 3: Comparing Different Trial Counts")
    print("=" * 60 + "\n")

    trial_counts = [1000, 10000, 100000]

    for trials in trial_counts:
        results = run_monty_hall_analysis(trials)
        switch_rate = results["switch_win_rate"]
        print(f"Trials: {trials:7,} | Switch Win Rate: {switch_rate:.4f} ({switch_rate*100:.2f}%)")


def example_4_poker_hand_strength():
    """Example 4: Calculate hand strength."""
    print("\n" + "=" * 60)
    print("EXAMPLE 4: Poker Hand Strength Calculation")
    print("=" * 60 + "\n")

    # Example hands
    hand1 = [("A", "Hearts"), ("K", "Clubs")]
    hand2 = [("2", "Diamonds"), ("3", "Spades")]

    community = [
        ("A", "Diamonds"),
        ("A", "Spades"),
        ("K", "Hearts"),
        ("Q", "Clubs"),
        ("J", "Diamonds"),
    ]

    strength1 = hand_strength(hand1 + community)
    strength2 = hand_strength(hand2 + community)

    print(f"Your hand: {format_cards(hand1)}")
    print(f"Community: {format_cards(community)}")
    print(f"\nYour strength: {strength1}")

    print(f"\n\nOpponent hand: {format_cards(hand2)}")
    print(f"Opponent strength: {strength2}")

    if strength1 > strength2:
        print("\n✓ You win!")
    elif strength1 < strength2:
        print("\n✗ Opponent wins.")
    else:
        print("\n= Tie!")


def example_5_poker_probability():
    """Example 5: Calculate poker win probability."""
    print("\n" + "=" * 60)
    print("EXAMPLE 5: Poker Win Probability Calculation")
    print("=" * 60 + "\n")

    # Your hand
    your_hand = [("A", "Hearts"), ("K", "Diamonds")]

    # Community cards so far
    community = [("A", "Clubs"), ("Q", "Spades"), ("J", "Hearts")]

    # Calculate probability with 5000 simulations
    win_probability = calculate_win_probability(your_hand, community, simulations=5000)

    print(f"Your hand: {format_cards(your_hand)}")
    print(f"Community cards: {format_cards(community)}")
    print(f"Cards remaining: 2 (Turn and River)")
    print(f"\nWin Probability: {win_probability:.2f}%")

    # Compare with different scenarios
    print("\n" + "-" * 60)
    print("Probability Progression Through Game Stages")
    print("-" * 60 + "\n")

    stages = [
        ("Pre-Flop", []),
        ("After Flop", [("A", "Clubs"), ("Q", "Spades"), ("J", "Hearts")]),
        (
            "After Turn",
            [("A", "Clubs"), ("Q", "Spades"), ("J", "Hearts"), ("2", "Clubs")],
        ),
    ]

    for stage_name, cards in stages:
        prob = calculate_win_probability(your_hand, cards, simulations=5000)
        print(f"{stage_name:15} | Win Probability: {prob:6.2f}%")


def example_6_batch_analysis():
    """Example 6: Run batch analysis of multiple scenarios."""
    print("\n" + "=" * 60)
    print("EXAMPLE 6: Batch Analysis of Monty Hall")
    print("=" * 60 + "\n")

    print("Running 5 independent 100K-trial simulations:\n")

    for run_num in range(1, 6):
        results = run_monty_hall_analysis(100000)
        print(
            f"Run {run_num}: Switch {results['switch_win_rate']:.4f} | "
            f"Stay {results['stay_win_rate']:.4f} | "
            f"Difference {results['difference']:.4f}"
        )

    print("\n(Notice how results converge to ~33% and ~67%)")


def example_7_simulation_comparison():
    """Example 7: Compare simulations with theoretical values."""
    print("\n" + "=" * 60)
    print("EXAMPLE 7: Theory vs Simulation")
    print("=" * 60 + "\n")

    theoretical_stay = 1 / 3  # 33.33%
    theoretical_switch = 2 / 3  # 66.67%

    print(f"Theoretical probabilities:")
    print(f"  Stay:   {theoretical_stay:.4f} ({theoretical_stay*100:.2f}%)")
    print(f"  Switch: {theoretical_switch:.4f} ({theoretical_switch*100:.2f}%)\n")

    # Run simulation
    results = run_monty_hall_analysis(1000000)

    print(f"Simulated probabilities (1M trials):")
    print(f"  Stay:   {results['stay_win_rate']:.4f} ({results['stay_win_rate']*100:.2f}%)")
    print(f"  Switch: {results['switch_win_rate']:.4f} ({results['switch_win_rate']*100:.2f}%)\n")

    print(f"Error from theory:")
    print(
        f"  Stay error:   {abs(results['stay_win_rate'] - theoretical_stay):.6f}"
    )
    print(
        f"  Switch error: {abs(results['switch_win_rate'] - theoretical_switch):.6f}"
    )


def main():
    """Run all examples."""
    print("\n" + "=" * 60)
    print("PROBABILITY GAMES - USAGE EXAMPLES")
    print("=" * 60)

    examples = [
        ("Basic Monty Hall", example_1_monty_hall_basic),
        ("Complete Analysis", example_2_monty_hall_analysis),
        ("Different Trial Counts", example_3_custom_trials),
        ("Poker Hand Strength", example_4_poker_hand_strength),
        ("Poker Probability", example_5_poker_probability),
        ("Batch Analysis", example_6_batch_analysis),
        ("Theory vs Simulation", example_7_simulation_comparison),
    ]

    print("\nAvailable examples:")
    for i, (name, _) in enumerate(examples, 1):
        print(f"  {i}. {name}")

    print(f"\n  {len(examples) + 1}. Run all examples")
    print(f"  {len(examples) + 2}. Exit\n")

    choice = input("Select example (or press Enter for all): ").strip()

    if not choice or choice == str(len(examples) + 1):
        # Run all
        for name, func in examples:
            func()
            input("\nPress Enter for next example...")
    elif choice == str(len(examples) + 2):
        print("Goodbye!")
        return
    else:
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(examples):
                examples[idx][1]()
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExamples interrupted. Goodbye!")
