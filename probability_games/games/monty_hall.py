"""Monty Hall Problem Simulator

This module simulates the famous Monty Hall problem to demonstrate
the probability of winning if you stay vs. if you switch doors.
"""

import random
from typing import Dict, Tuple


def simulate_monty_hall(num_trials: int, switch_choice: bool) -> float:
    """
    Simulate the Monty Hall problem.

    Args:
        num_trials: Number of simulations to run
        switch_choice: Boolean - True if player switches doors, False if stays

    Returns:
        Win rate as a decimal (e.g., 0.6667 for ~67%)
    """
    wins = 0

    for _ in range(num_trials):
        # Step 1: Randomly place the car behind one of 3 doors
        car = random.randint(0, 2)

        # Step 2: Player makes an initial choice
        player_choice = random.randint(0, 2)

        # Step 3: Host reveals a goat door (not car and not player's choice)
        possible_doors = [
            door for door in range(3) if door != player_choice and door != car
        ]
        host_reveal = random.choice(possible_doors)

        # Step 4: If switching, pick the remaining unopened door
        if switch_choice:
            remaining_doors = [
                door
                for door in range(3)
                if door != player_choice and door != host_reveal
            ]
            player_choice = remaining_doors[0]

        # Step 5: Check if player wins
        if player_choice == car:
            wins += 1

    return wins / num_trials


def run_monty_hall_analysis(num_trials: int) -> Dict[str, float]:
    """
    Run complete Monty Hall analysis with both strategies.

    Args:
        num_trials: Number of simulations to run

    Returns:
        Dictionary with results
    """
    stay_win_rate = simulate_monty_hall(num_trials, switch_choice=False)
    switch_win_rate = simulate_monty_hall(num_trials, switch_choice=True)

    return {
        "trials": num_trials,
        "stay_win_rate": stay_win_rate,
        "switch_win_rate": switch_win_rate,
        "difference": switch_win_rate - stay_win_rate,
    }


def display_monty_hall_results(results: Dict[str, float]) -> None:
    """
    Display Monty Hall simulation results in a formatted way.

    Args:
        results: Dictionary containing simulation results
    """
    print("\n" + "=" * 60)
    print("MONTY HALL PROBLEM ANALYSIS".center(60))
    print("=" * 60)
    print(f"\nTotal Simulations: {results['trials']:,}")
    print("\n" + "-" * 60)
    print(f"Stay Strategy Win Rate:   {results['stay_win_rate']:.4f} ({results['stay_win_rate']*100:.2f}%)")
    print(f"Switch Strategy Win Rate: {results['switch_win_rate']:.4f} ({results['switch_win_rate']*100:.2f}%)")
    print("-" * 60)
    print(f"Advantage of Switching:   {results['difference']:.4f} ({results['difference']*100:.2f}%)")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    from probability_games.config import MONTY_HALL_TRIALS

    results = run_monty_hall_analysis(MONTY_HALL_TRIALS)
    display_monty_hall_results(results)
