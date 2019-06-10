# Python BRfied

Why I create BRfied? Because localflavors dont validate user data and
dont apply a mask on inputs.


## Data types

* [x] Estado Civil
* [x] Raça
* [x] Sexo
* [x] Sexo opcional
* [x] Zona de habitação
* [x] Região geopolítica
* [x] Sim/Não
* [x] Sim/Não opcional 
* [x] Necessidade especial
* [x] Unidade federativa


## Validações e formatações

* [x] validate_masked_value
* [x] validate_cpf
* [x] validate_cnpj
* [x] validate_mask
* [x] validate_mod11
* [x] validate_dv_by_mask
* [ ] CEP
* [ ] Data
* [ ] Hora
* [ ] Data e hora
* [ ] CNES
* [ ] CNS
* [ ] Protocolo integrado (https://protocolointegrado.gov.br/Protocolo/projeto.jsf)
* [ ] Protocolo justiça (https://www.conjur.com.br/2009-jan-23/cnj-define-padrao-numeracao-processos-todos-tribunais http://www.stf.jus.br/portal/cms/verTexto.asp?servico=processoPeticaoEletronica&pagina=Informacoes_gerais_apos_desligamento_v1)
* [ ] PJe
* [ ] Linha digitável de boleto
* [ ] Código de barra de boleto
* [ ] Linha digitável de título
* [ ] Código de barra de título
* [ ] Nota fiscal eletrônica
* [ ] Código de município do IBGE (https://github.com/chinnonsantos/sql-paises-estados-cidades https://concla.ibge.gov.br/classificacoes/por-tema/codigo-de-areas/codigo-de-areas)
* [ ] 


## Funções

* [x] str2bool
* [x] percentage
* [x] instantiate_class
* [x] build_chain
* [x] only_digits
* [x] apply_mask


## Sync HTTP requests shortcuts

* [x] requests_get
* [x] get_json
* [x] get_zip
* [x] get_zip_content
* [x] get_zip_csv_content
* [x] get_zip_fwf_content


## Classes
* [x] BaseHandler
* [x] BaseDirector


## ZIP shortcuts

* [x] unzip_content
* [x] unzip_csv_content
* [x] unzip_fwf_content


## LICENSE

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

