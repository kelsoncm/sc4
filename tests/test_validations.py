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
from python_brfied.exceptions import MaskException, DVException, EmptyMaskException, MaskNotStringException, \
    MaskWithoutDigitsException, MaskWithoutSpecialCharsException, TooManyDigitsException
from python_brfied.validations import only_digits, apply_mask, validate_masked_value, validate_cpf, validate_cnpj
from python_brfied.validations import validate_mask, validate_mod11, validate_dv_by_mask


class TestPythonBrfiedValidations(TestCase):

    def test_only_digits(self):
        self.assertEqual('123', only_digits('123'))
        self.assertEqual('12312312312', only_digits('123.123.123-12'))
        self.assertEqual('1234', only_digits('1.234-x'))
        self.assertEqual('', only_digits('-x'))
        self.assertEqual('', only_digits(''))

    def test_apply_mask(self):

        # valor perfeito com ou sem máscara
        self.assertEqual('1/2-3', apply_mask('123', '9/0-0'))
        self.assertEqual('12.345-678', apply_mask('12.345-678', '99.999-999'))
        self.assertEqual('12.345-678', apply_mask('12345678', '99.999-999'))

        # valor None com ou sem máscara
        self.assertRaises(AttributeError, apply_mask, None, '99.999-999')
        self.assertRaises(AttributeError, apply_mask, '01.234-567', None)

        # valor menor com ou sem máscara
        self.assertEqual('00.000-000', apply_mask('', '99.999-999'))
        self.assertEqual('01.234-567', apply_mask('01.234-567', '99.999-999'))
        self.assertEqual('01.234-567', apply_mask('1234567', '99.999-999'))

        # Valor maior com ou sem máscara
        self.assertRaises(MaskException, apply_mask, '123456789', '99.999-999')
        self.assertRaises(MaskException, apply_mask, '123.456-789', '99.999-999')

        # Máscara sem dígito na composição
        self.assertRaises(MaskException, apply_mask, '123.456-789', '')
        self.assertRaises(MaskException, apply_mask, '123.456-789', '.+-*/')

    def test_validate_masked_value(self):
        # valor perfeito com ou sem máscara
        self.assertEqual('1/2-3', validate_masked_value('123', '9/0-0'))
        self.assertEqual('12.345-678', validate_masked_value('12.345-678', '99.999-999'))
        self.assertEqual('12.345-678', validate_masked_value('12345678', '99.999-999'))

        # valor None com ou sem máscara
        self.assertRaises(AttributeError, validate_masked_value, None, '99.999-999')
        self.assertRaises(AttributeError, validate_masked_value, '01.234-567', None)

        # valor menor com ou sem máscara
        self.assertEqual('00.000-000', validate_masked_value('', '99.999-999'))
        self.assertEqual('01.234-567', validate_masked_value('01.234-567', '99.999-999'))
        self.assertEqual('01.234-567', validate_masked_value('1234567', '99.999-999'))

        # Valor maior com ou sem máscara
        self.assertRaises(MaskException, validate_masked_value, '123456789', '99.999-999')
        self.assertRaises(MaskException, validate_masked_value, '123.456-789', '99.999-999')

        # Máscara sem dígito na composição
        self.assertRaises(MaskException, validate_masked_value, '123.456-789', '')
        self.assertRaises(MaskException, validate_masked_value, '123.456-789', '.+-*/')


        # valor perfeito com máscara
        self.assertEqual('1/2-3', validate_masked_value('1/2-3', '9/0-0', False))

        # valor com máscara imperfeita
        self.assertRaises(MaskException, validate_masked_value, '', '99.999-999', False)
        self.assertRaises(MaskException, validate_masked_value, '12345678', '99.999-999', False)
        self.assertRaises(MaskException, validate_masked_value, '123456789', '99.999-999', False)
        self.assertRaises(MaskException, validate_masked_value, '1.234-567', '99.999-999', False)
        self.assertRaises(MaskException, validate_masked_value, ' 1.234-567', '99.999-999', False)
        self.assertRaises(MaskException, validate_masked_value, '123.456-7', '99.999-999', False)
        self.assertRaises(MaskException, validate_masked_value, '123.456-789', '99.999-999', False)

        # valor None
        self.assertRaises(TypeError, validate_masked_value, None, '99.999-999', False)
        self.assertRaises(TypeError, validate_masked_value, '01.234-567', None, False)

        # Máscara sem dígito na composição
        self.assertRaises(MaskException, validate_masked_value, '123.456-789', '', False)
        self.assertRaises(MaskException, validate_masked_value, '123.456-789', '.+-*/', False)

    def test_validate_cpf(self):
        self.assertIsNone(validate_cpf('11111111111'))
        self.assertIsNone(validate_cpf('111.111.111-11'))
        self.assertIsNone(validate_cpf('000.000.001-91'))

        self.assertRaises(DVException, validate_cpf, '000.000.001-81')
        self.assertRaises(MaskException, validate_cpf, '181')

    def test_validate_cnpj(self):
        self.assertIsNone(validate_cnpj('12.345.678/9000-05'))
        self.assertIsNone(validate_cnpj('12345678900005'))
        self.assertIsNone(validate_cnpj('00.000.000/0001-08'))
        self.assertIsNone(validate_cnpj('00000000000108'))
        self.assertIsNone(validate_cnpj('00000000000.108'))

        self.assertRaises(MaskException, validate_cnpj, '108')
        self.assertRaises(DVException, validate_cnpj, '00000000000109')
        self.assertIsNone(validate_cnpj('108'.zfill(14)))

    def test_validate_mod11(self):
        self.assertIsNone(validate_mod11('2615339', 7, 1))
        self.assertIsNone(validate_mod11('00000000191', 11, 1))
        self.assertIsNone(validate_mod11('12345678909', 11, 1))
        self.assertRaises(TooManyDigitsException, validate_mod11, '123456789012', 12, 1)
        self.assertRaises(DVException, validate_mod11, '2615339', 6, 1)
        self.assertRaises(DVException, validate_mod11, '2615339', 8, 1)

    def test_validate_mask(self):
        self.assertRaises(EmptyMaskException, validate_mask, '')
        self.assertRaises(MaskException, validate_mask, ' ')
        self.assertRaises(MaskException, validate_mask, None)
        self.assertRaises(MaskNotStringException, validate_mask, 1)
        self.assertRaises(MaskWithoutDigitsException, validate_mask, '.+-*/')
        self.assertRaises(MaskWithoutSpecialCharsException, validate_mask, '9999')
        self.assertRaises(MaskWithoutDigitsException, validate_mask, '00')

        self.assertIsNone(validate_mask('99999-999'))

    def test_validate_dv_by_mask(self):
        self.assertEqual('000.000.001-91', validate_dv_by_mask('000.000.001-91', '999.999.999-00'))
        self.assertEqual('000.000.001-91', validate_dv_by_mask('00000000191', '999.999.999-00'))
        self.assertRaises(ValueError, validate_dv_by_mask, None, '999.999.999-00')
        self.assertRaises(ValueError, validate_dv_by_mask, '', '999.999.999-00')
        self.assertRaises(ValueError, validate_dv_by_mask, ' ', '999.999.999-00')
        self.assertRaises(ValueError, validate_dv_by_mask, 1, '999.999.999-00')
        self.assertRaises(MaskNotStringException, validate_dv_by_mask, '00000000191', None)
