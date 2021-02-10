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

import json
from os import getenv
from .str import str2bool


def env(name, default=None, wrapped=False):
    result = getenv(name, default)
    if wrapped and isinstance(result, str) and result[0:1] == "'" and result[-1:] == "'":
        return result[1:-1]
    return result


def env_as_list(name, default='', delimiter=',', wrapped=False):
    result = env(name, default, wrapped)
    if result is None:
        return None
    if type(result) == str:
        if result.strip() == '' and default.strip() == '':
            return []
        return result.split(delimiter)
    if type(result) in (list, tuple):
        return list(result)
    raise TypeError("env_as_list requires str, list or tuple as default")


def env_as_list_of_maps(name, key, default='', delimiter=',', wrapped=False):
    return [{key: x} for x in env_as_list(name, default, delimiter, wrapped)]


def env_as_bool(name, default=None, wrapped=False):
    return str2bool(env(name, default, wrapped))


def env_from_json(key, default='', wrapped=False):
    result = env(key, default, wrapped)
    return json.loads(result) if result is not None else result


def env_as_int(key, default=None, wrapped=False):
    result = env(key, default, wrapped)
    return int(result) if result is not None else result
