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

__author__ = 'Kelson da Costa Medeiros <kelsoncm@gmail.com>'


class ValidationException(Exception):
    pass


class MaskException(ValidationException):
    def __init__(self, message='Valor informado não está no formato correto'):
        super(MaskException, self).__init__(message)


class EmptyMaskException(MaskException):
    def __init__(self, message='Nenhuma máscara informada'):
        super(EmptyMaskException, self).__init__(message)


class MaskNotStringException(MaskException):
    def __init__(self, message='A máscara não é uma string'):
        super(MaskNotStringException, self).__init__(message)


class DVException(ValidationException):
    def __init__(self, message='Valor incorreto. Dígito verifcador inconsistente.'):
        super(DVException, self).__init__(message)


class MaskWithoutDigitsException(ValidationException):
    def __init__(self, message='A máscara não tem dígitos 9'):
        super(MaskWithoutDigitsException, self).__init__(message)


class MaskWithoutSpecialCharsException(ValidationException):
    def __init__(self, message='A máscara só contém dígitos'):
        super(MaskWithoutSpecialCharsException, self).__init__(message)


class TooManyDigitsException(MaskException):
    def __init__(self, message='A quantidade de dígitos é muito grande'):
        super(TooManyDigitsException, self).__init__(message)
