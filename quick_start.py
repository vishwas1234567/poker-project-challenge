#!/usr/bin/env python3
"""Quick start script for probability games.

This script provides an interactive menu to choose and run games.
"""

import sys
import os

# Add the project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from probability_games.games.monty_hall import run_monty_hall_analysis, display_monty_hall_results
from probability_games.games.poker import play_poker_simple, play_poker_probability


def clear_screen():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def main_menu():
    """Display main menu and get user choice."""
    clear_screen()
    print("=" * 60)
    print("PROBABILITY GAMES & SIMULATIONS".center(60))
    print("=" * 60)
    print("\nSelect a game to play:\n")
    print("1. Monty Hall Problem Simulation")
    print("2. Simple Poker Casino")
    print("3. Poker with Probability Analysis")
    print("4. Exit\n")

    choice = input("Enter your choice (1-4): ").strip()
    return choice


def run_monty_hall():
    """Run Monty Hall simulation with user input."""
    clear_screen()
    print("=" * 60)
    print("MONTY HALL PROBLEM SIMULATION".center(60))
    print("=" * 60 + "\n")

    try:
        trials = input("Enter number of trials (default 100000): ").strip()
        trials = int(trials) if trials else 100000

        if trials < 1:
            print("Number of trials must be positive!")
            return

        print(f"\nRunning simulation with {trials:,} trials...")
        results = run_monty_hall_analysis(trials)
        display_monty_hall_results(results)

    except ValueError:
        print("Invalid input. Using default 100,000 trials...")
        results = run_monty_hall_analysis(100000)
        display_monty_hall_results(results)

    input("Press Enter to return to main menu...")


def main():
    """Main application loop."""
    while True:
        choice = main_menu()

        if choice == "1":
            run_monty_hall()
        elif choice == "2":
            clear_screen()
            play_poker_simple()
        elif choice == "3":
            clear_screen()
            play_poker_probability()
        elif choice == "4":
            print("\nThank you for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Goodbye!")
        sys.exit(0)
