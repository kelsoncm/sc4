from enum import Enum, EnumMeta
from typing import Any


def to_choice(*args) -> list[tuple[Any, Any]]:
    """
    Convert a list of values to a list of choices.

    Args:
        *args: A list of values to convert to choices. Each value can be an Enum, an EnumMeta, or any other value.
            If the value is an Enum, it will be converted to a tuple of (value, description). If the value is an
            EnumMeta, it will be converted to a list of tuples of (value, description) for each member of the Enum.
            If the value is any other value, it will be converted to a tuple of (value, value).

    Returns:
        list of tuples: A list of tuples of (value, description) for each value in the input list. The description
        is the value of the "description" attribute of the Enum member, if it exists, or the value itself if it
        does not exist.

    Examples::

        from sc4py.choice import to_choice
        from enum import Enum

        class Status(Enum):
            ACTIVE   = (1, "Ativo",   "🟢")
            INACTIVE = (2, "Inativo", "🔴")
            PENDING  = (3, "Pendente", "🟡")

            def __init__(self, value, label, icon):
                self._value_ = value
                self.label = label
                self.icon = icon

            def __str__(self):
                return f"{self.icon} {self.label}"

        to_choice(Status)
        # [(1, '🟢 Ativo'), (2, '🔴 Inativo'), (3, '🟡 Pendente')]
        to_choice(Status.ACTIVE)
        # [(1, '🟢 Ativo')]
        to_choice(1, 2, 3)
        # [(1, 1), (2, 2), (3, 3)]
    """
    result = []
    for x in args:
        if isinstance(x, EnumMeta):
            result.extend(to_choice(*[y for y in x]))
        elif isinstance(x, Enum):
            result.append((x.value, str(x)))
        else:
            result.append((x, x))
    return result
