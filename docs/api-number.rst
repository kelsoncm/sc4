sc4py.number
===============

Numeric helpers.

Functions
---------

`percentage(num1, num2, precision=2) → float`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Returns `num1 / num2 * 100` rounded to `precision` decimal places.
- Returns `0.0` if either argument is zero.

=========== ======= ======= ============================
Parameter   Type    Default Description
=========== ======= ======= ============================
`num1`      `float` —       Numerator
`num2`      `float` —       Denominator
`precision` `int`   `2`     Decimal places in the result
=========== ======= ======= ============================

.. code-block::python
    from sc4py.number import percentage

    percentage(45, 60)         # 75.0
    percentage(1, 3)           # 33.33
    percentage(1, 3, precision=4)  # 33.3333
    percentage(0, 100)         # 0.0
    percentage(100, 0)         # 0.0
