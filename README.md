# Probability Games & Simulations

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A collection of Python scripts demonstrating probability concepts through interactive games and Monte Carlo simulations. Perfect for learning probability theory through hands-on experimentation.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Resources](#resources)

## Overview

This project brings probability concepts to life through practical, interactive examples. Whether you're learning about the Monty Hall paradox or exploring Monte Carlo methods in poker, these games make probability intuitive and fun.

## Features

- 🎰 **Interactive Games**: Play Monty Hall and Texas Hold'em against the dealer
- 📊 **Monte Carlo Simulations**: Real-time probability calculations with 50,000+ trial simulations
- 🎓 **Educational Focus**: Learn probability concepts while playing
- 🚀 **Zero Dependencies**: Uses only Python's standard library
- ⚡ **Lightweight**: No heavy frameworks or complex setups

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/probability-games.git
cd probability-games

# Install the package
pip install .

# Or install in development mode
pip install -e .
```

### Running Games via CLI

```bash
# Run Monty Hall simulation
python -m probability_games monty-hall

# Run with custom number of trials
python -m probability_games monty-hall --trials 50000

# Play simple poker
python -m probability_games poker-simple

# Play poker with probability analysis
python -m probability_games poker-probability
```

### Command-line Help

```bash
python -m probability_games --help
```

## Games

### 1. Monty Hall Simulation
Demonstrates the famous Monty Hall paradox through 100,000 simulations. Shows why switching doors increases your win probability from 33% to 67%.

```bash
python -m probability_games monty-hall --trials 100000
```

### 2. Simple Poker Casino
Play Texas Hold'em against a dealer with $1000 starting capital. Learn basic hand evaluation and poker mechanics.

```bash
python -m probability_games poker-simple
```

### 3. Poker with Probability Analysis
Enhanced poker game that calculates your win probability at each game stage using Monte Carlo simulations. Perfect for learning poker odds.

```bash
python -m probability_games poker-probability
```

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)
- Works on Windows, macOS, and Linux

## Installation Methods

### Method 1: From Source (Recommended)

```bash
git clone https://github.com/yourusername/probability-games.git
cd probability-games
pip install .
```

### Method 2: Development Installation

```bash
git clone https://github.com/yourusername/probability-games.git
cd probability-games
pip install -e .  # Install in editable mode
```

### Method 3: Direct Module Execution

No installation needed! Just clone and run:

```bash
git clone https://github.com/yourusername/probability-games.git
cd probability-games
python -m probability_games monty-hall
```

### Verify Installation

```bash
probability-games monty-hall --help
```

## Google Colab

Run directly in your browser without installing anything!

```python
!git clone https://github.com/yourusername/probability-games.git
%cd probability-games
!pip install -e .

from probability_games.games.monty_hall import run_monty_hall_analysis, display_monty_hall_results
results = run_monty_hall_analysis(100000)
display_monty_hall_results(results)
```

See [GOOGLE_COLAB.md](GOOGLE_COLAB.md) for detailed instructions.

## 🎯 Learning Outcomes

- **Monty Hall**: Understanding conditional probability and why intuition can be misleading
- **Poker Simple**: Basic game logic and hand evaluation
- **Poker Probability**: Monte Carlo methods for probability estimation and practical application in decision-making

## Usage

### Running the Scripts

All scripts can be run directly from the command line:

```bash
# Run Monty Hall Simulation
python monty_hall_simulation.py

# Run Simple Poker Game
python poker_simple.py

# Run Poker with Probability Calculations
python poker_probability.py
```

### How to Play

#### Monty Hall Simulation
Simply run the script to see the results of 100,000 simulations showing the probability advantage of switching doors. The output will display:
- Win rate when staying
- Win rate when switching
- Clear demonstration of the 33% vs 67% probability difference

#### Poker Games
1. Start with $1000 in your bankroll
2. Enter your bet amount for each hand
3. Review your hole cards (your two private cards)
4. Follow the game through Flop → Turn → River phases
   - Flop: 3 community cards revealed
   - Turn: 1 additional community card
   - River: Final community card
5. In the Probability version, see live odds updates at each stage
6. See the final hand results at showdown
7. Continue playing until you're out of money or choose to quit

## Project Structure

```
probability-games/
├── probability_games/             # Main package
│   ├── __init__.py               # Package initialization
│   ├── __main__.py               # CLI entry point
│   ├── cli.py                    # Command-line interface
│   ├── config.py                 # Configuration and constants
│   └── games/                    # Game modules
│       ├── __init__.py
│       ├── monty_hall.py         # Monty Hall simulation
│       └── poker.py              # Poker games
├── notebooks/                    # Jupyter notebooks for Colab
│   └── Probability_Games_Tutorial.ipynb
├── setup.py                      # Package setup
├── pyproject.toml                # Project metadata
├── Makefile                      # Development commands
├── README.md                     # This file
├── GOOGLE_COLAB.md               # Colab instructions
├── CONTRIBUTING.md               # Contribution guidelines
├── CODE_OF_CONDUCT.md            # Community standards
├── LICENSE                       # MIT License
└── .gitignore                    # Git ignore rules
```

## Contributing

We welcome contributions from the community! Whether it's bug fixes, new features, or documentation improvements, your help makes this project better.

### Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/your-username/probability-games.git
   cd probability-games
   ```
3. **Create a new branch** for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Make your changes** and test thoroughly
5. **Commit your changes** with clear, descriptive messages:
   ```bash
   git commit -m "Add feature: description of what you added"
   ```
6. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Open a Pull Request** with a clear description of your changes

### Contribution Guidelines

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines on:
- Code style and standards
- Testing requirements
- Commit message format
- Pull request process
- Code of conduct

### Ideas for Contributions

- Add more probability games or simulations
- Enhance poker hand evaluation logic
- Improve UI/output formatting
- Add statistical analysis features
- Create tutorials or educational content
- Fix bugs or improve documentation

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Code of Conduct

This project adheres to a [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior.

## Development

### Using Make Commands

```bash
make help          # Show all available commands
make dev           # Install in development mode
make run-monty     # Run Monty Hall simulation
make run-poker     # Run Simple Poker
make run-poker-prob # Run Poker with probability
make lint          # Check code style
make format        # Format code
make clean         # Clean build artifacts
```

### Running in Python Scripts

```python
from probability_games.games.monty_hall import run_monty_hall_analysis
from probability_games.games.poker import play_poker_probability

# Monty Hall
results = run_monty_hall_analysis(100000)

# Poker
play_poker_probability()
```

## Resources

- [Monty Hall Problem - Wikipedia](https://en.wikipedia.org/wiki/Monty_Hall_problem)
- [Texas Hold'em - Wikipedia](https://en.wikipedia.org/wiki/Texas_hold_%27em)
- [Monte Carlo Method - Wikipedia](https://en.wikipedia.org/wiki/Monte_Carlo_method)
- [Probability Theory - Khan Academy](https://www.khanacademy.org/math/probability)
