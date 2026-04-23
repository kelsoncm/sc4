def percentage(num1: float, num2: float, precision: int = 2) -> float:
    """
    Calculates the percentage of num1 over num2.

    Args:
        num1 (float): The numerator.
        num2 (float): The denominator.
        precision (int, optional): Number of decimal places. Default is 2.

    Returns:
        float: The percentage value, or 0.0 if num1 or num2 is 0.

    Example::
        >>> percentage(45, 60)
        75.0
    """
    if num1 == 0 or num2 == 0:
        return float(0)
    else:
        return round(float(num1) / float(num2) * 100.0, precision)
