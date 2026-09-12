# -*- coding: utf-8 -*-
"""Incretinas e amilinas de nova geração: levantamento de fonte primaria.

Apurado em 12 de setembro de 2026, num dia proprio -- por isso importa
DATA_NOVAS_CLASSES e nao DATA_APURACAO.

Nome de arquivo descritivo, e nao proprios20/21, de proposito: este repo
tem sessoes paralelas criando modulos numerados ao mesmo tempo.
"""

from datas import DATA_NOVAS_CLASSES as _DT

INCRETINAS = {
"proprio_incretinas": dict(
    secoes=[
        dict(h="Por que estas treze, e o que elas não são", tipo="p", corpo=[
                    "Este site nasceu de uma fonte secundária sobre peptídeos de pesquisa. As moléculas desta página são outra coisa: quase todas são <strong>programas de desenvolvimento farmacêutico</strong>, com patrocinador nomeado, registro público e milhares de participantes recrutados. Elas entram aqui porque aparecem na mesma conversa em que aparece a <a href=\"protocol_retatrutide.html\">retatrutida</a> — e porque a distância entre as duas categorias é exatamente o que este site existe para medir.",
            "Três delas não são novas e estão aqui de propósito, como régua: <strong>liraglutida</strong> e <strong>dulaglutida</strong>, registradas no Brasil há anos, e a <strong>pramlintida</strong>, o análogo de amilina mais antigo — a régua para julgar o que a <a href=\"protocol_cagrilintide.html\">cagrilintida</a>, que este site já cobre, está prometendo.",
            "Duas linhas da tabela não são nome de substância, são <strong>código de desenvolvimento</strong>: VK2735 e HRS-9531. Busquei os dois pelo código porque é o que existe. Se ganharem DCI, a contagem muda de lugar e esta página envelhece — é uma limitação declarada, não um descuido.",
            "Nenhum número desta página veio da fonte secundária do site. Tudo foi levantado direto no PubMed, no ClinicalTrials.gov e no dado aberto de medicamentos registrados da ANVISA.",
                ]),
        dict(h="Quanta evidência existe, composto a composto", tipo="p", corpo=[
                    f"Os números abaixo foram levantados por mim em {_DT}, no PubMed e no ClinicalTrials.gov. A consulta de cada linha está escrita <strong>inteira</strong>, ao lado do número, para qualquer pessoa repetir e me contradizer — e para o script que reconfere as contagens deste site conseguir rodar todas.",
            "A coluna de condição <strong>não é afirmação de mecanismo</strong>: é o campo <em>Condition</em> copiado dos registros de fase 3 que a própria busca devolveu. Quando não há registro de fase 3, a célula diz isso.",
                ], tabela=dict(cap="Levantamento de evidência — incretinas e amilinas de nova geração", linhas=[
                    ["Composto", "Condição nos registros de fase 3", "Consulta", "Artigos no PubMed", "Estudos no ClinicalTrials.gov"],
            ["<strong>Orforglipron</strong>", "<small>Obesity; Overweight</small>", "<code>orforglipron OR LY3502970</code>", "136", "54"],
            ["<strong>MariTide</strong>", "<small>Obesity; Overweight; Type 2 Diabetes Mellitus (T2DM); Obesity or Overweight</small>", "<code>maridebart OR \"AMG 133\"</code>", "21", "27"],
            ["<strong>Amicretina</strong>", "<small>nenhum registro de fase 3 nesta busca</small>", "<code>amycretin</code>", "21", "1"],
            ["<strong>Eloralintida</strong>", "<small>Osteoarthritis; Overweight or Obesity; Overweight; Obesity</small>", "<code>eloralintide</code>", "8", "18"],
            ["<strong>Petrelintida</strong>", "<small>nenhum registro de fase 3 nesta busca</small>", "<code>petrelintide</code>", "6", "6"],
            ["<strong>Pemvidutida</strong>", "<small>Metabolic Dysfunction-Associated Steatohepatitis (MASH)</small>", "<code>pemvidutide</code>", "13", "8"],
            ["<strong>VK2735</strong>", "<small>Weight Loss</small>", "<code>VK2735</code>", "1", "5"],
            ["<strong>Enicepatida</strong>", "<small>Obesity or Overweight; Type 2 Diabetes Mellitus; Obesity; Overweight</small>", "<code>enicepatide OR \"CT-388\"</code>", "2", "8"],
            ["<strong>Ecnoglutida</strong>", "<small>T2DM; Type 2 Diabetes Mellitus; OSA - Obstructive Sleep Apnea; Obesity</small>", "<code>ecnoglutide OR XW003</code>", "14", "16"],
            ["<strong>HRS-9531</strong>", "<small>Type 2 Diabetes; Chronic Management of Body Weight</small>", "<code>\"HRS-9531\"</code>", "0", "33"],
            ["<strong>Liraglutida</strong>", "<small>Overweight; Obesity; Type 1 Diabetes; Glucocorticoid Induced Hyperglycemia</small>", "<code>liraglutide</code>", "5.909", "514"],
            ["<strong>Dulaglutida</strong>", "<small>Type 2 Diabetes; Diabetes Mellitus; Type 2; Intracranial Atherosclerosis</small>", "<code>dulaglutide</code>", "1.323", "140"],
            ["<strong>Pramlintida</strong>", "<small>Obesity; Appetite Regulation; PreDiabetes; Diabetes Mellitus</small>", "<code>pramlintide</code>", "496", "64"],
                ])),
        dict(h="O que existe de fase 3, e de quem é", tipo="p", corpo=[
                    "Contagem de artigo mede atenção acadêmica, não evidência de desfecho. A tabela abaixo separa o que tem <strong>ensaio de fase 3 registrado</strong> — e mostra o maior registro que a busca devolveu em cada linha, com o número de participantes declarado e o patrocinador.",
            "Registro não é resultado. Um ensaio de fase 3 recrutando é intenção declarada com dinheiro atrás, e nada mais que isso.",
                ], tabela=dict(cap="Ensaios de fase 3 registrados — incretinas e amilinas", linhas=[
                    ["Composto", "Consulta", "Ensaios registrados de fase 3", "O maior registro que abri"],
            ["<strong>Orforglipron</strong>", "<code>(orforglipron OR LY3502970) AND AREA[Phase]PHASE3</code>", "27", "<strong>NCT06972459</strong> · n = 800 · Eli Lilly and Company<br><small>Obesity, Overweight</small>"],
            ["<strong>MariTide</strong>", "<code>(maridebart OR \"AMG 133\") AND AREA[Phase]PHASE3</code>", "10", "<strong>NCT07684235</strong> · n = 3.200 · Amgen<br><small>Obesity, Overweight</small>"],
            ["<strong>Amicretina</strong>", "<code>(amycretin) AND AREA[Phase]PHASE3</code>", "0", "—"],
            ["<strong>Eloralintida</strong>", "<code>(eloralintide) AND AREA[Phase]PHASE3</code>", "5", "<strong>NCT07321886</strong> · n = 1.980 · Eli Lilly and Company<br><small>Obesity, Overweight</small>"],
            ["<strong>Petrelintida</strong>", "<code>(petrelintide) AND AREA[Phase]PHASE3</code>", "0", "—"],
            ["<strong>Pemvidutida</strong>", "<code>(pemvidutide) AND AREA[Phase]PHASE3</code>", "1", "<strong>NCT07795164</strong> · n = 1.800 · Altimmune, Inc.<br><small>Metabolic Dysfunction-Associated Steatohepatitis (MASH)</small>"],
            ["<strong>VK2735</strong>", "<code>(VK2735) AND AREA[Phase]PHASE3</code>", "2", "<strong>NCT07104500</strong> · n = 4.500 · Viking Therapeutics, Inc.<br><small>Weight Loss</small>"],
            ["<strong>Enicepatida</strong>", "<code>(enicepatide OR \"CT-388\") AND AREA[Phase]PHASE3</code>", "3", "<strong>NCT07351045</strong> · n = 2.000 · Hoffmann-La Roche<br><small>Obesity or Overweight</small>"],
            ["<strong>Ecnoglutida</strong>", "<code>(ecnoglutide OR XW003) AND AREA[Phase]PHASE3</code>", "6", "<strong>NCT07734311</strong> · n = 360 · Hangzhou Sciwind Biosciences Co., Ltd.<br><small>Knee Osteoarthritis, Obesity</small>"],
            ["<strong>HRS-9531</strong>", "<code>(\"HRS-9531\") AND AREA[Phase]PHASE3</code>", "9", "<strong>NCT06649344</strong> · n = 884 · Fujian Shengdi Pharmaceutical Co., Ltd.<br><small>Type 2 Diabetes</small>"],
            ["<strong>Liraglutida</strong>", "<code>(liraglutide) AND AREA[Phase]PHASE3</code>", "112", "<strong>NCT04074161</strong> · n = 338 · Novo Nordisk A/S<br><small>Overweight, Obesity</small>"],
            ["<strong>Dulaglutida</strong>", "<code>(dulaglutide) AND AREA[Phase]PHASE3</code>", "34", "<strong>NCT01075282</strong> · n = 810 · Eli Lilly and Company<br><small>Diabetes Mellitus, Type 2</small>"],
            ["<strong>Pramlintida</strong>", "<code>(pramlintide) AND AREA[Phase]PHASE3</code>", "8", "<strong>NCT00042458</strong> · n = 296 · AstraZeneca<br><small>Diabetes Mellitus, Type 1</small>"],
                ])),
        dict(h="Onde a conta não fecha", tipo="li", corpo=[
                    "<strong>A literatura não acompanha o desenvolvimento.</strong> Só a liraglutida tem 5.909 artigos; as dez moléculas novas desta página, somadas, têm 222. O dinheiro já se moveu; a literatura ainda não.",
            "<strong>HRS-9531 é o caso que quebra a régua.</strong> 0 artigos no PubMed com o código entre aspas, 33 estudos registrados e 9 de fase 3. Quem julgar a molécula pela contagem de artigos conclui que ela não existe.",
            "<strong>Amicretina é o oposto, e merece a mesma desconfiança.</strong> 21 artigos no PubMed, 1 estudo no ClinicalTrials.gov e 0 de fase 3 na busca por <code>amycretin</code>. Nome recente, grafia ainda instável entre as bases: a ausência aqui mede indexação, não ausência de programa.",
            "<strong>Nas amilinas, o registro anda na frente da publicação.</strong> A eloralintida tem 8 artigos e 5 ensaios de fase 3, um deles com 1.980 participantes. É mais gente recrutada do que artigo escrito.",
            "<strong>9 das 11 com DCI publicada não têm nenhum registro ativo na ANVISA.</strong> As duas que têm são as antigas. Nenhuma das moléculas novas desta página está aprovada para uso no Brasil, em indicação nenhuma.",
                ]),
        dict(h="No Brasil", tipo="p", corpo=[
                    f"Busquei cada princípio ativo no <strong>dado aberto de medicamentos registrados da ANVISA</strong>, baixado em {_DT} — 43.508 linhas. A tabela conta apenas os registros com situação <strong>Ativo</strong> e lista os nomes de produto encontrados.",
            "As duas linhas que são código de desenvolvimento (VK2735 e HRS-9531) ficam fora desta tabela: sem DCI publicada, não há princípio ativo para procurar. Ausência na base <strong>não</strong> quer dizer que a molécula seja proibida — quer dizer que não existe produto registrado, e que qualquer frasco vendido aqui com esse nome está fora do sistema de registro.",
                ], tabela=dict(cap="Registro na ANVISA — incretinas e amilinas de nova geração", linhas=[
                    ["Princípio ativo", "Padrão buscado", "Registros ativos", "Classe terapêutica declarada", "Produtos"],
            ["<strong>Orforglipron</strong>", "<code>ORFORGLIPRON</code>", "<strong>0</strong>", "<small>—</small>", "—"],
            ["<strong>MariTide</strong>", "<code>MARIDEBART</code>", "<strong>0</strong>", "<small>—</small>", "—"],
            ["<strong>Amicretina</strong>", "<code>AMICRETIN</code>", "<strong>0</strong>", "<small>—</small>", "—"],
            ["<strong>Eloralintida</strong>", "<code>ELORALINTID</code>", "<strong>0</strong>", "<small>—</small>", "—"],
            ["<strong>Petrelintida</strong>", "<code>PETRELINTID</code>", "<strong>0</strong>", "<small>—</small>", "—"],
            ["<strong>Pemvidutida</strong>", "<code>PEMVIDUTID</code>", "<strong>0</strong>", "<small>—</small>", "—"],
            ["<strong>Enicepatida</strong>", "<code>ENICEPATID</code>", "<strong>0</strong>", "<small>—</small>", "—"],
            ["<strong>Ecnoglutida</strong>", "<code>ECNOGLUTID</code>", "<strong>0</strong>", "<small>—</small>", "—"],
            ["<strong>Liraglutida</strong>", "<code>LIRAGLUTID</code>", "<strong>8</strong>", "<small>OUTROS HORMONIOS E MODULADORES DO METABOLISMO E DA DIGESTAO; ANTIDIABETICOS</small>", "LIRACLICK, LIRAGLUTIDA, LIRUX, OLIRE, SAXENDA, VICTOZA"],
            ["<strong>Dulaglutida</strong>", "<code>DULAGLUTID</code>", "<strong>1</strong>", "<small>ANTIDIABETICOS</small>", "TRULICITY"],
            ["<strong>Pramlintida</strong>", "<code>PRAMLINTID</code>", "<strong>0</strong>", "<small>—</small>", "—"],
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
               "n"
               "a"
               "s"
               " "
               "b"
               "a"
               "s"
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
               "O"
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
               "i"
               "n"
               "d"
               "i"
               "v"
               "i"
               "d"
               "u"
               "a"
               "i"
               "s"
               " "
               "q"
               "u"
               "e"
               " "
               "a"
               "b"
               "r"
               "i"
               " "
               "e"
               "s"
               "t"
               "ã"
               "o"
               " "
               "l"
               "i"
               "n"
               "k"
               "a"
               "d"
               "o"
               "s"
               " "
               "a"
               "b"
               "a"
               "i"
               "x"
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
        ("Registro NCT07684235 no ClinicalTrials.gov — o maior ensaio de fase 3 de MariTide que a busca devolveu, com 3.200 participantes, patrocínio da Amgen.",
         "https://clinicaltrials.gov/study/NCT07684235"),
        ("Registro NCT07104500 no ClinicalTrials.gov — o maior de VK2735, com 4.500 participantes, patrocínio da Viking Therapeutics.",
         "https://clinicaltrials.gov/study/NCT07104500"),
        ("Registro NCT07351058 no ClinicalTrials.gov — enicepatida (antes CT-388), 1.600 participantes, patrocínio da Hoffmann-La Roche.",
         "https://clinicaltrials.gov/study/NCT07351058"),
        ("Registro NCT07795164 no ClinicalTrials.gov — pemvidutida, 1.800 participantes, patrocínio da Altimmune.",
         "https://clinicaltrials.gov/study/NCT07795164"),
        ("Dado aberto de medicamentos registrados da ANVISA — a mesma base usada na página O que existe no Brasil.",
         "https://dados.anvisa.gov.br/dados/"),
    ],
),
}
