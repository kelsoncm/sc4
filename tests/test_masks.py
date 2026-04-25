import unittest

from sc4py.masks import (
    DVException,
    EmptyMaskException,
    MaskException,
    MaskNotStringException,
    MaskWithoutDigitsException,
    MaskWithoutSpecialCharsException,
    TooManyDigitsException,
    apply_mask,
    validate_dv_by_mask,
    validate_mask,
    validate_masked_value,
    validate_mod11,
)


class TestApplyMask(unittest.TestCase):
    def test_apply_mask_basic(self):
        self.assertEqual(apply_mask("12345678901", "999.999.999-99"), "123.456.789-01")
        self.assertEqual(apply_mask("12345678901", "###.###.###-##"), "123.456.789-01")
        self.assertEqual(apply_mask("1", "##-##"), "00-01")
        self.assertEqual(apply_mask("0000000", "999-9999"), "000-0000")

    def test_apply_mask_with_letters(self):
        self.assertEqual(apply_mask("abc1234567", "###-####"), "123-4567")

    def test_apply_mask_invalid_length(self):
        with self.assertRaises(MaskException):
            apply_mask("123", "999.999.999-99")


class TestValidateMaskedValue(unittest.TestCase):
    def test_validate_masked_value_non_digit_in_digit_position(self):
        # Máscara espera dígito, mas valor tem letra na posição, usando force=False
        with self.assertRaises(MaskException):
            validate_masked_value("123.A56.789-01", "###.###.###-##", force=False)

    def test_validate_masked_value_valid(self):
        self.assertEqual(validate_masked_value("12345678901", "###.###.###-##"), "123.456.789-01")
        self.assertEqual(validate_masked_value("123.456.789-01", "###.###.###-##", force=False), "123.456.789-01")

    def test_validate_masked_value_invalid(self):
        with self.assertRaises(MaskException):
            validate_masked_value("1234567890", "###.###.###-##")
        with self.assertRaises(MaskException):
            validate_masked_value("123.456.789-0", "###.###.###-##", force=False)


class TestValidateMask(unittest.TestCase):
    def test_valid_mask(self):
        # Mask with digits and special chars
        validate_mask("###.###-##")
        validate_mask("999-9999")

    def test_empty_mask(self):
        with self.assertRaises(EmptyMaskException):
            validate_mask("")
        with self.assertRaises(EmptyMaskException):
            validate_mask("   ")

    def test_mask_without_digits(self):
        with self.assertRaises(MaskWithoutDigitsException):
            validate_mask("...---...")

    def test_mask_without_special_chars(self):
        with self.assertRaises(MaskWithoutSpecialCharsException):
            validate_mask("999999")
        with self.assertRaises(MaskWithoutSpecialCharsException):
            validate_mask("###")

    def test_mask_not_string(self):
        with self.assertRaises(MaskNotStringException):
            validate_mask(123)


class TestValidateMod11(unittest.TestCase):
    def test_valid_mod11(self):
        # For num_len <= 11, valid DV at the end
        # Example: 12345678909 (CPF válido)
        validate_mod11("12345678909", 11, 2)

    def test_invalid_mod11(self):
        # Invalid DV
        with self.assertRaises(DVException):
            validate_mod11("12345678901", 11, 2)

    def test_too_many_digits(self):
        with self.assertRaises(TooManyDigitsException):
            validate_mod11("123456789012", 12, 2)


class TestValidateDvByMask(unittest.TestCase):
    def test_valid_dv_by_mask(self):
        # Mask with two DVs at the end (CPF, zeros as DV)
        self.assertEqual(validate_dv_by_mask("12345678909", "#########00"), "12345678909")

    def test_invalid_dv_by_mask(self):
        # Valor com DV inválido (último dígito alterado)
        with self.assertRaises(DVException):
            validate_dv_by_mask("12345678908", "#########00")

    def test_invalid_value_type(self):
        with self.assertRaises(ValueError):
            validate_dv_by_mask(12345678909, "###.###.###-##")

    def test_empty_value(self):
        with self.assertRaises(ValueError):
            validate_dv_by_mask("", "###.###.###-##")

    def test_invalid_mask(self):
        with self.assertRaises(MaskWithoutDigitsException):
            validate_dv_by_mask("12345678909", "...---...")
