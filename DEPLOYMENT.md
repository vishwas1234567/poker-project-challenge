# Deployment Guide

Complete guide to deploying the Probability Games package as a professional open-source project.

## GitHub Repository Setup

### 1. Create Repository

```bash
# Go to github.com/new and create a new repository named "probability-games"

# In your local project directory:
git init
git add .
git commit -m "Initial commit: Professional probability games package"
git branch -M main
git remote add origin https://github.com/yourusername/probability-games.git
git push -u origin main
```

### 2. Repository Settings

**Settings → Code and automation → Actions:**
- ✅ Enable Actions for CI/CD (optional)

**Settings → Code and automation → Branch protection:**
- ✅ Require pull request reviews before merging
- ✅ Require status checks to pass before merging
- ✅ Dismiss stale pull request approvals

**Settings → Discussions:**
- ✅ Enable discussions for community Q&A

**Settings → Pages:**
- ✅ Enable GitHub Pages from main branch (optional for docs)

## Distribution Methods

### Method 1: Install from GitHub (No PyPI)

```bash
pip install git+https://github.com/yourusername/probability-games.git
```

### Method 2: Install from Source (Local)

```bash
git clone https://github.com/yourusername/probability-games.git
cd probability-games
pip install .
```

### Method 3: Install in Development Mode

```bash
git clone https://github.com/yourusername/probability-games.git
cd probability-games
pip install -e .  # Editable install
```

### Method 4: PyPI Distribution (Advanced)

When ready for wider distribution:

```bash
# Build distribution
pip install build
python -m build

# Upload to PyPI (requires account)
pip install twine
twine upload dist/*
```

Then users can simply:
```bash
pip install probability-games
```

## Continuous Integration (Optional)

### GitHub Actions Workflow

Create `.github/workflows/tests.yml`:

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.6, 3.9, 3.11]
    
    steps:
    - uses: actions/checkout@v2
    - uses: actions/setup-python@v2
      with:
        python-version: ${{ matrix.python-version }}
    - run: pip install -e .
    - run: python -m pytest tests/
```

## Docker Support (Optional)

Create `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install .

ENTRYPOINT ["probability-games"]
```

Build and run:

```bash
docker build -t probability-games .
docker run probability-games monty-hall
```

## Documentation Website (Optional)

### Using GitHub Pages

1. Create `docs/` directory
2. Add documentation files (Markdown)
3. Enable GitHub Pages in settings

### Using Read the Docs

1. Sign up at readthedocs.org
2. Import your GitHub repository
3. Enable automatic builds on push

## Release Process

### Semantic Versioning

Update version in:
- `setup.py`
- `pyproject.toml`
- `probability_games/__init__.py`

### Create Release

```bash
# Tag version
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0

# GitHub automatically creates release if you use the web interface
```

In GitHub:
1. Go to "Releases"
2. Click "Create a new release"
3. Set tag to `v1.0.0`
4. Add release notes
5. Click "Publish release"

## Changelog Management

Create `CHANGELOG.md`:

```markdown
# Changelog

## [1.0.0] - 2024-03-02
### Added
- Initial release
- Monty Hall simulation
- Simple Poker game
- Poker with probability analysis
- CLI interface
- Google Colab support

### Fixed
- Bug fixes from beta

### Changed
- Initial version
```

## Social Media & Promotion

### Repository Topics

In GitHub settings, add topics:
- `probability`
- `simulation`
- `monte-carlo`
- `poker`
- `monty-hall`
- `education`
- `python`

### README Badges

Add to README:

```markdown
[![Python 3.6+](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/yourusername/probability-games.svg)](https://github.com/yourusername/probability-games)
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yourusername/probability-games/blob/main/notebooks/Probability_Games_Tutorial.ipynb)
```

## Community Building

### Engage Users

- **Respond to issues** promptly
- **Feature contributors** in README
- **Create discussion topics** for ideas
- **Share success stories** in discussions

### Regular Maintenance

- Update dependencies monthly
- Review and merge PRs
- Triage issues weekly
- Document new features

## Analytics

### Track Engagement

- GitHub Insights tab shows traffic
- Google Analytics on documentation site
- Star count growth
- Download statistics (if on PyPI)

## Security

### Dependabot

GitHub enables automatically:
- Checks for vulnerable dependencies
- Creates security PRs
- Automatic updates available

## Performance Optimization

### Code Profiling

```python
import cProfile
cProfile.run('calculate_win_probability(...)')
```

### Benchmarking

Track performance improvements across versions.

## Troubleshooting Deployments

### Installation Issues

**Problem:** `pip install` fails

**Solution:**
```bash
pip install --upgrade pip setuptools
pip install --upgrade wheel
pip install -e .
```

### Import Errors

**Problem:** `ModuleNotFoundError`

**Solution:**
```bash
pip install -e .  # Reinstall
```

### Colab Issues

**Problem:** Module not found in Colab

**Solution:**
```python
!pip install git+https://github.com/yourusername/probability-games.git
```

## Success Metrics

Track these metrics:

- **GitHub Stars**: Community interest
- **Forks**: Active users
- **Issues/PRs**: Community engagement
- **Downloads**: PyPI adoption
- **Contributors**: Project growth
- **Citations**: Academic use

## Maintenance Timeline

- **Weekly**: Review issues/PRs
- **Monthly**: Update dependencies, release patch if needed
- **Quarterly**: Major features, new games
- **Annually**: Major version updates

## Next Steps After Launch

1. ✅ Push to GitHub
2. ✅ Share with communities (Reddit, Twitter, etc.)
3. ✅ Submit to awesome-python lists
4. ✅ Monitor issues and feedback
5. ✅ Engage with contributors
6. ✅ Plan future features
7. ✅ Consider PyPI distribution for v2.0

---

Your project is ready to become a successful open-source initiative! 🚀
