# -*- coding: utf-8 -*-
"""Metadado das paginas de lacuna (indice, cartao, resumo e alerta).

Gerado por build/json/gera_paginas_2026_10_05.py a partir de
build/json/coleta_2026_10_05.json (local, fora do git). Editar o gerador, nao
este arquivo -- os numeros saem da coleta, nao da mao.

A data da apuracao nao aparece aqui: o marcador {DATA} e trocado no import
pelo valor de datas.DATA_LACUNAS, como manda a trava de datas.
"""

from datas import DATA_LACUNAS as _DT


def _d(x):
    if isinstance(x, str):
        return x.replace("{DATA}", _DT)
    if isinstance(x, list):
        return [_d(i) for i in x]
    if isinstance(x, tuple):
        return tuple(_d(i) for i in x)
    if isinstance(x, dict):
        return {k: _d(v) for k, v in x.items()}
    return x


EXTRA_LACUNAS = _d({'proprio_gnrh': {'nome': 'GnRH e gonadotrofinas — os análogos que têm bula',
                  'categoria': 'primaria',
                  'aprovado': 'parcial',
                  'tagline': 'Triptorrelina, leuprorrelina e gosserrelina têm 86, 124 e 125 ensaios de fase 3 '
                             'registrados, em câncer e fertilidade. Nos registros das cinco buscas, nenhum é sobre '
                             'recuperação depois de anabolizante',
                  'resumo': 'Cinco hormônios do eixo reprodutivo vendidos como peptídeo de pesquisa: os análogos de '
                            'GnRH triptorrelina, leuprorrelina, gosserrelina e histrelina, e a menotropina (hMG). Ao '
                            'contrário da maior parte deste site, os cinco são medicamentos com bula. E a bula '
                            'desmente a promessa comercial: o análogo de GnRH contínuo desliga o eixo, não reinicia — '
                            'é remédio de câncer de próstata e de mama.',
                  'alerta': 'Análogo de GnRH em uso contínuo produz castração química: é para isso que ele existe. '
                            'Usar esses princípios ativos para "recuperar" o eixo depois de anabolizante não tem '
                            'ensaio registrado que sustente, e o efeito descrito em bula é o oposto. Menotropina e '
                            'análogos de GnRH são medicamentos de prescrição, com indicação e monitoramento '
                            'definidos.'},
 'proprio_gh_miostatina': {'nome': 'GH e miostatina — o que ainda faltava',
                           'categoria': 'primaria',
                           'aprovado': 'nao',
                           'tagline': 'O PEG-MGF tem 5 artigos e 0 estudos. A folistatina vendida em frasco nunca foi '
                                      'testada em gente — o que existe em registro é terapia gênica. O ACE-031 parou '
                                      'por segurança',
                           'resumo': 'Os nomes do eixo do GH que ainda faltavam no site — GHRP-1, somatorrelina, '
                                     'grelina, PEG-MGF — e o outro lado do crescimento muscular, os inibidores de '
                                     'miostatina: folistatina 344 e 288 e ACE-031. O padrão é o de sempre, mais '
                                     'carregado: literatura de bancada, quase nada registrado em gente e, no único que '
                                     'chegou a ensaio de miostatina, parada por segurança.',
                           'alerta': 'Nenhum destes compostos tem produto registrado no Brasil para uso humano. O '
                                     'ACE-031 foi interrompido em crianças com distrofia muscular por sangramento '
                                     'nasal e vasos dilatados na pele — num ensaio feito para doença grave, não para '
                                     'ganho de massa. O que se compra com esses nomes é vendido como insumo de '
                                     'pesquisa, sem controle de pureza, esterilidade ou dose.'},
 'proprio_intestino': {'nome': 'Intestino — os análogos de GLP-2 e a larazotida',
                       'categoria': 'primaria',
                       'aprovado': 'parcial',
                       'tagline': 'A fase 3 dos análogos de GLP-2 é de síndrome do intestino curto, não de intestino '
                                  'permeável. O único ensaio de fase 3 da larazotida foi encerrado pelo patrocinador — '
                                  'e a busca por ela devolve registros de um remédio de doença de Fabry',
                       'resumo': 'Teduglutida, glepaglutida e apraglutida são análogos do GLP-2 desenvolvidos para a '
                                 'síndrome do intestino curto; a larazotida, para doença celíaca. Chegam à venda como '
                                 'peptídeo para "intestino permeável". Só a teduglutida tem bula, e a bula é de doença '
                                 'rara com dependência de nutrição pela veia.',
                       'alerta': 'A teduglutida é medicamento de prescrição para uma doença grave e rara; a bula '
                                 'americana pede colonoscopia de controle, por risco de acelerar crescimento de tumor, '
                                 'e alerta para obstrução intestinal. Os outros três não têm produto registrado no '
                                 'Brasil. O que se compra com esses nomes é vendido como insumo de pesquisa.'},
 'proprio_metabolismo': {'nome': 'Metabolismo e gordura — exenatida, AICAR, CBL-514 e outros',
                         'categoria': 'primaria',
                         'aprovado': 'parcial',
                         'tagline': 'A exenatida tem 93 ensaios de fase 3 e zero registro ativo na ANVISA. A '
                                    'oxintomodulina, zero de fase 3. O CBL-514 tem 7 artigos e 16 estudos registrados, '
                                    'todos da mesma empresa',
                         'resumo': 'Seis compostos de peso e metabolismo que faltavam no site: exenatida, '
                                   'oxintomodulina, efinopegdutida, AICAR (acadesina), CBL-514 e L-carnitina. Vão do '
                                   'mais estudado ao quase nada, e o que separa é sempre a mesma pergunta: em quem foi '
                                   'testado, e para quê.',
                         'alerta': 'Nenhum destes compostos tem registro ativo de medicamento no Brasil. A exenatida é '
                                   'agonista de GLP-1 com os mesmos cuidados da classe; o AICAR é ferramenta de '
                                   'laboratório; o CBL-514 ainda não terminou a fase 3. O que se compra com esses '
                                   'nomes é vendido como insumo de pesquisa, sem controle de pureza, esterilidade ou '
                                   'dose.'},
 'proprio_neuro_faltavam': {'nome': 'Neuro — as formas acetiladas e os que pararam na fase 3',
                            'categoria': 'primaria',
                            'aprovado': 'nao',
                            'tagline': 'O Semax e o Selank "N-acetil amidato" têm 6 e 2 artigos e zero estudo '
                                       'registrado. O rapastinel teve 10 ensaios de fase 3 e foi abandonado; a '
                                       'davunetida não superou o placebo',
                            'resumo': 'As versões acetiladas do Semax e do Selank, vendidas como mais potentes, e três '
                                      'peptídeos neurológicos que chegaram mais longe: rapastinel (GLYX-13), '
                                      'davunetida (NAP) e colivelina. Os que mais avançaram são justamente os que '
                                      'mostram o que costuma acontecer depois: programa encerrado, ou ensaio negativo.',
                            'alerta': 'Nenhum destes compostos tem produto registrado no Brasil ou em outra agência. '
                                      'Dois deles foram testados a sério e não viraram remédio. O que se compra com '
                                      'esses nomes é vendido como insumo de pesquisa, sem controle de pureza, '
                                      'esterilidade ou dose.'},
 'proprio_timo': {'nome': 'Timo e Cardiogen — timulina, timopentina e o bioregulador do coração',
                  'categoria': 'primaria',
                  'aprovado': 'nao',
                  'tagline': 'A timulina tem 886 artigos e zero estudo registrado. A timopentina tem registros de HIV '
                             'com o nome comercial Timunox. O Cardiogen divide o nome com um gerador de rubídio usado '
                             'em exame do coração',
                  'resumo': 'Dois fatores do timo que faltavam — timulina e timopentina (TP-5) — e o Cardiogen, '
                            'bioregulador cardíaco da escola de Khavinson. Moléculas antigas, muita fisiologia, quase '
                            'nada de ensaio, e nenhuma com produto registrado no Brasil.',
                  'alerta': 'Nenhum destes compostos tem produto registrado no Brasil. O registro que a busca encontra '
                            'na ANVISA é de timostimulina, outro extrato. O que se compra com esses nomes é vendido '
                            'como insumo de pesquisa, sem controle de pureza, esterilidade ou dose.'},
 'proprio_bancada': {'nome': 'Peptídeos de bancada — SS-20, SHLP-2, SHLP-3 e PNC-27',
                     'categoria': 'primaria',
                     'aprovado': 'nao',
                     'tagline': 'Os quatro somam 77 artigos e zero estudo registrado no ClinicalTrials.gov. O PNC-27 '
                                'aparece em loja descrito como antitumoral, sem um único ensaio em gente',
                     'resumo': 'SS-20, SHLP-2, SHLP-3 e PNC-27: quatro peptídeos que existem em artigo de célula e de '
                               'animal e em frasco de loja, e em nenhum lugar entre os dois. Nenhum tem registro de '
                               'ensaio clínico de qualquer fase.',
                     'alerta': 'Nenhum destes compostos foi testado em gente. Usar PNC-27 no lugar de tratamento de '
                               'câncer é trocar o que tem evidência pelo que não tem nenhuma. O que se compra com '
                               'esses nomes é vendido como insumo de pesquisa, sem controle de pureza, esterilidade ou '
                               'dose.'},
 'proprio_cosmeticos': {'nome': 'Peptídeos cosméticos — argirelina, Matrixyl e companhia',
                        'categoria': 'primaria',
                        'aprovado': 'nao',
                        'tagline': 'A argirelina, a mais estudada, tem 50 artigos e 6 estudos — os que dizem a via no '
                                   'título são de creme e sérum. 6 dos 10 nomes têm 4 artigos ou menos no PubMed',
                        'resumo': 'Dez peptídeos de cosmético que aparecem ao lado dos injetáveis em biblioteca de '
                                  'loja: argirelina, SNAP-8, Matrixyl, Matrixyl 3000 e seus dois componentes, Matrixyl '
                                  "synthe'6, Syn-Coll, Syn-Ake e acetil tetrapeptídeo-5. A evidência é pequena, e a "
                                  'que existe é de creme na pele.',
                        'alerta': 'Estes peptídeos foram desenvolvidos como ingrediente tópico. Não há estudo deles '
                                  'como injeção. O que se compra em frasco com esses nomes é vendido como insumo de '
                                  'pesquisa, sem controle de pureza, esterilidade ou dose.'},
 'proprio_blends': {'nome': 'Blends prontos — o que a combinação tem de estudo',
                    'categoria': 'primaria',
                    'aprovado': 'nao',
                    'tagline': '32 dos 33 blends vendidos prontos têm zero estudo registrado. 11 não têm nem um artigo '
                               'que cite os componentes juntos',
                    'resumo': '33 misturas de peptídeo listadas como blend pronto na biblioteca de uma loja '
                              'brasileira, de CJC-1295 com GHRP-2 a GHK-Cu com Matrixyl. Para cada uma, a pergunta é '
                              'se a combinação existe na literatura e nos registros de ensaio — e a resposta quase '
                              'sempre é não.',
                    'alerta': 'Nenhuma destas combinações foi testada em gente como combinação. Misturar dois '
                              'compostos sem estudo não soma evidência; acrescenta a incerteza de como eles se '
                              'comportam juntos. O que se compra com esses nomes é vendido como insumo de pesquisa, '
                              'sem controle de pureza, esterilidade ou dose.'}})
