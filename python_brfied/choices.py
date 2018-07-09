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

from enum import Enum, EnumMeta


def to_choice(*args):
    result = []
    for x in args:
        if isinstance(x, EnumMeta):
            result += to_choice(*[y for y in x])
        elif isinstance(x, Enum) and hasattr(x, 'description'):
            result += [(x.value, x.description)]
        elif isinstance(x, Enum) and not hasattr(x, 'description'):
            result += [(x.value, x.value)]
        else:
            result += [(x, x)]
    return result


class EstadoCivilEnum(Enum):
    SOLTEIRO = 'Solteiro(a)'
    CASADO = 'Casado(a)'
    DIVORCIADO = 'Divorciado(a)'
    SEPARADO = 'Separado(a)'
    VIUVO = 'Viúvo(a)'
    UNIAO_ESTAVEL = 'União estável'
EstadoCivilEnum.CHOICES = to_choice(EstadoCivilEnum)


class RacaEnum(Enum):
    AMARELO = 'Amarelo(a)'
    BRANCO = 'Branco(a)'
    INDIGENA = 'Indígena'
    PARDO = 'Pardo(a)'
    PRETO = 'Preto(a)'
    NAO_DECLARADO = 'Não declarado'
RacaEnum.CHOICES = to_choice(RacaEnum)


class SexoDeclaradoEnum(Enum):
    SEXO_FEMININO = 'F'
    SEXO_MASCULINO = 'M'
SexoDeclaradoEnum.SEXO_FEMININO.description = 'Feminino'
SexoDeclaradoEnum.SEXO_MASCULINO.description = 'Masculino'
SexoDeclaradoEnum.SEXO_DECLARADO_CHOICES = to_choice(SexoDeclaradoEnum)
SexoDeclaradoEnum.CHOICES = to_choice(SexoDeclaradoEnum)


class SexoEnum(Enum):
    SEXO_FEMININO = SexoDeclaradoEnum.SEXO_FEMININO.value
    SEXO_MASCULINO = SexoDeclaradoEnum.SEXO_MASCULINO.value
    SEXO_NAO_DECLARADO = 'N'
SexoEnum.SEXO_FEMININO.description = SexoDeclaradoEnum.SEXO_FEMININO.description
SexoEnum.SEXO_MASCULINO.description = SexoDeclaradoEnum.SEXO_MASCULINO.description
SexoEnum.SEXO_NAO_DECLARADO.description = 'Não declarado'
SexoEnum.CHOICES = to_choice(SexoEnum)


class ZonaEnum(Enum):
    URBANA = 'Urbana'
    RURAL = 'Rural'
ZonaEnum.CHOICES = to_choice(ZonaEnum)


class RegiaoEnum(Enum):
    NORTE = 'N'
    NORDESTE = 'NE'
    SUDESTE = 'SE'
    SUL = 'S'
    CENTRO_OESTE = 'CO'
RegiaoEnum.NORTE.description = 'Norte'
RegiaoEnum.NORDESTE.description = 'Nordeste'
RegiaoEnum.SUDESTE.description = 'Sudeste'
RegiaoEnum.SUL.description = 'Sul'
RegiaoEnum.CENTRO_OESTE.description = 'Centro-oeste'
RegiaoEnum.CHOICES = to_choice(RegiaoEnum)


class SimNaoEnum(Enum):
    SIM = 'S'
    NAO = 'N'
SimNaoEnum.SIM.description = 'Sim'
SimNaoEnum.NAO.description = 'Não'
SimNaoEnum.CHOICES = to_choice(SimNaoEnum)


class SimNaoNaoDeclaradoEnum(Enum):
    SIM = SimNaoEnum.SIM.value
    NAO = SimNaoEnum.NAO.value
    NAO_DECLARADO = 'I'
SimNaoNaoDeclaradoEnum.SIM.description = 'Sim'
SimNaoNaoDeclaradoEnum.NAO.description = 'Não'
SimNaoNaoDeclaradoEnum.NAO_DECLARADO.description = 'Não declarado'
SimNaoNaoDeclaradoEnum.CHOICES = to_choice(SimNaoNaoDeclaradoEnum)


class NecessidadeEspecialEnum(Enum):
    CEGUEIRA = 'Cegueira'
    BAIXA_VISAO = 'Baixa visão'
    SURDEZ = 'Surdez'
NecessidadeEspecialEnum.CHOICES = to_choice(NecessidadeEspecialEnum)


class UnidadeFederativaEnum(Enum):
    AC = 'AC'
    AL = 'AL'
    AP = 'AP'
    AM = 'AM'
    BA = 'BA'
    CE = 'CE'
    DF = 'DF'
    ES = 'ES'
    GO = 'GO'
    MA = 'MA'
    MT = 'MT'
    MS = 'MS'
    MG = 'MG'
    PA = 'PA'
    PB = 'PB'
    PR = 'PR'
    PE = 'PE'
    PI = 'PI'
    RJ = 'RJ'
    RN = 'RN'
    RS = 'RS'
    RO = 'RO'
    RR = 'RR'
    SC = 'SC'
    SP = 'SP'
    SE = 'SE'
    TO = 'TO'
UnidadeFederativaEnum.AC.description = 'Acre'
UnidadeFederativaEnum.AL.description = 'Alagoas'
UnidadeFederativaEnum.AP.description = 'Amapá'
UnidadeFederativaEnum.AM.description = 'Amazonas'
UnidadeFederativaEnum.BA.description = 'Bahia'
UnidadeFederativaEnum.CE.description = 'Ceará'
UnidadeFederativaEnum.DF.description = 'Distrito Federal'
UnidadeFederativaEnum.ES.description = 'Espírito Santo'
UnidadeFederativaEnum.GO.description = 'Goiás'
UnidadeFederativaEnum.MA.description = 'Maranhão'
UnidadeFederativaEnum.MT.description = 'Mato Grosso'
UnidadeFederativaEnum.MS.description = 'Mato Grosso do Sul'
UnidadeFederativaEnum.MG.description = 'Minas Gerais'
UnidadeFederativaEnum.PA.description = 'Pará'
UnidadeFederativaEnum.PB.description = 'Paraíba'
UnidadeFederativaEnum.PR.description = 'Paraná'
UnidadeFederativaEnum.PE.description = 'Pernambuco'
UnidadeFederativaEnum.PI.description = 'Piauí'
UnidadeFederativaEnum.RJ.description = 'Rio de Janeiro'
UnidadeFederativaEnum.RN.description = 'Rio Grande do Norte'
UnidadeFederativaEnum.RS.description = 'Rio Grande do Sul'
UnidadeFederativaEnum.RO.description = 'Rondônia'
UnidadeFederativaEnum.RR.description = 'Roraima'
UnidadeFederativaEnum.SC.description = 'Santa Catarina'
UnidadeFederativaEnum.SP.description = 'São Paulo'
UnidadeFederativaEnum.SE.description = 'Sergipe'
UnidadeFederativaEnum.TO.description = 'Tocantins'
UnidadeFederativaEnum.AC.code = '12'
UnidadeFederativaEnum.AL.code = '27'
UnidadeFederativaEnum.AP.code = '16'
UnidadeFederativaEnum.AM.code = '13'
UnidadeFederativaEnum.BA.code = '29'
UnidadeFederativaEnum.CE.code = '23'
UnidadeFederativaEnum.DF.code = '53'
UnidadeFederativaEnum.ES.code = '32'
UnidadeFederativaEnum.GO.code = '52'
UnidadeFederativaEnum.MA.code = '21'
UnidadeFederativaEnum.MT.code = '51'
UnidadeFederativaEnum.MS.code = '50'
UnidadeFederativaEnum.MG.code = '31'
UnidadeFederativaEnum.PA.code = '15'
UnidadeFederativaEnum.PB.code = '25'
UnidadeFederativaEnum.PR.code = '41'
UnidadeFederativaEnum.PE.code = '26'
UnidadeFederativaEnum.PI.code = '22'
UnidadeFederativaEnum.RJ.code = '33'
UnidadeFederativaEnum.RN.code = '24'
UnidadeFederativaEnum.RS.code = '43'
UnidadeFederativaEnum.RO.code = '11'
UnidadeFederativaEnum.RR.code = '14'
UnidadeFederativaEnum.SC.code = '42'
UnidadeFederativaEnum.SP.code = '35'
UnidadeFederativaEnum.SE.code = '28'
UnidadeFederativaEnum.TO.code = '17'
UnidadeFederativaEnum.CHOICES = to_choice(UnidadeFederativaEnum)
UnidadeFederativaEnum.SIGLAS = [x.value for x in UnidadeFederativaEnum]
UnidadeFederativaEnum.NOMES = [x.description for x in UnidadeFederativaEnum]
UnidadeFederativaEnum.CODIGOS = [x.code for x in UnidadeFederativaEnum]
