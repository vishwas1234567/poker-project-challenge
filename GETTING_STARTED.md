# Getting Started with Probability Games

Welcome! This guide will help you get up and running with the probability games in minutes.

## Choose Your Starting Method

### Option 1: Quick Start (Recommended for Beginners)

The easiest way to get started is with the interactive menu:

```bash
python quick_start.py
```

This provides a simple menu to choose which game to play. No advanced knowledge needed!

### Option 2: Command Line Interface (CLI)

Once installed, use the professional CLI:

```bash
# Install first
pip install .

# Run commands
probability-games monty-hall
probability-games poker-simple
probability-games poker-probability
```

### Option 3: Python Module Import

Use the games directly in your Python code:

```python
from probability_games.games.monty_hall import run_monty_hall_analysis
from probability_games.games.poker import play_poker_probability

# Run simulations
results = run_monty_hall_analysis(100000)

# Play games
play_poker_probability()
```

### Option 4: Google Colab (No Installation!)

Run directly in your browser:

1. Go to https://colab.research.google.com/
2. Click "New Notebook"
3. Paste and run:

```python
!git clone https://github.com/yourusername/probability-games.git
%cd probability-games
!pip install -e .

from probability_games.games.monty_hall import run_monty_hall_analysis, display_monty_hall_results
results = run_monty_hall_analysis(100000)
display_monty_hall_results(results)
```

## Installation Steps

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/probability-games.git
cd probability-games
```

### Step 2: Install the Package

Choose one method:

**Production Install:**
```bash
pip install .
```

**Development Install** (if you want to modify code):
```bash
pip install -e .
```

**No Install** (run directly):
```bash
python -m probability_games monty-hall
```

### Step 3: Verify Installation

```bash
python -m probability_games --help
```

You should see the help menu. Success!

## Your First Game

### Monty Hall (Quick 2-Minute Experience)

This is the fastest way to see the package in action:

```bash
python -m probability_games monty-hall
```

**Output Example:**
```
============================================================
           MONTY HALL PROBLEM ANALYSIS
============================================================

Total Simulations: 100,000

------------------------------------------------------------
Stay Strategy Win Rate:   0.3321 (33.21%)
Switch Strategy Win Rate: 0.6679 (66.79%)
------------------------------------------------------------
Advantage of Switching:   0.3358 (33.58%)
============================================================
```

**What's happening?** The simulation shows why switching doors is better than staying!

### Simple Poker (Interactive Game)

Play against a dealer:

```bash
python -m probability_games poker-simple
```

**How to play:**
1. You start with $1000
2. Enter your bet
3. See your cards
4. Watch community cards reveal
5. See if you win!

### Poker with Probability (Learn Odds)

See your winning odds at each stage:

```bash
python -m probability_games poker-probability
```

**What's different?** You'll see live probability calculations showing your chances of winning at each phase.

## Common Questions

### Q: I get "command not found: probability-games"

**A:** You haven't installed the package yet. Try:
```bash
pip install -e .
```

Or use the module directly:
```bash
python -m probability_games monty-hall
```

### Q: Can I use this in Google Colab?

**A:** Yes! See [GOOGLE_COLAB.md](GOOGLE_COLAB.md) for detailed instructions.

### Q: Do I need to install any packages?

**A:** No! The project uses only Python's standard library. Zero external dependencies.

### Q: Can I modify the games?

**A:** Absolutely! It's open source. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Q: What Python versions work?

**A:** Python 3.6 and above. Check your version:
```bash
python --version
```

## Next Steps

### Learn More About the Games

- **Monty Hall**: Study [USE_CASES.md](USE_CASES.md) for real-world applications
- **Poker**: Read about hand rankings and probability in the code comments
- **Monte Carlo**: Understand how simulations work with our commented code

### Run on Your Own Machine

1. Clone the repository
2. Install with `pip install -e .`
3. Explore the code in `probability_games/games/`
4. Modify and experiment!

### Contribute to the Project

Help make this better:
- Report bugs
- Suggest new games
- Improve documentation
- Fix issues

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

### Use in a Project

Import and use the functions in your own Python projects:

```python
from probability_games.games.monty_hall import simulate_monty_hall
from probability_games.games.poker import calculate_win_probability

# Use in your own code
win_rate = simulate_monty_hall(10000, switch_choice=True)
poker_odds = calculate_win_probability(my_hand, community_cards)
```

## Need Help?

- **Questions?** Open an issue on GitHub
- **Found a bug?** Report it in Issues
- **Want to contribute?** See CONTRIBUTING.md
- **Questions about math?** Check USE_CASES.md for educational resources

## Quick Reference

```bash
# Install
pip install .

# Run games
probability-games monty-hall
probability-games poker-simple
probability-games poker-probability

# Quick start menu
python quick_start.py

# Help
probability-games --help

# Development
make help          # Show all commands
make run-monty     # Run Monty Hall
```

Happy learning! 🎓
