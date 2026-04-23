import json
from os import getenv

from .str import str2bool


def env(name: str, default=None, wrapped: bool = False) -> str | None:
    """
    Reads an environment variable as a string.

    Args:
        name (str): The environment variable name.
        default (Any, optional): Default value if variable is not set. Default is None.
        wrapped (bool, optional): If True, removes single quotes around the value. Default is False.

    Returns:
        str | None: The value of the environment variable or default.

    Example::
        >>> env('HOME')
        '/home/user'
    """
    result = getenv(name, default)
    if wrapped and isinstance(result, str) and result[0:1] == "'" and result[-1:] == "'":
        return result[1:-1]
    return result


def env_as_list(
    name: str,
    default: str | list[str] | tuple[str, ...] = "",
    delimiter: str = ",",
    wrapped: bool = False,
) -> list[str] | None:
    """
    Reads an environment variable and returns it as a list of strings.

    Args:
        name (str): The environment variable name.
        default (str | list[str] | tuple[str, ...], optional): Default value if variable is not set. Default is "".
        delimiter (str, optional): Delimiter to split the string. Default is ",".
        wrapped (bool, optional): If True, removes single quotes around the value. Default is False.

    Returns:
        list[str] | None: List of strings or None if not set.

    Example::
        >>> env_as_list('PATH', delimiter=':')
        ['/usr/bin', '/bin', '/usr/local/bin']
    """
    result = env(name, default, wrapped)
    if result is None:
        return None
    if isinstance(result, str):
        if result.strip() == "" and isinstance(default, str) and default.strip() == "":
            return []
        return result.split(delimiter)
    if isinstance(result, (list, tuple)):
        return list(result)
    raise TypeError("env_as_list requires str, list or tuple as default")


def env_as_list_of_maps(
    name: str,
    key: str,
    default: str | list[str] | tuple[str, ...] = "",
    delimiter: str = ",",
    wrapped: bool = False,
) -> list[dict] | None:
    """
    Reads an environment variable and returns a list of dictionaries with a given key.

    Args:
        name (str): The environment variable name.
        key (str): The key for each dictionary.
        default (str | list[str] | tuple[str, ...], optional): Default value if variable is not set. Default is "".
        delimiter (str, optional): Delimiter to split the string. Default is ",".
        wrapped (bool, optional): If True, removes single quotes around the value. Default is False.

    Returns:
        list[dict] | None: List of dictionaries or None if not set.

    Example::
        >>> env_as_list_of_maps('PATH', key='dir', delimiter=':')
        [{'dir': '/usr/bin'}, {'dir': '/bin'}, {'dir': '/usr/local/bin'}]
    """
    result = env_as_list(name, default, delimiter, wrapped)
    return [{key: x} for x in result] if result is not None else None


def env_as_bool(name: str, default=None, wrapped: bool = False) -> bool | None:
    """
    Reads an environment variable and converts it to a boolean.

    Args:
        name (str): The environment variable name.
        default (Any, optional): Default value if variable is not set. Default is None.
        wrapped (bool, optional): If True, removes single quotes around the value. Default is False.

    Returns:
        bool | None: Boolean value or None if not set.

    Example::
        >>> env_as_bool('FEATURE_ENABLED', 'true')
        True
    """
    return str2bool(env(name, default, wrapped))


def env_from_json(key: str, default: str | dict | list = "", wrapped: bool = False) -> dict | list | None:
    """
    Reads an environment variable and parses it as JSON.

    Args:
        key (str): The environment variable name.
        default (str | dict | list, optional): Default value if variable is not set. Default is "".
        wrapped (bool, optional): If True, removes single quotes around the value. Default is False.

    Returns:
        dict | list | None: Parsed JSON object or None if not set.

    Example::
        >>> env_from_json('CONFIG', default='{"a":1}')
        {'a': 1}
    """
    result = env(key, default, wrapped)
    return json.loads(result) if result is not None else result


def env_as_int(key: str, default=None, wrapped: bool = False) -> int | None:
    """
    Reads an environment variable and converts it to an integer.

    Args:
        key (str): The environment variable name.
        default (Any, optional): Default value if variable is not set. Default is None.
        wrapped (bool, optional): If True, removes single quotes around the value. Default is False.

    Returns:
        int | None: Integer value or None if not set.

    Example::
        >>> env_as_int('PORT', default='8080')
        8080
    """
    result = env(key, default, wrapped)
    return int(result) if result is not None else result
