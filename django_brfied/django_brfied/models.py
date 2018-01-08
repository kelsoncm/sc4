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
from django.db.models import Model, CharField
from django.db.models import ForeignKey as OriginalForeignKey, ManyToManyField as OriginalManyToManyField
from python_brfied import validate_dv_by_mask, validate_mask, validate_mod11, validate_cnpj
from python_brfied import only_digits, apply_mask, ValidationException
from python_brfied import CPF_MASK, CNPJ_MASK, CEP_MASK, RegiaoChoices
from python_brfied import SexoChoices
from django_brfied.django_brfied import forms
from django_brfied.django_brfied.validators import CPFValidator

# __all__ = ['MaskField', 'CPFField', 'CNPJField', 'CEPField', 'UFField', 'UnidadeFederativa', 'ForeignKey', 'Sexo']

__author__ = 'Kelson da Costa Medeiros <kelsoncm@gmail.com>'


class MaskField(CharField):
    description = "String with mask %(mask)"

    def __init__(self, verbose_name='', mask='', mask_stored=False, *args, **kwargs):
        self.mask, self.mask_stored = mask, mask_stored
        self.validator = validate_mod11
        kwargs['max_length'] = len(mask) if mask_stored else len(only_digits(mask))
        validate_mask(self.mask)
        super(MaskField, self).__init__(verbose_name, *args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(MaskField, self).deconstruct()
        if self.mask:
            kwargs['mask'] = self.mask
        if self.mask_stored:
            kwargs['mask_stored'] = self.mask_stored
        kwargs['max_length'] = len(self.mask) if self.mask_stored else len(only_digits(self.mask))
        return name, path, args, kwargs

    def from_db_value(self, value, *args, **kwargs):
        try:
            if value is None:
                return value
            return apply_mask(only_digits(value), self.mask)
        except ValidationException as e:
            raise ValidationError(e.message)

    def get_db_prep_value(self, value, connection, prepared=False):
        try:
            value = super(MaskField, self).get_db_prep_value(value, connection, prepared)
            if value is None:
                return None
            return apply_mask(only_digits(value), self.mask) if self.mask_stored else only_digits(value)
        except ValidationException as e:
            raise ValidationError(e.message)

    def validate(self, value, model_instance):
        super(MaskField, self).validate(value, model_instance)
        try:
            validate_dv_by_mask(value, self.mask, validate_dv=self.validator)
        except ValidationException as e:
            raise ValidationError(e.message)


class CPFField(MaskField):
    description = "CPF field"

    def __init__(self, max_length=11, validators=[CPFValidator()], *args, **kwargs):
        kwargs['mask'] = CPF_MASK
        kwargs['max_length'] = max_length
        kwargs['validators'] = validators
        super(CPFField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = kwargs.copy()
        defaults['form_class'] = forms.CPFField
        return super(CPFField, self).formfield(**defaults)


class CNPJField(MaskField):
    description = "CNPJ field"

    def __init__(self, *args, **kwargs):
        kwargs['mask'] = CNPJ_MASK
        super(CNPJField, self).__init__(*args, **kwargs)
        self.validator = validate_cnpj

    def formfield(self, **kwargs):
        defaults = kwargs.copy()
        defaults['form_class'] = forms.CNPJField
        return super(CNPJField, self).formfield(**defaults)


class CEPField(MaskField):
    description = "CEP field"

    def __init__(self, verbose_name='CEP', mask=CEP_MASK, mask_stored=True, *args, **kwargs):
        super(CEPField, self).__init__(verbose_name, mask, mask_stored, *args, **kwargs)

    def formfield(self, **kwargs):
        defaults = kwargs.copy()
        defaults['form_class'] = forms.CEPField
        return super(CEPField, self).formfield(**defaults)


class ForeignKey(OriginalForeignKey):

    def __init__(self, verbose_name, to, on_delete=None, related_name=None, related_query_name=None,
                 limit_choices_to=None, parent_link=False, to_field=None, db_constraint=True, **kwargs):
        kwargs['verbose_name'] = verbose_name
        super(ForeignKey, self).__init__(to, on_delete, related_name, related_query_name, limit_choices_to, parent_link,
                                         to_field, db_constraint, **kwargs)


class ManyToManyField(OriginalManyToManyField):

    def __init__(self, verbose_name, to, related_name=None, related_query_name=None, limit_choices_to=None,
                 symmetrical=None, through=None, through_fields=None, db_constraint=True, db_table=None, swappable=True,
                 **kwargs):
        super(ManyToManyField, self).__init__(to, related_name, related_query_name, limit_choices_to, symmetrical,
                                              through, through_fields, db_constraint, db_table, swappable,
                                              verbose_name=verbose_name, **kwargs)


class SexoField(CharField):
    description = "Sex"

    def __init__(self, verbose_name='Sexo', max_length=1, choices=SexoChoices.CHOICES, *args, **kwargs):
        super(SexoField, self).__init__(verbose_name=verbose_name, max_length=max_length, choices=choices,
                                        *args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(SexoField, self).deconstruct()
        kwargs['max_length'] = 1
        kwargs['choices'] = SexoChoices.CHOICES
        return name, path, args, kwargs


class URL(CharField):
    description = "Sex"

    def __init__(self, verbose_name='Sexo', max_length=1, choices=SexoChoices.CHOICES, *args, **kwargs):
        super(SexoField, self).__init__(verbose_name=verbose_name, max_length=max_length, choices=choices,
                                        *args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(SexoField, self).deconstruct()
        kwargs['max_length'] = 1
        kwargs['choices'] = SexoChoices.CHOICES
        return name, path, args, kwargs


class UnidadeFederativa(Model):
    sigla = CharField('Sigla', max_length=2, primary_key=True)
    codigo = CharField('Código', max_length=2, unique=True)
    nome = CharField('Nome', max_length=250)
    regiao = CharField('Região', max_length=2, choices=RegiaoChoices.CHOICES)

    class Meta:
        verbose_name = 'Unidade federativa'
        verbose_name_plural = 'Unidades federativas'
        ordering = ['nome']

    def __str__(self):
        return '%s (%s)' % (self.nome, self.sigla, )


class UFField(ForeignKey):
    def __init__(self, verbose_name='UF', to=UnidadeFederativa, on_delete=None, related_name=None,
                 related_query_name=None, limit_choices_to=None, parent_link=False, to_field=None,
                 db_constraint=True, **kwargs):
        super(UFField, self).__init__(verbose_name, to, on_delete, related_name, related_query_name, limit_choices_to,
                                      parent_link, to_field, db_constraint, **kwargs)


class Municipio(Model):
    codigo = CharField('Código', max_length=6, primary_key=True)
    nome = CharField('Código', max_length=255)
    uf = UFField()

    class Meta:
        verbose_name = 'Município'
        verbose_name_plural = 'Municípios'
        ordering = ['nome']

    def __str__(self):
        return '%s/%s' % (self.nome, self.uf_id, )


class MunicipioField(ForeignKey):
    def __init__(self, verbose_name='Município', to=Municipio, on_delete=None, related_name=None,
                 related_query_name=None, limit_choices_to=None, parent_link=False, to_field=None,
                 db_constraint=True, **kwargs):
        super(MunicipioField, self).__init__(verbose_name, to, on_delete, related_name, related_query_name,
                                             limit_choices_to, parent_link, to_field, db_constraint, **kwargs)
