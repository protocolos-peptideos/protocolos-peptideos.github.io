# -*- coding: utf-8 -*-
"""Músculo, osso, eixo HPG e imune: levantamento de fonte primaria.

Apurado em 12 de setembro de 2026, num dia proprio -- por isso importa
DATA_NOVAS_CLASSES e nao DATA_APURACAO.

Nome de arquivo descritivo, e nao proprios20/21, de proposito: este repo
tem sessoes paralelas criando modulos numerados ao mesmo tempo.
"""

from datas import DATA_NOVAS_CLASSES as _DT

MUSCULO_HPG = {
"proprio_musculo_hpg": dict(
    secoes=[
        dict(h="Quatro blocos, uma pergunta só", tipo="p", corpo=[
                    "A pergunta é sempre a mesma neste site: <strong>o que o ensaio testou, e o que o frasco promete</strong>. Nestas quinze linhas a resposta é quase sempre que o ensaio testou uma doença rara e o frasco promete recomposição corporal.",
            "O caso mais limpo é o da <strong>afamelanotida</strong>: os registros de fase 3 que a busca devolve são de <strong>protoporfiria eritropoiética</strong>, patrocínio da Clinuvel — uma doença de pele rara com fotossensibilidade. Nada a ver com bronzeamento, que é o motivo pelo qual o melanotan I circula. O da <strong>setmelanotida</strong> é igual: os registros são de obesidade por deficiência genética definida, patrocínio da Rhythm, e um deles tem quinze participantes.",
            "A <strong>carbetocina</strong> é outro exemplo do mesmo tipo: os dois maiores registros de fase 3 que abri são de hiperfagia na síndrome de Prader-Willi, patrocínio da ACADIA — e não de vínculo, ansiedade ou libido, que é como o análogo de ocitocina costuma ser vendido.",
            "Três ressalvas de largura de busca estão no aviso acima e valem para gonadorelina e enclomifeno. A terceira é o <strong>imunofan</strong>: busquei pela grafia latina que a literatura usa, e o número é pequeno o bastante para que qualquer variação de grafia mude a ordem de grandeza.",
            "Nenhum número desta página veio da fonte secundária do site.",
                ]),
        dict(h="Quanta evidência existe, composto a composto", tipo="p", corpo=[
                    f"Os números abaixo foram levantados por mim em {_DT}, no PubMed e no ClinicalTrials.gov. A consulta de cada linha está escrita <strong>inteira</strong>, ao lado do número, para qualquer pessoa repetir e me contradizer — e para o script que reconfere as contagens deste site conseguir rodar todas.",
            "A coluna de condição <strong>não é afirmação de mecanismo</strong>: é o campo <em>Condition</em> copiado dos registros de fase 3 que a própria busca devolveu. Quando não há registro de fase 3, a célula diz isso.",
                ], tabela=dict(cap="Levantamento de evidência — músculo, osso, eixo HPG e imune", linhas=[
                    ["Composto", "Condição nos registros de fase 3", "Consulta", "Artigos no PubMed", "Estudos no ClinicalTrials.gov"],
            ["<strong>Apitegromabe</strong>", "<small>Spinal Muscular Atrophy; Spinal Muscular Atrophy Type 3; Spinal Muscular Atrophy Type 2</small>", "<code>apitegromab</code>", "14", "7"],
            ["<strong>Romosozumabe</strong>", "<small>FHA (Functional Hypothalamic Amenorrhea); Postmenopausal Osteoporosis; Osteoporosis</small>", "<code>romosozumab</code>", "869", "49"],
            ["<strong>Abaloparatida</strong>", "<small>Postmenopausal Women With Osteoporosis; Osteoporosis; Age-Related; Osteoporosis Localized to Spine</small>", "<code>abaloparatide</code>", "405", "25"],
            ["<strong>Palopegteriparatida</strong>", "<small>Hypoparathyroidism; Endocrine System Diseases; Parathyroid Diseases</small>", "<code>palopegteriparatide</code>", "46", "9"],
            ["<strong>Vosoritida</strong>", "<small>Hypochondroplasia; Achondroplasia</small>", "<code>vosoritide</code>", "132", "17"],
            ["<strong>Setmelanotida</strong>", "<small>Leptin Receptor Deficiency Obesity; Obesity; Genetic Obesity; Bardet-Biedl Syndrome</small>", "<code>setmelanotide</code>", "238", "27"],
            ["<strong>Afamelanotida</strong>", "<small>Erythropoietic Protoporphyria</small>", "<code>afamelanotide OR \"melanotan I\"</code>", "136", "23"],
            ["<strong>Gonadorelina</strong>", "<small>Prostate Cancer; Metastatic Hormone-Sensitive Prostate Cancer</small>", "<code>gonadorelin</code>", "43.237", "1.157"],
            ["<strong>hCG</strong>", "<small>Hypogonadism; Hypogonadotropic Hypogonadism</small>", "<code>\"human chorionic gonadotropin\" AND hypogonadism</code>", "434", "17"],
            ["<strong>Enclomifeno</strong>", "<small>Secondary Hypogonadism; Polycystic Ovarian Syndrome</small>", "<code>enclomiphene</code>", "97", "259"],
            ["<strong>Carbetocina</strong>", "<small>Hyperphagia in Prader-Willi Syndrome; Delivery</small>", "<code>carbetocin</code>", "448", "103"],
            ["<strong>Efgartigimode</strong>", "<small>Thyroid Eye Disease; Graves' Disease; Graves Disease</small>", "<code>efgartigimod</code>", "472", "84"],
            ["<strong>Tezepelumabe</strong>", "<small>Asthma; Severe Asthma</small>", "<code>tezepelumab</code>", "554", "72"],
            ["<strong>IL-2 em dose baixa</strong>", "<small>Melanoma; Chronic Spontaneous Urticaria; Dermatomyositis</small>", "<code>\"low-dose interleukin-2\"</code>", "447", "57"],
            ["<strong>Imunofan</strong>", "<small>nenhum registro de fase 3 nesta busca</small>", "<code>imunofan</code>", "51", "0"],
                ])),
        dict(h="O que existe de fase 3, e de quem é", tipo="p", corpo=[
                    "Contagem de artigo mede atenção acadêmica, não evidência de desfecho. A tabela abaixo separa o que tem <strong>ensaio de fase 3 registrado</strong> — e mostra o maior registro que a busca devolveu em cada linha, com o número de participantes declarado e o patrocinador.",
            "Registro não é resultado. Um ensaio de fase 3 recrutando é intenção declarada com dinheiro atrás, e nada mais que isso.",
                ], tabela=dict(cap="Ensaios de fase 3 registrados — músculo, osso, eixo HPG e imune", linhas=[
                    ["Composto", "Consulta", "Ensaios registrados de fase 3", "O maior registro que abri"],
            ["<strong>Apitegromabe</strong>", "<code>(apitegromab) AND AREA[Phase]PHASE3</code>", "2", "<strong>NCT05626855</strong> · n = 238 · Scholar Rock, Inc.<br><small>Spinal Muscular Atrophy, Spinal Muscular Atrophy Type 3, Spinal Muscular Atrophy Type 2</small>"],
            ["<strong>Romosozumabe</strong>", "<code>(romosozumab) AND AREA[Phase]PHASE3</code>", "12", "<strong>NCT01796301</strong> · n = 436 · Amgen<br><small>Postmenopausal Osteoporosis</small>"],
            ["<strong>Abaloparatida</strong>", "<code>(abaloparatide) AND AREA[Phase]PHASE3</code>", "7", "<strong>NCT06898060</strong> · n = 282 · Qilu Pharmaceutical Co., Ltd.<br><small>Postmenopausal Women With Osteoporosis</small>"],
            ["<strong>Palopegteriparatida</strong>", "<code>(palopegteriparatide) AND AREA[Phase]PHASE3</code>", "3", "<strong>NCT04701203</strong> · n = 84 · Ascendis Pharma Bone Diseases A/S<br><small>Hypoparathyroidism, Endocrine System Diseases, Parathyroid Diseases</small>"],
            ["<strong>Vosoritida</strong>", "<code>(vosoritide) AND AREA[Phase]PHASE3</code>", "5", "<strong>NCT07441876</strong> · n = 160 · BioMarin Pharmaceutical<br><small>Achondroplasia</small>"],
            ["<strong>Setmelanotida</strong>", "<code>(setmelanotide) AND AREA[Phase]PHASE3</code>", "10", "<strong>NCT05093634</strong> · n = 296 · Rhythm Pharmaceuticals, Inc.<br><small>Obesity, Genetic Obesity</small>"],
            ["<strong>Afamelanotida</strong>", "<code>(afamelanotide OR \"melanotan I\") AND AREA[Phase]PHASE3</code>", "6", "<strong>NCT01605136</strong> · n = 93 · Clinuvel Pharmaceuticals Limited<br><small>Erythropoietic Protoporphyria</small>"],
            ["<strong>Gonadorelina</strong>", "<code>(gonadorelin) AND AREA[Phase]PHASE3</code>", "300", "<strong>NCT00002651</strong> · n = 3.040 · SWOG Cancer Research Network<br><small>Prostate Cancer</small>"],
            ["<strong>hCG</strong>", "<code>(\"human chorionic gonadotropin\" AND hypogonadism) AND AREA[Phase]PHASE3</code>", "4", "<strong>NCT01084265</strong> · n = 31 · Merck KGaA, Darmstadt, Germany<br><small>Hypogonadism</small>"],
            ["<strong>Enclomifeno</strong>", "<code>(enclomiphene) AND AREA[Phase]PHASE3</code>", "51", "<strong>NCT01534208</strong> · n = 499 · Repros Therapeutics Inc.<br><small>Secondary Hypogonadism</small>"],
            ["<strong>Carbetocina</strong>", "<code>(carbetocin) AND AREA[Phase]PHASE3</code>", "13", "<strong>NCT02304042</strong> · n = 200 · Cairo University<br><small>Delivery</small>"],
            ["<strong>Efgartigimode</strong>", "<code>(efgartigimod) AND AREA[Phase]PHASE3</code>", "33", "<strong>NCT07570316</strong> · n = 230 · argenx<br><small>Graves' Disease, Graves Disease</small>"],
            ["<strong>Tezepelumabe</strong>", "<code>(tezepelumab) AND AREA[Phase]PHASE3</code>", "23", "<strong>NCT03347279</strong> · n = 1.061 · AstraZeneca<br><small>Asthma</small>"],
            ["<strong>IL-2 em dose baixa</strong>", "<code>(\"low-dose interleukin-2\") AND AREA[Phase]PHASE3</code>", "4", "<strong>NCT00477906</strong> · n = 387 · AVAX Technologies<br><small>Melanoma</small>"],
            ["<strong>Imunofan</strong>", "<code>(imunofan) AND AREA[Phase]PHASE3</code>", "0", "—"],
                ])),
        dict(h="Onde a conta não fecha", tipo="li", corpo=[
                    "<strong>A afamelanotida tem 6 ensaios de fase 3, todos os que abri em protoporfiria eritropoiética.</strong> É a prova de que existe programa clínico sério de melanocortina — para uma doença rara de fotossensibilidade, e não para pigmentar pele saudável.",
            "<strong>O apitegromabe é o anti-miostatina com ensaio, e não é de emagrecimento.</strong> 14 artigos, 7 estudos, 2 de fase 3, patrocínio da Scholar Rock. É o mesmo alvo que o <a href=\"proprio_anticorpos.html\">bimagrumabe</a> persegue por outro caminho.",
            "<strong>Osso é onde o registro brasileiro está.</strong> Romosozumabe (EVENITY) e vosoritida (VOXZOGO) têm registro ativo; abaloparatida e palopegteriparatida, 0.",
            "<strong>O imune tem duas bulas e dois nadas.</strong> Efgartigimode (VYVGART) e tezepelumabe (TEZSPIRE) têm registro ativo. A IL-2 em dose baixa é uma estratégia, não um produto — 57 estudos registrados, e o maior de fase 3 que abri é de melanoma. O imunofan tem 51 artigos e 0 estudos.",
            "<strong>8 das 14 buscas voltam vazias na ANVISA.</strong> Entre elas, setmelanotida, afamelanotida, enclomifeno e apitegromabe — as quatro que aparecem em fórum como se fossem compráveis.",
                ]),
        dict(h="No Brasil", tipo="p", corpo=[
                    f"Busquei cada princípio ativo no <strong>dado aberto de medicamentos registrados da ANVISA</strong>, baixado em {_DT} — 43.508 linhas, contando apenas situação <strong>Ativo</strong>. A coluna de classe terapêutica é a que a própria base declara.",
            "Duas buscas foram desdobradas de propósito. <strong>Gonadotrofina coriônica</strong> entra separada do hCG da tabela de evidência porque é assim que a base nomeia o princípio ativo. E <strong>clomifeno</strong> entra ao lado de <strong>enclomifeno</strong> porque os dois nomes convivem no assunto — e o resultado mostra que o que existe registrado aqui é o clomifeno, não o enclomifeno.",
                ], tabela=dict(cap="Registro na ANVISA — músculo, osso, eixo HPG e imune", linhas=[
                    ["Princípio ativo", "Padrão buscado", "Registros ativos", "Classe terapêutica declarada", "Produtos"],
            ["<strong>Apitegromabe</strong>", "<code>APITEGROMAB</code>", "<strong>0</strong>", "<small>—</small>", "—"],
            ["<strong>Romosozumabe</strong>", "<code>ROMOSOZUMAB</code>", "<strong>1</strong>", "<small>OUTROS PRODUTOS COM ACAO NO SISTEMA MUSCULO ESQUELETICO</small>", "EVENITY"],
            ["<strong>Abaloparatida</strong>", "<code>ABALOPARATID</code>", "<strong>0</strong>", "<small>—</small>", "—"],
            ["<strong>Palopegteriparatida</strong>", "<code>PALOPEGTERIPARATID</code>", "<strong>0</strong>", "<small>—</small>", "—"],
            ["<strong>Vosoritida</strong>", "<code>VOSORITID</code>", "<strong>1</strong>", "<small>MEDICAMENTOS AFETANDO A ESTRUTURA ÓSSEA E MINERALIZAÇÃO</small>", "VOXZOGO"],
            ["<strong>Setmelanotida</strong>", "<code>SETMELANOTID</code>", "<strong>0</strong>", "<small>—</small>", "—"],
            ["<strong>Afamelanotida</strong>", "<code>AFAMELANOTID</code>", "<strong>0</strong>", "<small>—</small>", "—"],
            ["<strong>Gonadorelina</strong>", "<code>GONADORELIN</code>", "<strong>0</strong>", "<small>—</small>", "—"],
            ["<strong>Gonadotrofina corionica</strong>", "<code>GONADOTROFINA CORIONICA</code>", "<strong>0</strong>", "<small>—</small>", "—"],
            ["<strong>Enclomifeno</strong>", "<code>ENCLOMIFEN</code>", "<strong>0</strong>", "<small>—</small>", "—"],
            ["<strong>Clomifeno</strong>", "<code>CLOMIFEN</code>", "<strong>2</strong>", "<small>OUTROS PRODUTOS PARA USO EM GINECOLOGIA E OBSTETRICIA</small>", "CLOMID, INDUX"],
            ["<strong>Carbetocina</strong>", "<code>CARBETOCIN</code>", "<strong>2</strong>", "<small>PREPARAÇÕES HORMONAIS PARA USO SISTÊMICO, EXCLUINDO HORMÔNIOS SEXUAIS E INSULINAS</small>", "DURATOCIN, TOCYNAE"],
            ["<strong>Efgartigimode</strong>", "<code>EFGARTIGIMOD</code>", "<strong>1</strong>", "<small>IMUNOSUPRESSOR</small>", "VYVGART"],
            ["<strong>Tezepelumabe</strong>", "<code>TEZEPELUMAB</code>", "<strong>1</strong>", "<small>—</small>", "TEZSPIRE"],
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
               "r"
               "e"
               "s"
               "s"
               "a"
               "l"
               "v"
               "a"
               "s"
               " "
               "d"
               "e"
               " "
               "l"
               "a"
               "r"
               "g"
               "u"
               "r"
               "a"
               " "
               "d"
               "e"
               " "
               "b"
               "u"
               "s"
               "c"
               "a"
               " "
               "—"
               " "
               "g"
               "o"
               "n"
               "a"
               "d"
               "o"
               "r"
               "e"
               "l"
               "i"
               "n"
               "a"
               ","
               " "
               "e"
               "n"
               "c"
               "l"
               "o"
               "m"
               "i"
               "f"
               "e"
               "n"
               "o"
               " "
               "e"
               " "
               "i"
               "m"
               "u"
               "n"
               "o"
               "f"
               "a"
               "n"
               " "
               "—"
               " "
               "e"
               "s"
               "t"
               "ã"
               "o"
               " "
               "e"
               "s"
               "c"
               "r"
               "i"
               "t"
               "a"
               "s"
               " "
               "a"
               "n"
               "t"
               "e"
               "s"
               " "
               "d"
               "a"
               "s"
               " "
               "t"
               "a"
               "b"
               "e"
               "l"
               "a"
               "s"
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
        ("Registro NCT00979745 no ClinicalTrials.gov — afamelanotida em protoporfiria eritropoiética, patrocínio da Clinuvel.",
         "https://clinicaltrials.gov/study/NCT00979745"),
        ("Registro NCT05093634 no ClinicalTrials.gov — EMANATE, setmelanotida em obesidade por variante genética, patrocínio da Rhythm Pharmaceuticals.",
         "https://clinicaltrials.gov/study/NCT05093634"),
        ("Registro NCT06173531 no ClinicalTrials.gov — carbetocina em spray nasal para hiperfagia na síndrome de Prader-Willi, patrocínio da ACADIA.",
         "https://clinicaltrials.gov/study/NCT06173531"),
        ("Registro NCT05156320 no ClinicalTrials.gov — apitegromabe, patrocínio da Scholar Rock.",
         "https://clinicaltrials.gov/study/NCT05156320"),
        ("Dado aberto de medicamentos registrados da ANVISA — a mesma base usada na página O que existe no Brasil.",
         "https://dados.anvisa.gov.br/dados/"),
    ],
),
}
