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
import os
import threading
# import socket
from http.server import HTTPServer, BaseHTTPRequestHandler
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


FILE_NOT_FOUND_ERROR_MESSAGE = 'File not found'


dir_path = os.path.dirname(os.path.realpath(__file__)) + "/assets/"


def mock_ftpd():

    # def serve_ftpd_thread_function(server, *args, **kwargs):
    #     server.serve_forever()

    authorizer = DummyAuthorizer()
    authorizer.add_anonymous(dir_path)
    handler = FTPHandler
    handler.authorizer = authorizer
    handler.banner = "pyftpdlib based ftpd ready."
    server = FTPServer(('', 2121), handler)

    # thread = threading.Thread(target=serve_ftpd_thread_function, kwargs={"server": server})
    thread = threading.Thread(target=server.serve_forever)
    thread.setDaemon(True)
    thread.start()

    return server


class MockHttpServerRequestHandler(BaseHTTPRequestHandler):

    def __init__(self, request, client_address, server):
        super(MockHttpServerRequestHandler, self).__init__(request, client_address, server)

    def log_error(self, format, *args):
        pass

    def log_message(self, format, *args):
        pass

    def do_GET(self):
        parts = self.path.split('/')
        filepath = parts[len(parts)-1]
        full_file_name = dir_path + filepath

        if not os.path.exists(full_file_name):
            self.send_error(404, FILE_NOT_FOUND_ERROR_MESSAGE)
            return

        self.send_response(200)
        self.end_headers()
        with open(full_file_name, "rb") as f:
            self.wfile.write(f.read())
        return


def mock_httpd():
    # https://realpython.com/testing-third-party-apis-with-mock-servers/
    # Configure mock server.
    # def get_free_port():
    #     s = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM)
    #     s.bind(('localhost', 0))
    #     address, port = s.getsockname()
    #     s.close()
    #     return port
    # mock_http_server_port = get_free_port()

    mock_http_server_port = 1234
    mock_http_server = HTTPServer(('localhost', mock_http_server_port), MockHttpServerRequestHandler)

    # Start running mock server in a separate thread.
    # Daemon threads automatically shut down when the main process exits.
    thread = threading.Thread(target=mock_http_server.serve_forever)
    thread.setDaemon(True)
    thread.start()

    return "http://%s:%d" % ('localhost', mock_http_server_port)
