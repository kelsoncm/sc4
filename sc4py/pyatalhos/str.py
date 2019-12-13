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
