"""Probability Games and Simulations

A comprehensive package for learning probability through interactive games
and Monte Carlo simulations.
"""

__version__ = "1.0.0"
__author__ = "Community Contributors"
__description__ = "Educational probability games and simulations"

from probability_games.games.monty_hall import simulate_monty_hall
from probability_games.games.poker import (
    calculate_win_probability,
    play_poker_simple,
    play_poker_probability,
)

__all__ = [
    "simulate_monty_hall",
    "calculate_win_probability",
    "play_poker_simple",
    "play_poker_probability",
]
