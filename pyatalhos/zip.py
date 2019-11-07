"""
The MIT License (MIT)

Copyright (c) 2015 kelsoncm

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from zipfile import ZipFile
from io import BytesIO, StringIO
from csv import DictReader
from pyfwf.readers import Reader


class FileNotFoundInZipError(FileNotFoundError):
    pass


def unzip_content(content, file_id=0, encoding='utf-8'):
    with ZipFile(BytesIO(content)) as zip_file:
        try:
            filename = file_id if type(file_id) == str else zip_file.filelist[file_id].filename
        except IndexError:
            raise FileNotFoundInZipError("Não existe arquivo no índice %d")
        try:
            with zip_file.open(filename) as zipped_file:
                binary_file_content = zipped_file.read()
            return binary_file_content if encoding is None else binary_file_content.decode(encoding)
        except KeyError:
            raise FileNotFoundInZipError("Não existe arquivo com o nome %s" % filename)


def unzip_csv_content(content, file_id=0, encoding='utf-8', **kwargs):
    csv_stream_content = StringIO(unzip_content(content, file_id, encoding))
    return [dict(row) for row in DictReader(csv_stream_content, **kwargs)]


def unzip_fwf_content(content, file_descriptor, file_id=0, encoding='utf-8', newline="\n\r"):
    _iterable = StringIO(unzip_content(content, file_id, encoding))
    return [row for row in Reader(_iterable, file_descriptor, newline)]
