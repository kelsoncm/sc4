import importlib


def instantiate_class(full_class_name: str, *args, **kwargs) -> object:
    """
    Dynamically instantiates a class from a dotted path string.

    Args:
        full_class_name (str): The full dotted path to the class (e.g., 'package.module.ClassName').
        *args: Positional arguments to pass to the class constructor.
        **kwargs: Keyword arguments to pass to the class constructor.

    Returns:
        object: An instance of the specified class.

    Example::
        >>> instance = instantiate_class('collections.Counter', 'abc')
        >>> type(instance)
        <class 'collections.Counter'>
    """
    module_name, class_name = full_class_name.rsplit(".", 1)
    MyClass = getattr(importlib.import_module(module_name), class_name)
    return MyClass(*args, **kwargs)
