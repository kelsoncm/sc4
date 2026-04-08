# sc4

[![Python CI and PyPI Deploy](https://github.com/kelsoncm/sc4/actions/workflows/pythonapp.yml/badge.svg)](https://github.com/kelsoncm/sc4/actions/workflows/pythonapp.yml)
![PyPI - sc4py Version](https://img.shields.io/pypi/v/sc4py)
![PyPI - sc4net Version](https://img.shields.io/pypi/v/sc4net)
[![Coverage - sc4py](https://codecov.io/gh/kelsoncm/sc4/branch/main/graph/badge.svg?flag=sc4py)](https://codecov.io/gh/kelsoncm/sc4)
[![Coverage - sc4net](https://codecov.io/gh/kelsoncm/sc4/branch/main/graph/badge.svg?flag=sc4net)](https://codecov.io/gh/kelsoncm/sc4)

Monorepo with two Python packages:

* `sc4py` - Python utility helpers
* `sc4net` - HTTP(S)/FTP network helpers

## Package documentation

* `sc4py`: [sc4py/README](sc4py/README)
* `sc4net`: [sc4net/README](sc4net/README)

## Installation

Install each package independently from PyPI:

```bash
pip install sc4py
pip install sc4net
```

## Security

Please report vulnerabilities according to [SECURITY.md](SECURITY.md).

## How to contribute

```bash
git clone git@github.com:kelsoncm/sc4.git ~/projetos/PESSOAL/sc4
code ~/projetos/PESSOAL/sc4
```

## Pre-commit

This repository provides a pre-commit hook that runs CI-like quality
and test checks locally.

Setup:

```bash
python3 -m pip install pre-commit
pre-commit install
```

Run manually:

```bash
pre-commit run --all-files
```

Notes:

* The hook script creates `.venv` automatically if it does not exist.
* It runs quality checks (black, isort, bandit, flake8, semgrep)
  and test suites for `sc4py` and `sc4net`.
* If available, it also runs shellcheck and markdownlint.
