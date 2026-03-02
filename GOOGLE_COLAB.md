# Running Probability Games in Google Colab

Google Colab is a free cloud-based Jupyter notebook environment. You can run all probability games directly in your browser without installing anything!

## Quick Start

### Option 1: Run from Repository (Recommended)

1. Open Google Colab: https://colab.research.google.com/
2. Click "File" → "Open notebook" → "GitHub" tab
3. Paste this URL: `https://github.com/yourusername/probability-games`
4. Select the notebook: `notebooks/Probability_Games_Tutorial.ipynb`

### Option 2: Clone and Run

```python
# In a Colab cell, run:
!git clone https://github.com/yourusername/probability-games.git
cd probability-games
!pip install -e .
```

Then run games directly:
```python
from probability_games.games.monty_hall import run_monty_hall_analysis, display_monty_hall_results

results = run_monty_hall_analysis(100000)
display_monty_hall_results(results)
```

## Running Games in Colab

### Monty Hall Simulation

```python
from probability_games.games.monty_hall import run_monty_hall_analysis, display_monty_hall_results

# Run with 100,000 trials
results = run_monty_hall_analysis(100000)
display_monty_hall_results(results)
```

**Output:**
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

### Simple Poker Game

```python
from probability_games.games.poker import play_poker_simple

# Play with Colab-friendly input
play_poker_simple(is_colab=True)
```

In Colab mode, the game will guide you through each hand automatically.

### Poker with Probability Analysis

```python
from probability_games.games.poker import play_poker_probability

# Play with live win probability calculations
play_poker_probability(is_colab=True)
```

See your win probability update at each stage of the game!

## Using the CLI in Colab

You can also use the command-line interface directly:

```python
import subprocess
subprocess.run(["python", "-m", "probability_games", "monty-hall", "--trials", "50000"])
```

## Saving Your Work

To keep your results, download the notebook:
1. Click "File" → "Download"
2. Choose format (`.ipynb`, `.py`, or `.pdf`)

Or save directly to Google Drive:
```python
from google.colab import drive
drive.mount('/content/drive')

# Your work is now saved to your Drive
```

## Troubleshooting

### Issue: Module not found error

**Solution:** Reinstall the package:
```python
!pip install --force-reinstall -e .
```

### Issue: Input errors in games

**Solution:** Use the `is_colab=True` parameter in game functions to run without interactive input prompts.

### Issue: Package installation fails

**Solution:** Try installing directly from GitHub:
```python
!pip install git+https://github.com/yourusername/probability-games.git
```

## Learning Resources in Colab

The `notebooks/` directory contains:
- **Probability_Games_Tutorial.ipynb** - Complete tutorial with explanations
- **Monty_Hall_Analysis.ipynb** - Deep dive into the Monty Hall paradox
- **Poker_Probability_Guide.ipynb** - Understanding poker odds

## Tips for Colab

1. **Free GPU**: Enable GPU acceleration: Runtime → Change Runtime Type → GPU
2. **Save automatically**: Colab saves every few minutes, but use Ctrl+S to be safe
3. **Share notebooks**: Click "Share" button to collaborate with others
4. **Run in background**: Use Colab Pro to keep notebooks running longer

## Next Steps

- Modify parameters to see how results change
- Combine multiple games in one notebook
- Create visualizations of probability distributions
- Export results to analyze in other tools

Happy learning!
