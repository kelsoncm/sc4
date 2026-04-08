# sc4

[![Python CI and PyPI Deploy](https://github.com/kelsoncm/sc4/actions/workflows/pythonapp.yml/badge.svg)](https://github.com/kelsoncm/sc4/actions/workflows/pythonapp.yml)
![PyPI - sc4py Version](https://img.shields.io/pypi/v/sc4py)
![PyPI - sc4net Version](https://img.shields.io/pypi/v/sc4net)
[![Coverage - sc4py](https://codecov.io/gh/kelsoncm/sc4/graph/badge.svg?flag=sc4py)](https://codecov.io/gh/kelsoncm/sc4)
[![Coverage - sc4net](https://codecov.io/gh/kelsoncm/sc4/graph/badge.svg?flag=sc4net)](https://codecov.io/gh/kelsoncm/sc4)

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
## License

The MIT License (MIT)

Copyright (c) 2019 kelsoncm

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

