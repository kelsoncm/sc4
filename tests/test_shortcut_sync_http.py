from unittest import TestCase
from python_brfied.shortcuts.sync_http import get, get_json, get_zip, get_zip_content, get_zip_csv_content
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
from http.client import HTTPException
from threading import Thread
from tests import FILE01_CSV_EXPECTED, FILE01_CSV_EXPECTED_BINARY, FILE01_CSV_EXPECTED_LATIN1
from tests import FILE02_JSON_EXPECTED, FILE02_JSON_EXPECTED_BINARY, FILE02_JSON_EXPECTED_LATIN1
from tests import ZIP_EXPECTED, JSON_EXPECTED, CSV_EXPECTED
from zipfile import ZipFile, ZipInfo


def get_free_port():
    s = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM)
    s.bind(('localhost', 0))
    address, port = s.getsockname()
    s.close()
    return port


class MockServerRequestHandler(BaseHTTPRequestHandler):
    with open("assets/file01.csv", "rb") as f:
        file01_csv = f.read()

    with open("assets/file01.zip", "rb") as f:
        file01_zip = f.read()

    with open("assets/file02.json", "rb") as f:
        file02_json = f.read()

    with open("assets/file02.zip", "rb") as f:
        file02_zip = f.read()

    files = {'file01_csv': file01_csv, 'file01_zip': file01_zip, 'file02_json': file02_json, 'file02_zip': file02_zip, }

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
            get(self.file_not_found)
            self.fail('Deveria dar um erro')
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

    def test_get_json(self):
        self.assertEqual(JSON_EXPECTED, get_json(self.file02_json_url))

    def test_get_zip(self):
        self.assertIsInstance(get_zip(self.file01_zip_url), ZipFile)
        self.assertIsInstance(get_zip(self.file01_zip_url).filelist[0], ZipInfo)
        self.assertEqual('file.csv', get_zip(self.file01_zip_url).filelist[0].filename)

    def test_get_zip_content(self):
        self.assertEqual(FILE01_CSV_EXPECTED, get_zip_content(self.file01_zip_url))

    def test_get_zip_csv_content(self):
        self.assertEqual(CSV_EXPECTED, get_zip_csv_content(self.file01_zip_url))
