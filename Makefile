# Makefile for chess engine project

# Variables
VENV_NAME := venv
PYTHON := python3
PIP := $(VENV_NAME)/bin/pip
PYTEST := $(VENV_NAME)/bin/pytest

# Phony targets
.PHONY: all venv install test clean

# Default targets
all: venv install

# Create virtual environment
venv:
	$(PYTHON) -m venv $(VENV_NAME)

# Install dependencies
install: venv
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

# Run tests
test: install
	$(PYTEST)

# Clean up
clean:
	rm -rf $(VENV_NAME)
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete

# Help
help:
	@echo "Available targets:"
	@echo "  make          : Create venv and install dependencies"
	@echo "  make venv     : Create virtual environment"
	@echo "  make install  : Install dependencies in venv"
	@echo "  make test     : Run tests"
	@echo "  make clean    : Remove venv and cache files"
	@echo "  make help     : Show this help message"

