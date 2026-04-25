def str2bool(v: str | bool | int | None) -> bool | None:
    """
    Converts a string, boolean, or integer to a boolean value.

    Args:
        v (str | bool | int | None): Value to convert. Accepts various representations of true/false.

    Returns:
        bool | None: True, False, or None if input is None or empty.

    Example::
        >>> str2bool('yes')
        True
        >>> str2bool('no')
        False
        >>> str2bool(None)
        None
    """
    TRUE_STRS = ("true", "verdade", "yes", "sim", "t", "v", "y", "s", "1")
    FALSE_STRS = ("false", "falso", "no", "nao", "não", "f", "n", "0")

    if isinstance(v, bool):
        return v

    if v is None or (isinstance(v, str) and v.strip() == ""):
        return None

    if isinstance(v, int) and v in (1, 0):
        return v == 1

    if isinstance(v, str) and v.strip().lower() in TRUE_STRS + FALSE_STRS:
        return v.strip().lower() in TRUE_STRS

    raise ValueError("Boolean value expected.")


def only_digits(code: str) -> str:
    """Removes all non-digit characters from the input string."""
    return "".join(c for c in filter(str.isdigit, code))
