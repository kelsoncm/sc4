import json
from io import BytesIO
from zipfile import ZipFile
from http.client import HTTPException
import requests
from .zip import unzip_content, unzip_csv_content


# from http.client import HTTPConnection, HTTPException
# from urllib.parse import urlparse
#
#
# def native_get(url, headers={}, encoding='utf-8'):
#     url_parts = urlparse(url)
#     conn = HTTPConnection(url_parts.hostname, port=url_parts.port if url_parts.port is not None else 80)
#     try:
#         conn.request('GET', url, headers=headers)
#         response = conn.getresponse()
#         if response.status == 200:
#             byte_array_content = response.read()
#             return byte_array_content if encoding is None else byte_array_content.decode(encoding)
#         elif response.status == 301:
#             byte_array_content = response.read()
#             return byte_array_content if encoding is None else byte_array_content.decode(encoding)
#         else:
#             exc = HTTPException('%s - %s' % (response.status, response.reason))
#             exc.status = response.status
#             exc.reason = response.reason
#             exc.headers = response.headers
#             exc.url = url
#             raise exc
#     finally:
#         conn.close()


def requests_get(url, headers={}, encoding='utf-8', decode=True):
    response = requests.get(url, headers=headers)
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


def get_json(url, headers={}, encoding='utf-8'):
    content = get(url, headers=headers, encoding=encoding)
    return json.loads(content)


def get_zip(url, headers={}):
    return ZipFile(BytesIO(get(url, headers, encoding=None)))


def get_zip_content(url, headers={}, file_id=0, encoding='utf-8'):
    content = get(url, encoding=None, headers=headers)
    return unzip_content(content, file_id=file_id, encoding=encoding)


def get_zip_csv_content(url, headers={}, file_id=0, encoding='utf-8', **kargs):
    content = get(url, encoding=None, headers=headers)
    return unzip_csv_content(content, file_id=file_id, encoding=encoding, **kargs)
