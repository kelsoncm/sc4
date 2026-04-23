"""
The MIT License (MIT)
Copyright 2015 Umbrella Tech.
Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

__author__ = "Kelson da Costa Medeiros <kelsoncm@gmail.com>"


from enum import Enum, EnumMeta
from typing import Any


def to_choice(*args) -> list[tuple[Any, Any]]:
    """Convert a list of values to a list of choices.

    Args:
        - *args: A list of values to convert to choices. Each value can be an Enum, an EnumMeta, or any other value.
            If the value is an Enum, it will be converted to a tuple of (value, description). If the value is an
            EnumMeta, it will be converted to a list of tuples of (value, description) for each member of the Enum.
            If the value is any other value, it will be converted to a tuple of (value, value).

    Returns:
        - A list of tuples of (value, description) for each value in the input list. The description is the value
        of the "description" attribute of the Enum member, if it exists, or the value itself if it does not exist.

    Examples:

        **Example 1**
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
