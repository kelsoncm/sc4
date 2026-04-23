sc4py
=====
Utilities for date/time, environment parsing, dynamic class loading,
percentages, string-to-bool conversion, choice tuples, and in-memory ZIP reading.

.. image:: https://img.shields.io/badge/GitHub-Repository-blue?logo=github
   :target: https://github.com/kelsoncm/python-sc4py
   :alt: GitHub Repository

.. image:: https://img.shields.io/badge/License-MIT-lemon.svg
   :target: https://opensource.org/licenses/MIT
   :alt: License

.. image:: https://img.shields.io/pypi/pyversions/sc4py.svg
   :target: https://pypi.org/project/sc4py/
   :alt: Python

.. image:: https://github.com/kelsoncm/python-sc4py/actions/workflows/qa.yml/badge.svg
   :target: https://github.com/kelsoncm/python-sc4py/actions/workflows/qa.yml
   :alt: QA

.. image:: https://codecov.io/gh/kelsoncm/python-sc4py/branch/main/graph/badge.svg
   :target: https://codecov.io/gh/kelsoncm/python-sc4py
   :alt: Coverage

.. image:: https://github.com/kelsoncm/python-sc4py/actions/workflows/publish.yml/badge.svg
   :target: https://github.com/kelsoncm/python-sc4py/actions/workflows/publish.yml
   :alt: Publish

.. image:: https://github.com/kelsoncm/python-sc4py/actions/workflows/docs.yml/badge.svg
   :target: https://kelsoncm.github.io/python-sc4py/
   :alt: Docs

.. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit


Installation
------------

.. code-block::bash
    pip install sc4py

Modules
-------

=================================== ===================================================================
Module                              Purpose
=================================== ===================================================================
[`sc4py.choice`](api-choice.md)     Convert plain values and `Enum` types to Django-style choice tuples
[`sc4py.datetime`](api-datetime.md) Date/time helpers and `daterange` generator
[`sc4py.env`](api-env.md)           Type-safe environment variable reading
[`sc4py.klass`](api-klass.md)       Dynamic class instantiation from dotted path strings
[`sc4py.number`](api-number.md)     Percentage calculation
[`sc4py.str`](api-str.md)           Multilingual boolean string parsing
[`sc4py.zip`](api-zip.md)           In-memory ZIP extraction (text and CSV)
=================================== ===================================================================

Quick start
-----------

.. code-block::python
    from sc4py.datetime import now_str, daterange
    from sc4py.env import env_as_bool
    from sc4py.number import percentage
    from sc4py.str import str2bool
    from datetime import date

    print(now_str())                                    # "20-04-2026 14:30:00"
    print(env_as_bool("FEATURE_ENABLED", "true"))       # True
    print(percentage(45, 60))                           # 75.0
    print(str2bool("sim"))                              # True

    for d in daterange(date(2026, 1, 1), date(2026, 1, 3)):
        print(d)

    # 2026-01-01
    # 2026-01-02
    # 2026-01-03

Next steps
----------

.. toctree::
   :maxdepth: 1

   index
   api-choice.md
   api-datetime.md
   api-env.md
   api-klass.md
   api-number.md
   api-str.md
   api-zip.md
