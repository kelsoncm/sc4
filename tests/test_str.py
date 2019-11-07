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
from unittest import TestCase
from pyatalhos import str2bool


class TestPythonBrfiedInit(TestCase):

    def test_str2bool(self):
        self.assertTrue(str2bool(True))
        self.assertTrue(str2bool('True'))
        self.assertTrue(str2bool('true'))
        self.assertTrue(str2bool('TRUE'))
        self.assertTrue(str2bool('verdade'))
        self.assertTrue(str2bool('Verdade'))
        self.assertTrue(str2bool('Yes'))
        self.assertTrue(str2bool('yes'))
        self.assertTrue(str2bool('YES'))
        self.assertTrue(str2bool('Sim'))
        self.assertTrue(str2bool('sim'))
        self.assertTrue(str2bool('SIM'))
        self.assertTrue(str2bool('T'))
        self.assertTrue(str2bool('t'))
        self.assertTrue(str2bool('v'))
        self.assertTrue(str2bool('V'))
        self.assertTrue(str2bool('Y'))
        self.assertTrue(str2bool('y'))
        self.assertTrue(str2bool('s'))
        self.assertTrue(str2bool('S'))
        self.assertTrue(str2bool('1'))
        self.assertTrue(str2bool(1))

        self.assertFalse(str2bool(False))
        self.assertFalse(str2bool('False'))
        self.assertFalse(str2bool('false'))
        self.assertFalse(str2bool('FALSE'))
        self.assertFalse(str2bool('Falso'))
        self.assertFalse(str2bool('falso'))
        self.assertFalse(str2bool('FALSO'))
        self.assertFalse(str2bool('No'))
        self.assertFalse(str2bool('no'))
        self.assertFalse(str2bool('NO'))
        self.assertFalse(str2bool('Nao'))
        self.assertFalse(str2bool('nao'))
        self.assertFalse(str2bool('NAO'))
        self.assertFalse(str2bool('Não'))
        self.assertFalse(str2bool('não'))
        self.assertFalse(str2bool('NÃO'))
        self.assertFalse(str2bool('F'))
        self.assertFalse(str2bool('f'))
        self.assertFalse(str2bool('N'))
        self.assertFalse(str2bool('n'))
        self.assertFalse(str2bool('0'))
        self.assertFalse(str2bool(0))

        self.assertIsNone(str2bool(None))
        self.assertIsNone(str2bool(''))
        self.assertIsNone(str2bool(' '))

        self.assertRaises(ValueError, str2bool, 2)
