# sc4py

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/pypi/pyversions/sc4py.svg)](https://pypi.org/project/sc4py/)
[![Tests](https://github.com/kelsoncm/python-sc4py/actions/workflows/test.yml/badge.svg)](https://github.com/kelsoncm/python-sc4py/actions/workflows/test.yml)
[![Coverage](https://codecov.io/gh/kelsoncm/python-sc4py/branch/main/graph/badge.svg)](https://codecov.io/gh/kelsoncm/python-sc4py)
[![PyPI Deploy](https://github.com/kelsoncm/python-sc4py/actions/workflows/publish.yml/badge.svg)](https://github.com/kelsoncm/python-sc4py/actions/workflows/publish.yml)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)

Utilities for date/time, environment parsing, dynamic class loading, percentages, string-to-bool conversion, choice tuples, and in-memory ZIP reading.

> [Package source](https://github.com/kelsoncm/python-sc4py/)


## Installation

```bash
pip install sc4py
```

## Modules

| Module | Purpose |
|---|---|
| [`sc4py.choice`](api/choice.md) | Convert plain values and `Enum` types to Django-style choice tuples |
| [`sc4py.datetime`](api/datetime.md) | Date/time helpers and `daterange` generator |
| [`sc4py.env`](api/env.md) | Type-safe environment variable reading |
| [`sc4py.klass`](api/klass.md) | Dynamic class instantiation from dotted path strings |
| [`sc4py.number`](api/number.md) | Percentage calculation |
| [`sc4py.str`](api/str.md) | `str2bool` — multilingual boolean string parsing |
| [`sc4py.zip`](api/zip.md) | In-memory ZIP extraction (text and CSV) |

## Quick start

```python
from sc4py.datetime import now_str, daterange
from sc4py.env import env_as_bool
from sc4py.number import percentage
from sc4py.str import str2bool
from datetime import date

print(now_str())                                    # "20-04-2026 14:30:00"
print(env_as_bool("FEATURE_ENABLED", "true"))       # True
print(percentage(45, 60))                           # 75.0
print(str2bool("sim"))                              # True

for d in daterange(date(2026, 1, 1), date(2026, 1, 3)):
    print(d)

# 2026-01-01
# 2026-01-02
# 2026-01-03
```
