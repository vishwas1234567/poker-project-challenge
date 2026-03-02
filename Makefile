.PHONY: help install dev test clean lint format run

help:
	@echo "Probability Games - Development Commands"
	@echo "=========================================="
	@echo ""
	@echo "install         Install package in production mode"
	@echo "dev             Install package in development mode"
	@echo "test            Run all tests"
	@echo "lint            Run linting checks"
	@echo "format          Format code with black"
	@echo "clean           Remove build artifacts"
	@echo "run-monty       Run Monty Hall simulation"
	@echo "run-poker       Run Simple Poker game"
	@echo "run-poker-prob  Run Poker with probability"
	@echo ""

install:
	pip install .

dev:
	pip install -e ".[dev]"

test:
	python -m pytest tests/ -v

lint:
	python -m flake8 probability_games/

format:
	python -m black probability_games/

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info

run-monty:
	python -m probability_games monty-hall

run-poker:
	python -m probability_games poker-simple

run-poker-prob:
	python -m probability_games poker-probability
