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
   :target: https://github.com/kelsoncm/python-sc4py
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

.. code-block:: bash

    pip install sc4py

Modules
-------

* :doc:`sc4py.choice <sc4py.choice>` - Convert plain values and `Enum` types to Django-style choice tuples
* :doc:`sc4py.datetime <sc4py.datetime>` - Date/time helpers and `daterange` generator
* :doc:`sc4py.env <sc4py.env>` - Type-safe environment variable reading
* :doc:`sc4py.klass <sc4py.klass>` - Dynamic class instantiation from dotted path strings
* :doc:`sc4py.number <sc4py.number>` - Percentage calculation
* :doc:`sc4py.str <sc4py.str>` - Multilingual boolean string parsing
* :doc:`sc4py.zip <sc4py.zip>` - In-memory ZIP extraction (text and CSV)

Quick start
-----------

.. code-block:: python

    from sc4py.datetime import now_str, range_date
    from sc4py.env import env_as_bool
    from sc4py.number import percentage
    from sc4py.str import str2bool
    from datetime import date

    print(now_str())                                    # "20-04-2026 14:30:00"
    print(env_as_bool("FEATURE_ENABLED", "true"))       # True
    print(percentage(45, 60))                           # 75.0
    print(str2bool("sim"))                              # True

    for d in range_date(date(2026, 1, 1), date(2026, 1, 3)):
        print(d)

    # 2026-01-01
    # 2026-01-02
    # 2026-01-03


Next steps
----------

.. toctree::
   :maxdepth: 1

   sc4py
   modules
