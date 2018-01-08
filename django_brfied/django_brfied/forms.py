# -*- coding: utf-8 -*-
"""
BR-specific Form helpers


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
from django.forms import ValidationError
from django.forms.fields import CharField
from python_brfied import validate_dv_by_mask, validate_mask, validate_mod11, validate_cnpj
from python_brfied import only_digits, apply_mask
from python_brfied import CPF_MASK, CNPJ_MASK, CEP_MASK
from python_brfied import ValidationException

__all__ = ['MaskField', 'CPFField', 'CNPJField', 'CEPField', ]

__author__ = 'Kelson da Costa Medeiros <kelsoncm@gmail.com>'


class MaskField(CharField):
    """
    Um campo de formulário que valida um número mascarado genérico (CPF, CNPJ, Processo, Agencia, Conta-Corrente, ).
    Informe a máscara no argumento mask. Obrigatório.
    Se desejar obrigar que o valor venha com máscara informe mask_required=True. Opcional, default = False.
    Se desejar forçar a máscara para valores imcompletos informe mask_forced=True. Opcional, default = True.
    Ainda não suporta máscaras multiplas (CNPF).
    Ainda não suporta escolher o módulo.
    """

    def __init__(self, mask, mask_forced=True, mask_required=False, *args, **kwargs):
        if mask_forced and mask_required:
            raise ValidationException('Os argumentos mask_forced e mask_required são excludentes')
        validate_mask(mask)

        self.mask_required = mask_required
        self.mask_forced = mask_forced
        self.mask = mask
        self.validator = validate_mod11
        kwargs['max_length'] = len(mask)
        kwargs['min_length'] = len(mask) if mask_required or mask_forced else len(only_digits(mask))
        super(MaskField, self).__init__(*args, **kwargs)

    def clean(self, value):
        """
        O valor pode ou não ter máscara.

        :parameter value Valor a ser validado
        """
        try:
            if value in self.empty_values:
                return super(MaskField, self).clean(value)
            if self.mask_forced:
                value = super(MaskField, self).clean(apply_mask(value, self.mask))
            else:
                value = super(MaskField, self).clean(value)
            return self.clean_mask(value)
        except ValidationException as e:
            raise ValidationError(e.message)

    def clean_mask(self, value):
        if self.mask_required:
            result = validate_dv_by_mask(only_digits(value), self.mask, False, validate_dv=self.validator)
            if result != value:
                raise ValidationException('O campos tem que ser informado com máscara')
            return value
        else:
            return validate_dv_by_mask(value, self.mask, self.mask_forced, validate_dv=self.validator)

    def widget_attrs(self, widget):
        attrs = super(MaskField, self).widget_attrs(widget)
        attrs.update({'mask': str(self.mask)})
        return attrs


class CPFField(MaskField):
    """
    Um campo de formulário que valida o número do CPF.

    See: http://en.wikipedia.org/wiki/Cadastro_de_Pessoas_F%C3%ADsicas
    """
    def __init__(self, mask_forced=True, mask_required=False, *args, **kwargs):
        super(CPFField, self).__init__(CPF_MASK, mask_forced, mask_required, *args, **kwargs)


class CNPJField(MaskField):
    """
    Um campo de formulário que valida o número do CNPJ.

    See: http://en.wikipedia.org/wiki/National_identification_number#Brazil
    """
    def __init__(self, mask_forced=True, mask_required=False, *args, **kwargs):
        super(CNPJField, self).__init__(CNPJ_MASK, mask_forced, mask_required, *args, **kwargs)
        self.validator = validate_cnpj


class CEPField(MaskField):
    """
    Um campo de formulário que valida o número do CEP.
    """
    def __init__(self, mask_forced=True, mask_required=False, *args, **kwargs):
        super(CEPField, self).__init__(CEP_MASK, mask_forced, mask_required, *args, **kwargs)
