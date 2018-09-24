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


def env(name, default=None):
    return getenv(name, default)


def env_as_list(name, default='', delimiter=','):
    if default.strip() == '':
        return []
    return getenv(name, default).split(delimiter)


def env_as_list_of_maps(name, key, default='', delimiter=','):
    return [{key: x} for x in env_as_list(name, default, delimiter)]


def env_as_bool(name, default=None):
    from python_brfied import str2bool
    return str2bool(getenv(name, default))


def env_from_json(key, default=''):
    result = env(key, default)
    return json.loads(result) if result is not None else result


def env_as_int(key, default=None):
    result = env(key, default)
    return int(result) if result is not None else result
