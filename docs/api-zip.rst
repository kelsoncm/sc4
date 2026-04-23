sc4py.zip
===============

In-memory ZIP extraction helpers — read text files and CSV files directly from raw bytes without writing to disk.

Exceptions
----------

`FileNotFoundInZipError`
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Subclass of `FileNotFoundError`. Raised when the requested file cannot be found inside the ZIP archive.

Functions
---------

`unzip_content(content, file_id=0, encoding="utf-8") → str | bytes`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Extracts a single file from a ZIP archive provided as `bytes`.

========== ============ ========= ====================================================================
Parameter  Type         Default   Description
========== ============ ========= ====================================================================
`content`  `bytes`      —         Raw ZIP bytes
`file_id`  `int | str`  `0`       Index (int) or filename (str) of the entry to extract
`encoding` `str | None` `"utf-8"` Encoding used to decode the bytes; pass `None` to return raw `bytes`
========== ============ ========= ====================================================================

.. code-block::python
    import requests
    from sc4py.zip import unzip_content

    raw = requests.get("https://example.com/data.zip").content

    # First file by index
    text = unzip_content(raw)

    # Specific file by name
    text = unzip_content(raw, file_id="report.txt")

    # Raw bytes (no decoding)
    data = unzip_content(raw, encoding=None)

`unzip_csv_content(content, file_id=0, encoding="utf-8", **kwargs) → list[dict]`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Extracts a CSV file from a ZIP archive and returns it as a list of dicts (one per row).

Extra keyword arguments are forwarded to `csv.DictReader` (e.g. `delimiter`, `fieldnames`).

========== ============ ========= ====================================================================
Parameter  Type         Default   Description
========== ============ ========= ====================================================================
`content`  `bytes`      -         Raw ZIP bytes
`file_id`  `int | str`  `0`       Index or filename of the CSV entry
`encoding` `str`        `"utf-8"` Encoding of the CSV text
`**kwargs`  -           -         Forwarded to `csv.DictReader`
========== ============ ========= ====================================================================

.. code-block::python
    from sc4py.zip import unzip_csv_content

    with open("archive.zip", "rb") as f:
        rows = unzip_csv_content(f.read(), file_id="sales.csv")

    for row in rows:
        print(row)
    # {"date": "2026-01-01", "amount": "100.00"}

.. code-block::python
    # Custom delimiter
    rows = unzip_csv_content(raw, file_id="data.txt", delimiter=";")
