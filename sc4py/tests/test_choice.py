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
from enum import Enum
from unittest import TestCase
from sc4py.choice import to_choice


class PlainEnum(Enum):
    A = 1
    B = 2


class DescribedEnum(Enum):
    description: str
    X = (10, 'ten')
    Y = (20, 'twenty')

    def __new__(cls, value, description):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.description = description
        return obj


class TestPythonBrfiedChoice(TestCase):

    def test_to_choice_from_plain_values(self):
        self.assertEqual([('x', 'x'), (2, 2)], to_choice('x', 2))

    def test_to_choice_from_plain_enum_class(self):
        self.assertEqual([(1, 1), (2, 2)], to_choice(PlainEnum))

    def test_to_choice_from_described_enum_class(self):
        self.assertEqual([(10, 'ten'), (20, 'twenty')], to_choice(DescribedEnum))

    def test_to_choice_from_enum_item(self):
        self.assertEqual([(10, 'ten')], to_choice(DescribedEnum.X))
