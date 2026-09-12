# -*- coding: utf-8 -*-
"""Calvície — o antigo e o que está chegando: levantamento de fonte primaria.

Apurado em 12 de setembro de 2026, num dia proprio -- por isso importa
DATA_NOVAS_CLASSES e nao DATA_APURACAO.

Nome de arquivo descritivo, e nao proprios20/21, de proposito: este repo
tem sessoes paralelas criando modulos numerados ao mesmo tempo.
"""

from datas import DATA_NOVAS_CLASSES as _DT

CALVICIE = {
"proprio_calvicie": dict(
    secoes=[
        dict(h="Quatro doenças, uma palavra", tipo="p", corpo=[
                    "Antes de qualquer número: <strong>alopecia androgenética</strong> (o padrão masculino e feminino), <strong>areata</strong> (autoimune, em placas), <strong>eflúvio telógeno</strong> (queda difusa, pós-parto, tireoide, dieta) e as <strong>cicatriciais</strong>, como a frontal fibrosante, são doenças diferentes. A busca desta página cruza cada tratamento com <code>alopecia</code> ou <code>hair loss</code> justamente para não misturar a literatura de hipertensão do minoxidil com a de cabelo.",
            "Três linhas fogem desse cruzamento de propósito, e a consulta declarada mostra: clascoterona, ritlecitinibe e deuruxolitinibe foram buscados pelo nome puro, porque o nome já é específico o bastante. O baricitinibe, que é usado em muita coisa, foi cruzado com <code>\"alopecia areata\"</code> — sem isso, o número seria o da artrite.",
            "A coluna de condição, como no resto do site, é o campo <em>Condition</em> copiado dos registros de fase 3 que a própria busca devolveu. É onde fica visível que baricitinibe, ritlecitinibe e deuruxolitinibe estão em <strong>areata</strong>, e que minoxidil, finasterida e clascoterona estão em <strong>androgenética</strong>.",
            "Nenhum número desta página veio da fonte secundária do site.",
                ]),
        dict(h="Quanta evidência existe, composto a composto", tipo="p", corpo=[
                    f"Os números abaixo foram levantados por mim em {_DT}, no PubMed e no ClinicalTrials.gov. A consulta de cada linha está escrita <strong>inteira</strong>, ao lado do número, para qualquer pessoa repetir e me contradizer — e para o script que reconfere as contagens deste site conseguir rodar todas.",
            "A coluna de condição <strong>não é afirmação de mecanismo</strong>: é o campo <em>Condition</em> copiado dos registros de fase 3 que a própria busca devolveu. Quando não há registro de fase 3, a célula diz isso.",
                ], tabela=dict(cap="Levantamento de evidência — tratamentos de calvície", linhas=[
                    ["Composto", "Condição nos registros de fase 3", "Consulta", "Artigos no PubMed", "Estudos no ClinicalTrials.gov"],
            ["<strong>Minoxidil topico</strong>", "<small>Androgenic Alopecia; Androgenetic Alopecia; Female Pattern Alopecia</small>", "<code>minoxidil AND (alopecia OR \"hair loss\")</code>", "1.919", "90"],
            ["<strong>Minoxidil oral</strong>", "<small>Androgenetic Alopecia; Androgenetic Alopecia (AGA); Androgenic Alopecia; Female Pattern Baldness</small>", "<code>\"oral minoxidil\" AND (alopecia OR \"hair loss\")</code>", "282", "9"],
            ["<strong>Finasterida</strong>", "<small>Androgenic Alopecia; Androgenetic Alopecia</small>", "<code>finasteride AND (alopecia OR \"hair loss\")</code>", "1.058", "20"],
            ["<strong>Dutasterida</strong>", "<small>Alopecia</small>", "<code>dutasteride AND (alopecia OR \"hair loss\")</code>", "279", "10"],
            ["<strong>Espironolactona</strong>", "<small>nenhum registro de fase 3 nesta busca</small>", "<code>spironolactone AND (alopecia OR \"hair loss\")</code>", "176", "2"],
            ["<strong>Bicalutamida</strong>", "<small>nenhum registro de fase 3 nesta busca</small>", "<code>bicalutamide AND (alopecia OR \"hair loss\")</code>", "42", "0"],
            ["<strong>Clascoterona</strong>", "<small>Acne Vulgaris; Alopecia; Androgenetic</small>", "<code>clascoterone</code>", "93", "22"],
            ["<strong>Pirilutamida</strong>", "<small>Androgenetic Alopecia; Androgenetic Alopecia (AGA)</small>", "<code>pirilutamide OR \"KX-826\"</code>", "1", "7"],
            ["<strong>PP405</strong>", "<small>nenhum registro de fase 3 nesta busca</small>", "<code>\"PP405\"</code>", "1", "1"],
            ["<strong>VDPHL01</strong>", "<small>Androgenetic Alopecia; AGA; Male Pattern Baldness; Androgenetic Alopecia (AGA)</small>", "<code>VDPHL01</code>", "0", "4"],
            ["<strong>Baricitinibe</strong>", "<small>Alopecia Areata; Areata Alopecia; Alopecia; Hypotrichosis</small>", "<code>baricitinib AND \"alopecia areata\"</code>", "332", "12"],
            ["<strong>Ritlecitinibe</strong>", "<small>Stable Nonsegmental Vitiligo; Active Nonsegmental Vitiligo; Severe Alopecia Areata; Alopecia Areata</small>", "<code>ritlecitinib</code>", "276", "34"],
            ["<strong>Deuruxolitinibe</strong>", "<small>Alopecia Areata</small>", "<code>deuruxolitinib</code>", "49", "4"],
            ["<strong>PRP capilar</strong>", "<small>nenhum registro de fase 3 nesta busca</small>", "<code>\"platelet-rich plasma\" AND (alopecia OR \"hair loss\")</code>", "533", "42"],
            ["<strong>Microagulhamento</strong>", "<small>Androgenetic Alopecia</small>", "<code>microneedling AND (alopecia OR \"hair loss\")</code>", "324", "28"],
            ["<strong>Laser de baixa intensidade</strong>", "<small>nenhum registro de fase 3 nesta busca</small>", "<code>\"low-level laser\" AND (alopecia OR \"hair loss\")</code>", "113", "10"],
            ["<strong>Transplante capilar</strong>", "<small>nenhum registro de fase 3 nesta busca</small>", "<code>\"hair transplantation\"</code>", "1.655", "18"],
            ["<strong>Exossomo capilar</strong>", "<small>Androgenetic Alopecia; Exosomes</small>", "<code>exosome AND (alopecia OR \"hair loss\")</code>", "173", "16"],
                ])),
        dict(h="O que existe de fase 3, e de quem é", tipo="p", corpo=[
                    "Contagem de artigo mede atenção acadêmica, não evidência de desfecho. A tabela abaixo separa o que tem <strong>ensaio de fase 3 registrado</strong> — e mostra o maior registro que a busca devolveu em cada linha, com o número de participantes declarado e o patrocinador.",
            "Registro não é resultado. Um ensaio de fase 3 recrutando é intenção declarada com dinheiro atrás, e nada mais que isso.",
                ], tabela=dict(cap="Ensaios de fase 3 registrados — tratamentos de calvície", linhas=[
                    ["Composto", "Consulta", "Ensaios registrados de fase 3", "O maior registro que abri"],
            ["<strong>Minoxidil topico</strong>", "<code>(minoxidil AND (alopecia OR \"hair loss\")) AND AREA[Phase]PHASE3</code>", "21", "<strong>NCT07435012</strong> · n = 420 · Triple Hair Inc<br><small>Androgenic Alopecia</small>"],
            ["<strong>Minoxidil oral</strong>", "<code>(\"oral minoxidil\" AND (alopecia OR \"hair loss\")) AND AREA[Phase]PHASE3</code>", "3", "<strong>NCT05888922</strong> · n = 520 · Industrial Farmacéutica Cantabria, S.A.<br><small>Androgenetic Alopecia, Female Pattern Baldness</small>"],
            ["<strong>Finasterida</strong>", "<code>(finasteride AND (alopecia OR \"hair loss\")) AND AREA[Phase]PHASE3</code>", "8", "<strong>NCT07435012</strong> · n = 420 · Triple Hair Inc<br><small>Androgenic Alopecia</small>"],
            ["<strong>Dutasterida</strong>", "<code>(dutasteride AND (alopecia OR \"hair loss\")) AND AREA[Phase]PHASE3</code>", "5", "<strong>NCT00441116</strong> · n = 153 · GlaxoSmithKline<br><small>Alopecia</small>"],
            ["<strong>Espironolactona</strong>", "<code>(spironolactone AND (alopecia OR \"hair loss\")) AND AREA[Phase]PHASE3</code>", "0", "—"],
            ["<strong>Bicalutamida</strong>", "<code>(bicalutamide AND (alopecia OR \"hair loss\")) AND AREA[Phase]PHASE3</code>", "0", "—"],
            ["<strong>Clascoterona</strong>", "<code>(clascoterone) AND AREA[Phase]PHASE3</code>", "7", "<strong>NCT05914805</strong> · n = 762 · Cassiopea SpA<br><small>Alopecia, Androgenetic</small>"],
            ["<strong>Pirilutamida</strong>", "<code>(pirilutamide OR \"KX-826\") AND AREA[Phase]PHASE3</code>", "2", "<strong>NCT06622824</strong> · n = 756 · Suzhou Kintor Pharmaceutical Inc,<br><small>Androgenetic Alopecia (AGA)</small>"],
            ["<strong>PP405</strong>", "<code>(\"PP405\") AND AREA[Phase]PHASE3</code>", "0", "—"],
            ["<strong>VDPHL01</strong>", "<code>(VDPHL01) AND AREA[Phase]PHASE3</code>", "3", "<strong>NCT07146022</strong> · n = 552 · Veradermics, Inc.<br><small>Androgenetic Alopecia (AGA), Androgenetic Alopecia, AGA</small>"],
            ["<strong>Baricitinibe</strong>", "<code>(baricitinib AND \"alopecia areata\") AND AREA[Phase]PHASE3</code>", "3", "<strong>NCT03570749</strong> · n = 784 · Eli Lilly and Company<br><small>Alopecia Areata</small>"],
            ["<strong>Ritlecitinibe</strong>", "<code>(ritlecitinib) AND AREA[Phase]PHASE3</code>", "9", "<strong>NCT03732807</strong> · n = 718 · Pfizer<br><small>Alopecia Areata</small>"],
            ["<strong>Deuruxolitinibe</strong>", "<code>(deuruxolitinib) AND AREA[Phase]PHASE3</code>", "2", "<strong>NCT07133308</strong> · n = 355 · Sun Pharmaceutical Industries, Inc.<br><small>Alopecia Areata</small>"],
            ["<strong>PRP capilar</strong>", "<code>(\"platelet-rich plasma\" AND (alopecia OR \"hair loss\")) AND AREA[Phase]PHASE3</code>", "0", "—"],
            ["<strong>Microagulhamento</strong>", "<code>(microneedling AND (alopecia OR \"hair loss\")) AND AREA[Phase]PHASE3</code>", "1", "<strong>NCT05989165</strong> · n = 36 · Indonesia University<br><small>Androgenetic Alopecia</small>"],
            ["<strong>Laser de baixa intensidade</strong>", "<code>(\"low-level laser\" AND (alopecia OR \"hair loss\")) AND AREA[Phase]PHASE3</code>", "0", "—"],
            ["<strong>Transplante capilar</strong>", "<code>(\"hair transplantation\") AND AREA[Phase]PHASE3</code>", "0", "—"],
            ["<strong>Exossomo capilar</strong>", "<code>(exosome AND (alopecia OR \"hair loss\")) AND AREA[Phase]PHASE3</code>", "1", "<strong>NCT06539273</strong> · n = 30 · Yeditepe University Hospital<br><small>Androgenetic Alopecia, Exosomes</small>"],
                ])),
        dict(h="Onde a conta não fecha", tipo="li", corpo=[
                    "<strong>A clascoterona está registrada no Brasil, e não é para cabelo.</strong> 1 registro ativo, WINLEVI, classe produtos anti-acne. Existir o princípio ativo na farmácia não é o mesmo que existir a apresentação e a indicação de alopecia — e é exatamente aí que o mercado cinza costuma se instalar.",
            "<strong>PP405 é o caso mais claro de nome vendido antes de existir.</strong> 1 artigo no PubMed, 1 estudo registrado, 0 de fase 3, e nenhum registro na base da ANVISA. Não existe produto: existe um programa de pesquisa, e um nome que já circula à venda.",
            "<strong>VDPHL01 tem o padrão oposto: 0 artigos no PubMed e 3 ensaios de fase 3</strong>, os dois maiores com 552 e 480 participantes, patrocínio da Veradermics. Quem procurar no PubMed conclui que não existe; quem procurar no registro vê mil pessoas recrutadas.",
            "<strong>A pirilutamida é o mesmo padrão, com patrocinador chinês.</strong> 1 artigo indexado, 2 ensaios de fase 3 com 756 e 740 participantes, patrocínio da Kintor. Nenhum registro ativo na ANVISA.",
            "<strong>Os procedimentos têm literatura e quase nenhum ensaio de fase 3.</strong> PRP capilar tem 533 artigos e 0 ensaios de fase 3; o transplante tem 1.655 artigos e 0. Volume de publicação, aqui, mede prática clínica — não programa de registro.",
            "<strong>Exossomo capilar: 173 artigos, 16 estudos registrados e 1 de fase 3, com 30 participantes.</strong> O problema de identidade do frasco está descrito na <a href=\"proprio_exossomos.html\">página de exossomos</a>, e vale inteiro aqui: injetável humano sem registro não é cosmético.",
            "<strong>6 das 18 linhas não têm nenhum ensaio de fase 3 registrado.</strong> São Espironolactona, Bicalutamida, PP405, PRP capilar, Laser de baixa intensidade, Transplante capilar.",
                ]),
        dict(h="No Brasil", tipo="p", corpo=[
                    f"Busquei cada princípio ativo no <strong>dado aberto de medicamentos registrados da ANVISA</strong>, baixado em {_DT} — 43.508 linhas, contando apenas situação <strong>Ativo</strong>. A coluna de classe terapêutica é a que a própria base declara.",
            "Ela é o dado mais útil desta tabela. O minoxidil aparece na classe <strong>antialopecia</strong>; a finasterida e a dutasterida, como <strong>inibidor da alfa-redutase</strong> e produtos de trato urinário; a espironolactona, como <strong>diurético</strong>; a bicalutamida, como <strong>antineoplásico</strong>; o ritlecitinibe, como <strong>imunossupressor</strong>. Três dessas classes — diurético, antineoplásico, imunossupressor — não são classes de cabelo, e é a própria base que diz isso, sem que eu precise afirmar nada sobre a bula de cada produto.",
            "Os procedimentos — PRP, microagulhamento, laser, transplante — não entram nesta tabela porque não têm princípio ativo. Não estar aqui não é sinal de nada sobre eles.",
                ], tabela=dict(cap="Registro na ANVISA — tratamentos de calvície", linhas=[
                    ["Princípio ativo", "Padrão buscado", "Registros ativos", "Classe terapêutica declarada", "Produtos"],
            ["<strong>Minoxidil</strong>", "<code>MINOXIDIL</code>", "<strong>23</strong>", "<small>ANTIALOPECIA</small>", "ACTFIO, ALLOVITA, ALOXIDIL, CAPITRAT MEN, CAPY, DIXIL"],
            ["<strong>Finasterida</strong>", "<code>FINASTERID</code>", "<strong>27</strong>", "<small>INIBIDOR DA ALFA-REDUTASE; OUTROS PRODUTOS COM ACAO NO TRATO URINARIO; OUTROS PRODUTOS COM ACAO NA PELE E MUCOSAS</small>", "DUOMO HP, EXCALV, FENDICAL, FINALOP, FINARID, FINASTERIDA"],
            ["<strong>Dutasterida</strong>", "<code>DUTASTERID</code>", "<strong>15</strong>", "<small>OUTROS PRODUTOS COM ACAO NO TRATO URINARIO; INIBIDOR DA ALFA-REDUTASE</small>", "AVODART, COMBODART, DASTENE, DASTENE DUO, DROALFA, DUTAM"],
            ["<strong>Espironolactona</strong>", "<code>ESPIRONOLACTONA</code>", "<strong>8</strong>", "<small>DIURETICOS SIMPLES; DIURETICOS</small>", "ALDACTONE, DIACQUA, ESPIRONOLACTONA"],
            ["<strong>Bicalutamida</strong>", "<code>BICALUTAMID</code>", "<strong>6</strong>", "<small>ANTINEOPLASICO</small>", "BICALUTAMIDA, BYCAL, BYCAL 150, CASODEX"],
            ["<strong>Clascoterona</strong>", "<code>CLASCOTERON</code>", "<strong>1</strong>", "<small>PRODUTOS ANTI-ACNE</small>", "WINLEVI"],
            ["<strong>Pirilutamida</strong>", "<code>PIRILUTAMID</code>", "<strong>0</strong>", "<small>—</small>", "—"],
            ["<strong>Baricitinibe</strong>", "<code>BARICITINIB</code>", "<strong>1</strong>", "<small>—</small>", "OLUMIANT"],
            ["<strong>Ritlecitinibe</strong>", "<code>RITLECITINIB</code>", "<strong>1</strong>", "<small>IMUNOSUPRESSOR</small>", "LITFULO"],
            ["<strong>Deuruxolitinibe</strong>", "<code>DEURUXOLITINIB</code>", "<strong>0</strong>", "<small>—</small>", "—"],
                ])),
    ],
    nota_refs=("T"
               "o"
               "d"
               "a"
               "s"
               " "
               "a"
               "s"
               " "
               "c"
               "o"
               "n"
               "t"
               "a"
               "g"
               "e"
               "n"
               "s"
               " "
               "d"
               "e"
               "s"
               "t"
               "a"
               " "
               "p"
               "á"
               "g"
               "i"
               "n"
               "a"
               " "
               "f"
               "o"
               "r"
               "a"
               "m"
               " "
               "l"
               "e"
               "v"
               "a"
               "n"
               "t"
               "a"
               "d"
               "a"
               "s"
               " "
               "p"
               "o"
               "r"
               " "
               "m"
               "i"
               "m"
               " "
               "e"
               "m"
               " "
               "«"
               "D"
               "T"
               "»"
               ","
               " "
               "c"
               "o"
               "m"
               " "
               "a"
               " "
               "c"
               "o"
               "n"
               "s"
               "u"
               "l"
               "t"
               "a"
               " "
               "d"
               "e"
               "c"
               "l"
               "a"
               "r"
               "a"
               "d"
               "a"
               " "
               "a"
               "o"
               " "
               "l"
               "a"
               "d"
               "o"
               " "
               "d"
               "e"
               " "
               "c"
               "a"
               "d"
               "a"
               " "
               "n"
               "ú"
               "m"
               "e"
               "r"
               "o"
               "."
               " "
               "A"
               "s"
               " "
               "i"
               "n"
               "d"
               "i"
               "c"
               "a"
               "ç"
               "õ"
               "e"
               "s"
               " "
               "c"
               "i"
               "t"
               "a"
               "d"
               "a"
               "s"
               " "
               "v"
               "ê"
               "m"
               " "
               "d"
               "a"
               " "
               "c"
               "l"
               "a"
               "s"
               "s"
               "e"
               " "
               "t"
               "e"
               "r"
               "a"
               "p"
               "ê"
               "u"
               "t"
               "i"
               "c"
               "a"
               " "
               "d"
               "e"
               "c"
               "l"
               "a"
               "r"
               "a"
               "d"
               "a"
               " "
               "n"
               "o"
               " "
               "d"
               "a"
               "d"
               "o"
               " "
               "a"
               "b"
               "e"
               "r"
               "t"
               "o"
               " "
               "d"
               "a"
               " "
               "A"
               "N"
               "V"
               "I"
               "S"
               "A"
               " "
               "e"
               " "
               "d"
               "o"
               " "
               "c"
               "a"
               "m"
               "p"
               "o"
               " "
               "d"
               "e"
               " "
               "c"
               "o"
               "n"
               "d"
               "i"
               "ç"
               "ã"
               "o"
               " "
               "d"
               "o"
               "s"
               " "
               "r"
               "e"
               "g"
               "i"
               "s"
               "t"
               "r"
               "o"
               "s"
               " "
               "d"
               "e"
               " "
               "f"
               "a"
               "s"
               "e"
               " "
               "3"
               " "
               "—"
               " "
               "n"
               "ã"
               "o"
               " "
               "d"
               "e"
               " "
               "b"
               "u"
               "l"
               "a"
               " "
               "l"
               "i"
               "d"
               "a"
               " "
               "p"
               "o"
               "r"
               " "
               "m"
               "i"
               "m"
               ","
               " "
               "e"
               " "
               "a"
               " "
               "p"
               "á"
               "g"
               "i"
               "n"
               "a"
               " "
               "n"
               "ã"
               "o"
               " "
               "a"
               "f"
               "i"
               "r"
               "m"
               "a"
               " "
               "m"
               "a"
               "i"
               "s"
               " "
               "d"
               "o"
               " "
               "q"
               "u"
               "e"
               " "
               "i"
               "s"
               "s"
               "o"
               "."
               " "
               "<"
               "s"
               "t"
               "r"
               "o"
               "n"
               "g"
               ">"
               "E"
               "s"
               "t"
               "a"
               " "
               "p"
               "á"
               "g"
               "i"
               "n"
               "a"
               " "
               "f"
               "o"
               "i"
               " "
               "a"
               "p"
               "u"
               "r"
               "a"
               "d"
               "a"
               " "
               "e"
               "m"
               " "
               "d"
               "i"
               "a"
               " "
               "p"
               "r"
               "ó"
               "p"
               "r"
               "i"
               "o"
               "<"
               "/"
               "s"
               "t"
               "r"
               "o"
               "n"
               "g"
               ">"
               ","
               " "
               "e"
               " "
               "p"
               "o"
               "r"
               " "
               "i"
               "s"
               "s"
               "o"
               " "
               "c"
               "a"
               "r"
               "r"
               "e"
               "g"
               "a"
               " "
               "d"
               "a"
               "t"
               "a"
               " "
               "p"
               "r"
               "ó"
               "p"
               "r"
               "i"
               "a"
               "."),
    referencias=[
        ("API pública do ClinicalTrials.gov, versão 2 — a base de todas as contagens de estudo e de fase 3 desta página.",
         "https://clinicaltrials.gov/data-api/api"),
        ("E-utilities do PubMed (esearch) — a base de todas as contagens de artigo desta página.",
         "https://www.ncbi.nlm.nih.gov/books/NBK25501/"),
        ("Registro NCT07146022 no ClinicalTrials.gov — VDPHL01, 552 participantes, patrocínio da Veradermics.",
         "https://clinicaltrials.gov/study/NCT07146022"),
        ("Registro NCT06622824 no ClinicalTrials.gov — pirilutamida (KX-826), 756 participantes, patrocínio da Kintor Pharmaceutical.",
         "https://clinicaltrials.gov/study/NCT06622824"),
        ("Registro NCT05914805 no ClinicalTrials.gov — clascoterona, 762 participantes, patrocínio da Cassiopea.",
         "https://clinicaltrials.gov/study/NCT05914805"),
        ("Registro NCT06539273 no ClinicalTrials.gov — o único ensaio de fase 3 de exossomo em alopecia que a busca devolveu, 30 participantes.",
         "https://clinicaltrials.gov/study/NCT06539273"),
        ("Dado aberto de medicamentos registrados da ANVISA — a mesma base usada na página O que existe no Brasil.",
         "https://dados.anvisa.gov.br/dados/"),
    ],
),
}
