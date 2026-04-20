# sc4py

[![PyPI](https://img.shields.io/pypi/v/sc4py)](https://pypi.org/project/sc4py/)
[![CI](https://github.com/kelsoncm/sc4/actions/workflows/pythonapp.yml/badge.svg)](https://github.com/kelsoncm/sc4/actions/workflows/pythonapp.yml)
[![Coverage](https://codecov.io/gh/kelsoncm/sc4/branch/main/graph/badge.svg?flag=sc4py)](https://codecov.io/gh/kelsoncm/sc4)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/kelsoncm/sc4/blob/main/LICENSE.txt)

Python utility helpers for everyday tasks.

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
