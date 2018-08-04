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
import datetime
from pyfwf.descriptors import FileDescriptor, DetailRowDescriptor, HeaderRowDescriptor, FooterRowDescriptor
from pyfwf.columns import CharColumn, RightCharColumn, PositiveIntegerColumn, PositiveDecimalColumn, DateTimeColumn, \
    DateColumn, TimeColumn

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

FILE_DESCRIPTOR = FileDescriptor([DetailRowDescriptor([CharColumn("row_type", 1),
                                                       CharColumn("name", 60),
                                                       RightCharColumn("right_name", 60),
                                                       PositiveIntegerColumn("positive_interger", 9),
                                                       PositiveDecimalColumn("positive_decimal", 9, 2),
                                                       DateTimeColumn("datetime", "%d%m%Y%H%M"),
                                                       DateColumn("date", "%d%m%Y"),
                                                       TimeColumn("datetime", "%H%M")])],
                                 HeaderRowDescriptor([CharColumn("row_type", 1),
                                                      CharColumn("filetype", 3),
                                                      CharColumn("fill", 159)]),
                                 FooterRowDescriptor([CharColumn("row_type", 1),
                                                      PositiveIntegerColumn("detail_count", 4),
                                                      PositiveIntegerColumn("row_count", 4),
                                                      CharColumn("fill", 154)]))
FWF_EXPECTED = [{'row_type': '1',
                 'filetype': 'FWF',
                 'fill': ''},
                {'row_type': '2',
                 'name': 'KELSON DA COSTA MEDEIROS',
                 'right_name': 'KELSON DA COSTA MEDEIROS',
                 'positive_interger': 123456789,
                 'positive_decimal': 1234567.89,
                 'datetime': datetime.time(23, 59),
                 'date': datetime.date(228, 1, 20)},
                {'row_type': '2',
                 'name': 'KELSON DA COSTA MEDEIROS',
                 'right_name': 'KELSON DA COSTA MEDEIROS',
                 'positive_interger': 0,
                 'positive_decimal': 0.0,
                 'datetime': None,
                 'date': None},
                {'row_type': '9',
                 'detail_count': 2,
                 'row_count': 3,
                 'fill': ''}]
