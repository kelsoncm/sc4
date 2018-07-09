"""
The MIT License (MIT)

Copyright 2015 Umbrella Tech.

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

__author__ = 'Kelson da Costa Medeiros <kelsoncm@gmail.com>'

import zipfile, io, csv
from typing import List
from python_brfied.choices import *
from python_brfied.datetime import *
from python_brfied.env import *
from python_brfied.exceptions import *
from python_brfied.validations import *
from python_brfied.validations import *


def str2bool(v):
    TRUE_STRS = ('true', 'verdade', 'yes', 'sim', 't', 'v', 'y', 's', '1')
    FALSE_STRS = ('false', 'falso', 'no', 'nao', 'não', 'f', 'n', '0')

    if isinstance(v, bool):
        return v

    if v is None or (isinstance(v, str) and v.strip() == ''):
        return None

    if isinstance(v, int) and v in (1, 0):
        return v == 1

    if isinstance(v, str) and v.strip().lower() in TRUE_STRS + FALSE_STRS:
        return v.lower() in TRUE_STRS

    raise ValueError('Boolean value expected.')


def percentage(num1, num2, precision=2):
    if num1 == 0 or num2 == 0:
        return float(0)
    else:
        return round(float(num1) / float(num2) * 100.0, precision)


def instantiate_class(full_class_name, *args, **kwargs):
    import importlib
    module_name, class_name = full_class_name.rsplit(".", 1)
    MyClass = getattr(importlib.import_module(module_name), class_name)
    return MyClass(*args, **kwargs)


def build_chain(loaders: List[str]):
    instance = None
    loaders.reverse()
    for loader in loaders:
        instance = instantiate_class(loader, instance)
    loaders.reverse()
    return instance


def unzip_content(content, file_index=0, encoding='utf-8'):
    with zipfile.ZipFile(io.BytesIO(content)) as zip_files:
        with zip_files.open(zip_files.filelist[file_index].filename) as zip_file:
            binary_file_content = zip_file.read()
            return binary_file_content if encoding is None else binary_file_content.decode(encoding)


def unzip_csv_content(content, file_index=0, encoding='utf-8', **kwargs):
    csv_stream_content = io.StringIO(unzip_content(content, file_index, encoding))
    return [dict(row) for row in csv.DictReader(csv_stream_content, **kwargs)]


class BaseHandler(object):
    def __init__(self, successor=None):
        self._successor = successor

    def on_start(self):
        pass

    def handle(self, *args, **kwargs):
        raise NotImplementedError()

    def on_stop(self):
        pass


class BaseDirector(object):

    def __init__(self, loaders: List[str]):
        self._loaders = loaders
        self._first_loader = build_chain(loaders)
