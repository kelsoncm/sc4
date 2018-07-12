
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
