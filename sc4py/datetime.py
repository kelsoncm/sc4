from collections.abc import Generator
from datetime import date, datetime, timedelta

today = date.today
now = datetime.now


def now_str() -> str:
    """
    Returns the current date and time as a formatted string.

    Returns:
        str: The current date and time in the format "DD-MM-YYYY HH:MM:SS".

    Example::
        >>> now_str()
        '23-04-2026 14:30:00'
    """
    return now().strftime("%d-%m-%Y %H:%M:%S")


def this_month() -> int:
    """
    Returns the current month as an integer.

    Returns:
        int: The current month (1-12).

    Example::
        >>> this_month()
        4
    """
    return now().month


def this_year() -> int:
    """
    Returns the current year as an integer.

    Returns:
        int: The current year.

    Example::
        >>> this_year()
        2026
    """
    return now().year


def today_str() -> str:
    """
    Returns the current date as a formatted string.

    Returns:
        str: The current date in the format "DD-MM-YYYY".

    Example::
        >>> today_str()
        '23-04-2026'
    """
    return today().strftime("%d-%m-%Y")


def others_months() -> list[int]:
    """
    Returns a list of all months except the current one.

    Returns:
        list[int]: A list of integers (1-12) excluding the current month.

    Example::
        >>> others_months()
        [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12]
    """
    t = this_month()
    return [m for m in range(1, 13) if m != t]


def daterange(start: date, end: date, step: timedelta = timedelta(days=1)) -> Generator[date, None, None]:
    """
    Generates a range of dates from start to end (inclusive).

    Args:
        start (date): The start date.
        end (date): The end date.
        step (timedelta): The difference between each date in the range.

    Yields:
        date: The next date in the range.

    Example::
        >>> from datetime import date, timedelta
        >>> list(daterange(date(2026, 4, 1), date(2026, 4, 3)))
        [datetime.date(2026, 4, 1), datetime.date(2026, 4, 2), datetime.date(2026, 4, 3)]
        >>> list(daterange(date(2026, 4, 1), date(2026, 4, 5), step=timedelta(days=2)))
        [datetime.date(2026, 4, 1), datetime.date(2026, 4, 3), datetime.date(2026, 4, 5)]
    """
    curr = start
    while curr <= end:
        yield curr
        curr += step
