"""Monty Hall Problem Simulator

This script simulates the famous Monty Hall problem to demonstrate
the probability of winning if you stay vs. if you switch doors.
"""

import random


def simulate_monty_hall(num_trials, switch_choice):
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
        possible_doors = [door for door in range(3)
                          if door != player_choice and door != car]
        host_reveal = random.choice(possible_doors)

        # Step 4: If switching, pick the remaining unopened door
        if switch_choice:
            remaining_doors = [door for door in range(3)
                               if door != player_choice and door != host_reveal]
            player_choice = remaining_doors[0]

        # Step 5: Check if player wins
        if player_choice == car:
            wins += 1

    return wins / num_trials


if __name__ == "__main__":
    # Number of simulations
    trials = 100000

    stay_win_rate = simulate_monty_hall(trials, switch_choice=False)
    switch_win_rate = simulate_monty_hall(trials, switch_choice=True)

    print(f"Trials: {trials}")
    print(f"Probability of winning if you STAY: {stay_win_rate:.4f}")
    print(f"Probability of winning if you SWITCH: {switch_win_rate:.4f}")
