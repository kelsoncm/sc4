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
from zipfile import ZipFile, ZipInfo
from http.client import HTTPException
from sc4net import get, get_json, get_zip, get_zip_content, get_zip_csv_content
from .mocks import mock_httpd, mock_ftpd, FILE_NOT_FOUND_ERROR_MESSAGE


FILE01_CSV_EXPECTED = "codigo;nome\n1;um\n2;Dois\n3;três\n"
FILE01_CSV_EXPECTED_BINARY = b'codigo;nome\n1;um\n2;Dois\n3;tr\xc3\xaas\n'
FILE01_CSV_EXPECTED_LATIN1 = 'codigo;nome\n1;um\n2;Dois\n3;trÃªs\n'

FILE02_JSON_EXPECTED = '["caça"]'
FILE02_JSON_EXPECTED_LATIN1 = '["caÃ§a"]'

FILE02_JSON_EXPECTED_BINARY = b'["ca\xc3\xa7a"]'

CSV_EXPECTED = [{'codigo': '1', 'nome': 'um'}, {'codigo': '2', 'nome': 'Dois'}, {'codigo': '3', 'nome': 'três'}]
JSON_EXPECTED = ['caça']
ZIP_EXPECTED = b'PK\x03\x04\n\x00\x00\x00\x00\x00&z\xe9L\xad\rM\x07 \x00\x00\x00 \x00' \
               b'\x00\x00\x08\x00\x1c\x00file.csvUT\t\x00\x03\xa8\xa6C[\xd6\xa6C[u' \
               b'x\x0b\x00\x01\x04\xe8\x03\x00\x00\x04\xe8\x03\x00\x00codigo;nome\n1;um\n2' \
               b';Dois\n3;tr\xc3\xaas\nPK\x01\x02\x1e\x03\n\x00\x00\x00\x00\x00&z\xe9L\xad\r' \
               b'M\x07 \x00\x00\x00 \x00\x00\x00\x08\x00\x18\x00\x00\x00\x00\x00\x01\x00' \
               b'\x00\x00\xb4\x81\x00\x00\x00\x00file.csvUT\x05\x00\x03\xa8\xa6C[ux\x0b' \
               b'\x00\x01\x04\xe8\x03\x00\x00\x04\xe8\x03\x00\x00PK\x05\x06\x00\x00\x00\x00' \
               b'\x01\x00\x01\x00N\x00\x00\x00b\x00\x00\x00\x00\x00'


class TestPythonBrfiedShortcutSyncHttp(TestCase):

    def setUp(self):
        http_root = TestPythonBrfiedShortcutSyncHttp.http_root
        self.file_not_found = http_root + "/file_not_found"
        self.file01_csv_url = http_root + "/file01.csv"
        self.file01_zip_url = http_root + "/file01.zip"
        self.file02_json_url = http_root + "/file02.json"
        self.file02_zip_url = http_root + "/file02.zip"

    @classmethod
    def setUpClass(cls):
        cls.http_root = mock_httpd()
        cls.ftpd = mock_ftpd()

    # @httpretty.activate
    def test_get(self):
        self.assertRaisesRegex(HTTPException, FILE_NOT_FOUND_ERROR_MESSAGE, get, self.file_not_found)

        try:
            self.assertIsNotNone(get(self.file_not_found))
        except Exception as exc:
            self.assertEqual(404, getattr(exc, 'status', None))
            self.assertEqual('File not found', getattr(exc, 'reason', None))
            self.assertTrue('Content-Type' in getattr(exc, 'headers'))
            self.assertEqual(self.file_not_found, getattr(exc, 'url', None))

        self.assertRaises(UnicodeDecodeError, get, self.file01_zip_url, None)

        self.assertEqual(FILE01_CSV_EXPECTED, get(self.file01_csv_url))
        self.assertEqual(FILE01_CSV_EXPECTED_BINARY, get(self.file01_csv_url, encoding=None))
        self.assertEqual(FILE01_CSV_EXPECTED_LATIN1, get(self.file01_csv_url, encoding='latin1'))

        self.assertEqual(FILE02_JSON_EXPECTED, get(self.file02_json_url))
        self.assertEqual(FILE02_JSON_EXPECTED_BINARY, get(self.file02_json_url, encoding=None))
        self.assertEqual(FILE02_JSON_EXPECTED_LATIN1, get(self.file02_json_url, encoding='latin1'))

        self.assertEqual(ZIP_EXPECTED, get(self.file01_zip_url, encoding=None))

    def test_get_json(self):
        self.assertEqual(JSON_EXPECTED, get_json(self.file02_json_url))

    def test_get_zip(self):
        self.assertIsInstance(get_zip(self.file01_zip_url), ZipFile)
        self.assertIsInstance(get_zip(self.file01_zip_url).filelist[0], ZipInfo)
        self.assertEqual('file.csv', get_zip(self.file01_zip_url).filelist[0].filename)
        self.assertEqual('file.csv', get_zip(self.file01_zip_url).filelist[0].filename)

    def test_get_zip_content(self):
        self.assertEqual(FILE01_CSV_EXPECTED, get_zip_content(self.file01_zip_url))

    def test_get_zip_csv_content(self):
        self.assertEqual(CSV_EXPECTED, get_zip_csv_content(self.file01_zip_url, unzip_kwargs={"delimiter": ';'}))

    def test_get_zip_content_ftp(self):
        self.assertEqual(FILE01_CSV_EXPECTED, get_zip_content("ftp://localhost:2121/file01.ZIP"))

    def test_get_ftp(self):
        self.assertEqual("pong", get("ftp://localhost:2121/ping.txt"))
