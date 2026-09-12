# -*- coding: utf-8 -*-
"""Fígado e lipídio: levantamento de fonte primaria.

Apurado em 12 de setembro de 2026, num dia proprio -- por isso importa
DATA_NOVAS_CLASSES e nao DATA_APURACAO.

Nome de arquivo descritivo, e nao proprios20/21, de proposito: este repo
tem sessoes paralelas criando modulos numerados ao mesmo tempo.
"""

from datas import DATA_NOVAS_CLASSES as _DT

FIGADO_LIPIDIO = {
"proprio_figado_lipidio": dict(
    secoes=[
        dict(h="Por que fígado e lipídio entram num site de peptídeos", tipo="p", corpo=[
                    "Entram por dois motivos. O primeiro é que a <a href=\"protocol_retatrutide.html\">retatrutida</a> e a <a href=\"protocol_survodutide.html\">survodutida</a>, que este site já cobre, são estudadas também em fígado — e quem procura “peptídeo para gordura no fígado” acaba nestas moléculas sem saber que mudou de categoria.",
            "O segundo é mais importante. Estes treze programas são a melhor régua disponível para o que este site cobra do resto: <strong>ensaio grande, com desfecho duro, registrado antes de começar</strong>. Quatro deles declaram mais de sete mil participantes. Nenhum composto de comunidade deste site chega perto disso, e a diferença não é de grau.",
            "Uma ressalva de método: as buscas usam a DCI de cada molécula, sem sinônimos comerciais. Onde a molécula ainda tinha código de desenvolvimento em uso — o caso do CT-388, hoje enicepatida, que está na página de <a href=\"proprio_incretinas.html\">incretinas</a> — o código entra na consulta. Aqui não foi preciso.",
            "Nenhum número desta página veio da fonte secundária do site.",
                ]),
        dict(h="Quanta evidência existe, composto a composto", tipo="p", corpo=[
                    f"Os números abaixo foram levantados por mim em {_DT}, no PubMed e no ClinicalTrials.gov. A consulta de cada linha está escrita <strong>inteira</strong>, ao lado do número, para qualquer pessoa repetir e me contradizer — e para o script que reconfere as contagens deste site conseguir rodar todas.",
            "A coluna de condição <strong>não é afirmação de mecanismo</strong>: é o campo <em>Condition</em> copiado dos registros de fase 3 que a própria busca devolveu. Quando não há registro de fase 3, a célula diz isso.",
                ], tabela=dict(cap="Levantamento de evidência — fígado e lipídio", linhas=[
                    ["Composto", "Condição nos registros de fase 3", "Consulta", "Artigos no PubMed", "Estudos no ClinicalTrials.gov"],
            ["<strong>Resmetiroma</strong>", "<small>Non-Alcoholic Fatty Liver Disease; NASH - Nonalcoholic Steatohepatitis</small>", "<code>resmetirom</code>", "487", "22"],
            ["<strong>Efruxifermina</strong>", "<small>NASH/MASH; NAFLD/MASLD; NASH - Nonalcoholic Steatohepatitis; MASH - Metabolic Dysfunction-Associated Steatohepatitis</small>", "<code>efruxifermin</code>", "45", "6"],
            ["<strong>Pegozafermina</strong>", "<small>Metabolic Dysfunction-Associated Steatotic Liver Disease (MASH) / Nonalcoholic Steatohepatitis (NASH) With Fibrosis; Metabolic Dysfunction-Associated Steatohepatitis (MASH) / Nonalcoholic Steatohepatitis (NASH) With Compensated Cirrhosis; Severe Hypertriglyceridemia</small>", "<code>pegozafermin</code>", "32", "6"],
            ["<strong>Efimosfermina</strong>", "<small>Non-alcoholic Fatty Liver Disease; Metabolic Dysfunction-associated Steatohepatitis</small>", "<code>efimosfermin</code>", "9", "9"],
            ["<strong>Lanifibranor</strong>", "<small>NASH - Nonalcoholic Steatohepatitis</small>", "<code>lanifibranor</code>", "77", "7"],
            ["<strong>Denifanstat</strong>", "<small>MASH; NASH; Metabolic Dysfunction-associated Steatohepatitis; Acne</small>", "<code>denifanstat</code>", "19", "7"],
            ["<strong>Inclisirana</strong>", "<small>Heterozygous or Homozygous Familial Hypercholesterolemia; ASCVD; Elevated Cholesterol; Hypercholesterolemia</small>", "<code>inclisiran</code>", "745", "81"],
            ["<strong>Pelacarsena</strong>", "<small>Atherosclerotic Cardiovascular Disease; Atherosclerotic Cardiovascular Disease (ASCVD); Hyperlipoproteinemia(a)</small>", "<code>pelacarsen</code>", "90", "14"],
            ["<strong>Olpasirana</strong>", "<small>Atherosclerotic Cardiovascular Disease; Cardiovascular Disease</small>", "<code>olpasiran</code>", "82", "9"],
            ["<strong>Lepodisirana</strong>", "<small>Atherosclerotic Cardiovascular Disease (ASCVD); Elevated Lp(a); Atherosclerosis; Cardiovascular Diseases</small>", "<code>lepodisiran</code>", "54", "3"],
            ["<strong>Muvalaplina</strong>", "<small>Elevated Lp(a); Atherosclerotic Cardiovascular Disease (ASCVD)</small>", "<code>muvalaplin</code>", "34", "1"],
            ["<strong>Obicetrapibe</strong>", "<small>Lipidemia; Type 2 Diabetes (T2DM); Metabolic Syndrome (MetS); Coronary Artery Disease</small>", "<code>obicetrapib</code>", "88", "21"],
            ["<strong>Zilebesirana</strong>", "<small>High Risk Cardiovascular Disease; Hypertension; High Cardiovascular Risk</small>", "<code>zilebesiran</code>", "53", "7"],
                ])),
        dict(h="O que existe de fase 3, e de quem é", tipo="p", corpo=[
                    "Contagem de artigo mede atenção acadêmica, não evidência de desfecho. A tabela abaixo separa o que tem <strong>ensaio de fase 3 registrado</strong> — e mostra o maior registro que a busca devolveu em cada linha, com o número de participantes declarado e o patrocinador.",
            "Registro não é resultado. Um ensaio de fase 3 recrutando é intenção declarada com dinheiro atrás, e nada mais que isso.",
                ], tabela=dict(cap="Ensaios de fase 3 registrados — fígado e lipídio", linhas=[
                    ["Composto", "Consulta", "Ensaios registrados de fase 3", "O maior registro que abri"],
            ["<strong>Resmetiroma</strong>", "<code>(resmetirom) AND AREA[Phase]PHASE3</code>", "4", "<strong>NCT03900429</strong> · n = 1.759 · Madrigal Pharmaceuticals, Inc.<br><small>NASH - Nonalcoholic Steatohepatitis</small>"],
            ["<strong>Efruxifermina</strong>", "<code>(efruxifermin) AND AREA[Phase]PHASE3</code>", "3", "<strong>NCT06528314</strong> · n = 2.150 · Akero Therapeutics, Inc<br><small>NASH - Nonalcoholic Steatohepatitis, MASH - Metabolic Dysfunction-Associated Steatohepatitis</small>"],
            ["<strong>Pegozafermina</strong>", "<code>(pegozafermin) AND AREA[Phase]PHASE3</code>", "3", "<strong>NCT06318169</strong> · n = 1.350 · 89bio, Inc.<br><small>Metabolic Dysfunction-Associated Steatotic Liver Disease (MASH) / Nonalcoholic Steatohepatitis (NASH) With Fibrosis</small>"],
            ["<strong>Efimosfermina</strong>", "<code>(efimosfermin) AND AREA[Phase]PHASE3</code>", "4", "<strong>NCT07221188</strong> · n = 1.250 · GlaxoSmithKline<br><small>Non-alcoholic Fatty Liver Disease</small>"],
            ["<strong>Lanifibranor</strong>", "<code>(lanifibranor) AND AREA[Phase]PHASE3</code>", "1", "<strong>NCT04849728</strong> · n = 1.000 · Inventiva Pharma<br><small>NASH - Nonalcoholic Steatohepatitis</small>"],
            ["<strong>Denifanstat</strong>", "<code>(denifanstat) AND AREA[Phase]PHASE3</code>", "4", "<strong>NCT06248008</strong> · n = 240 · Ascletis Pharmaceuticals Co., Ltd.<br><small>Acne</small>"],
            ["<strong>Inclisirana</strong>", "<code>(inclisiran) AND AREA[Phase]PHASE3</code>", "24", "<strong>NCT03399370</strong> · n = 1.561 · The Medicines Company<br><small>ASCVD, Elevated Cholesterol</small>"],
            ["<strong>Pelacarsena</strong>", "<code>(pelacarsen) AND AREA[Phase]PHASE3</code>", "8", "<strong>NCT06875973</strong> · n = 599 · Novartis Pharmaceuticals<br><small>Atherosclerotic Cardiovascular Disease</small>"],
            ["<strong>Olpasirana</strong>", "<code>(olpasiran) AND AREA[Phase]PHASE3</code>", "3", "<strong>NCT07136012</strong> · n = 11.000 · Amgen<br><small>Cardiovascular Disease</small>"],
            ["<strong>Lepodisirana</strong>", "<code>(lepodisiran) AND AREA[Phase]PHASE3</code>", "2", "<strong>NCT06292013</strong> · n = 17.300 · Eli Lilly and Company<br><small>Atherosclerotic Cardiovascular Disease (ASCVD), Elevated Lp(a)</small>"],
            ["<strong>Muvalaplina</strong>", "<code>(muvalaplin) AND AREA[Phase]PHASE3</code>", "1", "<strong>NCT07157774</strong> · n = 10.450 · Eli Lilly and Company<br><small>Elevated Lp(a), Atherosclerotic Cardiovascular Disease (ASCVD)</small>"],
            ["<strong>Obicetrapibe</strong>", "<code>(obicetrapib) AND AREA[Phase]PHASE3</code>", "7", "<strong>NCT06005597</strong> · n = 407 · NewAmsterdam Pharma<br><small>Dyslipidemias, Hypercholesterolemia, Familial Hypercholesterolemia</small>"],
            ["<strong>Zilebesirana</strong>", "<code>(zilebesiran) AND AREA[Phase]PHASE3</code>", "1", "<strong>NCT07181109</strong> · n = 11.000 · Alnylam Pharmaceuticals<br><small>High Risk Cardiovascular Disease, Hypertension, High Cardiovascular Risk</small>"],
                ])),
        dict(h="Onde a conta não fecha", tipo="li", corpo=[
                    "<strong>Os quatro maiores registros desta página somam mais de quarenta mil participantes.</strong> Lepodisirana (17.300), zilebesirana (11.000), muvalaplina (10.450) e olpasirana (7.297). São ensaios de desfecho cardiovascular, o desenho mais caro e mais lento que existe — e a razão pela qual nenhum deles tem resposta ainda.",
            "<strong>A inclisirana é a única com bula no Brasil.</strong> 1 registro ativo, sob o nome SYBRAVA, na classe antilipemicos. As outras doze não têm nenhum.",
            "<strong>O resmetiroma tem 487 artigos e 4 ensaios de fase 3</strong>, os dois maiores com 1.343 e 810 participantes, patrocínio da Madrigal. É a linha com mais evidência publicada do bloco de fígado — e mesmo assim não tem registro ativo na ANVISA.",
            "<strong>Os três análogos de FGF21 somam 86 artigos no PubMed e 10 ensaios de fase 3.</strong> Frasco de “FGF21 de pesquisa” não é nenhuma das três: o que está em ensaio é proteína de fusão engenheirada, com patrocinador e número de registro.",
            "<strong>Denifanstat tem um registro de fase 3 com inscrição declarada em zero.</strong> Entre os 4 que a busca devolve, o primeiro que abri, da Sagimet, declara zero participantes. Contagem de fase 3 não é contagem de gente.",
                ]),
        dict(h="No Brasil", tipo="p", corpo=[
                    f"Busquei cada princípio ativo no <strong>dado aberto de medicamentos registrados da ANVISA</strong>, baixado em {_DT} — 43.508 linhas, contando apenas situação <strong>Ativo</strong>. A coluna de classe terapêutica é a que a própria base declara para o produto.",
            "Doze das treze linhas voltam vazias. Isso não quer dizer que a molécula seja proibida: quer dizer que ela ainda não é medicamento aqui, e que não existe produto legal para comprar com esse princípio ativo.",
                ], tabela=dict(cap="Registro na ANVISA — fígado e lipídio", linhas=[
                    ["Princípio ativo", "Padrão buscado", "Registros ativos", "Classe terapêutica declarada", "Produtos"],
            ["<strong>Resmetiroma</strong>", "<code>RESMETIROM</code>", "<strong>0</strong>", "<small>—</small>", "—"],
            ["<strong>Efruxifermina</strong>", "<code>EFRUXIFERMIN</code>", "<strong>0</strong>", "<small>—</small>", "—"],
            ["<strong>Pegozafermina</strong>", "<code>PEGOZAFERMIN</code>", "<strong>0</strong>", "<small>—</small>", "—"],
            ["<strong>Efimosfermina</strong>", "<code>EFIMOSFERMIN</code>", "<strong>0</strong>", "<small>—</small>", "—"],
            ["<strong>Lanifibranor</strong>", "<code>LANIFIBRANOR</code>", "<strong>0</strong>", "<small>—</small>", "—"],
            ["<strong>Denifanstat</strong>", "<code>DENIFANSTAT</code>", "<strong>0</strong>", "<small>—</small>", "—"],
            ["<strong>Inclisirana</strong>", "<code>INCLISIRAN</code>", "<strong>1</strong>", "<small>ANTILIPEMICOS</small>", "SYBRAVA"],
            ["<strong>Pelacarsena</strong>", "<code>PELACARSEN</code>", "<strong>0</strong>", "<small>—</small>", "—"],
            ["<strong>Olpasirana</strong>", "<code>OLPASIRAN</code>", "<strong>0</strong>", "<small>—</small>", "—"],
            ["<strong>Lepodisirana</strong>", "<code>LEPODISIRAN</code>", "<strong>0</strong>", "<small>—</small>", "—"],
            ["<strong>Muvalaplina</strong>", "<code>MUVALAPLIN</code>", "<strong>0</strong>", "<small>—</small>", "—"],
            ["<strong>Obicetrapibe</strong>", "<code>OBICETRAPIB</code>", "<strong>0</strong>", "<small>—</small>", "—"],
            ["<strong>Zilebesirana</strong>", "<code>ZILEBESIRAN</code>", "<strong>0</strong>", "<small>—</small>", "—"],
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
        ("Registro NCT06292013 no ClinicalTrials.gov — lepodisirana, 17.300 participantes, patrocínio da Eli Lilly. O maior ensaio desta página.",
         "https://clinicaltrials.gov/study/NCT06292013"),
        ("Registro NCT07181109 no ClinicalTrials.gov — zilebesirana, 11.000 participantes, patrocínio da Alnylam.",
         "https://clinicaltrials.gov/study/NCT07181109"),
        ("Registro NCT05581303 no ClinicalTrials.gov — olpasirana, 7.297 participantes, patrocínio da Amgen.",
         "https://clinicaltrials.gov/study/NCT05581303"),
        ("Registro NCT04197479 no ClinicalTrials.gov — resmetiroma, 1.343 participantes, patrocínio da Madrigal Pharmaceuticals.",
         "https://clinicaltrials.gov/study/NCT04197479"),
        ("Dado aberto de medicamentos registrados da ANVISA — a mesma base usada na página O que existe no Brasil.",
         "https://dados.anvisa.gov.br/dados/"),
    ],
),
}
