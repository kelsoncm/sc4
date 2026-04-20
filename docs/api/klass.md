# sc4py.klass

Dynamic class instantiation from dotted-path strings.

## Functions

### `instantiate_class(full_class_name, *args, **kwargs) → object`

Imports the module and class identified by `full_class_name` and returns a new instance, forwarding any extra positional or keyword arguments to the constructor.

| Parameter | Type | Description |
|---|---|---|
| `full_class_name` | `str` | Dotted path: `"module.submodule.ClassName"` |
| `*args` | `Any` | Positional arguments forwarded to `__init__` |
| `**kwargs` | `Any` | Keyword arguments forwarded to `__init__` |

```python
from sc4py.klass import instantiate_class

# Equivalent to: from decimal import Decimal; Decimal("3.14")
d = instantiate_class("decimal.Decimal", "3.14")
print(d)        # Decimal('3.14')
print(type(d))  # <class 'decimal.Decimal'>
```

```python
from sc4py.klass import instantiate_class

# Instantiate a custom class from application code
svc = instantiate_class("myapp.services.EmailService", host="smtp.example.com", port=587)
```

!!! note
    `full_class_name` must contain at least one dot separating the module path from the class name.
