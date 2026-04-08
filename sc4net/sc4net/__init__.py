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
from ftplib import FTP  # nosec B402
from http.client import HTTPException
from io import BytesIO
from typing import NoReturn, Optional, cast
from urllib.error import HTTPError, URLError
from urllib.parse import unquote, urlencode, urlparse
from urllib.request import Request, urlopen
from zipfile import ZipFile

from sc4py.zip import unzip_content, unzip_csv_content

default_headers = {}


def _raise_http_exception(status, reason, url, headers=None) -> NoReturn:
    exc = HTTPException("%s - %s" % (status, reason))
    setattr(exc, "status", status)
    setattr(exc, "reason", reason)
    setattr(exc, "headers", headers or {})
    setattr(exc, "url", url)
    raise exc


def _merge_headers(headers):
    result = dict(default_headers)
    if headers:
        result.update(headers)
    return result


def _validate_web_url(url):
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https") or not parsed.netloc:
        _raise_http_exception(400, "Only http/https URLs are allowed", url)


def _ftp_get_with_stdlib(url, timeout=None) -> bytes:
    parsed = urlparse(url)
    host = parsed.hostname
    if host is None:
        _raise_http_exception(400, "Invalid FTP URL", url)

    port = parsed.port or 21
    username = unquote(parsed.username) if parsed.username else "anonymous"
    password = unquote(parsed.password) if parsed.password else "anonymous@"
    filepath = unquote(parsed.path.lstrip("/"))
    if filepath == "":
        _raise_http_exception(400, "FTP file path is required", url)

    try:
        with FTP() as ftp_client:  # nosec B321
            if timeout is None:
                ftp_client.connect(host=host, port=port)
            else:
                ftp_client.connect(host=host, port=port, timeout=float(timeout))
            ftp_client.login(user=username, passwd=password)
            output = BytesIO()
            ftp_client.retrbinary("RETR %s" % filepath, output.write)
            return output.getvalue()
    except Exception as exc:
        _raise_http_exception(502, str(exc), url)


def _http_get_with_stdlib(url, headers=None, timeout=None) -> bytes:
    _validate_web_url(url)
    request = Request(url, headers=_merge_headers(headers))
    try:
        with urlopen(request, timeout=timeout) as response:  # nosec B310
            return response.read()
    except HTTPError as exc:
        _raise_http_exception(exc.code, exc.reason, url, dict(exc.headers or {}))
    except URLError as exc:
        _raise_http_exception(502, str(exc.reason), url)


def _build_post_payload(data, json_data, request_headers, encoding):

    if json_data is not None:
        payload = json.dumps(json_data).encode(encoding or "utf-8")
        if "Content-Type" not in request_headers:
            request_headers["Content-Type"] = "application/json"
        return payload

    if data is None:
        return None

    if isinstance(data, bytes):
        return data
    if isinstance(data, str):
        return data.encode(encoding or "utf-8")
    if isinstance(data, dict):
        payload = urlencode(data, doseq=True).encode(encoding or "utf-8")
        if "Content-Type" not in request_headers:
            request_headers["Content-Type"] = "application/x-www-form-urlencoded"
        return payload

    return str(data).encode(encoding or "utf-8")


def requests_get(
    url, headers=None, encoding: Optional[str] = "utf-8", decode=True, **kwargs
):
    timeout = kwargs.get("timeout")
    if url.lower().startswith("ftp://"):
        byte_array_content = _ftp_get_with_stdlib(url, timeout=timeout)
    else:
        byte_array_content = _http_get_with_stdlib(
            url, headers=headers, timeout=timeout
        )

    return (
        byte_array_content.decode(encoding)
        if decode and encoding is not None
        else byte_array_content
    )


get = requests_get


def get_json(url, headers=None, encoding="utf-8", json_kwargs=None, **kwargs):
    content = cast(
        str | bytes | bytearray, get(url, headers=headers, encoding=encoding, **kwargs)
    )
    if not isinstance(content, (str, bytes, bytearray)):
        _raise_http_exception(500, "JSON content must be text or bytes", url)
    if isinstance(content, bytearray):
        content = bytes(content)
    return json.loads(content, **(json_kwargs or {}))


def get_zip(url, headers=None, **kwargs):
    content = cast(
        bytes | bytearray, get(url, headers=headers, encoding=None, **kwargs)
    )
    if not isinstance(content, (bytes, bytearray)):
        _raise_http_exception(500, "ZIP content must be bytes", url)
    if isinstance(content, bytearray):
        content = bytes(content)
    return ZipFile(BytesIO(content))


def get_zip_content(url, headers=None, file_id=0, encoding="utf-8", **kwargs):
    content = cast(
        bytes | bytearray, get(url, encoding=None, headers=headers, **kwargs)
    )
    if not isinstance(content, (bytes, bytearray)):
        _raise_http_exception(500, "ZIP content must be bytes", url)
    if isinstance(content, bytearray):
        content = bytes(content)
    return unzip_content(content, file_id=file_id, encoding=encoding)


def get_zip_csv_content(
    url, headers=None, file_id=0, encoding="utf-8", unzip_kwargs=None, **kwargs
):
    content = cast(
        bytes | bytearray, get(url, encoding=None, headers=headers, **kwargs)
    )
    if not isinstance(content, (bytes, bytearray)):
        _raise_http_exception(500, "ZIP content must be bytes", url)
    if isinstance(content, bytearray):
        content = bytes(content)
    return unzip_csv_content(
        content, file_id=file_id, encoding=encoding, **(unzip_kwargs or {})
    )


def post(
    url,
    data=None,
    json_data=None,
    headers=None,
    encoding="utf-8",
    decode=True,
    **kwargs
):
    timeout = kwargs.get("timeout")
    request_headers = _merge_headers(headers)
    _validate_web_url(url)

    payload = _build_post_payload(data, json_data, request_headers, encoding)

    request = Request(url, data=payload, headers=request_headers, method="POST")
    try:
        with urlopen(request, timeout=timeout) as response:  # nosec B310
            byte_array_content = response.read()
    except HTTPError as exc:
        _raise_http_exception(exc.code, exc.reason, url, dict(exc.headers or {}))
    except URLError as exc:
        _raise_http_exception(502, str(exc.reason), url)

    return (
        byte_array_content.decode(encoding)
        if decode and encoding is not None
        else byte_array_content
    )


def post_json(
    url,
    data=None,
    json_data=None,
    headers=None,
    encoding="utf-8",
    json_kwargs=None,
    **kwargs
):
    content = cast(
        str | bytes | bytearray,
        post(url, data, json_data, headers=headers, encoding=encoding, **kwargs),
    )
    if not isinstance(content, (str, bytes, bytearray)):
        _raise_http_exception(500, "JSON content must be text or bytes", url)
    if isinstance(content, bytearray):
        content = bytes(content)
    return json.loads(content, **(json_kwargs or {}))


def put(url, data=None, json_data=None, headers=None, encoding="utf-8", **kwargs):
    raise NotImplementedError()


def put_json(
    url,
    data=None,
    json_data=None,
    headers=None,
    encoding="utf-8",
    json_kwargs=None,
    **kwargs
):
    raise NotImplementedError()


def delete(url, headers=None, encoding="utf-8", decode=True, **kwargs):
    raise NotImplementedError()


def delete_json(url, headers=None, encoding="utf-8", json_kwargs=None, **kwargs):
    raise NotImplementedError()
