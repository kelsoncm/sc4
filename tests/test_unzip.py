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
from pyshortcuts import unzip_content, unzip_csv_content, unzip_fwf_content, FileNotFoundInZipError
from tests import FWF_EXPECTED, FILE_DESCRIPTOR


class TestPythonBrfiedInit(TestCase):

    def test_unzip_content(self):
        expected = "codigo;nome\n1;um\n2;Dois\n3;três\n"
        expected_binary = b'codigo;nome\n1;um\n2;Dois\n3;tr\xc3\xaas\n'
        expected_latin1 = 'codigo;nome\n1;um\n2;Dois\n3;trÃªs\n'
        with open("/src/tests/assets/file01.zip", "rb") as f:
            binary = f.read()
        self.assertEqual(expected, unzip_content(binary))
        self.assertEqual(expected, unzip_content(binary, 0))
        self.assertEqual(expected, unzip_content(binary, 'file.csv'))
        self.assertRaises(FileNotFoundInZipError, unzip_content, binary, 'file2.csv')
        self.assertRaises(FileNotFoundInZipError, unzip_content, binary, 1)

        self.assertEqual(expected_binary, unzip_content(binary, encoding=None))
        self.assertEqual(expected_latin1, unzip_content(binary, encoding='latin_1'))
        self.assertRaises(UnicodeDecodeError, unzip_content, binary, encoding='ascii')

    def test_unzip_csv_content(self):
        with open("/src/tests/assets/file01.zip", "rb") as f:
            content = unzip_csv_content(f.read(), delimiter=';')
            expected = [{"codigo": '1', 'nome': 'um'}, {"codigo": '2', 'nome': 'Dois'}, {"codigo": '3', 'nome': 'três'}]
            self.assertListEqual(expected, content)

    def test_unzip_fwf_content(self):
        with open("/src/tests/assets/example01_are_right.fwf.zip", "rb") as f:
            content = unzip_fwf_content(f.read(), FILE_DESCRIPTOR, newline="\n")
            self.assertListEqual(FWF_EXPECTED, content)
