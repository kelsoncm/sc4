# sc4py.datetime

Date and time helpers plus a `daterange` generator.

## Aliases

| Name | Aliased to |
|---|---|
| `today` | `datetime.date.today` |
| `now` | `datetime.datetime.now` |

## Functions

### `now_str() → str`

Returns the current local datetime as `"DD-MM-YYYY HH:MM:SS"`.

```python
from sc4py.datetime import now_str

print(now_str())  # "20-04-2026 14:30:00"
```

---

### `this_month() → int`

Returns the current month as an integer (`1`–`12`).

```python
from sc4py.datetime import this_month

print(this_month())  # 4
```

---

### `others_months() → list[int]`

Returns all months except the current one.

```python
from sc4py.datetime import others_months

# If current month is April (4):
others_months()
# [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12]
```

---

### `daterange(start, end, step=timedelta(1)) → Generator[date, None, None]`

Yields every date from `start` to `end` inclusive, advancing by `step`.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `start` | `date` | — | First date (inclusive) |
| `end` | `date` | — | Last date (inclusive) |
| `step` | `timedelta` | `timedelta(1)` | Interval between dates |

```python
from datetime import date, timedelta
from sc4py.datetime import daterange

# Daily
for d in daterange(date(2026, 1, 1), date(2026, 1, 3)):
    print(d)
# 2026-01-01
# 2026-01-02
# 2026-01-03

# Every 7 days
for d in daterange(date(2026, 1, 1), date(2026, 1, 22), timedelta(weeks=1)):
    print(d)
# 2026-01-01
# 2026-01-08
# 2026-01-15
# 2026-01-22
```
