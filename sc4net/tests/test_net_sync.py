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
import os
import socket
from zipfile import ZipFile, ZipInfo
from threading import Thread
from http.server import BaseHTTPRequestHandler, HTTPServer
from http.client import HTTPException
from sc4net import get, get_json, get_zip, get_zip_content, get_zip_csv_content

# /home/runner/work/
# from pyftpdlib.authorizers import DummyAuthorizer
# from pyftpdlib.handlers import FTPHandler
# from pyftpdlib.servers import FTPServer


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

# change 'user' to your user name and directory!
# authorizer = DummyAuthorizer()
# authorizer.add_user("user", "8231335704", "/home/user", perm="elradfmw")
# authorizer.add_anonymous("/home/user", perm="elradfmw")

# handler = FTPHandler
# handler.authorizer = authorizer

# server = FTPServer(("127.0.0.1", 1026), handler) #host goes here
# server.serve_forever()


dir_path = os.path.dirname(os.path.realpath(__file__))


def get_free_port():
    s = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM)
    s.bind(('localhost', 0))
    address, port = s.getsockname()
    s.close()
    return port


class MockServerRequestHandler(BaseHTTPRequestHandler):
    with open(dir_path + "/assets/file01.csv", "rb") as f:
        file01_csv = f.read()

    with open(dir_path + "/assets/file01.zip", "rb") as f:
        file01_zip = f.read()

    with open(dir_path + "/assets/file02.json", "rb") as f:
        file02_json = f.read()

    with open(dir_path + "/assets/file02.zip", "rb") as f:
        file02_zip = f.read()

    files = {'file01_csv': file01_csv, 'file01_zip': file01_zip, 'file02_json': file02_json, 'file02_zip': file02_zip}

    FILE_NOT_FOUND_ERROR_MESSAGE = 'File not found'

    def __init__(self, request, client_address, server):
        super(MockServerRequestHandler, self).__init__(request, client_address, server)

    def log_error(self, format, *args):
        # super(MockServerRequestHandler, self).log_message(format, *args)
        pass

    def log_message(self, format, *args):
        pass

    def do_GET(self):
        parts = self.path.split('/')
        prop = parts[len(parts)-1]

        if prop not in MockServerRequestHandler.files:
            self.send_error(404, MockServerRequestHandler.FILE_NOT_FOUND_ERROR_MESSAGE)
            return

        # Add response status code.
        self.send_response(200)

        # Add response headers.
        # self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.end_headers()

        # Add response content.
        self.wfile.write(MockServerRequestHandler.files[prop])

        return


class TestPythonBrfiedShortcutSyncHttp(TestCase):

    def setUp(self):
        self.port = TestPythonBrfiedShortcutSyncHttp.mock_server_port
        self.file_not_found = "http://localhost:%d/file_not_found" % self.port
        self.file01_csv_url = "http://localhost:%d/file01_csv" % self.port
        self.file01_zip_url = "http://localhost:%d/file01_zip" % self.port
        self.file02_json_url = "http://localhost:%d/file02_json" % self.port
        self.file02_zip_url = "http://localhost:%d/file02_zip" % self.port

    @classmethod
    def setUpClass(cls):
        # https://realpython.com/testing-third-party-apis-with-mock-servers/
        # Configure mock server.
        cls.mock_server_port = get_free_port()
        cls.mock_server = HTTPServer(('localhost', cls.mock_server_port), MockServerRequestHandler)

        # Start running mock server in a separate thread.
        # Daemon threads automatically shut down when the main process exits.
        cls.mock_server_thread = Thread(target=cls.mock_server.serve_forever)
        cls.mock_server_thread.setDaemon(True)
        cls.mock_server_thread.start()

    # @httpretty.activate
    def test_get(self):
        self.assertRaisesRegex(HTTPException, MockServerRequestHandler.FILE_NOT_FOUND_ERROR_MESSAGE,
                               get, self.file_not_found)

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

        self.assertEqual('file.csv', get_zip(self.file01_zip_url).filelist[0].filename)

    def test_get_ftp(self):
        self.assertEqual("04/09/2012 12:24:13\r\n", get("ftp://ftp.datasus.gov.br/cnes/informe_cnes.txt"))

    def test_get_json(self):
        self.assertEqual(JSON_EXPECTED, get_json(self.file02_json_url))

    def test_get_zip(self):
        self.assertIsInstance(get_zip(self.file01_zip_url), ZipFile)
        self.assertIsInstance(get_zip(self.file01_zip_url).filelist[0], ZipInfo)
        self.assertEqual('file.csv', get_zip(self.file01_zip_url).filelist[0].filename)

    def test_get_zip_content(self):
        self.assertEqual(FILE01_CSV_EXPECTED, get_zip_content(self.file01_zip_url))

    def test_get_zip_content_ftp(self):
        with open(dir_path + "/assets/IMPORT_201711.txt") as f:
            expected = f.read()
        self.assertEqual(expected, get_zip_content("ftp://ftp.datasus.gov.br/cnes/IMPORT_201711.ZIP").replace("\r", ""))

    def test_get_zip_csv_content(self):
        self.assertEqual(CSV_EXPECTED, get_zip_csv_content(self.file01_zip_url, unzip_kwargs={"delimiter": ';'}))
