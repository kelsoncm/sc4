from unittest import TestCase
from enum import Enum
from python_brfied import str2bool, percentage
from python_brfied import instantiate_class, build_chain
from python_brfied import unzip_content, unzip_csv_content, FileNotFoundInZipError
from python_brfied import BaseHandler, BaseDirector
from python_brfied.choices import to_choice, UnidadeFederativaEnum
from python_brfied.env import env, env_as_list, env_as_list_of_maps, env_as_bool
from python_brfied.exceptions import MaskException, DVException, EmptyMaskException, MaskNotStringException, \
    MaskWithoutDigitsException, MaskWithoutSpecialCharsException, TooManyDigitsException
from python_brfied.validations import only_digits, apply_mask, validate_masked_value, validate_cpf, validate_cnpj
from python_brfied.validations import validate_mask, validate_mod11, validate_dv_by_mask
from python_brfied.datetime import now, now_str, this_month, others_months


class TestBaseHandler(BaseHandler):
    def handle(self, inc, *args, **kwargs):
        if self._successor:
            return self._successor.handle(inc+1)
        return inc+1


class TestPythonBrfiedInit(TestCase):

    def test_str2bool(self):
        self.assertTrue(str2bool(True))
        self.assertTrue(str2bool('True'))
        self.assertTrue(str2bool('true'))
        self.assertTrue(str2bool('TRUE'))
        self.assertTrue(str2bool('verdade'))
        self.assertTrue(str2bool('Verdade'))
        self.assertTrue(str2bool('Yes'))
        self.assertTrue(str2bool('yes'))
        self.assertTrue(str2bool('YES'))
        self.assertTrue(str2bool('Sim'))
        self.assertTrue(str2bool('sim'))
        self.assertTrue(str2bool('SIM'))
        self.assertTrue(str2bool('T'))
        self.assertTrue(str2bool('t'))
        self.assertTrue(str2bool('v'))
        self.assertTrue(str2bool('V'))
        self.assertTrue(str2bool('Y'))
        self.assertTrue(str2bool('y'))
        self.assertTrue(str2bool('s'))
        self.assertTrue(str2bool('S'))
        self.assertTrue(str2bool('1'))
        self.assertTrue(str2bool(1))

        self.assertFalse(str2bool(False))
        self.assertFalse(str2bool('False'))
        self.assertFalse(str2bool('false'))
        self.assertFalse(str2bool('FALSE'))
        self.assertFalse(str2bool('Falso'))
        self.assertFalse(str2bool('falso'))
        self.assertFalse(str2bool('FALSO'))
        self.assertFalse(str2bool('No'))
        self.assertFalse(str2bool('no'))
        self.assertFalse(str2bool('NO'))
        self.assertFalse(str2bool('Nao'))
        self.assertFalse(str2bool('nao'))
        self.assertFalse(str2bool('NAO'))
        self.assertFalse(str2bool('Não'))
        self.assertFalse(str2bool('não'))
        self.assertFalse(str2bool('NÃO'))
        self.assertFalse(str2bool('F'))
        self.assertFalse(str2bool('f'))
        self.assertFalse(str2bool('N'))
        self.assertFalse(str2bool('n'))
        self.assertFalse(str2bool('0'))
        self.assertFalse(str2bool(0))

        self.assertIsNone(str2bool(None))
        self.assertIsNone(str2bool(''))
        self.assertIsNone(str2bool(' '))

        self.assertRaises(ValueError, str2bool, 2)

    def test_percentage(self):
        self.assertEqual(100, percentage(1, 1))
        self.assertEqual(0.0, percentage(0, 0))

    def test_instantiate_class(self):
        self.assertIsInstance(instantiate_class('python_brfied.BaseHandler', None), BaseHandler)
        self.assertIsInstance(instantiate_class('python_brfied.BaseDirector', []), BaseDirector)

    def test_build_chain(self):
        first = build_chain(['test_init.TestBaseHandler', 'test_init.TestBaseHandler'])
        self.assertIsNotNone(first)
        self.assertIsNone(first.on_start())
        self.assertIsInstance(first, TestBaseHandler)
        self.assertIsNone(first.on_stop())
        self.assertEqual(2, first.handle(0))
        base_handler = BaseHandler()
        self.assertIsNotNone(base_handler)
        self.assertRaises(NotImplementedError, base_handler.handle)

    def test_unzip_content(self):
        expected = "codigo;nome\n1;um\n2;Dois\n3;três\n"
        expected_binary = b'codigo;nome\n1;um\n2;Dois\n3;tr\xc3\xaas\n'
        expected_latin1 = 'codigo;nome\n1;um\n2;Dois\n3;trÃªs\n'
        with open("assets/file01.zip", "rb") as f:
            binary = f.read()
        self.assertEqual(expected, unzip_content(binary))
        self.assertEqual(expected, unzip_content(binary, 0))
        self.assertEqual(expected, unzip_content(binary, 'file.csv'))
        self.assertRaises(FileNotFoundInZipError, unzip_content, binary, 'file2.csv')
        self.assertRaises(FileNotFoundInZipError, unzip_content, binary, 1)

        self.assertEqual(expected_binary, unzip_content(binary, encoding=None))
        self.assertEqual(expected_latin1, unzip_content(binary, encoding='latin_1'))
        self.assertRaises(UnicodeDecodeError, unzip_content, binary, encoding='ascii')

    def test_unzip_csv_content(self):
        with open("assets/file01.zip", "rb") as f:
            content = unzip_csv_content(f.read(), delimiter=';')
            expected = [{"codigo": '1', 'nome': 'um'}, {"codigo": '2', 'nome': 'Dois'}, {"codigo": '3', 'nome': 'três'}]
            self.assertListEqual(expected, content)

    def test_BaseDirector(self):
        base_director = BaseDirector(['test_init.TestBaseHandler', 'test_init.TestBaseHandler'])
        self.assertIsInstance(base_director._first_loader, TestBaseHandler)
        self.assertEqual(2, base_director._first_loader.handle(0))
        # self.assertIsNone(BaseDirector()._first_loader)


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


class TestPythonBrfiedEnv(TestCase):

    def test_env(self):
        self.assertEqual('ASDF', env('DUMMY_ENV', 'ASDF'))

    def test_env_as_list(self):
        self.assertListEqual([], env_as_list('DUMMY_ENV'))
        self.assertListEqual([], env_as_list('DUMMY_ENV', ''))
        self.assertListEqual([], env_as_list('DUMMY_ENV', ' '))

        self.assertListEqual(['a'], env_as_list('DUMMY_ENV', 'a'))
        self.assertListEqual(['a', 'b'], env_as_list('DUMMY_ENV', 'a,b'))

        self.assertListEqual(['a', 'b'], env_as_list('DUMMY_ENV', 'a;b', delimiter=';'))

    def test_env_as_list_of_maps(self):
        self.assertListEqual([], env_as_list_of_maps('DUMMY_ENV', 'K'))
        self.assertListEqual([], env_as_list_of_maps('DUMMY_ENV', 'K', ''))
        self.assertListEqual([], env_as_list_of_maps('DUMMY_ENV', 'K', ' '))

        self.assertListEqual([{'K': 'a'}], env_as_list_of_maps('DUMMY_ENV', 'K', 'a'))
        self.assertListEqual([{'K': 'a'}, {'K': 'b'}], env_as_list_of_maps('DUMMY_ENV', 'K', 'a,b'))

        self.assertListEqual([{'K': 'a'}, {'K': 'b'}], env_as_list_of_maps('DUMMY_ENV', 'K', 'a;b', delimiter=';'))

    def test_env_as_bool(self):
        self.assertTrue(env_as_bool('DUMMY_ENV', 'true'))
        self.assertTrue(env_as_bool('DUMMY_ENV', True))

        self.assertFalse(env_as_bool('DUMMY_ENV', 'FALSE'))
        self.assertFalse(env_as_bool('DUMMY_ENV', False))

        self.assertIsNone(env_as_bool('DUMMY_ENV'))
        self.assertIsNone(env_as_bool('DUMMY_ENV', None))
        self.assertIsNone(env_as_bool('DUMMY_ENV', ' '))


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


class TestPythonBrfiedDatetime(TestCase):

    def test_now_str(self):
        self.assertEqual(now().strftime("%d-%m-%Y %H:%M:%S"), now_str())

    def test_this_month(self):
        self.assertEqual(now().month, this_month())

    def test_others_months(self):
        t = this_month()
        self.assertEqual([m for m in range(1, 13) if m != t], others_months())
