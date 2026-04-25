# sc4py

[![License](https://img.shields.io/badge/License-MIT-lemon.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/pypi/pyversions/sc4py.svg)](https://pypi.org/project/sc4py/)
[![QA](https://github.com/kelsoncm/python-sc4py/actions/workflows/qa.yml/badge.svg)](https://github.com/kelsoncm/python-sc4py/actions/workflows/qa.yml)
[![Coverage](https://codecov.io/gh/kelsoncm/python-sc4py/branch/main/graph/badge.svg)](https://codecov.io/gh/kelsoncm/python-sc4py)
[![Publish](https://github.com/kelsoncm/python-sc4py/actions/workflows/publish.yml/badge.svg)](https://github.com/kelsoncm/python-sc4py/actions/workflows/publish.yml)
[![Docs](https://github.com/kelsoncm/python-sc4py/actions/workflows/docs.yml/badge.svg)](https://kelsoncm.github.io/python-sc4py/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)

Utilities for date/time, environment parsing, dynamic class loading, percentages, string-to-bool conversion, choice tuples,
in-memory ZIP reading, and advanced string masking/validation (CPF/CNPJ, DVs, etc).

> See each package's [documentation](https://kelsoncm.github.io/python-sc4py/) for details and usage examples.

## Masks utilities (CPF/CNPJ, DVs, etc)

```python
from sc4py.masks import apply_mask, validate_masked_value, validate_mask, validate_mod11, validate_dv_by_mask

# Apply a mask
print(apply_mask('12345678901', '###.###.###-##'))  # '123.456.789-01'

# Validate masked value
print(validate_masked_value('12345678901', '###.###.###-##'))  # '123.456.789-01'

# Validate mask
validate_mask('###.###-##')

# Validate mod11 DV
validate_mod11('12345678909', 11, 2)

# Validate value and DV by mask
print(validate_dv_by_mask('12345678909', '#########00'))  # '12345678909'
```

## Installation

```bash
pip install sc4py
```

## Security

Please report vulnerabilities according to [SECURITY.md](SECURITY.md).

## Author

Kelson da Costa Medeiros <kelsoncm@gmail.com>
