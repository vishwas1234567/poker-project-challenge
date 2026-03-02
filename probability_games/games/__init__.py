"""Games module for probability simulations."""

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
