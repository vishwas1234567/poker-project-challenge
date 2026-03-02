"""Setup configuration for probability-games package."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="probability-games",
    version="1.0.0",
    author="Community Contributors",
    description="Interactive probability games and Monte Carlo simulations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/probability-games",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Topic :: Education",
        "Topic :: Games/Entertainment",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "probability-games=probability_games.cli:main",
        ],
    },
    keywords="probability simulation monte-carlo poker monty-hall education",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/probability-games/issues",
        "Source": "https://github.com/yourusername/probability-games",
        "Documentation": "https://github.com/yourusername/probability-games/wiki",
    },
)
