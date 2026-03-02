# Probability Games - Quick Reference Guide

A one-page reference for everything about this project.

## 🎮 Playing Games

### Easiest Way
```bash
python quick_start.py
```

### Via CLI
```bash
pip install .
probability-games monty-hall
probability-games poker-simple
probability-games poker-probability
```

### Via Python
```python
from probability_games.games.monty_hall import run_monty_hall_analysis
from probability_games.games.poker import play_poker_probability

run_monty_hall_analysis(100000)
play_poker_probability()
```

### In Google Colab
```python
!pip install git+https://github.com/yourusername/probability-games.git
from probability_games.games.monty_hall import run_monty_hall_analysis
run_monty_hall_analysis(100000)
```

## 📦 Installation

```bash
# Clone
git clone https://github.com/yourusername/probability-games.git
cd probability-games

# Install (choose one)
pip install .                    # Production
pip install -e .                 # Development
python -m probability_games ...  # No install needed
```

## 🎯 What's Included

| Game | Description | File |
|------|-------------|------|
| **Monty Hall** | 100,000 trial probability paradox | `probability_games/games/monty_hall.py` |
| **Poker Simple** | Texas Hold'em against dealer | `probability_games/games/poker.py` |
| **Poker Probability** | Poker with Monte Carlo odds | `probability_games/games/poker.py` |

## 📚 Documentation

| Doc | Purpose | Read If |
|-----|---------|---------|
| `README.md` | Main docs | Starting out |
| `GETTING_STARTED.md` | Quick start | First time |
| `GOOGLE_COLAB.md` | Cloud usage | Using Colab |
| `USE_CASES.md` | Real-world apps | Learning why |
| `CONTRIBUTING.md` | How to contribute | Want to help |
| `DEPLOYMENT.md` | GitHub launch | Publishing |
| `READY_FOR_GITHUB.md` | Pre-launch checklist | Before GitHub |
| `PROJECT_SUMMARY.md` | Technical overview | Deep dive |

## 🛠️ Development Commands

```bash
make help           # Show all commands
make install        # Install package
make dev            # Development install
make run-monty      # Run Monty Hall
make run-poker      # Run Poker
make run-poker-prob # Run Poker Probability
make clean          # Clean build files
```

## 📁 Project Structure

```
probability-games/
├── probability_games/     # Main package
│   ├── games/            # Game modules
│   ├── cli.py            # Command-line interface
│   └── config.py         # Configuration
├── examples.py           # Usage examples
├── quick_start.py        # Interactive menu
├── setup.py              # Package setup
└── [DOCS]                # Documentation files
```

## 💻 Platform Support

| Platform | Supported | How |
|----------|-----------|-----|
| Windows | ✅ | Direct or WSL |
| macOS | ✅ | Terminal |
| Linux | ✅ | Terminal |
| Google Colab | ✅ | Cloud notebook |
| Jupyter | ✅ | Import modules |
| Python 3.6+ | ✅ | All versions |

## 🔧 Code Examples

### Example 1: Monty Hall
```python
from probability_games.games.monty_hall import simulate_monty_hall

win_rate = simulate_monty_hall(10000, switch_choice=True)
print(f"Win rate: {win_rate:.4f}")  # Output: ~0.6667
```

### Example 2: Poker Probability
```python
from probability_games.games.poker import calculate_win_probability

hand = [("A", "Hearts"), ("K", "Diamonds")]
community = [("A", "Clubs"), ("Q", "Spades"), ("J", "Hearts")]

prob = calculate_win_probability(hand, community)
print(f"Win probability: {prob:.2f}%")
```

### Example 3: Hand Strength
```python
from probability_games.games.poker import hand_strength, format_cards

cards = [("A", "Hearts"), ("K", "Clubs"), ("Q", "Diamonds"), ("J", "Spades"), ("10", "Hearts")]
strength = hand_strength(cards)
print(f"Hand: {format_cards(cards)}")
print(f"Strength: {strength}")
```

## 🎯 Use Cases

- 📚 **Education**: Teaching probability
- 💼 **Business**: Risk assessment training
- 🎮 **Gaming**: Game design learning
- 🔬 **Research**: Probability studies
- 💡 **Startups**: Probabilistic thinking
- 👥 **Teams**: Team learning activities

## 🚀 Launch on GitHub

```bash
# 1. Create repo on github.com/new

# 2. Push code
git init
git add .
git commit -m "Initial commit: Probability games"
git remote add origin https://github.com/YOU/probability-games.git
git push -u origin main

# 3. Configure on GitHub (add topics, enable discussions)

# 4. Share!
```

## 📊 Features Summary

✅ 3 games included  
✅ CLI interface  
✅ Python module import  
✅ Google Colab support  
✅ Zero dependencies  
✅ Type hints  
✅ Comprehensive docs  
✅ Open source (MIT)  
✅ Community-friendly  
✅ Production-ready  

## ❓ FAQ

**Q: Do I need to install?**
A: No! Try `python -m probability_games monty-hall` first.

**Q: Can I use in Colab?**
A: Yes! See GOOGLE_COLAB.md for instructions.

**Q: Can I modify it?**
A: Yes! It's MIT licensed. See CONTRIBUTING.md.

**Q: What Python version?**
A: 3.6 and above. Check: `python --version`

**Q: Any dependencies?**
A: Zero! Only Python stdlib.

**Q: How do I contribute?**
A: Fork, make changes, submit PR. See CONTRIBUTING.md.

## 🔗 Useful Links

- **Repository**: https://github.com/yourusername/probability-games
- **Issues**: https://github.com/yourusername/probability-games/issues
- **Discussions**: https://github.com/yourusername/probability-games/discussions
- **Python Docs**: https://docs.python.org/3/
- **Monty Hall**: https://en.wikipedia.org/wiki/Monty_Hall_problem
- **Monte Carlo**: https://en.wikipedia.org/wiki/Monte_Carlo_method

## 🎓 Learning Path

1. **Start**: Play games with `quick_start.py`
2. **Explore**: Read GETTING_STARTED.md
3. **Learn**: Review code in `probability_games/`
4. **Practice**: Run examples.py
5. **Modify**: Change code and experiment
6. **Contribute**: Help improve the project

## 📞 Getting Help

- **Questions**: Open a discussion
- **Bugs**: File an issue
- **Ideas**: Feature request issue
- **Contributing**: See CONTRIBUTING.md

---

**Ready to launch?** See READY_FOR_GITHUB.md for final checklist.

**Want more details?** See GETTING_STARTED.md, README.md, or specific documentation files.

**Good luck!** 🚀
