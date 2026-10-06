# -*- coding: utf-8 -*-
"""Paginas abertas para cobrir o que faltava em relacao a biblioteca de uma loja de peptideos: levantamento de fonte primaria.

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


LACUNAS = _d({'proprio_gnrh': {'secoes': [{'h': 'Por que estes cinco estão juntos',
                              'tipo': 'p',
                              'corpo': ['Este site já tinha a <a href="protocol_kisspeptin.html">kisspeptina</a>, a '
                                        'gonadorelina e o hCG (na página de <a '
                                        'href="proprio_musculo_hpg.html">músculo, osso e eixo HPG</a>). Faltavam os '
                                        'análogos de GnRH de ação longa — triptorrelina, leuprorrelina, gosserrelina e '
                                        'histrelina — e a menotropina, a gonadotrofina extraída de urina de mulheres '
                                        'na menopausa. Os cinco estão na biblioteca de uma loja brasileira de '
                                        'peptídeos, que usei como lista do que faltava aqui, e a triptorrelina aparece '
                                        'lá descrita como usada em TPC para restaurar o eixo hormonal depois de '
                                        'ciclos. Este site não cita nem linka fornecedor.',
                                        'O contraste é o assunto da página: <strong>os cinco são medicamentos de '
                                        'verdade</strong>, com bula nos Estados Unidos e, quatro deles, registro ativo '
                                        'no Brasil. E a bula diz o contrário da promessa. O análogo de GnRH dado de '
                                        'forma contínua não liga o eixo — desliga. A bula do implante de histrelina '
                                        'descreve isso com todas as letras: depois de uma fase inicial de estímulo, a '
                                        'administração crônica dessensibiliza a hipófise e reduz a produção de '
                                        'esteroide no ovário e no testículo. É por isso que a triptorrelina, a '
                                        'leuprorrelina e a gosserrelina são remédio de câncer de próstata e de mama.',
                                        'Duas ressalvas de método, antes dos números. <strong>Uma:</strong> as '
                                        'contagens de fase 3 destes análogos são grandes porque eles entram como '
                                        'tratamento de base em ensaios de câncer — o maior registro da triptorrelina é '
                                        'um ensaio da Roche com outro remédio, o giredestrant, em câncer de mama. O '
                                        'número mede presença em protocolo, não estudo do análogo isolado. '
                                        '<strong>Duas:</strong> a busca da leuprorrelina usa os dois nomes, '
                                        '<code>leuprolide</code> (o nome nos Estados Unidos) e '
                                        '<code>leuprorelin</code> (a DCI).',
                                        'Nenhum número desta página veio da fonte secundária do site.']},
                             {'h': 'Quanta evidência existe, composto a composto',
                              'tipo': 'p',
                              'corpo': ['Os números abaixo foram levantados por mim em {DATA}, no PubMed e no '
                                        'ClinicalTrials.gov. A consulta de cada linha está escrita '
                                        '<strong>inteira</strong>, ao lado do número, para qualquer pessoa repetir e '
                                        'me contradizer — e para o script que reconfere as contagens deste site '
                                        'conseguir rodar todas.',
                                        'A coluna de condição <strong>não é afirmação de mecanismo</strong>: é o campo '
                                        '<em>Condition</em> copiado do maior registro de fase 3 que a própria busca '
                                        'devolveu. Quando não há registro de fase 3, a célula diz isso.'],
                              'tabela': {'cap': 'Levantamento de evidência — análogos de GnRH e gonadotrofinas',
                                         'linhas': [['Composto',
                                                     'Condição nos registros de fase 3',
                                                     'Consulta',
                                                     'Artigos no PubMed',
                                                     'Estudos no ClinicalTrials.gov'],
                                                    ['<strong>Triptorrelina</strong>',
                                                     '<small>Early Breast Cancer</small>',
                                                     '<code>triptorelin</code>',
                                                     '2.473',
                                                     '297'],
                                                    ['<strong>Leuprorrelina</strong>',
                                                     '<small>Breast Cancer</small>',
                                                     '<code>leuprolide OR leuprorelin</code>',
                                                     '4.222',
                                                     '521'],
                                                    ['<strong>Gosserrelina</strong>',
                                                     '<small>Breast Cancer</small>',
                                                     '<code>goserelin</code>',
                                                     '2.162',
                                                     '416'],
                                                    ['<strong>Histrelina</strong>',
                                                     '<small>Prostate Adenocarcinoma; Stage III Prostate Cancer AJCC '
                                                     'v8; Stage IVA Prostate Cancer AJCC v8</small>',
                                                     '<code>histrelin</code>',
                                                     '137',
                                                     '15'],
                                                    ['<strong>Menotropina (hMG)</strong>',
                                                     '<small>Subfertility</small>',
                                                     '<code>menotropins OR "human menopausal gonadotropin"</code>',
                                                     '3.914',
                                                     '170']]}},
                             {'h': 'O que existe de fase 3, e de quem é',
                              'tipo': 'p',
                              'corpo': ['Contagem de artigo mede atenção acadêmica, não evidência de desfecho. A '
                                        'tabela abaixo separa o que tem <strong>ensaio de fase 3 registrado</strong> — '
                                        'e mostra o maior registro que a busca devolveu, com o número de participantes '
                                        'declarado e o patrocinador. Registro não é resultado.'],
                              'tabela': {'cap': 'Ensaios registrados de fase 3 — análogos de GnRH e gonadotrofinas',
                                         'linhas': [['Composto',
                                                     'Consulta',
                                                     'Ensaios registrados de fase 3',
                                                     'O maior registro que abri'],
                                                    ['<strong>Triptorrelina</strong>',
                                                     '<code>(triptorelin) AND AREA[Phase]PHASE3</code>',
                                                     '86',
                                                     '<strong>NCT04961996</strong> · n = 4.170 · Hoffmann-La '
                                                     'Roche<br><small>Early Breast Cancer</small>'],
                                                    ['<strong>Leuprorrelina</strong>',
                                                     '<code>(leuprolide OR leuprorelin) AND AREA[Phase]PHASE3</code>',
                                                     '124',
                                                     '<strong>NCT00002582</strong> · n = 6.000 · Institute of Cancer '
                                                     'Research, United Kingdom<br><small>Breast Cancer</small>'],
                                                    ['<strong>Gosserrelina</strong>',
                                                     '<code>(goserelin) AND AREA[Phase]PHASE3</code>',
                                                     '125',
                                                     '<strong>NCT00002582</strong> · n = 6.000 · Institute of Cancer '
                                                     'Research, United Kingdom<br><small>Breast Cancer</small>'],
                                                    ['<strong>Histrelina</strong>',
                                                     '<code>(histrelin) AND AREA[Phase]PHASE3</code>',
                                                     '7',
                                                     '<strong>NCT04513717</strong> · n = 2.753 · NRG '
                                                     'Oncology<br><small>Prostate Adenocarcinoma, Stage III Prostate '
                                                     'Cancer AJCC v8, Stage IVA Prostate Cancer AJCC v8</small>'],
                                                    ['<strong>Menotropina (hMG)</strong>',
                                                     '<code>(menotropins OR "human menopausal gonadotropin") AND '
                                                     'AREA[Phase]PHASE3</code>',
                                                     '32',
                                                     '<strong>NCT02912988</strong> · n = 900 · The University of Hong '
                                                     'Kong<br><small>Subfertility</small>']]}},
                             {'h': 'Onde a conta não fecha',
                              'tipo': 'li',
                              'corpo': ['<strong>Nenhum registro testa recuperação depois de anabolizante.</strong> '
                                        'Varri o título e as condições dos 1.419 registros que as cinco buscas '
                                        'devolveram (um mesmo ensaio pode aparecer em mais de uma), procurando '
                                        'esteroide anabolizante, fisiculturismo e recuperação pós-ciclo. Achei 0. Os '
                                        '15 que falam em hipogonadismo tratam de diagnóstico de puberdade atrasada, '
                                        'hipogonadismo congênito, castração em câncer de próstata, contracepção e '
                                        'farmacocinética.',
                                        '<strong>A triptorrelina tem 86 ensaios de fase 3 registrados, e as bulas '
                                        'americanas dão duas indicações:</strong> câncer de próstata avançado '
                                        '(TRELSTAR) e puberdade precoce central a partir dos 2 anos (TRIPTODUR). Nas '
                                        'duas, o objetivo é baixar os hormônios sexuais. É o mesmo princípio ativo '
                                        'oferecido para "reiniciar" o eixo do homem.',
                                        '<strong>A histrelina é a única das cinco sem registro ativo na '
                                        'ANVISA</strong> — 0 registros. Nos Estados Unidos, a única aplicação que a '
                                        'busca devolve é um implante subcutâneo para puberdade precoce central.',
                                        '<strong>A menotropina é remédio de fertilização.</strong> 32 ensaios de fase '
                                        '3, com condições de infertilidade e reprodução assistida em todos os que vi, '
                                        'e a bula americana a indica para desenvolver vários folículos num ciclo de '
                                        'reprodução assistida. No Brasil, 2 registros ativos, na classe hormônio '
                                        'gonadotrófico.']},
                             {'h': 'Aprovação nos Estados Unidos',
                              'tipo': 'p',
                              'corpo': ['Para os que têm nome de medicamento nos Estados Unidos, consultei o '
                                        '<strong>Drugs@FDA</strong> pela API pública da openFDA, no mesmo dia. A busca '
                                        'está escrita na tabela; a data é a da submissão original aprovada mais antiga '
                                        'que a busca devolveu.'],
                              'tabela': {'cap': 'Drugs@FDA — análogos de GnRH e gonadotrofinas',
                                         'linhas': [['Composto',
                                                     'Busca na openFDA',
                                                     'Aplicações devolvidas',
                                                     'Marcas',
                                                     'Aprovação original mais antiga',
                                                     'Situação de mercado'],
                                                    ['<strong>Triptorrelina</strong>',
                                                     '<code>openfda.generic_name:"TRIPTORELIN"</code>',
                                                     '4',
                                                     'TRELSTAR, TRIPTODUR KIT',
                                                     '15/06/2000',
                                                     '<small>Prescription</small>'],
                                                    ['<strong>Leuprorrelina</strong>',
                                                     '<code>openfda.generic_name:"LEUPROLIDE"</code>',
                                                     '21',
                                                     'CAMCEVI KIT, ELIGARD KIT, FENSOLVI KIT, LEUPROLIDE ACETATE, '
                                                     'LEUPROLIDE ACETATE FOR DEPOT SUSPENSION, LUPRON DEPOT, LUPRON '
                                                     'DEPOT-PED KIT',
                                                     '26/01/1989',
                                                     '<small>Discontinued, Prescription</small>'],
                                                    ['<strong>Gosserrelina</strong>',
                                                     '<code>openfda.generic_name:"GOSERELIN"</code>',
                                                     '2',
                                                     'ZOLADEX',
                                                     '29/12/1989',
                                                     '<small>Prescription</small>'],
                                                    ['<strong>Histrelina</strong>',
                                                     '<code>openfda.generic_name:"HISTRELIN"</code>',
                                                     '1',
                                                     'SUPPRELIN LA',
                                                     '03/05/2007',
                                                     '<small>Prescription</small>'],
                                                    ['<strong>Menotropina (hMG)</strong>',
                                                     '<code>openfda.generic_name:"MENOTROPINS"</code>',
                                                     '1',
                                                     'MENOPUR',
                                                     '29/10/2004',
                                                     '<small>Prescription</small>']]}},
                             {'h': 'No Brasil',
                              'tipo': 'p',
                              'corpo': ['Busquei cada princípio ativo no <strong>dado aberto de medicamentos '
                                        'registrados da ANVISA</strong>, baixado em {DATA} — 43.596 linhas, contando '
                                        'apenas situação <strong>Ativo</strong>, no princípio ativo e no nome do '
                                        'produto, sem acento e sem diferença de caixa. A classe terapêutica é a que a '
                                        'própria base declara.',
                                        '4 dos 5 têm produto registrado. Registro não transforma o frasco vendido como '
                                        'peptídeo de pesquisa em medicamento: o que a ANVISA registrou é o produto '
                                        'daquele fabricante, com aquela apresentação e aquela indicação.'],
                              'tabela': {'cap': 'Registro na ANVISA — análogos de GnRH e gonadotrofinas',
                                         'linhas': [['Princípio ativo',
                                                     'Padrão buscado',
                                                     'Registros ativos',
                                                     'Classe terapêutica declarada',
                                                     'Produtos'],
                                                    ['<strong>Triptorrelina</strong>',
                                                     '<code>TRIPTORREL</code>',
                                                     '<strong>3</strong>',
                                                     '<small>OUTROS PRODS  NAO ENQUADRADOS EM CLASSE TERAPEUTICA '
                                                     'ESPECIF; OUTROS PRODUTOS PARA O APARELHO DIGESTIVO E '
                                                     'METABOLISMO</small>',
                                                     'GONAPEPTYL DAILY, GONAPEPTYL DEPOT, NEO DECAPEPTYL'],
                                                    ['<strong>Leuprorrelina</strong>',
                                                     '<code>LEUPRORREL</code>',
                                                     '<strong>2</strong>',
                                                     '<small>ANTINEOPLASICO; OUTROS HORMONIOS MEDIADORES E PRODUTOS '
                                                     'EQUIVALENTES</small>',
                                                     'ELIGARD, LECTRUM'],
                                                    ['<strong>Gosserrelina</strong>',
                                                     '<code>GOSSERREL</code>',
                                                     '<strong>1</strong>',
                                                     '<small>ANTINEOPLASICO</small>',
                                                     'ZOLADEX'],
                                                    ['<strong>Histrelina</strong>',
                                                     '<code>HISTREL</code>',
                                                     '<strong>0</strong>',
                                                     '<small>—</small>',
                                                     '—'],
                                                    ['<strong>Menotropina (hMG)</strong>',
                                                     '<code>MENOTROP</code>',
                                                     '<strong>2</strong>',
                                                     '<small>HORMONIO GONADOTROFICO</small>',
                                                     'MENOPUR, MERIONAL HG']]}}],
                  'nota_refs': 'Todas as contagens desta página foram levantadas por mim em {DATA}, com a consulta '
                               'declarada ao lado de cada número. As ressalvas de método estão escritas na primeira '
                               'seção, antes das tabelas. <strong>Esta página foi apurada em dia próprio</strong>, e '
                               'por isso carrega data própria.',
                  'referencias': [('API pública do ClinicalTrials.gov, versão 2 — a base de todas as contagens de '
                                   'estudo e de fase 3 desta página.',
                                   'https://clinicaltrials.gov/data-api/api'),
                                  ('E-utilities do PubMed (esearch) — a base de todas as contagens de artigo desta '
                                   'página.',
                                   'https://www.ncbi.nlm.nih.gov/books/NBK25501/'),
                                  ('Bula do SUPPRELIN LA (histrelina) no DailyMed — indicação em puberdade precoce '
                                   'central e o mecanismo de dessensibilização da hipófise com uso contínuo.',
                                   'https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d8fb000e-3cc9-4803-b71d-2cc597661977'),
                                  ('Bula do TRELSTAR (triptorrelina) no DailyMed — indicação em câncer de próstata '
                                   'avançado.',
                                   'https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b1b84d62-a369-a4b7-5c41-dd1f553a18f3'),
                                  ('Bula do TRIPTODUR (triptorrelina) no DailyMed — indicação em puberdade precoce '
                                   'central a partir dos 2 anos.',
                                   'https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f41380e7-b830-432d-a5f5-a872932f107e'),
                                  ('Bula do MENOPUR (menotropina) no DailyMed — indicação em reprodução assistida.',
                                   'https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=22c8db95-c3db-1770-8086-31356fbabe35'),
                                  ('Registro NCT04961996 no ClinicalTrials.gov.',
                                   'https://clinicaltrials.gov/study/NCT04961996'),
                                  ('API da openFDA, endpoint drugsfda — as aplicações e datas de aprovação desta '
                                   'página.',
                                   'https://open.fda.gov/apis/drug/drugsfda/'),
                                  ('Dado aberto de medicamentos registrados da ANVISA — a mesma base usada na página O '
                                   'que existe no Brasil.',
                                   'https://dados.anvisa.gov.br/dados/')]},
 'proprio_gh_miostatina': {'secoes': [{'h': 'O que faltava dos dois lados do músculo',
                                       'tipo': 'p',
                                       'corpo': ['Este site já cobre o eixo do hormônio do crescimento em <a '
                                                 'href="proprio_eixo_gh.html">uma página própria</a>, mais as páginas '
                                                 'de <a href="protocol_ghrp-6.html">GHRP-6</a>, <a '
                                                 'href="protocol_ipamorelin.html">ipamorelina</a>, <a '
                                                 'href="protocol_sermorelin.html">sermorelina</a> e <a '
                                                 'href="protocol_igf-1-lr3.html">IGF-1 LR3</a>. Faltavam quatro nomes '
                                                 'do mesmo eixo — o GHRP-1, a somatorrelina (o GHRH inteiro, de 44 '
                                                 'aminoácidos), a grelina e o PEG-MGF — e o outro lado do crescimento '
                                                 'muscular: os inibidores de miostatina, folistatina e ACE-031.',
                                                 'Três ressalvas de método, antes dos números. <strong>Uma:</strong> a '
                                                 'busca da somatorrelina no ClinicalTrials.gov devolve também '
                                                 'registros de tesamorelina, que é um análogo do mesmo GHRH 1-44 — 13 '
                                                 'dos 37 registros falam de TH9507, EGRIFTA ou tesamorelina no título, '
                                                 'e o maior de fase 3 é um deles. <strong>Duas:</strong> grelina e '
                                                 'folistatina são substâncias que o corpo produz, e a maior parte dos '
                                                 'registros as <em>mede</em> no sangue, não as administra. O número '
                                                 'dessas duas linhas é atenção à molécula, não teste do frasco. '
                                                 '<strong>Três:</strong> o único registro de fase 3 que a busca por '
                                                 'folistatina devolve é de atorvastatina em edema do miocárdio, com '
                                                 'folistatina como marcador.',
                                                 'Nenhum número desta página veio da fonte secundária do site.']},
                                      {'h': 'Quanta evidência existe, composto a composto',
                                       'tipo': 'p',
                                       'corpo': ['Os números abaixo foram levantados por mim em {DATA}, no PubMed e no '
                                                 'ClinicalTrials.gov. A consulta de cada linha está escrita '
                                                 '<strong>inteira</strong>, ao lado do número, para qualquer pessoa '
                                                 'repetir e me contradizer — e para o script que reconfere as '
                                                 'contagens deste site conseguir rodar todas.',
                                                 'A coluna de condição <strong>não é afirmação de mecanismo</strong>: '
                                                 'é o campo <em>Condition</em> copiado do maior registro de fase 3 que '
                                                 'a própria busca devolveu. Quando não há registro de fase 3, a célula '
                                                 'diz isso.'],
                                       'tabela': {'cap': 'Levantamento de evidência — GH e miostatina',
                                                  'linhas': [['Composto',
                                                              'Condição nos registros de fase 3',
                                                              'Consulta',
                                                              'Artigos no PubMed',
                                                              'Estudos no ClinicalTrials.gov'],
                                                             ['<strong>GHRP-1</strong>',
                                                              '<small>nenhum registro de fase 3 nesta busca</small>',
                                                              '<code>"GHRP-1"</code>',
                                                              '34',
                                                              '1'],
                                                             ['<strong>Somatorrelina (GHRH 1-44)</strong>',
                                                              '<small>HIV Infections; Lipodystrophy</small>',
                                                              '<code>somatorelin OR "GHRH(1-44)" OR "GHRH 1-44"</code>',
                                                              '97',
                                                              '37'],
                                                             ['<strong>Grelina</strong>',
                                                              '<small>Weight Loss</small>',
                                                              '<code>ghrelin</code>',
                                                              '13.877',
                                                              '252'],
                                                             ['<strong>PEG-MGF</strong>',
                                                              '<small>nenhum registro de fase 3 nesta busca</small>',
                                                              '<code>"PEG-MGF" OR "pegylated mechano growth '
                                                              'factor"</code>',
                                                              '5',
                                                              '0'],
                                                             ['<strong>Folistatina (qualquer forma)</strong>',
                                                              '<small>Myocardial Edema</small>',
                                                              '<code>follistatin</code>',
                                                              '3.241',
                                                              '15'],
                                                             ['<strong>Folistatina-344</strong>',
                                                              '<small>nenhum registro de fase 3 nesta busca</small>',
                                                              '<code>"follistatin 344" OR "follistatin-344" OR '
                                                              'FS344</code>',
                                                              '11',
                                                              '1'],
                                                             ['<strong>Folistatina-288</strong>',
                                                              '<small>nenhum registro de fase 3 nesta busca</small>',
                                                              '<code>"follistatin 288" OR "follistatin-288" OR '
                                                              'FS288</code>',
                                                              '69',
                                                              '0'],
                                                             ['<strong>ACE-031</strong>',
                                                              '<small>nenhum registro de fase 3 nesta busca</small>',
                                                              '<code>"ACE-031" OR ramatercept</code>',
                                                              '12',
                                                              '4']]}},
                                      {'h': 'O que existe de fase 3, e de quem é',
                                       'tipo': 'p',
                                       'corpo': ['Contagem de artigo mede atenção acadêmica, não evidência de '
                                                 'desfecho. A tabela abaixo separa o que tem <strong>ensaio de fase 3 '
                                                 'registrado</strong> — e mostra o maior registro que a busca '
                                                 'devolveu, com o número de participantes declarado e o patrocinador. '
                                                 'Registro não é resultado.'],
                                       'tabela': {'cap': 'Ensaios registrados de fase 3 — GH e miostatina',
                                                  'linhas': [['Composto',
                                                              'Consulta',
                                                              'Ensaios registrados de fase 3',
                                                              'O maior registro que abri'],
                                                             ['<strong>GHRP-1</strong>',
                                                              '<code>("GHRP-1") AND AREA[Phase]PHASE3</code>',
                                                              '0',
                                                              '—'],
                                                             ['<strong>Somatorrelina (GHRH 1-44)</strong>',
                                                              '<code>(somatorelin OR "GHRH(1-44)" OR "GHRH 1-44") AND '
                                                              'AREA[Phase]PHASE3</code>',
                                                              '4',
                                                              '<strong>NCT00123253</strong> · n = 412 · '
                                                              'Theratechnologies<br><small>HIV Infections, '
                                                              'Lipodystrophy</small>'],
                                                             ['<strong>Grelina</strong>',
                                                              '<code>(ghrelin) AND AREA[Phase]PHASE3</code>',
                                                              '11',
                                                              '<strong>NCT02810925</strong> · n = 200 · Hospital '
                                                              'General Universitario Elche<br><small>Weight '
                                                              'Loss</small>'],
                                                             ['<strong>PEG-MGF</strong>',
                                                              '<code>("PEG-MGF" OR "pegylated mechano growth factor") '
                                                              'AND AREA[Phase]PHASE3</code>',
                                                              '0',
                                                              '—'],
                                                             ['<strong>Folistatina (qualquer forma)</strong>',
                                                              '<code>(follistatin) AND AREA[Phase]PHASE3</code>',
                                                              '1',
                                                              '<strong>NCT02901379</strong> · n = 40 · National '
                                                              'Cardiovascular Center Harapan Kita Hospital '
                                                              'Indonesia<br><small>Myocardial Edema</small>'],
                                                             ['<strong>Folistatina-344</strong>',
                                                              '<code>("follistatin 344" OR "follistatin-344" OR FS344) '
                                                              'AND AREA[Phase]PHASE3</code>',
                                                              '0',
                                                              '—'],
                                                             ['<strong>Folistatina-288</strong>',
                                                              '<code>("follistatin 288" OR "follistatin-288" OR FS288) '
                                                              'AND AREA[Phase]PHASE3</code>',
                                                              '0',
                                                              '—'],
                                                             ['<strong>ACE-031</strong>',
                                                              '<code>("ACE-031" OR ramatercept) AND '
                                                              'AREA[Phase]PHASE3</code>',
                                                              '0',
                                                              '—']]}},
                                      {'h': 'Onde a conta não fecha',
                                       'tipo': 'li',
                                       'corpo': ['<strong>O GHRP-1 tem 1 estudo registrado, e ele parou com 3 '
                                                 'participantes.</strong> O registro NCT00381602, de fase 2, testava '
                                                 'um depósito de GHRP-1 em doença renal terminal e foi encerrado por '
                                                 'falta de recrutamento, segundo o próprio registro. Não há outro '
                                                 'registro com o nome.',
                                                 '<strong>O PEG-MGF tem 5 artigos e 0 estudos.</strong> A versão '
                                                 'peguilada do fator de crescimento mecânico quase não existe na '
                                                 'literatura. A linha do MGF sem PEG está na <a '
                                                 'href="proprio_eixo_gh.html">página do eixo do GH</a>, com a ressalva '
                                                 'de que a busca devolve registros de mecasermina.',
                                                 '<strong>Ninguém testou folistatina em frasco.</strong> Dos 15 '
                                                 'registros da busca, os que administram folistatina são terapia '
                                                 'gênica: 5 registros de terapia gênica — gene therapy, gene transfer, '
                                                 'plasmídeo ou AAV no título —, nas fases 1 inicial, 1, 1/2. Os outros '
                                                 'medem a folistatina no sangue. A proteína pronta, que é o que um '
                                                 'frasco de "Follistatin-344" diz conter, não aparece administrada em '
                                                 'nenhum registro desta busca.',
                                                 '<strong>O ACE-031 parou por segurança.</strong> Os dois registros de '
                                                 'fase 2 em distrofia muscular de Duchenne foram encerrados "com base '
                                                 'em dados preliminares de segurança", nas palavras do registro. O '
                                                 'artigo do ensaio, de 2017, atribui a parada a sangramento nasal e '
                                                 'telangiectasias — vasinhos dilatados na pele e nas mucosas — e '
                                                 'reporta só tendências, sem diferença estatística no teste de '
                                                 'caminhada de seis minutos.',
                                                 '<strong>A grelina tem 13.877 artigos e 11 registros de fase '
                                                 '3</strong> — e o maior deles testa estimulação elétrica percutânea '
                                                 'para perder peso, não grelina dada a alguém.']},
                                      {'h': 'No Brasil',
                                       'tipo': 'p',
                                       'corpo': ['Busquei cada princípio ativo no <strong>dado aberto de medicamentos '
                                                 'registrados da ANVISA</strong>, baixado em {DATA} — 43.596 linhas, '
                                                 'contando apenas situação <strong>Ativo</strong>, no princípio ativo '
                                                 'e no nome do produto, sem acento e sem diferença de caixa. A classe '
                                                 'terapêutica é a que a própria base declara.',
                                                 'O PEG-MGF e as duas isoformas de folistatina ficam fora desta '
                                                 'tabela: não são princípio ativo de medicamento em lugar nenhum, e '
                                                 'não há nome oficial para procurar. Ausência na base não quer dizer '
                                                 'proibição — quer dizer que não existe produto legal com aquele '
                                                 'princípio ativo.'],
                                       'tabela': {'cap': 'Registro na ANVISA — GH e miostatina',
                                                  'linhas': [['Princípio ativo',
                                                              'Padrão buscado',
                                                              'Registros ativos',
                                                              'Classe terapêutica declarada',
                                                              'Produtos'],
                                                             ['<strong>GHRP-1</strong>',
                                                              '<code>GHRP</code>',
                                                              '<strong>0</strong>',
                                                              '<small>—</small>',
                                                              '—'],
                                                             ['<strong>Somatorrelina (GHRH 1-44)</strong>',
                                                              '<code>SOMATOREL</code>',
                                                              '<strong>0</strong>',
                                                              '<small>—</small>',
                                                              '—'],
                                                             ['<strong>Grelina</strong>',
                                                              '<code>GRELIN</code>',
                                                              '<strong>0</strong>',
                                                              '<small>—</small>',
                                                              '—'],
                                                             ['<strong>Folistatina (qualquer forma)</strong>',
                                                              '<code>FOLISTAT</code>',
                                                              '<strong>0</strong>',
                                                              '<small>—</small>',
                                                              '—'],
                                                             ['<strong>ACE-031</strong>',
                                                              '<code>RAMATERCEPT</code>',
                                                              '<strong>0</strong>',
                                                              '<small>—</small>',
                                                              '—']]}}],
                           'nota_refs': 'Todas as contagens desta página foram levantadas por mim em {DATA}, com a '
                                        'consulta declarada ao lado de cada número. As ressalvas de método estão '
                                        'escritas na primeira seção, antes das tabelas. <strong>Esta página foi '
                                        'apurada em dia próprio</strong>, e por isso carrega data própria.',
                           'referencias': [('API pública do ClinicalTrials.gov, versão 2 — a base de todas as '
                                            'contagens de estudo e de fase 3 desta página.',
                                            'https://clinicaltrials.gov/data-api/api'),
                                           ('E-utilities do PubMed (esearch) — a base de todas as contagens de artigo '
                                            'desta página.',
                                            'https://www.ncbi.nlm.nih.gov/books/NBK25501/'),
                                           ('Campbell C et al. Myostatin inhibitor ACE-031 treatment of ambulatory '
                                            'boys with Duchenne muscular dystrophy: results of a randomized, '
                                            'placebo-controlled clinical trial. Muscle Nerve. 2017;55(4):458-464.',
                                            'https://pubmed.ncbi.nlm.nih.gov/27462804/'),
                                           ('Registro NCT01099761 no ClinicalTrials.gov.',
                                            'https://clinicaltrials.gov/study/NCT01099761'),
                                           ('Registro NCT00381602 no ClinicalTrials.gov.',
                                            'https://clinicaltrials.gov/study/NCT00381602'),
                                           ('Registro NCT06411366 no ClinicalTrials.gov.',
                                            'https://clinicaltrials.gov/study/NCT06411366'),
                                           ('Registro NCT01519349 no ClinicalTrials.gov.',
                                            'https://clinicaltrials.gov/study/NCT01519349'),
                                           ('Dado aberto de medicamentos registrados da ANVISA — a mesma base usada na '
                                            'página O que existe no Brasil.',
                                            'https://dados.anvisa.gov.br/dados/')]},
 'proprio_intestino': {'secoes': [{'h': 'Os análogos de GLP-2 e a promessa de intestino permeável',
                                   'tipo': 'p',
                                   'corpo': ['O GLP-2 é um hormônio do intestino, primo do GLP-1 das canetas de '
                                             'emagrecer. Os análogos dele — teduglutida, glepaglutida, apraglutida — '
                                             'foram desenvolvidos para uma doença rara e grave: a síndrome do '
                                             'intestino curto, em que a pessoa perdeu tanto intestino que depende de '
                                             'nutrição pela veia. A larazotida é outra coisa, um peptídeo pensado para '
                                             'fechar as junções entre as células da mucosa na doença celíaca.',
                                             'Na biblioteca de loja que usei como lista do que faltava, o GLP-2 e a '
                                             'larazotida aparecem ligados a outra coisa: "intestino permeável". A '
                                             'página mede essa distância.',
                                             'Uma ressalva de método que muda a leitura de uma linha inteira. '
                                             '<strong>A busca da larazotida no ClinicalTrials.gov devolve registros de '
                                             'outro remédio.</strong> O código de desenvolvimento AT1001 foi usado '
                                             'para a larazotida e também para o migalastat, um medicamento para doença '
                                             'de Fabry, e a base trata os dois como sinônimos. Dos 29 registros que a '
                                             'busca <code>larazotide</code> devolve, 19 são de Fabry; dos 9 de fase 3, '
                                             '1 é de doença celíaca. Publico o número da busca e escrevo a ressalva, '
                                             'porque trocar a consulta para fazer o número parecer certo seria '
                                             'esconder o problema de quem for repetir.',
                                             'Nenhum número desta página veio da fonte secundária do site.']},
                                  {'h': 'Quanta evidência existe, composto a composto',
                                   'tipo': 'p',
                                   'corpo': ['Os números abaixo foram levantados por mim em {DATA}, no PubMed e no '
                                             'ClinicalTrials.gov. A consulta de cada linha está escrita '
                                             '<strong>inteira</strong>, ao lado do número, para qualquer pessoa '
                                             'repetir e me contradizer — e para o script que reconfere as contagens '
                                             'deste site conseguir rodar todas.',
                                             'A coluna de condição <strong>não é afirmação de mecanismo</strong>: é o '
                                             'campo <em>Condition</em> copiado do maior registro de fase 3 que a '
                                             'própria busca devolveu. Quando não há registro de fase 3, a célula diz '
                                             'isso.'],
                                   'tabela': {'cap': 'Levantamento de evidência — intestino',
                                              'linhas': [['Composto',
                                                          'Condição nos registros de fase 3',
                                                          'Consulta',
                                                          'Artigos no PubMed',
                                                          'Estudos no ClinicalTrials.gov'],
                                                         ['<strong>Teduglutida</strong>',
                                                          '<small>Short Bowel Syndrome</small>',
                                                          '<code>teduglutide</code>',
                                                          '386',
                                                          '50'],
                                                         ['<strong>Glepaglutida</strong>',
                                                          '<small>Short Bowel Syndrome</small>',
                                                          '<code>glepaglutide</code>',
                                                          '36',
                                                          '9'],
                                                         ['<strong>Apraglutida</strong>',
                                                          '<small>Short Bowel Syndrome</small>',
                                                          '<code>apraglutide</code>',
                                                          '31',
                                                          '10'],
                                                         ['<strong>Larazotida</strong>',
                                                          '<small>Celiac Disease</small>',
                                                          '<code>larazotide</code>',
                                                          '81',
                                                          '29']]}},
                                  {'h': 'O que existe de fase 3, e de quem é',
                                   'tipo': 'p',
                                   'corpo': ['Contagem de artigo mede atenção acadêmica, não evidência de desfecho. A '
                                             'tabela abaixo separa o que tem <strong>ensaio de fase 3 '
                                             'registrado</strong> — e mostra o maior registro que a busca devolveu, '
                                             'com o número de participantes declarado e o patrocinador. Registro não é '
                                             'resultado.'],
                                   'tabela': {'cap': 'Ensaios registrados de fase 3 — intestino',
                                              'linhas': [['Composto',
                                                          'Consulta',
                                                          'Ensaios registrados de fase 3',
                                                          'O maior registro que abri'],
                                                         ['<strong>Teduglutida</strong>',
                                                          '<code>(teduglutide) AND AREA[Phase]PHASE3</code>',
                                                          '22',
                                                          '<strong>NCT00930644</strong> · n = 88 · '
                                                          'Shire<br><small>Short Bowel Syndrome</small>'],
                                                         ['<strong>Glepaglutida</strong>',
                                                          '<code>(glepaglutide) AND AREA[Phase]PHASE3</code>',
                                                          '6',
                                                          '<strong>NCT03905707</strong> · n = 150 · Zealand '
                                                          'Pharma<br><small>Short Bowel Syndrome</small>'],
                                                         ['<strong>Apraglutida</strong>',
                                                          '<code>(apraglutide) AND AREA[Phase]PHASE3</code>',
                                                          '3',
                                                          '<strong>NCT04627025</strong> · n = 164 · VectivBio '
                                                          'AG<br><small>Short Bowel Syndrome</small>'],
                                                         ['<strong>Larazotida</strong>',
                                                          '<code>(larazotide) AND AREA[Phase]PHASE3</code>',
                                                          '9',
                                                          '<strong>NCT03569007</strong> · n = 307 · 9 Meters '
                                                          'Biopharma, Inc.<br><small>Celiac Disease</small>']]}},
                                  {'h': 'Onde a conta não fecha',
                                   'tipo': 'li',
                                   'corpo': ['<strong>A fase 3 dos análogos de GLP-2 é de intestino curto.</strong> '
                                             'Dos 31 registros de fase 3 das três moléculas, 26 têm síndrome do '
                                             'intestino curto como condição; os outros são estudos de fisiologia de '
                                             'gordura no sangue e de ileostomia com teduglutida. Nenhum é de intestino '
                                             'permeável. O que se vende como "GLP-2" para isso usa o nome de uma '
                                             'molécula estudada para outra doença.',
                                             '<strong>A teduglutida é a única com bula</strong>: aprovada pela FDA em '
                                             '2012, para adultos e crianças a partir de 1 ano com intestino curto '
                                             'dependente de nutrição parenteral, e registrada no Brasil como '
                                             'REVESTIVE.',
                                             '<strong>O único ensaio de fase 3 da larazotida foi encerrado pelo '
                                             'patrocinador.</strong> O registro NCT03569007, em doença celíaca, tinha '
                                             '307 participantes e traz como motivo apenas "encerrado pelo '
                                             'patrocinador". Não há resultado publicado no registro.',
                                             '<strong>Glepaglutida e apraglutida não têm registro ativo na '
                                             'ANVISA.</strong> Não as procurei na openFDA, e por isso esta página não '
                                             'afirma nada sobre a situação delas nos Estados Unidos.']},
                                  {'h': 'No Brasil',
                                   'tipo': 'p',
                                   'corpo': ['Busquei cada princípio ativo no <strong>dado aberto de medicamentos '
                                             'registrados da ANVISA</strong>, baixado em {DATA} — 43.596 linhas, '
                                             'contando apenas situação <strong>Ativo</strong>, no princípio ativo e no '
                                             'nome do produto, sem acento e sem diferença de caixa. A classe '
                                             'terapêutica é a que a própria base declara.'],
                                   'tabela': {'cap': 'Registro na ANVISA — intestino',
                                              'linhas': [['Princípio ativo',
                                                          'Padrão buscado',
                                                          'Registros ativos',
                                                          'Classe terapêutica declarada',
                                                          'Produtos'],
                                                         ['<strong>Teduglutida</strong>',
                                                          '<code>TEDUGLUT</code>',
                                                          '<strong>1</strong>',
                                                          '<small>OUTROS HORMONIOS E MODULADORES DO METABOLISMO E DA '
                                                          'DIGESTAO</small>',
                                                          'REVESTIVE'],
                                                         ['<strong>Glepaglutida</strong>',
                                                          '<code>GLEPAGLUT</code>',
                                                          '<strong>0</strong>',
                                                          '<small>—</small>',
                                                          '—'],
                                                         ['<strong>Apraglutida</strong>',
                                                          '<code>APRAGLUT</code>',
                                                          '<strong>0</strong>',
                                                          '<small>—</small>',
                                                          '—'],
                                                         ['<strong>Larazotida</strong>',
                                                          '<code>LARAZOT</code>',
                                                          '<strong>0</strong>',
                                                          '<small>—</small>',
                                                          '—']]}}],
                       'nota_refs': 'Todas as contagens desta página foram levantadas por mim em {DATA}, com a '
                                    'consulta declarada ao lado de cada número. As ressalvas de método estão escritas '
                                    'na primeira seção, antes das tabelas. <strong>Esta página foi apurada em dia '
                                    'próprio</strong>, e por isso carrega data própria.',
                       'referencias': [('API pública do ClinicalTrials.gov, versão 2 — a base de todas as contagens de '
                                        'estudo e de fase 3 desta página.',
                                        'https://clinicaltrials.gov/data-api/api'),
                                       ('E-utilities do PubMed (esearch) — a base de todas as contagens de artigo '
                                        'desta página.',
                                        'https://www.ncbi.nlm.nih.gov/books/NBK25501/'),
                                       ('Bula do GATTEX (teduglutida) no DailyMed — indicação em síndrome do intestino '
                                        'curto dependente de suporte parenteral.',
                                        'https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=66b69c1e-b25c-44d3-b5ff-1c1de9a516fa'),
                                       ('Registro NCT03569007 no ClinicalTrials.gov.',
                                        'https://clinicaltrials.gov/study/NCT03569007'),
                                       ('Registro NCT03905707 no ClinicalTrials.gov.',
                                        'https://clinicaltrials.gov/study/NCT03905707'),
                                       ('Registro NCT04627025 no ClinicalTrials.gov.',
                                        'https://clinicaltrials.gov/study/NCT04627025'),
                                       ('API da openFDA, endpoint drugsfda — as aplicações e datas de aprovação desta '
                                        'página.',
                                        'https://open.fda.gov/apis/drug/drugsfda/'),
                                       ('Dado aberto de medicamentos registrados da ANVISA — a mesma base usada na '
                                        'página O que existe no Brasil.',
                                        'https://dados.anvisa.gov.br/dados/')]},
 'proprio_metabolismo': {'secoes': [{'h': 'Seis nomes de fora da fila das canetas',
                                     'tipo': 'p',
                                     'corpo': ['O site já tem semaglutida, tirzepatida, retatrutida, survodutida, '
                                               'cagrilintida, mazdutida e a <a href="proprio_incretinas.html">página '
                                               'das incretinas de nova geração</a>. Ficaram de fora a exenatida, '
                                               'aprovada nos Estados Unidos em 2005; a oxintomodulina, um hormônio do '
                                               'intestino; a efinopegdutida, da MSD; o AICAR, que a loja de onde tirei '
                                               'a lista descreve como imitador de exercício; o CBL-514, uma injeção '
                                               'para gordura localizada; e a L-carnitina.',
                                               'Três ressalvas de método. <strong>Uma:</strong> <code>AICAR OR '
                                               'acadesine</code> devolve a literatura inteira de uma ferramenta de '
                                               'laboratório, e o número é teto. Para medir isso: <code>(AICAR OR '
                                               'acadesine) AND AMPK</code> devolve 2.164 dos 2.891 artigos. '
                                               '<strong>Duas:</strong> a busca da L-carnitina devolve registros em que '
                                               'ela entra como cotratamento em ensaios de outra coisa; o maior de fase '
                                               '3 é um ensaio de antiviral em HIV. <strong>Três:</strong> a '
                                               'oxintomodulina é hormônio que o corpo produz, e parte dos registros a '
                                               'mede no sangue.',
                                               'Nenhum número desta página veio da fonte secundária do site.']},
                                    {'h': 'Quanta evidência existe, composto a composto',
                                     'tipo': 'p',
                                     'corpo': ['Os números abaixo foram levantados por mim em {DATA}, no PubMed e no '
                                               'ClinicalTrials.gov. A consulta de cada linha está escrita '
                                               '<strong>inteira</strong>, ao lado do número, para qualquer pessoa '
                                               'repetir e me contradizer — e para o script que reconfere as contagens '
                                               'deste site conseguir rodar todas.',
                                               'A coluna de condição <strong>não é afirmação de mecanismo</strong>: é '
                                               'o campo <em>Condition</em> copiado do maior registro de fase 3 que a '
                                               'própria busca devolveu. Quando não há registro de fase 3, a célula diz '
                                               'isso.'],
                                     'tabela': {'cap': 'Levantamento de evidência — metabolismo e gordura',
                                                'linhas': [['Composto',
                                                            'Condição nos registros de fase 3',
                                                            'Consulta',
                                                            'Artigos no PubMed',
                                                            'Estudos no ClinicalTrials.gov'],
                                                           ['<strong>Exenatida</strong>',
                                                            '<small>Type 2 Diabetes Mellitus</small>',
                                                            '<code>exenatide</code>',
                                                            '4.526',
                                                            '378'],
                                                           ['<strong>Oxintomodulina</strong>',
                                                            '<small>nenhum registro de fase 3 nesta busca</small>',
                                                            '<code>oxyntomodulin</code>',
                                                            '476',
                                                            '10'],
                                                           ['<strong>Efinopegdutida</strong>',
                                                            '<small>nenhum registro de fase 3 nesta busca</small>',
                                                            '<code>efinopegdutide OR "MK-6024"</code>',
                                                            '9',
                                                            '7'],
                                                           ['<strong>AICAR (acadesina)</strong>',
                                                            '<small>Coronary Artery Bypass; Myocardial Infarction; '
                                                            'Ventricular Dysfunction, Left; Stroke</small>',
                                                            '<code>AICAR OR acadesine</code>',
                                                            '2.891',
                                                            '5'],
                                                           ['<strong>CBL-514</strong>',
                                                            '<small>Subcutaneous Fat</small>',
                                                            '<code>"CBL-514"</code>',
                                                            '7',
                                                            '16'],
                                                           ['<strong>L-carnitina</strong>',
                                                            '<small>Cytomegalovirus Infections; HIV Infections</small>',
                                                            '<code>levocarnitine OR "L-carnitine"</code>',
                                                            '23.815',
                                                            '312']]}},
                                    {'h': 'O que existe de fase 3, e de quem é',
                                     'tipo': 'p',
                                     'corpo': ['Contagem de artigo mede atenção acadêmica, não evidência de desfecho. '
                                               'A tabela abaixo separa o que tem <strong>ensaio de fase 3 '
                                               'registrado</strong> — e mostra o maior registro que a busca devolveu, '
                                               'com o número de participantes declarado e o patrocinador. Registro não '
                                               'é resultado.'],
                                     'tabela': {'cap': 'Ensaios registrados de fase 3 — metabolismo e gordura',
                                                'linhas': [['Composto',
                                                            'Consulta',
                                                            'Ensaios registrados de fase 3',
                                                            'O maior registro que abri'],
                                                           ['<strong>Exenatida</strong>',
                                                            '<code>(exenatide) AND AREA[Phase]PHASE3</code>',
                                                            '93',
                                                            '<strong>NCT01144338</strong> · n = 14.752 · '
                                                            'AstraZeneca<br><small>Type 2 Diabetes Mellitus</small>'],
                                                           ['<strong>Oxintomodulina</strong>',
                                                            '<code>(oxyntomodulin) AND AREA[Phase]PHASE3</code>',
                                                            '0',
                                                            '—'],
                                                           ['<strong>Efinopegdutida</strong>',
                                                            '<code>(efinopegdutide OR "MK-6024") AND '
                                                            'AREA[Phase]PHASE3</code>',
                                                            '0',
                                                            '—'],
                                                           ['<strong>AICAR (acadesina)</strong>',
                                                            '<code>(AICAR OR acadesine) AND AREA[Phase]PHASE3</code>',
                                                            '1',
                                                            '<strong>NCT00872001</strong> · n = 3.080 · Merck Sharp '
                                                            '&amp; Dohme LLC<br><small>Coronary Artery Bypass, '
                                                            'Myocardial Infarction, Ventricular Dysfunction, Left, '
                                                            'Stroke</small>'],
                                                           ['<strong>CBL-514</strong>',
                                                            '<code>("CBL-514") AND AREA[Phase]PHASE3</code>',
                                                            '3',
                                                            '<strong>NCT07140939</strong> · n = 320 · Caliway '
                                                            'Biopharmaceuticals Co., Ltd.<br><small>Subcutaneous '
                                                            'Fat</small>'],
                                                           ['<strong>L-carnitina</strong>',
                                                            '<code>(levocarnitine OR "L-carnitine") AND '
                                                            'AREA[Phase]PHASE3</code>',
                                                            '53',
                                                            '<strong>NCT00001082</strong> · n = 505 · National '
                                                            'Institute of Allergy and Infectious Diseases '
                                                            '(NIAID)<br><small>Cytomegalovirus Infections, HIV '
                                                            'Infections</small>']]}},
                                    {'h': 'Onde a conta não fecha',
                                     'tipo': 'li',
                                     'corpo': ['<strong>A exenatida tem 93 ensaios de fase 3 e nenhum registro ativo '
                                               'na ANVISA.</strong> O maior é o EXSCEL, de desfecho cardiovascular, '
                                               'com 14.752 participantes. Nos Estados Unidos, a busca devolve o BYETTA '
                                               'como descontinuado e um genérico sintético aprovado em 2024. É a que '
                                               'tem mais ensaio de fase 3 nesta página — e não tem produto registrado '
                                               'no Brasil.',
                                               '<strong>A oxintomodulina não tem um único ensaio de fase 3</strong>, '
                                               'em 476 artigos. O maior registro é de fase 2, da OPKO Health, Inc., '
                                               'com 420 participantes em diabetes tipo 2; o resto é fase 1 ou '
                                               'fisiologia — o hormônio medido depois de cirurgia bariátrica, de '
                                               'exercício, de refeição.',
                                               '<strong>A efinopegdutida está, até agora, na fase 2</strong>: 4 '
                                               'registros de fase 2, todos da MSD e todos em fígado gorduroso, e '
                                               'nenhum de fase 3.',
                                               '<strong>O único ensaio de fase 3 do AICAR foi encerrado.</strong> Com '
                                               'o nome farmacêutico de acadesina, ele foi testado em 3.080 pacientes '
                                               'de cirurgia de revascularização do miocárdio, para reduzir eventos '
                                               'cardiovasculares e cerebrovasculares. O registro NCT00872001 está como '
                                               'encerrado. Nenhum dos 5 registros é sobre desempenho ou exercício.',
                                               '<strong>O CBL-514 tem mais registro que artigo</strong>: 7 artigos e '
                                               '16 estudos, todos da mesma empresa, a Caliway. Dos 3 de fase 3, nenhum '
                                               'tem situação de concluído — ainda sem recrutar, recrutando. É o '
                                               'desenvolvimento acontecendo agora, e ainda sem resultado de fase 3.',
                                               '<strong>A L-carnitina tem bula, para outra coisa.</strong> Nos Estados '
                                               'Unidos, a levocarnitina é aprovada para deficiência sistêmica primária '
                                               'de carnitina. Na base de medicamentos da ANVISA, a busca não encontra '
                                               'registro ativo com o princípio ativo.']},
                                    {'h': 'Aprovação nos Estados Unidos',
                                     'tipo': 'p',
                                     'corpo': ['Para os que têm nome de medicamento nos Estados Unidos, consultei o '
                                               '<strong>Drugs@FDA</strong> pela API pública da openFDA, no mesmo dia. '
                                               'A busca está escrita na tabela; a data é a da submissão original '
                                               'aprovada mais antiga que a busca devolveu.'],
                                     'tabela': {'cap': 'Drugs@FDA — metabolismo e gordura',
                                                'linhas': [['Composto',
                                                            'Busca na openFDA',
                                                            'Aplicações devolvidas',
                                                            'Marcas',
                                                            'Aprovação original mais antiga',
                                                            'Situação de mercado'],
                                                           ['<strong>Exenatida</strong>',
                                                            '<code>openfda.generic_name:"EXENATIDE"</code>',
                                                            '2',
                                                            'BYETTA, EXENATIDE SYNTHETIC',
                                                            '28/04/2005',
                                                            '<small>Discontinued, Prescription</small>'],
                                                           ['<strong>L-carnitina</strong>',
                                                            '<code>openfda.generic_name:"LEVOCARNITINE"</code>',
                                                            '12',
                                                            'CARNITOR, CARNITOR SF, LEVOCARNITINE, LEVOCARNITINE SF',
                                                            '27/12/1985',
                                                            '<small>Discontinued, Prescription</small>']]}},
                                    {'h': 'No Brasil',
                                     'tipo': 'p',
                                     'corpo': ['Busquei cada princípio ativo no <strong>dado aberto de medicamentos '
                                               'registrados da ANVISA</strong>, baixado em {DATA} — 43.596 linhas, '
                                               'contando apenas situação <strong>Ativo</strong>, no princípio ativo e '
                                               'no nome do produto, sem acento e sem diferença de caixa. A classe '
                                               'terapêutica é a que a própria base declara.',
                                               'O CBL-514 fica fora da tabela: código de desenvolvimento, sem DCI '
                                               'publicada, não tem princípio ativo para procurar.'],
                                     'tabela': {'cap': 'Registro na ANVISA — metabolismo e gordura',
                                                'linhas': [['Princípio ativo',
                                                            'Padrão buscado',
                                                            'Registros ativos',
                                                            'Classe terapêutica declarada',
                                                            'Produtos'],
                                                           ['<strong>Exenatida</strong>',
                                                            '<code>EXENAT</code>',
                                                            '<strong>0</strong>',
                                                            '<small>—</small>',
                                                            '—'],
                                                           ['<strong>Oxintomodulina</strong>',
                                                            '<code>OXINTOMOD</code>',
                                                            '<strong>0</strong>',
                                                            '<small>—</small>',
                                                            '—'],
                                                           ['<strong>Efinopegdutida</strong>',
                                                            '<code>EFINOPEG</code>',
                                                            '<strong>0</strong>',
                                                            '<small>—</small>',
                                                            '—'],
                                                           ['<strong>AICAR (acadesina)</strong>',
                                                            '<code>ACADESIN</code>',
                                                            '<strong>0</strong>',
                                                            '<small>—</small>',
                                                            '—'],
                                                           ['<strong>L-carnitina</strong>',
                                                            '<code>CARNITINA</code>',
                                                            '<strong>0</strong>',
                                                            '<small>—</small>',
                                                            '—']]}}],
                         'nota_refs': 'Todas as contagens desta página foram levantadas por mim em {DATA}, com a '
                                      'consulta declarada ao lado de cada número. As ressalvas de método estão '
                                      'escritas na primeira seção, antes das tabelas. <strong>Esta página foi apurada '
                                      'em dia próprio</strong>, e por isso carrega data própria.',
                         'referencias': [('API pública do ClinicalTrials.gov, versão 2 — a base de todas as contagens '
                                          'de estudo e de fase 3 desta página.',
                                          'https://clinicaltrials.gov/data-api/api'),
                                         ('E-utilities do PubMed (esearch) — a base de todas as contagens de artigo '
                                          'desta página.',
                                          'https://www.ncbi.nlm.nih.gov/books/NBK25501/'),
                                         ('Registro NCT01144338 no ClinicalTrials.gov.',
                                          'https://clinicaltrials.gov/study/NCT01144338'),
                                         ('Registro NCT00872001 no ClinicalTrials.gov.',
                                          'https://clinicaltrials.gov/study/NCT00872001'),
                                         ('Registro NCT07140939 no ClinicalTrials.gov.',
                                          'https://clinicaltrials.gov/study/NCT07140939'),
                                         ('Bula da levocarnitina solução oral no DailyMed — indicação em deficiência '
                                          'sistêmica primária de carnitina.',
                                          'https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=05ab18c1-fb01-48fa-8f05-0200bb8a5edf'),
                                         ('API da openFDA, endpoint drugsfda — as aplicações e datas de aprovação '
                                          'desta página.',
                                          'https://open.fda.gov/apis/drug/drugsfda/'),
                                         ('Dado aberto de medicamentos registrados da ANVISA — a mesma base usada na '
                                          'página O que existe no Brasil.',
                                          'https://dados.anvisa.gov.br/dados/')]},
 'proprio_neuro_faltavam': {'secoes': [{'h': 'As versões "mais fortes" e os que já foram testados de verdade',
                                        'tipo': 'p',
                                        'corpo': ['Este site tem o <a href="protocol_semax.html">Semax</a>, o <a '
                                                  'href="protocol_selank.html">Selank</a>, a <a '
                                                  'href="proprio_semax_evidencia.html">evidência do Semax</a> e a <a '
                                                  'href="proprio_neuro_novos.html">página de neuro e cognição</a>. '
                                                  'Faltavam as formas N-acetiladas e "amidadas" do Semax e do Selank, '
                                                  'vendidas como versões mais potentes, e três peptídeos que chegaram '
                                                  'mais longe: o rapastinel, a davunetida e a colivelina.',
                                                  'Uma ressalva de método: as formas acetiladas não têm nome oficial, '
                                                  'e cada vendedor escreve de um jeito. A busca reúne as grafias que '
                                                  'encontrei — <code>N-acetyl semax</code>, <code>NA-Semax</code>, '
                                                  '<code>N-acetylsemax</code>, <code>semax amidate</code> — e o mesmo '
                                                  'para o Selank. Se houver uma grafia que eu não vi, o número pode '
                                                  'estar baixo; não pode estar alto.',
                                                  'Nenhum número desta página veio da fonte secundária do site.']},
                                       {'h': 'Quanta evidência existe, composto a composto',
                                        'tipo': 'p',
                                        'corpo': ['Os números abaixo foram levantados por mim em {DATA}, no PubMed e '
                                                  'no ClinicalTrials.gov. A consulta de cada linha está escrita '
                                                  '<strong>inteira</strong>, ao lado do número, para qualquer pessoa '
                                                  'repetir e me contradizer — e para o script que reconfere as '
                                                  'contagens deste site conseguir rodar todas.',
                                                  'A coluna de condição <strong>não é afirmação de mecanismo</strong>: '
                                                  'é o campo <em>Condition</em> copiado do maior registro de fase 3 '
                                                  'que a própria busca devolveu. Quando não há registro de fase 3, a '
                                                  'célula diz isso.'],
                                        'tabela': {'cap': 'Levantamento de evidência — neuro',
                                                   'linhas': [['Composto',
                                                               'Condição nos registros de fase 3',
                                                               'Consulta',
                                                               'Artigos no PubMed',
                                                               'Estudos no ClinicalTrials.gov'],
                                                              ['<strong>N-acetil semax (e amidato)</strong>',
                                                               '<small>nenhum registro de fase 3 nesta busca</small>',
                                                               '<code>"N-acetyl semax" OR "NA-Semax" OR '
                                                               '"N-acetylsemax" OR "semax amidate"</code>',
                                                               '6',
                                                               '0'],
                                                              ['<strong>N-acetil selank (e amidato)</strong>',
                                                               '<small>nenhum registro de fase 3 nesta busca</small>',
                                                               '<code>"N-acetyl selank" OR "NA-Selank" OR "selank '
                                                               'amidate"</code>',
                                                               '2',
                                                               '0'],
                                                              ['<strong>Rapastinel (GLYX-13)</strong>',
                                                               '<small>Depressive Disorder, Major</small>',
                                                               '<code>rapastinel OR "GLYX-13"</code>',
                                                               '109',
                                                               '19'],
                                                              ['<strong>Davunetida (NAP)</strong>',
                                                               '<small>Progressive Supranuclear Palsy</small>',
                                                               '<code>davunetide OR "AL-108" OR NAPVSIPQ OR "NAP '
                                                               'peptide"</code>',
                                                               '244',
                                                               '5'],
                                                              ['<strong>Colivelina</strong>',
                                                               '<small>nenhum registro de fase 3 nesta busca</small>',
                                                               '<code>colivelin</code>',
                                                               '190',
                                                               '0']]}},
                                       {'h': 'O que existe de fase 3, e de quem é',
                                        'tipo': 'p',
                                        'corpo': ['Contagem de artigo mede atenção acadêmica, não evidência de '
                                                  'desfecho. A tabela abaixo separa o que tem <strong>ensaio de fase 3 '
                                                  'registrado</strong> — e mostra o maior registro que a busca '
                                                  'devolveu, com o número de participantes declarado e o patrocinador. '
                                                  'Registro não é resultado.'],
                                        'tabela': {'cap': 'Ensaios registrados de fase 3 — neuro',
                                                   'linhas': [['Composto',
                                                               'Consulta',
                                                               'Ensaios registrados de fase 3',
                                                               'O maior registro que abri'],
                                                              ['<strong>N-acetil semax (e amidato)</strong>',
                                                               '<code>("N-acetyl semax" OR "NA-Semax" OR '
                                                               '"N-acetylsemax" OR "semax amidate") AND '
                                                               'AREA[Phase]PHASE3</code>',
                                                               '0',
                                                               '—'],
                                                              ['<strong>N-acetil selank (e amidato)</strong>',
                                                               '<code>("N-acetyl selank" OR "NA-Selank" OR "selank '
                                                               'amidate") AND AREA[Phase]PHASE3</code>',
                                                               '0',
                                                               '—'],
                                                              ['<strong>Rapastinel (GLYX-13)</strong>',
                                                               '<code>(rapastinel OR "GLYX-13") AND '
                                                               'AREA[Phase]PHASE3</code>',
                                                               '10',
                                                               '<strong>NCT02951988</strong> · n = 1.304 · Naurex, '
                                                               'Inc, an affiliate of Allergan plc<br><small>Depressive '
                                                               'Disorder, Major</small>'],
                                                              ['<strong>Davunetida (NAP)</strong>',
                                                               '<code>(davunetide OR "AL-108" OR NAPVSIPQ OR "NAP '
                                                               'peptide") AND AREA[Phase]PHASE3</code>',
                                                               '1',
                                                               '<strong>NCT01110720</strong> · n = 313 · Allon '
                                                               'Therapeutics<br><small>Progressive Supranuclear '
                                                               'Palsy</small>'],
                                                              ['<strong>Colivelina</strong>',
                                                               '<code>(colivelin) AND AREA[Phase]PHASE3</code>',
                                                               '0',
                                                               '—']]}},
                                       {'h': 'Onde a conta não fecha',
                                        'tipo': 'li',
                                        'corpo': ['<strong>As versões "mais potentes" têm 6 e 2 artigos, e zero estudo '
                                                  'registrado.</strong> A afirmação, que aparece na loja, de que a '
                                                  'forma acetilada passa melhor pela barreira hematoencefálica ou dura '
                                                  'mais não tem ensaio em gente que a sustente.',
                                                  '<strong>O rapastinel é o que mais avançou, e foi '
                                                  'abandonado.</strong> 10 ensaios de fase 3 em depressão maior, o '
                                                  'maior com 1.304 participantes. 7 registros foram encerrados; em 5, '
                                                  'o motivo declarado é decisão de negócio de parar o programa. Nos '
                                                  'outros, o patrocinador foi comprado por outra empresa ou os '
                                                  'participantes passaram para outro estudo.',
                                                  '<strong>A davunetida chegou à fase 2/3 e não funcionou.</strong> O '
                                                  'ensaio em paralisia supranuclear progressiva, com 313 '
                                                  'participantes, publicado na Lancet Neurology em 2014, não encontrou '
                                                  'diferença contra placebo em nenhum dos dois desfechos principais. A '
                                                  'conclusão dos próprios autores: não é tratamento eficaz para a '
                                                  'doença. Houve mais sangramento nasal no grupo da davunetida.',
                                                  '<strong>A colivelina tem 190 artigos e 0 estudos '
                                                  'registrados.</strong> Nenhum registro de ensaio em gente, de '
                                                  'nenhuma fase.']},
                                       {'h': 'No Brasil',
                                        'tipo': 'p',
                                        'corpo': ['Busquei cada princípio ativo no <strong>dado aberto de medicamentos '
                                                  'registrados da ANVISA</strong>, baixado em {DATA} — 43.596 linhas, '
                                                  'contando apenas situação <strong>Ativo</strong>, no princípio ativo '
                                                  'e no nome do produto, sem acento e sem diferença de caixa. A classe '
                                                  'terapêutica é a que a própria base declara.',
                                                  'As formas acetiladas e a colivelina ficam fora da tabela: não têm '
                                                  'nome de princípio ativo para procurar.'],
                                        'tabela': {'cap': 'Registro na ANVISA — neuro',
                                                   'linhas': [['Princípio ativo',
                                                               'Padrão buscado',
                                                               'Registros ativos',
                                                               'Classe terapêutica declarada',
                                                               'Produtos'],
                                                              ['<strong>Rapastinel (GLYX-13)</strong>',
                                                               '<code>RAPASTINEL</code>',
                                                               '<strong>0</strong>',
                                                               '<small>—</small>',
                                                               '—'],
                                                              ['<strong>Davunetida (NAP)</strong>',
                                                               '<code>DAVUNET</code>',
                                                               '<strong>0</strong>',
                                                               '<small>—</small>',
                                                               '—']]}}],
                            'nota_refs': 'Todas as contagens desta página foram levantadas por mim em {DATA}, com a '
                                         'consulta declarada ao lado de cada número. As ressalvas de método estão '
                                         'escritas na primeira seção, antes das tabelas. <strong>Esta página foi '
                                         'apurada em dia próprio</strong>, e por isso carrega data própria.',
                            'referencias': [('API pública do ClinicalTrials.gov, versão 2 — a base de todas as '
                                             'contagens de estudo e de fase 3 desta página.',
                                             'https://clinicaltrials.gov/data-api/api'),
                                            ('E-utilities do PubMed (esearch) — a base de todas as contagens de artigo '
                                             'desta página.',
                                             'https://www.ncbi.nlm.nih.gov/books/NBK25501/'),
                                            ('Boxer AL et al. Davunetide in patients with progressive supranuclear '
                                             'palsy: a randomised, double-blind, placebo-controlled phase 2/3 trial. '
                                             'Lancet Neurol. 2014;13(7):676-85.',
                                             'https://pubmed.ncbi.nlm.nih.gov/24873720/'),
                                            ('Registro NCT02951988 no ClinicalTrials.gov.',
                                             'https://clinicaltrials.gov/study/NCT02951988'),
                                            ('Registro NCT03560518 no ClinicalTrials.gov.',
                                             'https://clinicaltrials.gov/study/NCT03560518'),
                                            ('Dado aberto de medicamentos registrados da ANVISA — a mesma base usada '
                                             'na página O que existe no Brasil.',
                                             'https://dados.anvisa.gov.br/dados/')]},
 'proprio_timo': {'secoes': [{'h': 'Fatores do timo e o bioregulador do coração',
                              'tipo': 'p',
                              'corpo': ['O site já tem a <a href="protocol_thymosin-alpha-1.html">timosina alfa-1</a>, '
                                        'o <a href="proprio_thymalin.html">Thymalin</a> e os <a '
                                        'href="proprio_bioreguladores.html">bioreguladores curtos de Khavinson</a>. '
                                        'Faltavam dois fatores do timo — a timulina e a timopentina (TP-5) — e o '
                                        'Cardiogen, o bioregulador "do coração" da mesma escola russa.',
                                        'Duas ressalvas de método. <strong>Uma:</strong> <code>cardiogen</code> '
                                        'sozinho no PubMed e no ClinicalTrials.gov devolve o CardioGen-82, um gerador '
                                        'de rubídio-82 usado em exame de imagem do coração, que não tem nada a ver com '
                                        'o peptídeo. Restringi a busca com <code>AND (peptide OR Khavinson)</code>; o '
                                        'único registro da busca sem filtro no ClinicalTrials.gov é de exame de PET '
                                        'com CardioGen-82. <strong>Duas:</strong> na ANVISA, o padrão '
                                        '<code>TIMULIN</code> encontra um registro — mas de '
                                        '<strong>timostimulina</strong>, outro extrato do timo, cujo nome contém as '
                                        'mesmas letras. Publico o achado com a ressalva: não há registro de timulina.',
                                        'Nenhum número desta página veio da fonte secundária do site.']},
                             {'h': 'Quanta evidência existe, composto a composto',
                              'tipo': 'p',
                              'corpo': ['Os números abaixo foram levantados por mim em {DATA}, no PubMed e no '
                                        'ClinicalTrials.gov. A consulta de cada linha está escrita '
                                        '<strong>inteira</strong>, ao lado do número, para qualquer pessoa repetir e '
                                        'me contradizer — e para o script que reconfere as contagens deste site '
                                        'conseguir rodar todas.',
                                        'A coluna de condição <strong>não é afirmação de mecanismo</strong>: é o campo '
                                        '<em>Condition</em> copiado do maior registro de fase 3 que a própria busca '
                                        'devolveu. Quando não há registro de fase 3, a célula diz isso.'],
                              'tabela': {'cap': 'Levantamento de evidência — timo e Cardiogen',
                                         'linhas': [['Composto',
                                                     'Condição nos registros de fase 3',
                                                     'Consulta',
                                                     'Artigos no PubMed',
                                                     'Estudos no ClinicalTrials.gov'],
                                                    ['<strong>Timulina</strong>',
                                                     '<small>nenhum registro de fase 3 nesta busca</small>',
                                                     '<code>thymulin OR "serum thymic factor" OR "facteur thymique '
                                                     'serique"</code>',
                                                     '886',
                                                     '0'],
                                                    ['<strong>Timopentina (TP-5)</strong>',
                                                     '<small>Hepatocellular Carcinoma</small>',
                                                     '<code>thymopentin</code>',
                                                     '564',
                                                     '10'],
                                                    ['<strong>Cardiogen</strong>',
                                                     '<small>nenhum registro de fase 3 nesta busca</small>',
                                                     '<code>cardiogen AND (peptide OR Khavinson)</code>',
                                                     '9',
                                                     '0']]}},
                             {'h': 'O que existe de fase 3, e de quem é',
                              'tipo': 'p',
                              'corpo': ['Contagem de artigo mede atenção acadêmica, não evidência de desfecho. A '
                                        'tabela abaixo separa o que tem <strong>ensaio de fase 3 registrado</strong> — '
                                        'e mostra o maior registro que a busca devolveu, com o número de participantes '
                                        'declarado e o patrocinador. Registro não é resultado.'],
                              'tabela': {'cap': 'Ensaios registrados de fase 3 — timo e Cardiogen',
                                         'linhas': [['Composto',
                                                     'Consulta',
                                                     'Ensaios registrados de fase 3',
                                                     'O maior registro que abri'],
                                                    ['<strong>Timulina</strong>',
                                                     '<code>(thymulin OR "serum thymic factor" OR "facteur thymique '
                                                     'serique") AND AREA[Phase]PHASE3</code>',
                                                     '0',
                                                     '—'],
                                                    ['<strong>Timopentina (TP-5)</strong>',
                                                     '<code>(thymopentin) AND AREA[Phase]PHASE3</code>',
                                                     '2',
                                                     '<strong>NCT00460681</strong> · n = 220 · Fudan '
                                                     'University<br><small>Hepatocellular Carcinoma</small>'],
                                                    ['<strong>Cardiogen</strong>',
                                                     '<code>(cardiogen AND (peptide OR Khavinson)) AND '
                                                     'AREA[Phase]PHASE3</code>',
                                                     '0',
                                                     '—']]}},
                             {'h': 'Onde a conta não fecha',
                              'tipo': 'li',
                              'corpo': ['<strong>A timulina tem 886 artigos e 0 estudos registrados.</strong> Muita '
                                        'fisiologia de um fator do timo, e nenhum registro de ensaio em gente.',
                                        '<strong>A timopentina já teve nome comercial</strong> — Timunox, no título de '
                                        'registros de HIV. 7 dos 10 registros são de HIV, todos do mesmo patrocinador '
                                        'e todos sem data de início informada. O maior de fase 3 é um ensaio chinês em '
                                        'câncer de fígado, com situação desconhecida.',
                                        '<strong>O Cardiogen tem 9 artigos e 0 estudos — e só 4 dos artigos são sobre '
                                        'o peptídeo.</strong> Li os títulos: os 4 são estudos de cultura de tecido e '
                                        'de rato, de 2006 a 2010, numa revista russa de gerontologia e num boletim de '
                                        'biologia experimental. Os outros usam a palavra em outro sentido, mesmo com o '
                                        'filtro. Nenhum é ensaio em gente.']},
                             {'h': 'No Brasil',
                              'tipo': 'p',
                              'corpo': ['Busquei cada princípio ativo no <strong>dado aberto de medicamentos '
                                        'registrados da ANVISA</strong>, baixado em {DATA} — 43.596 linhas, contando '
                                        'apenas situação <strong>Ativo</strong>, no princípio ativo e no nome do '
                                        'produto, sem acento e sem diferença de caixa. A classe terapêutica é a que a '
                                        'própria base declara.'],
                              'tabela': {'cap': 'Registro na ANVISA — timo',
                                         'linhas': [['Princípio ativo',
                                                     'Padrão buscado',
                                                     'Registros ativos',
                                                     'Classe terapêutica declarada',
                                                     'Produtos'],
                                                    ['<strong>Timulina</strong>',
                                                     '<code>TIMULIN</code>',
                                                     '<strong>1</strong>',
                                                     '<small>IMUNOMODULADOR</small>',
                                                     'EXTRATO DE CÉLULAS TÍMICAS'],
                                                    ['<strong>Timopentina (TP-5)</strong>',
                                                     '<code>TIMOPENT</code>',
                                                     '<strong>0</strong>',
                                                     '<small>—</small>',
                                                     '—']]}}],
                  'nota_refs': 'Todas as contagens desta página foram levantadas por mim em {DATA}, com a consulta '
                               'declarada ao lado de cada número. As ressalvas de método estão escritas na primeira '
                               'seção, antes das tabelas. <strong>Esta página foi apurada em dia próprio</strong>, e '
                               'por isso carrega data própria.',
                  'referencias': [('API pública do ClinicalTrials.gov, versão 2 — a base de todas as contagens de '
                                   'estudo e de fase 3 desta página.',
                                   'https://clinicaltrials.gov/data-api/api'),
                                  ('E-utilities do PubMed (esearch) — a base de todas as contagens de artigo desta '
                                   'página.',
                                   'https://www.ncbi.nlm.nih.gov/books/NBK25501/'),
                                  ('Registro NCT01424774 no ClinicalTrials.gov.',
                                   'https://clinicaltrials.gov/study/NCT01424774'),
                                  ('Registro NCT00460681 no ClinicalTrials.gov.',
                                   'https://clinicaltrials.gov/study/NCT00460681'),
                                  ('Dado aberto de medicamentos registrados da ANVISA — a mesma base usada na página O '
                                   'que existe no Brasil.',
                                   'https://dados.anvisa.gov.br/dados/')]},
 'proprio_bancada': {'secoes': [{'h': 'Quatro peptídeos que nunca saíram do laboratório',
                                 'tipo': 'p',
                                 'corpo': ['O SS-20 é da mesma família do <a href="protocol_ss-31.html">SS-31 '
                                           '(elamipretida)</a>. SHLP-2 e SHLP-3 são peptídeos codificados no DNA '
                                           'mitocondrial, da mesma família da <a '
                                           'href="protocol_humanin.html">humanina</a> e do <a '
                                           'href="protocol_mots-c.html">MOTS-c</a>. O PNC-27 é um peptídeo desenhado '
                                           'para matar célula de câncer. Os quatro estão na biblioteca de loja que '
                                           'usei como lista do que faltava aqui.',
                                           'Uma ressalva de método: <code>"SS-20"</code> sozinho é sigla de muita '
                                           'coisa, e por isso a busca exige <code>mitochondria</code>, '
                                           '<code>mitochondrial</code> ou <code>Szeto</code>, o sobrenome de quem '
                                           'criou a família. O número é piso, não teto.',
                                           'Nenhum número desta página veio da fonte secundária do site.']},
                                {'h': 'Quanta evidência existe, composto a composto',
                                 'tipo': 'p',
                                 'corpo': ['Os números abaixo foram levantados por mim em {DATA}, no PubMed e no '
                                           'ClinicalTrials.gov. A consulta de cada linha está escrita '
                                           '<strong>inteira</strong>, ao lado do número, para qualquer pessoa repetir '
                                           'e me contradizer — e para o script que reconfere as contagens deste site '
                                           'conseguir rodar todas.'],
                                 'tabela': {'cap': 'Levantamento de evidência — peptídeos de bancada',
                                            'linhas': [['Composto',
                                                        'Consulta',
                                                        'Artigos no PubMed',
                                                        'Estudos no ClinicalTrials.gov'],
                                                       ['<strong>SS-20</strong>',
                                                        '<code>"SS-20" AND (mitochondria OR mitochondrial OR '
                                                        'Szeto)</code>',
                                                        '12',
                                                        '0'],
                                                       ['<strong>SHLP-2</strong>',
                                                        '<code>"SHLP2" OR "SHLP-2" OR "small humanin-like peptide '
                                                        '2"</code>',
                                                        '25',
                                                        '0'],
                                                       ['<strong>SHLP-3</strong>',
                                                        '<code>"SHLP3" OR "SHLP-3" OR "small humanin-like peptide '
                                                        '3"</code>',
                                                        '15',
                                                        '0'],
                                                       ['<strong>PNC-27</strong>',
                                                        '<code>"PNC-27"</code>',
                                                        '25',
                                                        '0']]}},
                                {'h': 'Onde a conta não fecha',
                                 'tipo': 'li',
                                 'corpo': ['<strong>Os quatro somam 77 artigos e 0 estudos registrados.</strong> Não '
                                           'existe um registro de ensaio em gente para nenhum deles, de nenhuma fase.',
                                           '<strong>O PNC-27 aparece na loja descrito como antitumoral</strong> e tem '
                                           '25 artigos e 0 estudo registrado. Li os títulos de todos: são estudos de '
                                           'célula, de estrutura da molécula e de tecido retirado de paciente, mais '
                                           'dois que não são sobre o peptídeo — a sigla coincide. Nenhum é ensaio em '
                                           'gente. Quem trata câncer com ele está fazendo um experimento sem '
                                           'protocolo, sem controle e sem ninguém medindo.',
                                           '<strong>O SHLP-2 aparece em célula, em camundongo e como marcador</strong> '
                                           '— medido no sangue em estudos de câncer de próstata e de gordura no '
                                           'fígado. Pelos títulos, nenhum dos artigos é ensaio em gente. Medir um '
                                           'peptídeo no sangue não é o mesmo que mostrar que repô-lo faz alguma '
                                           'coisa.']}],
                     'nota_refs': 'Todas as contagens desta página foram levantadas por mim em {DATA}, com a consulta '
                                  'declarada ao lado de cada número. As ressalvas de método estão escritas na primeira '
                                  'seção, antes das tabelas. <strong>Esta página foi apurada em dia próprio</strong>, '
                                  'e por isso carrega data própria.',
                     'referencias': [('API pública do ClinicalTrials.gov, versão 2 — a base de todas as contagens de '
                                      'estudo e de fase 3 desta página.',
                                      'https://clinicaltrials.gov/data-api/api'),
                                     ('E-utilities do PubMed (esearch) — a base de todas as contagens de artigo desta '
                                      'página.',
                                      'https://www.ncbi.nlm.nih.gov/books/NBK25501/')]},
 'proprio_cosmeticos': {'secoes': [{'h': 'Ingrediente de creme vendido em frasco',
                                    'tipo': 'p',
                                    'corpo': ['Os peptídeos desta página são ingredientes de cosmético, com nome '
                                              'técnico na nomenclatura internacional de ingredientes (INCI) e nome '
                                              'comercial do fabricante: argirelina (acetil hexapeptídeo-3 ou -8), '
                                              'SNAP-8 (acetil octapeptídeo-3), Matrixyl (palmitoil pentapeptídeo-4), '
                                              'Matrixyl 3000 (palmitoil tripeptídeo-1 mais palmitoil tetrapeptídeo-7), '
                                              "Matrixyl synthe'6 (palmitoil tripeptídeo-38), Syn-Coll (palmitoil "
                                              'tripeptídeo-5), Syn-Ake (dipeptídeo diaminobutiroil benzilamida '
                                              'diacetato) e Eyeseryl (acetil tetrapeptídeo-5). A correspondência entre '
                                              'nome comercial e INCI é a que os fabricantes dos ingredientes declaram '
                                              '— entre eles Lipotec (hoje da Lubrizol), DSM-Firmenich e Sederma; '
                                              'conferi em fichas técnicas de distribuidores de ingrediente, que não '
                                              'linko porque este site não linka fornecedor. Os dez estão na mesma '
                                              'biblioteca de loja que os peptídeos injetáveis. O <a '
                                              'href="protocol_ghk-cu.html">GHK-Cu</a> já tem página própria.',
                                              'Duas ressalvas de método. <strong>Uma:</strong> busquei pelo nome INCI '
                                              'e pelo comercial juntos, porque a literatura usa os dois. '
                                              '<strong>Duas:</strong> cosmético não passa pela base de medicamentos da '
                                              'ANVISA, e por isso esta página não tem a seção "No Brasil". Não '
                                              'consultei a base de cosméticos — fica declarado como lacuna, não como '
                                              'ausência.',
                                              'Nenhum número desta página veio da fonte secundária do site.']},
                                   {'h': 'Quanta evidência existe, composto a composto',
                                    'tipo': 'p',
                                    'corpo': ['Os números abaixo foram levantados por mim em {DATA}, no PubMed e no '
                                              'ClinicalTrials.gov. A consulta de cada linha está escrita '
                                              '<strong>inteira</strong>, ao lado do número, para qualquer pessoa '
                                              'repetir e me contradizer — e para o script que reconfere as contagens '
                                              'deste site conseguir rodar todas.',
                                              'A coluna de condição <strong>não é afirmação de mecanismo</strong>: é o '
                                              'campo <em>Condition</em> copiado do maior registro de fase 3 que a '
                                              'própria busca devolveu. Quando não há registro de fase 3, a célula diz '
                                              'isso.'],
                                    'tabela': {'cap': 'Levantamento de evidência — peptídeos cosméticos',
                                               'linhas': [['Composto',
                                                           'Condição nos registros de fase 3',
                                                           'Consulta',
                                                           'Artigos no PubMed',
                                                           'Estudos no ClinicalTrials.gov'],
                                                          ['<strong>Argirelina</strong>',
                                                           '<small>Wrinkles</small>',
                                                           '<code>"acetyl hexapeptide-3" OR "acetyl hexapeptide-8" OR '
                                                           'argireline</code>',
                                                           '50',
                                                           '6'],
                                                          ['<strong>SNAP-8</strong>',
                                                           '<small>nenhum registro de fase 3 nesta busca</small>',
                                                           '<code>"acetyl octapeptide-3" OR "SNAP-8"</code>',
                                                           '2',
                                                           '0'],
                                                          ['<strong>Matrixyl (palmitoil pentapeptídeo-4)</strong>',
                                                           '<small>nenhum registro de fase 3 nesta busca</small>',
                                                           '<code>"palmitoyl pentapeptide-4" OR "pal-KTTKS" OR '
                                                           '"palmitoyl-KTTKS" OR Matrixyl</code>',
                                                           '33',
                                                           '0'],
                                                          ['<strong>Palmitoil tripeptídeo-1</strong>',
                                                           '<small>nenhum registro de fase 3 nesta busca</small>',
                                                           '<code>"palmitoyl tripeptide-1" OR "pal-GHK"</code>',
                                                           '7',
                                                           '0'],
                                                          ['<strong>Palmitoil tetrapeptídeo-7</strong>',
                                                           '<small>nenhum registro de fase 3 nesta busca</small>',
                                                           '<code>"palmitoyl tetrapeptide-7" OR "pal-GQPR"</code>',
                                                           '6',
                                                           '1'],
                                                          ['<strong>Matrixyl 3000</strong>',
                                                           '<small>nenhum registro de fase 3 nesta busca</small>',
                                                           '<code>"Matrixyl 3000"</code>',
                                                           '1',
                                                           '0'],
                                                          ["<strong>Matrixyl synthe'6 (palmitoil "
                                                           'tripeptídeo-38)</strong>',
                                                           '<small>nenhum registro de fase 3 nesta busca</small>',
                                                           '<code>"palmitoyl tripeptide-38" OR "Matrixyl '
                                                           'synthe"</code>',
                                                           '3',
                                                           '0'],
                                                          ['<strong>Syn-Coll (palmitoil tripeptídeo-5)</strong>',
                                                           '<small>nenhum registro de fase 3 nesta busca</small>',
                                                           '<code>"palmitoyl tripeptide-5" OR "Syn-Coll"</code>',
                                                           '4',
                                                           '2'],
                                                          ['<strong>Syn-Ake</strong>',
                                                           '<small>nenhum registro de fase 3 nesta busca</small>',
                                                           '<code>"Syn-Ake" OR "dipeptide diaminobutyroyl benzylamide '
                                                           'diacetate"</code>',
                                                           '2',
                                                           '0'],
                                                          ['<strong>Acetil tetrapeptídeo-5</strong>',
                                                           '<small>nenhum registro de fase 3 nesta busca</small>',
                                                           '<code>"acetyl tetrapeptide-5" OR Eyeseryl</code>',
                                                           '1',
                                                           '0']]}},
                                   {'h': 'Onde a conta não fecha',
                                    'tipo': 'li',
                                    'corpo': ['<strong>A argirelina é a mais estudada, e mesmo assim são 50 artigos e '
                                              '6 estudos registrados.</strong> 3 dos 6 registros dizem no título que o '
                                              'produto é de pele — sérum, creme, uso tópico. Nenhum título fala em '
                                              'injeção.',
                                              '<strong>8 dos 10 nomes têm 7 artigos ou menos no PubMed</strong>, e 6 '
                                              "têm 4 ou menos: SNAP-8, Matrixyl 3000, Matrixyl synthe'6, Syn-Coll, "
                                              'Syn-Ake, Acetil tetrapeptídeo-5. A evidência que existe sobre eles é, '
                                              'em boa parte, a do fabricante do ingrediente.',
                                              '<strong>Ingrediente de creme não vira injetável.</strong> Um '
                                              'ingrediente pensado para ficar na superfície da pele, numa concentração '
                                              'de creme, não tem dado como injeção. Os registros que existem testam '
                                              'produto aplicado na pele.']}],
                        'nota_refs': 'Todas as contagens desta página foram levantadas por mim em {DATA}, com a '
                                     'consulta declarada ao lado de cada número. As ressalvas de método estão escritas '
                                     'na primeira seção, antes das tabelas. <strong>Esta página foi apurada em dia '
                                     'próprio</strong>, e por isso carrega data própria.',
                        'referencias': [('API pública do ClinicalTrials.gov, versão 2 — a base de todas as contagens '
                                         'de estudo e de fase 3 desta página.',
                                         'https://clinicaltrials.gov/data-api/api'),
                                        ('E-utilities do PubMed (esearch) — a base de todas as contagens de artigo '
                                         'desta página.',
                                         'https://www.ncbi.nlm.nih.gov/books/NBK25501/'),
                                        ('Registro NCT01381484 no ClinicalTrials.gov.',
                                         'https://clinicaltrials.gov/study/NCT01381484'),
                                        ('Registro NCT00942851 no ClinicalTrials.gov.',
                                         'https://clinicaltrials.gov/study/NCT00942851')]},
 'proprio_blends': {'secoes': [{'h': 'A pergunta que um blend faz',
                                'tipo': 'p',
                                'corpo': ['Um frasco com dois ou três peptídeos misturados afirma, só por existir, que '
                                          'a combinação foi pensada. A pergunta desta página é se ela foi '
                                          '<strong>estudada</strong>: se existe artigo que fale das moléculas juntas, '
                                          'e se existe ensaio registrado com as duas.',
                                          'O método é deliberadamente generoso. A consulta junta os componentes com '
                                          '<code>AND</code> — basta um artigo <em>citar</em> os nomes para entrar na '
                                          'conta, mesmo que não teste nada. Por isso o número é teto: um artigo de '
                                          'revisão que cita BPC-157 num parágrafo e TB-500 em outro conta como um. Li '
                                          'os títulos e o tipo de publicação de todos os artigos devolvidos, até 30 '
                                          'por linha, e resumo o que eles são na última coluna.',
                                          'Uma ressalva que muda uma linha inteira. <code>gonadorelin</code> no PubMed '
                                          'cai no descritor do GnRH, o hormônio que o próprio corpo produz, e a '
                                          'combinação com kisspeptina devolve 1.566 artigos de fisiologia do eixo '
                                          'reprodutivo. Os 9 registros no ClinicalTrials.gov são estudos de '
                                          'kisspeptina em puberdade atrasada, hipogonadismo e fisiologia — pelos '
                                          'títulos, nenhum testa um frasco com as duas moléculas misturadas.',
                                          'Nenhum número desta página veio da fonte secundária do site.']},
                               {'h': 'Os blends, um a um',
                                'tipo': 'p',
                                'corpo': ['Os números abaixo foram levantados por mim em {DATA}, no PubMed e no '
                                          'ClinicalTrials.gov. A consulta de cada linha está escrita '
                                          '<strong>inteira</strong>, ao lado do número, para qualquer pessoa repetir e '
                                          'me contradizer — e para o script que reconfere as contagens deste site '
                                          'conseguir rodar todas.'],
                                'tabela': {'cap': 'Levantamento de evidência — blends vendidos prontos',
                                           'linhas': [['Blend vendido pronto',
                                                       'Consulta',
                                                       'Artigos no PubMed',
                                                       'Estudos no ClinicalTrials.gov',
                                                       'O que os artigos devolvidos são'],
                                                      ['<a href="protocol_cjc-1295-dac.html">CJC-1295 DAC</a> + <a '
                                                       'href="proprio_eixo_gh.html">GHRP-2</a>',
                                                       '<code>("CJC-1295" OR "CJC 1295") AND ("GHRP-2" OR '
                                                       'pralmorelin)</code>',
                                                       '2',
                                                       '0',
                                                       '<small>uma revisão e um método de detecção antidoping em '
                                                       'cavalo</small>'],
                                                      ['<a href="protocol_sermorelin.html">Sermorelina</a> + <a '
                                                       'href="protocol_ipamorelin.html">Ipamorelina</a>',
                                                       '<code>(sermorelin) AND (ipamorelin)</code>',
                                                       '5',
                                                       '0',
                                                       '<small>revisões sobre peptídeos e doping</small>'],
                                                      ['<a href="protocol_aod-9604.html">AOD-9604</a> + <a '
                                                       'href="protocol_5-amino-1mq.html">5-Amino-1MQ</a>',
                                                       '<code>("AOD-9604" OR AOD9604) AND ("5-amino-1MQ" OR '
                                                       '"5-amino-1-methylquinolinium")</code>',
                                                       '0',
                                                       '0',
                                                       '<small>—</small>'],
                                                      ['<a href="protocol_mots-c.html">MOTS-c</a> + <a '
                                                       'href="protocol_nad-plus.html">NAD+</a>',
                                                       '<code>("MOTS-c" OR MOTSc) AND ("nicotinamide adenine '
                                                       'dinucleotide" OR NAD)</code>',
                                                       '2',
                                                       '0',
                                                       '<small>dois estudos que medem marcadores em vesículas do '
                                                       'sangue, sem administrar nada</small>'],
                                                      ['<a href="protocol_epitalon.html">Epitalon</a> + <a '
                                                       'href="protocol_dsip.html">DSIP</a>',
                                                       '<code>(epitalon OR epithalon OR "AEDG peptide") AND ("delta '
                                                       'sleep-inducing peptide" OR DSIP)</code>',
                                                       '3',
                                                       '0',
                                                       '<small>uma revisão e estudos russos em camundongo e em '
                                                       'prevenção de câncer</small>'],
                                                      ['<a href="protocol_thymosin-alpha-1.html">Timosina alfa-1</a> + '
                                                       '<a href="protocol_bpc-157.html">BPC-157</a>',
                                                       '<code>("thymosin alpha 1" OR thymalfasin) AND ("BPC-157" OR '
                                                       '"BPC 157")</code>',
                                                       '1',
                                                       '0',
                                                       '<small>uma revisão</small>'],
                                                      ['<a href="protocol_tb-500.html">TB-500</a> + <a '
                                                       'href="protocol_ghk-cu.html">GHK-Cu</a>',
                                                       '<code>("TB-500" OR "thymosin beta 4" OR "thymosin beta-4") AND '
                                                       '("GHK-Cu" OR "GHK copper")</code>',
                                                       '6',
                                                       '0',
                                                       '<small>revisões de medicina esportiva e regenerativa</small>'],
                                                      ['<a href="protocol_igf-1-lr3.html">IGF-1 LR3</a> + <a '
                                                       'href="proprio_gh_miostatina.html">PEG-MGF</a>',
                                                       '<code>("IGF-1 LR3" OR "LR3 IGF-1" OR "LR3-IGF-I") AND '
                                                       '("PEG-MGF" OR "mechano growth factor")</code>',
                                                       '1',
                                                       '0',
                                                       '<small>uma revisão</small>'],
                                                      ['<a href="protocol_bremelanotide-pt-141.html">PT-141</a> + <a '
                                                       'href="protocol_kisspeptin.html">Kisspeptina</a>',
                                                       '<code>(bremelanotide OR "PT-141") AND (kisspeptin)</code>',
                                                       '0',
                                                       '0',
                                                       '<small>—</small>'],
                                                      ['<a href="protocol_bpc-157.html">BPC-157</a> + <a '
                                                       'href="protocol_ghk-cu.html">GHK-Cu</a> + <a '
                                                       'href="protocol_kpv.html">KPV</a>',
                                                       '<code>("BPC-157" OR "BPC 157") AND ("GHK-Cu" OR "GHK copper") '
                                                       'AND ("Lys-Pro-Val" OR "KPV peptide" OR "KPV '
                                                       'tripeptide")</code>',
                                                       '0',
                                                       '0',
                                                       '<small>—</small>'],
                                                      ['<a href="protocol_bpc-157.html">BPC-157</a> + <a '
                                                       'href="protocol_kpv.html">KPV</a> + <a '
                                                       'href="proprio_intestino.html">Larazotida</a>',
                                                       '<code>("BPC-157" OR "BPC 157") AND ("Lys-Pro-Val" OR "KPV '
                                                       'peptide" OR "KPV tripeptide") AND (larazotide)</code>',
                                                       '0',
                                                       '0',
                                                       '<small>—</small>'],
                                                      ['<a href="protocol_cjc-1295-dac.html">CJC-1295</a> + <a '
                                                       'href="protocol_ipamorelin.html">Ipamorelina</a> + <a '
                                                       'href="proprio_eixo_gh.html">GHRP-2</a>',
                                                       '<code>("CJC-1295" OR "CJC 1295") AND (ipamorelin) AND '
                                                       '("GHRP-2" OR pralmorelin)</code>',
                                                       '2',
                                                       '0',
                                                       '<small>uma revisão e um método de detecção antidoping em '
                                                       'cavalo</small>'],
                                                      ['<a href="protocol_igf-1-lr3.html">IGF-1 LR3</a> + <a '
                                                       'href="protocol_bpc-157.html">BPC-157</a>',
                                                       '<code>("IGF-1 LR3" OR "LR3 IGF-1" OR "LR3-IGF-I") AND '
                                                       '("BPC-157" OR "BPC 157")</code>',
                                                       '0',
                                                       '0',
                                                       '<small>—</small>'],
                                                      ['<a href="proprio_gh_miostatina.html">Folistatina-344</a> + <a '
                                                       'href="proprio_gh_miostatina.html">ACE-031</a>',
                                                       '<code>(follistatin) AND ("ACE-031" OR ramatercept)</code>',
                                                       '1',
                                                       '0',
                                                       '<small>uma revisão japonesa sobre anticorpo '
                                                       'antimiostatina</small>'],
                                                      ['<a href="proprio_eixo_gh.html">Hexarelina</a> + <a '
                                                       'href="protocol_cjc-1295-dac.html">CJC-1295</a>',
                                                       '<code>(hexarelin) AND ("CJC-1295" OR "CJC 1295")</code>',
                                                       '2',
                                                       '0',
                                                       '<small>uma revisão e um método de detecção antidoping em '
                                                       'cavalo</small>'],
                                                      ['<a href="proprio_eixo_gh.html">MK-677</a> + <a '
                                                       'href="protocol_ipamorelin.html">Ipamorelina</a>',
                                                       '<code>(ibutamoren OR "MK-677" OR "MK-0677") AND '
                                                       '(ipamorelin)</code>',
                                                       '6',
                                                       '0',
                                                       '<small>revisões, química de moléculas híbridas e um estudo em '
                                                       'rata com ipamorelina e GHRP-6</small>'],
                                                      ['<a href="protocol_tirzepatide.html">Tirzepatida</a> + <a '
                                                       'href="protocol_bpc-157.html">BPC-157</a>',
                                                       '<code>(tirzepatide) AND ("BPC-157" OR "BPC 157")</code>',
                                                       '3',
                                                       '0',
                                                       '<small>revisões sobre biohacking e mercado de '
                                                       'manipulados</small>'],
                                                      ['<a href="protocol_semaglutide.html">Semaglutida</a> + <a '
                                                       'href="protocol_mots-c.html">MOTS-c</a>',
                                                       '<code>(semaglutide) AND ("MOTS-c" OR MOTSc)</code>',
                                                       '1',
                                                       '0',
                                                       '<small>um estudo de obesidade materna em modelo '
                                                       'animal</small>'],
                                                      ['<a href="protocol_survodutide.html">Survodutida</a> + <a '
                                                       'href="protocol_cagrilintide.html">Cagrilintida</a>',
                                                       '<code>(survodutide) AND (cagrilintide)</code>',
                                                       '10',
                                                       '0',
                                                       '<small>revisões de remédios para obesidade, que citam as duas '
                                                       'moléculas separadas</small>'],
                                                      ['<a href="protocol_aod-9604.html">AOD-9604</a> + <a '
                                                       'href="proprio_metabolismo.html">L-carnitina</a> + <a '
                                                       'href="protocol_5-amino-1mq.html">5-Amino-1MQ</a>',
                                                       '<code>("AOD-9604" OR AOD9604) AND (carnitine OR levocarnitine) '
                                                       'AND ("5-amino-1MQ" OR "5-amino-1-methylquinolinium")</code>',
                                                       '0',
                                                       '0',
                                                       '<small>—</small>'],
                                                      ['<a href="protocol_mots-c.html">MOTS-c</a> + <a '
                                                       'href="protocol_ss-31.html">SS-31</a> + <a '
                                                       'href="protocol_nad-plus.html">NAD+</a>',
                                                       '<code>("MOTS-c" OR MOTSc) AND (elamipretide OR "SS-31") AND '
                                                       '("nicotinamide adenine dinucleotide" OR NAD)</code>',
                                                       '0',
                                                       '0',
                                                       '<small>—</small>'],
                                                      ['<a href="proprio_bancada.html">SHLP-2</a> + <a '
                                                       'href="protocol_humanin.html">Humanina</a> + <a '
                                                       'href="protocol_mots-c.html">MOTS-c</a>',
                                                       '<code>("SHLP2" OR "SHLP-2" OR "small humanin-like peptide 2") '
                                                       'AND (humanin) AND ("MOTS-c" OR MOTSc)</code>',
                                                       '8',
                                                       '0',
                                                       '<small>revisões e estudos que medem os peptídeos '
                                                       'mitocondriais, sem administrar a combinação</small>'],
                                                      ['<a href="protocol_epitalon.html">Epitalon</a> + <a '
                                                       'href="protocol_ghk-cu.html">GHK-Cu</a>',
                                                       '<code>(epitalon OR epithalon OR "AEDG peptide") AND ("GHK-Cu" '
                                                       'OR "GHK copper")</code>',
                                                       '2',
                                                       '0',
                                                       '<small>revisões</small>'],
                                                      ['<a href="protocol_nad-plus.html">NAD+</a> + <a '
                                                       'href="protocol_5-amino-1mq.html">5-Amino-1MQ</a>',
                                                       '<code>("nicotinamide adenine dinucleotide" OR NAD) AND '
                                                       '("5-amino-1MQ" OR "5-amino-1-methylquinolinium")</code>',
                                                       '1',
                                                       '0',
                                                       '<small>um estudo de câncer sobre a enzima NNMT</small>'],
                                                      ['<a href="proprio_geroprotetores.html">Klotho</a> + <a '
                                                       'href="protocol_epitalon.html">Epitalon</a>',
                                                       '<code>(klotho) AND (epitalon OR epithalon OR "AEDG '
                                                       'peptide")</code>',
                                                       '0',
                                                       '0',
                                                       '<small>—</small>'],
                                                      ['<a href="proprio_neuro_faltavam.html">N-acetil semax '
                                                       'amidato</a> + <a href="proprio_neuro_faltavam.html">N-acetil '
                                                       'selank amidato</a>',
                                                       '<code>("N-acetyl semax" OR "NA-Semax" OR "semax amidate") AND '
                                                       '("N-acetyl selank" OR "NA-Selank" OR "selank amidate")</code>',
                                                       '0',
                                                       '0',
                                                       '<small>—</small>'],
                                                      ['<a href="protocol_semax.html">Semax</a> + <a '
                                                       'href="protocol_selank.html">Selank</a> + <a '
                                                       'href="protocol_bpc-157.html">BPC-157</a>',
                                                       '<code>(semax) AND (selank) AND ("BPC-157" OR "BPC 157")</code>',
                                                       '1',
                                                       '0',
                                                       '<small>uma revisão</small>'],
                                                      ['<a href="protocol_cerebrolysin.html">Cerebrolisina</a> + <a '
                                                       'href="protocol_semax.html">Semax</a>',
                                                       '<code>(cerebrolysin) AND (semax)</code>',
                                                       '3',
                                                       '0',
                                                       '<small>uma revisão russa, um estudo em célula de rato e um '
                                                       'estudo de Semax em AVC que cita a cerebrolisina</small>'],
                                                      ['<a href="proprio_neuro_novos.html">Dihexa</a> + <a '
                                                       'href="proprio_neuro_novos.html">P021</a>',
                                                       '<code>(dihexa) AND ("P021")</code>',
                                                       '0',
                                                       '0',
                                                       '<small>—</small>'],
                                                      ['<a href="protocol_bremelanotide-pt-141.html">PT-141</a> + <a '
                                                       'href="protocol_oxytocin.html">Ocitocina</a>',
                                                       '<code>(bremelanotide OR "PT-141") AND (oxytocin)</code>',
                                                       '6',
                                                       '0',
                                                       '<small>revisões de disfunção sexual e um estudo em tecido de '
                                                       'coelho</small>'],
                                                      ['<a href="protocol_kisspeptin.html">Kisspeptina</a> + <a '
                                                       'href="proprio_musculo_hpg.html">Gonadorelina</a>',
                                                       '<code>(kisspeptin) AND (gonadorelin)</code>',
                                                       '1.566',
                                                       '9',
                                                       '<small>fisiologia do eixo reprodutivo — ver a ressalva no topo '
                                                       'da página</small>'],
                                                      ['<a href="protocol_ghk-cu.html">GHK-Cu</a> + <a '
                                                       'href="proprio_cosmeticos.html">Matrixyl synthe\'6</a> + <a '
                                                       'href="proprio_cosmeticos.html">Syn-Coll</a>',
                                                       '<code>("GHK-Cu" OR "GHK copper") AND ("palmitoyl '
                                                       'tripeptide-38") AND ("palmitoyl tripeptide-5" OR '
                                                       '"Syn-Coll")</code>',
                                                       '0',
                                                       '0',
                                                       '<small>—</small>'],
                                                      ['<a href="protocol_glutathione.html">Glutationa</a> + <a '
                                                       'href="protocol_ghk-cu.html">GHK-Cu</a>',
                                                       '<code>(glutathione) AND ("GHK-Cu" OR "GHK copper")</code>',
                                                       '7',
                                                       '0',
                                                       '<small>estudos de química do cobre, sem uso em '
                                                       'gente</small>']]}},
                               {'h': 'Onde a conta não fecha',
                                'tipo': 'li',
                                'corpo': ['<strong>32 dos 33 blends têm zero estudo registrado no '
                                          'ClinicalTrials.gov.</strong> O único que não zera é kisspeptina com '
                                          'gonadorelina, pelos motivos da ressalva acima.',
                                          '<strong>11 dos 33 não têm nem um artigo que cite os componentes '
                                          'juntos.</strong> Entre eles, o "triplo de oxidação de gordura" (AOD-9604, '
                                          'L-carnitina e 5-Amino-1MQ), o "triplo mitocondrial" (MOTS-c, SS-31 e NAD+) '
                                          'e o protocolo de barreira intestinal (BPC-157, KPV e larazotida).',
                                          '<strong>Nos outros, o que aparece é revisão.</strong> Dos artigos que citam '
                                          'os componentes juntos, nenhum, pelo título, é ensaio que tenha dado a '
                                          'combinação a pessoas e medido o resultado.',
                                          '<strong>Blend não é soma.</strong> Dois peptídeos sem estudo misturados num '
                                          'frasco não viram um produto com o dobro da evidência: viram um produto com '
                                          'nenhuma, mais a incerteza de como os dois se comportam juntos na mesma '
                                          'solução.']},
                               {'h': 'Os blends que este site já tinha',
                                'tipo': 'p',
                                'corpo': ['Estes estavam na lista da loja e já tinham página aqui: <a '
                                          'href="stacks_wolverine-stack.html">BPC-157 + TB-500</a>, <a '
                                          'href="stacks_cjc-1295-ipamorelin-gh-pulse-stack.html">CJC-1295 + '
                                          'ipamorelina</a>, <a href="stacks_tesamorelin-ipamorelin.html">tesamorelina '
                                          '+ ipamorelina</a>, <a '
                                          'href="stacks_cagrilintide-tirzepatide.html">tirzepatida + cagrilintida</a>, '
                                          '<a href="stacks_cagrisema.html">semaglutida + cagrilintida</a>, <a '
                                          'href="stacks_cagrilintide-retatrutide.html">retatrutida + cagrilintida</a>, '
                                          '<a href="stacks_russian-nootropic-stack.html">Semax + Selank</a>, <a '
                                          'href="stacks_klow-stack.html">KLOW</a> e <a '
                                          'href="stacks_glow-stack.html">GLOW</a> (BPC-157 + TB-500 + GHK-Cu). O '
                                          'Matrixyl 3000, que a loja lista como blend, está na <a '
                                          'href="proprio_cosmeticos.html">página dos peptídeos cosméticos</a>.']}],
                    'nota_refs': 'Todas as contagens desta página foram levantadas por mim em {DATA}, com a consulta '
                                 'declarada ao lado de cada número. As ressalvas de método estão escritas na primeira '
                                 'seção, antes das tabelas. <strong>Esta página foi apurada em dia próprio</strong>, e '
                                 'por isso carrega data própria.',
                    'referencias': [('API pública do ClinicalTrials.gov, versão 2 — a base de todas as contagens de '
                                     'estudo e de fase 3 desta página.',
                                     'https://clinicaltrials.gov/data-api/api'),
                                    ('E-utilities do PubMed (esearch) — a base de todas as contagens de artigo desta '
                                     'página.',
                                     'https://www.ncbi.nlm.nih.gov/books/NBK25501/')]}})
