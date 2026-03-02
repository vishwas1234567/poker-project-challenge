# Contributing to Probability Games & Simulations

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to the project.

## Code of Conduct

Please read and adhere to our [Code of Conduct](CODE_OF_CONDUCT.md) before contributing.

## How to Contribute

### Reporting Bugs

Before creating a bug report, please check if the issue already exists. When creating a bug report, include:

- **Clear description** of the problem
- **Steps to reproduce** the issue
- **Expected behavior** vs. actual behavior
- **Python version** and operating system
- **Code samples** or error messages if applicable

### Suggesting Enhancements

We welcome suggestions for improvements! When proposing an enhancement:

- Use a clear, descriptive title
- Provide a detailed description of the suggested enhancement
- Explain why this enhancement would be useful
- List examples of similar features in other projects (if applicable)

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Write clear, descriptive commit messages**
3. **Test your changes thoroughly** before submitting
4. **Follow the coding standards** outlined below
5. **Keep pull requests focused** - one feature per PR when possible
6. **Update documentation** if your changes affect it

## Coding Standards

### Python Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions small and focused on a single responsibility
- Write comments for complex logic

### Code Quality

- Ensure all scripts run without errors
- Test your code thoroughly
- Consider edge cases and error handling
- Keep the code simple and readable

### Example Code Style

```python
def calculate_hand_strength(hole_cards, community_cards):
    """
    Calculate the strength of a poker hand.
    
    Args:
        hole_cards (list): Player's two hole cards
        community_cards (list): Community cards on the board
        
    Returns:
        int: Hand strength score (higher is better)
    """
    # Your implementation here
    pass
```

## Development Workflow

### Setting Up Your Development Environment

```bash
# Clone the repository
git clone https://github.com/yourusername/probability-games.git
cd probability-games

# Create a new branch for your feature
git checkout -b feature/your-feature-name
```

### Testing Your Changes

```bash
# Run the script you modified
python your_script.py

# Test with various inputs
# Verify output is correct and no errors occur
```

### Commit Messages

Write clear commit messages that explain what changed and why:

```bash
# Good commit message
git commit -m "Add Monte Carlo hand strength calculation for poker"

# Avoid vague messages
git commit -m "Fixed stuff"  # ❌ Don't do this
```

### Push and Create Pull Request

```bash
# Push your branch to your fork
git push origin feature/your-feature-name

# Create a Pull Request on GitHub with:
# 1. Clear title describing the change
# 2. Description of what changed and why
# 3. Reference any related issues (#123)
# 4. Screenshots or output examples if relevant
```

## Project Structure

- **monty_hall_simulation.py**: Monty Hall problem implementation
- **poker_simple.py**: Basic Texas Hold'em game
- **poker_probability.py**: Poker with Monte Carlo probability calculations
- **README.md**: Project documentation
- **CONTRIBUTING.md**: This file
- **CODE_OF_CONDUCT.md**: Community standards
- **LICENSE**: MIT License

## Areas for Contribution

### High Priority

- Bug fixes and error handling improvements
- Code optimization for faster simulations
- Better user interface and output formatting
- Comprehensive documentation

### Medium Priority

- Additional probability games or simulations
- Enhanced poker hand evaluation
- Statistical analysis features
- Tutorial or educational content

### Nice to Have

- GUI version of the games
- Web-based interface
- Additional visualization options
- Performance benchmarking

## Questions or Need Help?

- Open a GitHub Issue for questions or discussions
- Check existing issues and discussions first
- Be respectful and patient with responses

## License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.

## Recognition

Contributors will be recognized in the project documentation. Thank you for helping make this project better!

---

Happy coding! We appreciate your contributions! 🎉
