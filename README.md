# sc4py

[![Publish](https://github.com/kelsoncm/sc4py/actions/workflows/pythonapp.yml/badge.svg)](https://github.com/kelsoncm/sc4py/actions/workflows/pythonapp.yml)
![Version](https://img.shields.io/pypi/v/sc4py)
[![Coverage](https://codecov.io/gh/kelsoncm/sc4py/branch/main/graph/badge.svg?flag=sc4py)](https://codecov.io/gh/kelsoncm/sc4py)

Utilities for date/time, environment parsing, dynamic class loading, percentages, string-to-bool conversion, choice tuples, and in-memory ZIP reading.

## Package documentation

* [sc4py/README](sc4py/README)

## Installation

```bash
pip install sc4py
```

## Security

Please report vulnerabilities according to [SECURITY.md](SECURITY.md).


## How to contribute

```bash
git clone git@github.com:kelsoncm/sc4.git ~/projetos/PESSOAL/sc4py
code ~/projetos/PESSOAL/sc4py
```

## Pre-commit

This repository uses [pre-commit](https://pre-commit.com/) to run quality checks
before each commit and coverage regression checks before each push.

Setup:

```bash
python -m venv .venv
.venv\bin\activate
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip uv
uv pip install --upgrade -e ".[dev]"
pre-commit install
pre-commit install --hook-type pre-push
```

Run manually:

```bash
pre-commit run --all-files
pre-commit run --hook-stage pre-push --all-files
```

Hooks:

* **pre-commit**: `black`, `isort`, `bandit`, `flake8` (with `flake8-bandit`)
* **pre-push**:
  1. Runs `python -m pytest --cov=sc4py --cov-report=xml -q` to produce `coverage.xml`
  2. Run [`pytest-coverage-gate`](https://github.com/kelsoncm/pytest-coverage-gate) reads
     `coverage.xml`, compares against `.coverage-baseline` (2 decimal places), blocks
     the push on regression and updates the baseline on improvement
* **GitHub Actions only**: `semgrep` SAST
