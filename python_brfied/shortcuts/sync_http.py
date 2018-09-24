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
import json
from io import BytesIO
from zipfile import ZipFile
from http.client import HTTPException
from requests_ftp import ftp
import requests
from .zip import unzip_content, unzip_csv_content, unzip_fwf_content


def requests_get(url, headers={}, encoding='utf-8', decode=True, **kwargs):
    if url.lower().startswith("ftp://"):
        response = ftp.FTPSession().get(url, **kwargs)
    else:
        response = requests.get(url, headers=headers, **kwargs)

    if response.ok:
        byte_array_content = response.content
        return byte_array_content.decode(encoding) if decode and encoding is not None else byte_array_content
    else:
        exc = HTTPException('%s - %s' % (response.status_code, response.reason))
        exc.status = response.status_code
        exc.reason = response.reason
        exc.headers = response.headers
        exc.url = url
        raise exc


get = requests_get


def get_json(url, headers={}, encoding='utf-8', json_kwargs={}, **kwargs):
    content = get(url, headers=headers, encoding=encoding, **kwargs)
    return json.loads(content, **json_kwargs)


def get_zip(url, headers={}, **kwargs):
    return ZipFile(BytesIO(get(url, headers, encoding=None, **kwargs)))


def get_zip_content(url, headers={}, file_id=0, encoding='utf-8', **kwargs):
    content = get(url, encoding=None, headers=headers, **kwargs)
    return unzip_content(content, file_id=file_id, encoding=encoding)


def get_zip_csv_content(url, headers={}, file_id=0, encoding='utf-8', unzip_kwargs={}, **kwargs):
    content = get(url, encoding=None, headers=headers, **kwargs)
    return unzip_csv_content(content, file_id=file_id, encoding=encoding, **unzip_kwargs)


def get_zip_fwf_content(url, file_descriptor, headers={}, file_id=0, encoding='utf-8', newline="\n\r", **kwargs):
    content = get(url, encoding=None, headers=headers, **kwargs)
    return unzip_fwf_content(content, file_descriptor, file_id, encoding, newline)
