# sc4py.str

String conversion helpers.

## Functions

### `str2bool(v) → bool | None`

Converts a boolean-like value to `True`, `False`, or `None`.

| Parameter | Type | Description |
|---|---|---|
| `v` | `str \| bool \| int \| None` | Value to convert |

**Returns `True` for:**

`"true"`, `"verdade"`, `"yes"`, `"sim"`, `"t"`, `"v"`, `"y"`, `"s"`, `"1"`, `1`, `True`

**Returns `False` for:**

`"false"`, `"falso"`, `"no"`, `"nao"`, `"não"`, `"f"`, `"n"`, `"0"`, `0`, `False`

**Returns `None` for:**

`None`, `""`, `"   "`

**Raises `ValueError`** for any other value.

Matching is case-insensitive and strips surrounding whitespace.

```python
from sc4py.str import str2bool

str2bool("true")    # True
str2bool("sim")     # True   (Portuguese)
str2bool("yes")     # True
str2bool(1)         # True

str2bool("false")   # False
str2bool("não")     # False  (Portuguese)
str2bool(0)         # False

str2bool(None)      # None
str2bool("")        # None

str2bool("maybe")   # raises ValueError
```
