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
from django.core.exceptions import ValidationError
from django.db.models import Field, CharField
from python_brfied import validate_dv_by_mask, only_digits, validate_mask, apply_mask
from python_brfied import CPF_MASK, CNPJ_MASK, CEP_MASK

__all__ = ['MaskField', 'CPFField', 'CNPJField', 'CEPField', ]

__author__ = 'Kelson da Costa Medeiros <kelsoncm@gmail.com>'


class MaskField(CharField):
    description = "String with mask %(mask)"

    def __init__(self, mask, mask_stored=False, mask_forced=True, mask_required=False, *args, **kwargs):
        if mask_forced and mask_required:
            raise ValidationError('O argumento mask_forced não pode ser combinado com mask_required.')
        if mask_stored and (not mask_forced or not mask_required):
            raise ValidationError('Se o argumento mask_stored for True o mask_forced ou o mask_required também '
                                  'deve ser True.')
        validate_mask(mask)

        self.mask_stored = mask_stored
        self.mask_required = mask_required
        self.mask_forced = mask_forced
        self.mask = mask
        max_length = len(mask) if mask_stored else len(only_digits(mask))
        min_length = max_length
        super(MaskField, self).__init__(max_length, min_length, *args, **kwargs)
    #
    # def db_type(self, connection):
    #     return 'varchar'

    def to_python(self, value, expression, connection, context):
        if value is None:
            return value
        return value if self.mask_forced else apply_mask(self.mask, value)


class CPFField(Field):
    description = "CPF field with mask_stored = %(mask_stored)"

    def __init__(self, mask_stored=False, mask_forced=True, mask_required=False, *args, **kwargs):
        super(CPFField, self).__init__(CPF_MASK, mask_stored, mask_forced, mask_required, *args, **kwargs)


class CNPJField(Field):
    description = "CNPJ field with mask_stored = %(mask_stored)"

    def __init__(self, mask_stored=False, mask_forced=True, mask_required=False, *args, **kwargs):
        super(CNPJField, self).__init__(CNPJ_MASK, mask_stored, mask_forced, mask_required, *args, **kwargs)


class CEPField(Field):
    description = "CEP field with mask_stored = %(mask_stored)"

    def __init__(self, mask_stored=False, mask_forced=True, mask_required=False, *args, **kwargs):
        super(CEPField, self).__init__(CEP_MASK, mask_stored, mask_forced, mask_required, *args, **kwargs)
