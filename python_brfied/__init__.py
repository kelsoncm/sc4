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

from typing import List
from python_brfied.choices import *
from python_brfied.datetime import *
from python_brfied.env import *
from python_brfied.exceptions import *
from python_brfied.validations import *
from python_brfied.validations import *
from python_brfied.shortcuts.zip import *


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


def build_chain(links_names: List[str]):
    link = None
    links = []
    for link_name in links_names[::-1]:
        if isinstance(link_name, str):
            link = instantiate_class(link_name, link)
        else:
            link = link_name(link)
        links.append(link)
    return links[::-1]


class BaseHandler(object):
    def __init__(self, successor=None):
        self._successor = successor

    def on_start(self, *args, **kwargs):
        pass

    def handle(self, *args, **kwargs):
        raise NotImplementedError()

    def on_stop(self, *args, **kwargs):
        pass


class BaseDirector(object):

    def __init__(self, links_names: List[str]):
        self._links_names = links_names
        self._links = build_chain(links_names)
        self._first_loader = self._links[0] if len(self._links) > 0 else []

    def on_start(self, *args, **kwargs):
        for link in self._links:
            link.on_start(*args, **kwargs)

    def execute(self, *args, **kwargs):
        for link in self._links:
            link.handle(*args, **kwargs)

    def on_stop(self, *args, **kwargs):
        for link in self._links:
            link.on_stop(*args, **kwargs)
