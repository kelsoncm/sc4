# -*- coding: utf-8 -*-
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
from __future__ import unicode_literals
import re


__author__ = 'Kelson da Costa Medeiros <kelsoncm@gmail.com>'


CPF_MASK = '999.999.999-00'
CPF_RE = re.compile(r'^(\d{3})\.(\d{3})\.(\d{3})-(\d{2})$')

CNPJ_MASK = '99.999.999.999/9999-00'
CNPJ_RE = re.compile('^(\d{2})[.-]?(\d{3})[.-]?(\d{3})/(\d{4})-(\d{2})$')

CEP_MASK = '99999-999'
CEP_RE = '^\d{5}-\d{3}$'

PROCESSO_MASK = '9999999-99.9999.9.99.9999'
PROCESSO_RE = re.compile('^(\d{7})-?(\d{2})\.?(\d{4})\.?(\d)\.?(\d{2})\.?(\d{4})$')



class ValidationException(Exception):
    pass


class MaskException(ValidationException):
    def __init__(self):
        super(MaskException, self).__init__('Valor informado não está no formato correto')


class DVException(ValidationException):
    def __init__(self):
        super(DVException, self).__init__('Valor incorreto. Dígito verifcador inconsistente.')


class MaskWithoutDigitsException(ValidationException):
    def __init__(self):
        super(DVException, self).__init__('A máscara não tem dígitos')


class MaskWithoutDVException(ValidationException):
    def __init__(self):
        super(DVException, self).__init__('A máscara não tem dígitos verificador')


class MaskWithoutSpecialCharsException(ValidationException):
    def __init__(self):
        super(DVException, self).__init__('A máscara só contém dígitos')


def only_digits(seq):
    return filter(type(seq).isdigit, seq)


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


def validate_mod11(unmasked_value, num_digits, num_dvs):
    for v in range(num_dvs, 0, -1):
        num_digito = num_digits - v + 1
        dv = sum([i * int(unmasked_value[idx]) for idx, i in enumerate(range(num_digito, 1, -1))]) % 11
        calculated_dv = '%d' % (11 - dv if dv >= 2 else 0,)
        if calculated_dv != unmasked_value[-v]:
            raise DVException()


def validate_mask(mask):
    unmask = only_digits(mask)

    if unmask.find('9') < 0:
        raise MaskWithoutDigitsException()

    if unmask.find('0') < 0:
        raise MaskWithoutDVException()

    if len(unmask) == len(mask):
        raise MaskWithoutSpecialCharsException()


def validate_dv_by_mask(value, mask, force=True, validata_dv=validate_mod11):
    validate_mask(mask)
    unmask = only_digits(mask)
    masked_value = validate_masked_value(value, mask, force)
    unmasked_value = only_digits(masked_value)
    num_dvs = len([x for x in unmask if x == '0'])
    num_digits = len(unmask)
    validata_dv(unmasked_value, num_digits, num_dvs)
    return masked_value
