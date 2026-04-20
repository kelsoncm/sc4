# sc4py.choice

Convert plain values and `Enum` types into Django-style `(value, label)` choice tuples.

## Functions

### `to_choice(*args) → list[tuple[Any, Any]]`

Accepts any mix of plain values, `Enum` classes, or `Enum` instances and returns a flat list of `(value, label)` pairs.

| Input type | Value | Label |
|---|---|---|
| Plain value | the value itself | the value itself |
| `Enum` class | each member's `.value` | `.description` if present, else `.value` |
| `Enum` instance | `.value` | `.description` if present, else `.value` |

## Examples

### Plain values

```python
from sc4py.choice import to_choice

to_choice("active", "inactive")
# [("active", "active"), ("inactive", "inactive")]

to_choice("x", 2)
# [("x", "x"), (2, 2)]
```

### Plain `Enum`

```python
from enum import Enum
from sc4py.choice import to_choice

class Status(Enum):
    ACTIVE = 1
    INACTIVE = 2

to_choice(Status)
# [(1, 1), (2, 2)]
```

### `Enum` with descriptions

```python
from enum import Enum
from sc4py.choice import to_choice

class Priority(Enum):
    description: str
    LOW = (1, "Low priority")
    HIGH = (2, "High priority")

    def __new__(cls, value, description):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.description = description
        return obj

to_choice(Priority)
# [(1, "Low priority"), (2, "High priority")]

to_choice(Priority.HIGH)
# [(2, "High priority")]
```

### Mix of types

```python
to_choice("none", Status, Priority.HIGH)
# [("none", "none"), (1, 1), (2, 2), (2, "High priority")]
```
