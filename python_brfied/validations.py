"""
The MIT License (MIT)

Copyright 2015 Umbrella Tech.

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

__author__ = 'Kelson da Costa Medeiros <kelsoncm@gmail.com>'


import re
from .exceptions import MaskException, EmptyMaskException, DVException, \
    MaskWithoutDigitsException, MaskWithoutSpecialCharsException, MaskNotStringException, TooManyDigitsException


CPF_MASK = '999.999.999-00'
CPF_RE = re.compile(r'^(\d{3})\.(\d{3})\.(\d{3})-(\d{2})$')

CNPJ_MASK = '99.999.999/9999-00'
CNPJ_RE = re.compile('^(\d{2})[.-]?(\d{3})[.-]?(\d{3})/(\d{4})-(\d{2})$')

CEP_MASK = '99999-999'
CEP_RE = '^\d{5}-\d{3}$'

PROCESSO_MASK = '9999999-99.9999.9.99.9999'
PROCESSO_RE = re.compile('^(\d{7})-?(\d{2})\.?(\d{4})\.?(\d)\.?(\d{2})\.?(\d{4})$')


def only_digits(seq):
    return ''.join(c for c in filter(type(seq).isdigit, seq))


def apply_mask(value, mask):
    unmask = only_digits(mask)
    zfill_value = only_digits(value).zfill(len(unmask))
    if len(unmask) != len(zfill_value):
        raise MaskException()

    result = ''
    i = 0
    for m in mask:
        if m.isdigit():
            result += zfill_value[i]
            i += 1
        else:
            result += m
    return result


def validate_masked_value(value, mask, force=True):
    masked_value = apply_mask(only_digits(value), mask) if force else value
    if len(mask) != len(masked_value):
        raise MaskException()

    for i in range(0, len(mask)):
        m = mask[i]
        v = masked_value[i]
        if (not m.isdigit() and m != v) or m.isdigit() != v.isdigit():
            raise MaskException()
    return masked_value


def validate_cpf(unmasked_value, *args, **kwargs):
    value = only_digits(unmasked_value)

    if len(value) != 11:
        raise MaskException('O CPF deve ter exatamente 11 digitos')

    dv1 = sum([int(value[i]) * (10-i) for i in range(0, 9)]) * 10 % 11
    dv2 = sum([int(value[i]) * (11-i) for i in range(0, 10)]) * 10 % 11
    dv1 = dv1 if dv1 != 10 else 0
    dv2 = dv2 if dv2 != 10 else 0

    if value[-2:] != "%d%d" % (dv1, dv2):
        raise DVException('O dígito verificador informado está inválido')


def validate_cnpj(unmasked_value, *args, **kwargs):
    value = only_digits(unmasked_value)

    if len(value) != 14:
        raise MaskException('O CNPJ ter exatamente 14 digitos')

    c1 = (5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)
    c2 = (6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)
    dv1 = sum([int(value[i]) * c1[i] for i in range(0, 12)])
    dv2 = sum([int(value[i]) * c2[i] for i in range(0, 13)])
    dv1 = 11 - dv1 % 11 if dv1 % 11 > 2 else 0
    dv2 = 11 - dv2 % 11 if dv2 % 11 > 2 else 0
    dvs = "%d%d" % (dv1, dv2)

    if value[-2:] != dvs:
        raise DVException('O dígito verificador informado está inválido')


def validate_mask(mask):
    if not isinstance(mask, str):
        raise MaskNotStringException()

    if mask is None or mask.strip() == '':
        raise EmptyMaskException()

    unmask = only_digits(mask)

    if unmask.find('9') < 0:
        raise MaskWithoutDigitsException()

    if len(unmask) == len(mask):
        raise MaskWithoutSpecialCharsException()


def validate_mod11(unmasked_value, num_len, dvs_len):
    if num_len > 11:
        raise TooManyDigitsException()
    for v in range(dvs_len, 0, -1):
        num_dvs = num_len - v + 1
        dv = sum([i * int(unmasked_value[idx]) for idx, i in enumerate(range(num_dvs, 1, -1))]) % 11
        calculated_dv = '%d' % (11 - dv if dv >= 2 else 0,)
        if calculated_dv != unmasked_value[-v]:
            raise DVException()


def validate_dv_by_mask(value, mask, force=True, validate_dv=validate_mod11):
    if not isinstance(value, str):
        raise ValueError('O valor deve ser uma string')

    if value is None or value.strip() == '':
        raise ValueError('O valor não poder ser nulo ou uma string vazia')
    validate_mask(mask)
    unmask = only_digits(mask)
    masked_value = validate_masked_value(value, mask, force)
    unmasked_value = only_digits(masked_value)
    num_dvs = len([x for x in unmask if x == '0'])
    num_digits = len(unmask)
    validate_dv(unmasked_value, num_digits, num_dvs)
    return masked_value
