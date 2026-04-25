from sc4py.str import only_digits


class MaskException(Exception):
    """
    Exceção base para erros relacionados a máscaras.
    """

    pass


class EmptyMaskException(MaskException):
    """
    Exceção para máscara vazia ou nula.
    """

    pass


class DVException(MaskException):
    """
    Exceção para erro de dígito verificador (DV) inválido.
    """

    pass


class MaskWithoutDigitsException(MaskException):
    """
    Exceção para máscara sem dígitos ou placeholders de dígitos.
    """

    pass


class MaskWithoutSpecialCharsException(MaskException):
    """
    Exceção para máscara sem caracteres especiais (apenas dígitos/placeholders).
    """

    pass


class MaskNotStringException(MaskException):
    """
    Exceção para máscara que não é string.
    """

    pass


class TooManyDigitsException(MaskException):
    """
    Exceção para quantidade de dígitos acima do permitido.
    """

    pass


def apply_mask(value, mask):
    """
    Aplica uma máscara a um valor, inserindo caracteres especiais conforme o padrão.

    Args:
        value (str): Valor a ser mascarado.
        mask (str): Máscara no formato com dígitos (9, # ou 0) e separadores.

    Returns:
        str: Valor mascarado conforme a máscara.

    Raises:
        MaskException: Se o número de dígitos não corresponder ao esperado.

    Examples:
        >>> apply_mask('12345678901', '###.###.###-##')
        '123.456.789-01'
        >>> apply_mask('1', '##-##')
        '00-01'
    """
    unmask_len = len([m for m in mask if m.isdigit() or m == "#"])
    digits_only_value = only_digits(value)

    if len(digits_only_value) != unmask_len and len(digits_only_value) > 1:
        raise MaskException()

    zfill_value = digits_only_value.zfill(unmask_len)

    result = ""
    i = 0
    for m in mask:
        if m.isdigit() or m == "#":
            result += zfill_value[i]
            i += 1
        else:
            result += m
    return result


def validate_masked_value(value, mask, force=True):
    """
    Valida se um valor está de acordo com a máscara informada.

    Args:
        value (str): Valor a ser validado.
        mask (str): Máscara de validação.
        force (bool, opcional): Se True, aplica a máscara antes de validar. Padrão: True.

    Returns:
        str: Valor mascarado validado.

    Raises:
        MaskException: Se o valor não corresponder à máscara.

    Examples:
        >>> validate_masked_value('12345678901', '###.###.###-##')
        '123.456.789-01'
        >>> validate_masked_value('123.456.789-01', '###.###.###-##', force=False)
        '123.456.789-01'
    """
    masked_value = apply_mask(only_digits(value), mask) if force else value
    if len(mask) != len(masked_value):
        raise MaskException()

    for i in range(0, len(mask)):
        m = mask[i]
        v = masked_value[i]
        if (not m.isdigit() and m != "#" and m != v) or ((m.isdigit() or m == "#") and not v.isdigit()):
            raise MaskException()
    return masked_value


def validate_mask(mask):
    """
    Valida se a máscara é válida, contendo dígitos/placeholders e caracteres especiais.

    Args:
        mask (str): Máscara a ser validada.

    Returns:
        None

    Raises:
        MaskNotStringException: Se a máscara não for string.
        EmptyMaskException: Se a máscara for vazia.
        MaskWithoutDigitsException: Se não houver dígitos/placeholders.
        MaskWithoutSpecialCharsException: Se não houver caracteres especiais.

    Examples:
        >>> validate_mask('###.###-##')
        >>> validate_mask('999-9999')
    """
    if not isinstance(mask, str):
        raise MaskNotStringException()

    if mask is None or mask.strip() == "":
        raise EmptyMaskException()

    unmask = "".join(m for m in mask if m.isdigit() or m == "#")

    if unmask.find("9") < 0 and unmask.find("#") < 0 and unmask.find("0") < 0:
        raise MaskWithoutDigitsException()

    if len(unmask) == len(mask) and mask.find("0") < 0:
        raise MaskWithoutSpecialCharsException()


def validate_mod11(unmasked_value, num_len, dvs_len):
    """
    Valida dígitos verificadores (DV) usando o algoritmo módulo 11.

    Args:
        unmasked_value (str): Valor numérico sem máscara.
        num_len (int): Quantidade total de dígitos.
        dvs_len (int): Quantidade de dígitos verificadores (DV) no final.

    Returns:
        None

    Raises:
        TooManyDigitsException: Se num_len > 11.
        DVException: Se o DV calculado não corresponder ao informado.

    Examples:
        >>> validate_mod11('12345678909', 11, 2)  # CPF válido
        >>> validate_mod11('12345678901', 11, 2)  # DVException
    """
    if num_len > 11:
        raise TooManyDigitsException()
    for v in range(dvs_len, 0, -1):
        num_dvs = num_len - v + 1
        dv = sum([i * int(unmasked_value[idx]) for idx, i in enumerate(range(num_dvs, 1, -1))]) % 11
        calculated_dv = "%d" % (11 - dv if dv >= 2 else 0,)
        if calculated_dv != unmasked_value[-v]:
            raise DVException()


def validate_dv_by_mask(value, mask, force=True, validate_dv=validate_mod11):
    """
    Valida um valor mascarado e seus dígitos verificadores conforme a máscara.

    Args:
        value (str): Valor a ser validado.
        mask (str): Máscara com zeros ('0') indicando posições de DV.
        force (bool, opcional): Se True, aplica a máscara antes de validar. Padrão: True.
        validate_dv (callable, opcional): Função de validação de DV. Padrão: validate_mod11.

    Returns:
        str: Valor validado e mascarado.

    Raises:
        ValueError: Se value não for string ou for vazio.
        MaskException: Se a máscara for inválida.
        DVException: Se o DV for inválido.

    Examples:
        >>> validate_dv_by_mask('12345678909', '#########00')
        '12345678909'
        >>> validate_dv_by_mask('12345678908', '#########00')
        DVException
    """
    if not isinstance(value, str):
        raise ValueError("O valor deve ser uma string")

    if value is None or value.strip() == "":
        raise ValueError("O valor não poder ser nulo ou uma string vazia")
    validate_mask(mask)
    unmask = "".join(m for m in mask if m.isdigit() or m == "#")
    masked_value = validate_masked_value(value, mask, force)
    unmasked_value = only_digits(masked_value)
    num_dvs = len([x for x in unmask if x == "0"])
    num_digits = len(unmask)
    validate_dv(unmasked_value, num_digits, num_dvs)
    return masked_value
