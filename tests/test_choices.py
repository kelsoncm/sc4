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
from unittest import TestCase
from enum import Enum
from python_brfied.choices import to_choice, UnidadeFederativaEnum


class TestPythonBrfiedChoices(TestCase):

    def test_to_choice(self):
        self.assertListEqual([('F', 'F'), ('M', 'M')], to_choice('F', 'M'))

        class Cenario01(Enum):
            F = 'F'
            M = 'M'
        self.assertListEqual([('F', 'F'), ('M', 'M')], to_choice(Cenario01))

        class Cenario02(Enum):
            F = 'F'
            M = 'M'
        Cenario02.F.description = 'Feminino'
        Cenario02.M.description = 'Masculino'
        self.assertListEqual([('F', 'Feminino'), ('M', 'Masculino')], to_choice(Cenario02))

    def test_ufs(self):
        uf_siglas = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR',
                     'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
        self.assertListEqual(uf_siglas, UnidadeFederativaEnum.SIGLAS)

        uf_nomes = ['Acre', 'Alagoas', 'Amapá', 'Amazonas', 'Bahia', 'Ceará', 'Distrito Federal', 'Espírito Santo',
                    'Goiás', 'Maranhão', 'Mato Grosso', 'Mato Grosso do Sul', 'Minas Gerais', 'Pará', 'Paraíba', 'Paraná', 'Pernambuco', 'Piauí', 'Rio de Janeiro', 'Rio Grande do Norte', 'Rio Grande do Sul', 'Rondônia', 'Roraima', 'Santa Catarina', 'São Paulo', 'Sergipe', 'Tocantins']
        self.assertListEqual(uf_nomes, UnidadeFederativaEnum.NOMES)

        uf_codigos = ['12', '27', '16', '13', '29', '23', '53', '32', '52', '21', '51', '50', '31', '15', '25', '41',
                      '26', '22', '33', '24', '43', '11', '14', '42', '35', '28', '17']
        self.assertListEqual(uf_codigos, UnidadeFederativaEnum.CODIGOS)
