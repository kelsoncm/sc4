# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.deconstruct import deconstructible
from python_brfied import validate_cpf


@deconstructible
class CPFValidator(object):
    message = 'Informe um email válido'
    code = 'invalid'

    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        return validate_cpf(value)

    def __eq__(self, other):
        return (
            isinstance(other, CPFValidator) and
            (self.message == other.message) and
            (self.code == other.code)
        )


class CPFAuthValidator:
    def validate(self, password, user=None):
        validate_cpf(user.username)

    def get_help_text(self):
        return 'Informe um CPF válido'
