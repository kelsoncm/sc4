# sc4py.env

Type-safe helpers for reading environment variables.

All functions share an optional `wrapped` parameter: when `True`, leading and trailing single-quotes are stripped from the value (useful for values set as `'foo'` in shell scripts).

## Functions

### `env(name, default=None, wrapped=False) → str | None`

Reads an environment variable as a raw string.

```python
import os
from sc4py.env import env

os.environ["APP_NAME"] = "sc4py"
env("APP_NAME")           # "sc4py"
env("MISSING", "default") # "default"
env("MISSING")            # None
```

---

### `env_as_list(name, default="", delimiter=",", wrapped=False) → list[str] | None`

Splits the variable value by `delimiter`.

```python
import os
from sc4py.env import env_as_list

os.environ["ALLOWED_HOSTS"] = "localhost,127.0.0.1,example.com"
env_as_list("ALLOWED_HOSTS")
# ["localhost", "127.0.0.1", "example.com"]

env_as_list("MISSING")   # []
env_as_list("MISSING", default=None)  # None
```

---

### `env_as_list_of_maps(name, key, default="", delimiter=",", wrapped=False) → list[dict] | None`

Same as `env_as_list` but wraps each item in a dict with `key`.

```python
import os
from sc4py.env import env_as_list_of_maps

os.environ["SERVERS"] = "host1,host2"
env_as_list_of_maps("SERVERS", "host")
# [{"host": "host1"}, {"host": "host2"}]
```

---

### `env_as_bool(name, default=None, wrapped=False) → bool | None`

Parses the variable value via [`str2bool`](str.md#str2bool).

```python
import os
from sc4py.env import env_as_bool

os.environ["DEBUG"] = "true"
env_as_bool("DEBUG")           # True

os.environ["DEBUG"] = "false"
env_as_bool("DEBUG")           # False

env_as_bool("MISSING")         # None
env_as_bool("MISSING", "true") # True
```

---

### `env_as_int(name, default=None, wrapped=False) → int | None`

Parses the variable value as an integer.

```python
import os
from sc4py.env import env_as_int

os.environ["PORT"] = "8080"
env_as_int("PORT")      # 8080
env_as_int("MISSING")   # None
```

---

### `env_from_json(name, default="", wrapped=False) → dict | list | None`

Parses the variable value as JSON.

```python
import os
from sc4py.env import env_from_json

os.environ["CONFIG"] = '{"debug": true, "port": 8080}'
env_from_json("CONFIG")
# {"debug": True, "port": 8080}
```
