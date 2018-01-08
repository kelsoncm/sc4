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
from django.db import models
from django.db.models import CharField, DateField
from python_brfied import UF_LIST
from python_brfied import ZonaChoices
from django_brfied.django_brfied.models import CEPField, UFField, MunicipioField


__author__ = 'Kelson da Costa Medeiros <kelsoncm@gmail.com>'


class EnderecoMixin(models.Model):
    endereco_logradouro = CharField('Logradouro', max_length=150, null=False, blank=False)
    endereco_numero = CharField('Número', max_length=150, null=False, blank=False)
    endereco_complemento = CharField('Complemento', max_length=150, null=True, blank=True)
    endereco_bairro = CharField('Bairro', max_length=150, null=False, blank=False)
    endereco_municipio = MunicipioField(null=False, blank=False)
    endereco_cep = CEPField(null=False, blank=False)
    endereco_referencia = CharField('Referência', max_length=150, null=False, blank=False)
    endereco_zona = CharField('Zona residencial', max_length=150, choices=ZonaChoices.CHOICES, null=False, blank=False)

    class Meta:
        abstract = True

    @property
    def endereco(self):
        return '%s, %s - %s, %s, %s' % \
               (self.endereco_logradouro, self.endereco_numero, self.endereco_complemento, self.endereco_bairro,
                self.endereco_municipio, )

    @property
    def enderecamento_correios(self):
        return '%s %s %s\n%s\n%s\n%s' % \
               (self.endereco_logradouro, self.endereco_numero, self.endereco_complemento, self.endereco_bairro,
                self.endereco_municipio, self.endereco_cep,)


class RegistroGeralMixin(models.Model):
    rg_numero = CharField('Número do RG', max_length=20, null=False, blank=False)
    rg_orgao = CharField('Órgão expedidor do RG', max_length=20, null=False, blank=False)
    rg_uf = UFField('UF de expedição do RG', max_length=2, choices=UF_LIST, null=False, blank=False)

    class Meta:
        abstract = True

    @property
    def rg(self):
        return '%s %s/%s' % (self.rg_numero, self.rg_orgao, self.rg_uf)


class NascimentoMixin(models.Model):
    nascimento_data = DateField('Data de nascimento', null=False, blank=False)
    nascimento_municipio = MunicipioField('Município de nascimento', max_length=150, null=False, blank=False)
    nascimento_pais = CharField('País de nascimento', max_length=150, null=False, blank=False)

    class Meta:
        abstract = True
