"""Command-line interface for probability games."""

import argparse
import sys
from typing import Optional

from probability_games.games.monty_hall import run_monty_hall_analysis, display_monty_hall_results
from probability_games.games.poker import play_poker_simple, play_poker_probability
from probability_games.config import MONTY_HALL_TRIALS


def create_parser() -> argparse.ArgumentParser:
    """Create and configure argument parser."""
    parser = argparse.ArgumentParser(
        prog="probability-games",
        description="Interactive probability games and simulations",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run Monty Hall simulation
  python -m probability_games monty-hall
  
  # Run Monty Hall with custom trials
  python -m probability_games monty-hall --trials 50000
  
  # Play simple poker
  python -m probability_games poker-simple
  
  # Play poker with probabilities
  python -m probability_games poker-probability
  
  # Run in Google Colab mode
  python -m probability_games poker-simple --colab
        """,
    )

    subparsers = parser.add_subparsers(dest="game", help="Game to play")

    # Monty Hall subcommand
    monty_parser = subparsers.add_parser(
        "monty-hall",
        help="Run Monty Hall problem simulation",
        aliases=["monty", "mh"],
    )
    monty_parser.add_argument(
        "--trials",
        type=int,
        default=MONTY_HALL_TRIALS,
        help=f"Number of trials (default: {MONTY_HALL_TRIALS})",
    )

    # Poker simple subcommand
    poker_simple_parser = subparsers.add_parser(
        "poker-simple",
        help="Play simple poker game",
        aliases=["poker", "p"],
    )
    poker_simple_parser.add_argument(
        "--colab",
        action="store_true",
        help="Run in Google Colab mode (no interactive input)",
    )

    # Poker probability subcommand
    poker_prob_parser = subparsers.add_parser(
        "poker-probability",
        help="Play poker with probability calculations",
        aliases=["poker-prob", "pp"],
    )
    poker_prob_parser.add_argument(
        "--colab",
        action="store_true",
        help="Run in Google Colab mode (no interactive input)",
    )

    return parser


def handle_monty_hall(args: argparse.Namespace) -> None:
    """Handle Monty Hall simulation."""
    print("\nRunning Monty Hall simulation with {} trials...".format(args.trials))
    results = run_monty_hall_analysis(args.trials)
    display_monty_hall_results(results)


def handle_poker_simple(args: argparse.Namespace) -> None:
    """Handle simple poker game."""
    play_poker_simple(is_colab=args.colab)


def handle_poker_probability(args: argparse.Namespace) -> None:
    """Handle poker with probability calculations."""
    play_poker_probability(is_colab=args.colab)


def main(argv: Optional[list] = None) -> int:
    """Main entry point for CLI."""
    parser = create_parser()
    args = parser.parse_args(argv)

    # If no game specified, show help
    if args.game is None:
        parser.print_help()
        return 0

    try:
        if args.game in ["monty-hall", "monty", "mh"]:
            handle_monty_hall(args)
        elif args.game in ["poker-simple", "poker", "p"]:
            handle_poker_simple(args)
        elif args.game in ["poker-probability", "poker-prob", "pp"]:
            handle_poker_probability(args)
        else:
            parser.print_help()
            return 1

    except KeyboardInterrupt:
        print("\n\nGame interrupted by user.")
        return 1
    except Exception as e:
        print(f"\nError: {e}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
