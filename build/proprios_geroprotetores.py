# -*- coding: utf-8 -*-
"""Geroprotetores: levantamento de fonte primaria.

Apurado em 12 de setembro de 2026, num dia proprio -- por isso importa
DATA_NOVAS_CLASSES e nao DATA_APURACAO.

Nome de arquivo descritivo, e nao proprios20/21, de proposito: este repo
tem sessoes paralelas criando modulos numerados ao mesmo tempo.
"""

from datas import DATA_NOVAS_CLASSES as _DT

GEROPROTETORES = {
"proprio_geroprotetores": dict(
    secoes=[
        dict(h="Dezessete coisas diferentes com o mesmo rótulo", tipo="p", corpo=[
                    "“Geroprotetor” é uma palavra que junta, na mesma frase, o sirolimo — imunossupressor de transplante, com bula — e o pó de urolitina A comprado pela internet. A função desta página não é ordenar essa lista por promessa, é medir <strong>quanta evidência de desfecho humano existe em cada linha</strong>, e mostrar que a resposta muda em duas ordens de grandeza de uma linha para a outra.",
            "Três ressalvas de método, escritas antes dos números:",
            "<strong>Primeira.</strong> A busca <code>rapamycin OR sirolimus</code> devolve a literatura inteira do fármaco, quase toda de transplante e oncologia. O número é o tamanho do campo, não a evidência de uso em longevidade — que é justamente o que não existe em fase 3.",
            "<strong>Segunda.</strong> Onde o composto só faz sentido nesta página se estiver ligado a envelhecimento, a consulta traz o cruzamento escrito: <code>metformin AND (aging OR longevity)</code>, <code>acarbose AND (aging OR lifespan)</code>, <code>\"therapeutic plasma exchange\" AND aging</code>. Sem o cruzamento, a metformina traria a literatura do diabetes e o número não diria nada sobre o assunto desta página.",
            "<strong>Terceira.</strong> A linha do anti-IL-11 mede a classe, não um produto: <code>\"interleukin-11\" AND (antibody OR monoclonal)</code>. Não há DCI para buscar.",
            "Nenhum número desta página veio da fonte secundária do site.",
                ]),
        dict(h="Quanta evidência existe, composto a composto", tipo="p", corpo=[
                    f"Os números abaixo foram levantados por mim em {_DT}, no PubMed e no ClinicalTrials.gov. A consulta de cada linha está escrita <strong>inteira</strong>, ao lado do número, para qualquer pessoa repetir e me contradizer — e para o script que reconfere as contagens deste site conseguir rodar todas.",
            "A coluna de condição <strong>não é afirmação de mecanismo</strong>: é o campo <em>Condition</em> copiado dos registros de fase 3 que a própria busca devolveu. Quando não há registro de fase 3, a célula diz isso.",
                ], tabela=dict(cap="Levantamento de evidência — geroprotetores", linhas=[
                    ["Composto", "Condição nos registros de fase 3", "Consulta", "Artigos no PubMed", "Estudos no ClinicalTrials.gov"],
            ["<strong>Rapamicina</strong>", "<small>Pediatric Heart Transplantation; Immunosuppression; Chronic Kidney Diseases; Coronary Artery Disease</small>", "<code>rapamycin OR sirolimus</code>", "62.814", "2.382"],
            ["<strong>Metformina e envelhecimento</strong>", "<small>COPD; PreDiabetes; Aging; Insulin Sensitivity</small>", "<code>metformin AND (aging OR longevity)</code>", "1.672", "16"],
            ["<strong>Canaquinumabe</strong>", "<small>Periodic Fevers Syndrome; Acute Gout; Hereditary Periodic Fevers</small>", "<code>canakinumab</code>", "1.409", "117"],
            ["<strong>Anti-IL-11</strong>", "<small>nenhum registro de fase 3 nesta busca</small>", "<code>\"interleukin-11\" AND (antibody OR monoclonal)</code>", "296", "3"],
            ["<strong>Dasatinibe + quercetina</strong>", "<small>Obesity; Healthy Lifestyle</small>", "<code>dasatinib AND quercetin</code>", "371", "22"],
            ["<strong>Fisetina</strong>", "<small>Meniscus Tear; Meniscus; Derangement; Meniscus Lesion; Knee Osteoarthritis</small>", "<code>fisetin</code>", "1.647", "36"],
            ["<strong>Urolitina A</strong>", "<small>Adenocarcinoma of the Prostate</small>", "<code>\"urolithin A\"</code>", "707", "24"],
            ["<strong>NMN</strong>", "<small>Chronic Fatigue Syndrome (CFS); Post-COVID ME/CFS</small>", "<code>\"nicotinamide mononucleotide\"</code>", "1.718", "32"],
            ["<strong>NR</strong>", "<small>Parkinson Disease; Peripheral Artery Disease; Peripheral Artery Disease (PAD)</small>", "<code>\"nicotinamide riboside\"</code>", "956", "123"],
            ["<strong>GlyNAC</strong>", "<small>nenhum registro de fase 3 nesta busca</small>", "<code>GlyNAC</code>", "22", "3"],
            ["<strong>MitoQ</strong>", "<small>Schizophrenia and Related Disorders; Mitochondrial Alteration; Cognitive Impairment</small>", "<code>MitoQ OR mitoquinone</code>", "921", "44"],
            ["<strong>SkQ1</strong>", "<small>Dry Eye Syndrome</small>", "<code>SkQ1</code>", "264", "3"],
            ["<strong>PQQ</strong>", "<small>Glaucoma; Neuroprotection</small>", "<code>\"pyrroloquinoline quinone\"</code>", "1.177", "11"],
            ["<strong>Klotho recombinante</strong>", "<small>nenhum registro de fase 3 nesta busca</small>", "<code>klotho AND recombinant</code>", "303", "0"],
            ["<strong>Troca plasmatica</strong>", "<small>nenhum registro de fase 3 nesta busca</small>", "<code>\"therapeutic plasma exchange\" AND aging</code>", "29", "3"],
            ["<strong>Acarbose</strong>", "<small>nenhum registro de fase 3 nesta busca</small>", "<code>acarbose AND (aging OR lifespan)</code>", "136", "2"],
            ["<strong>17-alfa-estradiol</strong>", "<small>nenhum registro de fase 3 nesta busca</small>", "<code>\"17-alpha-estradiol\" AND lifespan</code>", "20", "0"],
                ])),
        dict(h="O que existe de fase 3, e de quem é", tipo="p", corpo=[
                    "Contagem de artigo mede atenção acadêmica, não evidência de desfecho. A tabela abaixo separa o que tem <strong>ensaio de fase 3 registrado</strong> — e mostra o maior registro que a busca devolveu em cada linha, com o número de participantes declarado e o patrocinador.",
            "Registro não é resultado. Um ensaio de fase 3 recrutando é intenção declarada com dinheiro atrás, e nada mais que isso.",
                ], tabela=dict(cap="Ensaios de fase 3 registrados — geroprotetores", linhas=[
                    ["Composto", "Consulta", "Ensaios registrados de fase 3", "O maior registro que abri"],
            ["<strong>Rapamicina</strong>", "<code>(rapamycin OR sirolimus) AND AREA[Phase]PHASE3</code>", "259", "<strong>NCT07407517</strong> · n = 904 · Fudan University<br><small>Breast Cancer Females, Triple Negative Breast Cancer (TNBC)</small>"],
            ["<strong>Metformina e envelhecimento</strong>", "<code>(metformin AND (aging OR longevity)) AND AREA[Phase]PHASE3</code>", "4", "<strong>NCT06999343</strong> · n = 212 · Fundación Instituto de Investigación Sanitaria de Navarra<br><small>COPD</small>"],
            ["<strong>Canaquinumabe</strong>", "<code>(canakinumab) AND AREA[Phase]PHASE3</code>", "36", "<strong>NCT01029652</strong> · n = 230 · Novartis Pharmaceuticals<br><small>Acute Gout</small>"],
            ["<strong>Anti-IL-11</strong>", "<code>(\"interleukin-11\" AND (antibody OR monoclonal)) AND AREA[Phase]PHASE3</code>", "0", "—"],
            ["<strong>Dasatinibe + quercetina</strong>", "<code>(dasatinib AND quercetin) AND AREA[Phase]PHASE3</code>", "1", "<strong>NCT05653258</strong> · n = 160 · Cedars-Sinai Medical Center<br><small>Obesity, Healthy Lifestyle</small>"],
            ["<strong>Fisetina</strong>", "<code>(fisetin) AND AREA[Phase]PHASE3</code>", "2", "<strong>NCT05505747</strong> · n = — · Austin V Stone<br><small>Meniscus Tear, Meniscus; Derangement, Meniscus Lesion</small>"],
            ["<strong>Urolitina A</strong>", "<code>(\"urolithin A\") AND AREA[Phase]PHASE3</code>", "1", "<strong>NCT03535675</strong> · n = 59 · Sidney Kimmel Comprehensive Cancer Center at Johns Hopkins<br><small>Adenocarcinoma of the Prostate</small>"],
            ["<strong>NMN</strong>", "<code>(\"nicotinamide mononucleotide\") AND AREA[Phase]PHASE3</code>", "1", "<strong>NCT06739720</strong> · n = 130 · The University of Hong Kong<br><small>Chronic Fatigue Syndrome (CFS), Post-COVID ME/CFS</small>"],
            ["<strong>NR</strong>", "<code>(\"nicotinamide riboside\") AND AREA[Phase]PHASE3</code>", "5", "<strong>NCT03568968</strong> · n = 410 · Haukeland University Hospital<br><small>Parkinson Disease</small>"],
            ["<strong>GlyNAC</strong>", "<code>(GlyNAC) AND AREA[Phase]PHASE3</code>", "0", "—"],
            ["<strong>MitoQ</strong>", "<code>(MitoQ OR mitoquinone) AND AREA[Phase]PHASE3</code>", "1", "<strong>NCT06191965</strong> · n = 100 · Mclean Hospital<br><small>Schizophrenia and Related Disorders, Mitochondrial Alteration, Cognitive Impairment</small>"],
            ["<strong>SkQ1</strong>", "<code>(SkQ1) AND AREA[Phase]PHASE3</code>", "2", "<strong>NCT04206020</strong> · n = 610 · Mitotech, SA<br><small>Dry Eye Syndrome</small>"],
            ["<strong>PQQ</strong>", "<code>(\"pyrroloquinoline quinone\") AND AREA[Phase]PHASE3</code>", "1", "<strong>NCT06431113</strong> · n = 40 · Fondazione IRCCS Policlinico San Matteo di Pavia<br><small>Glaucoma, Neuroprotection</small>"],
            ["<strong>Klotho recombinante</strong>", "<code>(klotho AND recombinant) AND AREA[Phase]PHASE3</code>", "0", "—"],
            ["<strong>Troca plasmatica</strong>", "<code>(\"therapeutic plasma exchange\" AND aging) AND AREA[Phase]PHASE3</code>", "0", "—"],
            ["<strong>Acarbose</strong>", "<code>(acarbose AND (aging OR lifespan)) AND AREA[Phase]PHASE3</code>", "0", "—"],
            ["<strong>17-alfa-estradiol</strong>", "<code>(\"17-alpha-estradiol\" AND lifespan) AND AREA[Phase]PHASE3</code>", "0", "—"],
                ])),
        dict(h="Onde a conta não fecha", tipo="li", corpo=[
                    "<strong>6 das 17 linhas não têm nenhum ensaio de fase 3 registrado.</strong> São Anti-IL-11, GlyNAC, Klotho recombinante, Troca plasmatica, Acarbose, 17-alfa-estradiol. Entre elas estão as duas que mais aparecem em material de venda de longevidade: o klotho recombinante e a troca plasmática.",
            "<strong>A rapamicina tem 259 ensaios de fase 3 e nenhum dos que abri é sobre envelhecimento</strong> — transplante cardíaco pediátrico, stent coronariano, câncer de mama. É o composto com mais biologia séria da lista e, ao mesmo tempo, o que mais se apoia em extrapolação quando o assunto é idade.",
            "<strong>Os precursores de NAD+ têm mais registro que os senolíticos.</strong> NMN e NR somam 155 estudos registrados; fisetina e a dupla dasatinibe + quercetina somam 58. O site já tem uma <a href=\"protocol_nad-plus.html\">página de NAD+</a> que diz que a via de administração muda tudo; a contagem aqui não contradiz isso — só mostra onde o esforço clínico foi.",
            "<strong>Os 2 ensaios de fase 3 de fisetina declaram inscrição de zero participantes.</strong> Os dois são de investigador individual, não de patrocinador industrial, e os dois estão registrados com o campo de inscrição em zero. Registro não é evidência — e aqui nem gente houve.",
            "<strong>8 dos 13 princípios ativos buscados não têm registro ativo na ANVISA.</strong> Os que têm — sirolimo, metformina, canaquinumabe, dasatinibe, acarbose — têm para transplante, diabetes, doença autoinflamatória e leucemia. Nenhum tem para idade.",
                ]),
        dict(h="No Brasil", tipo="p", corpo=[
                    f"Busquei cada princípio ativo no <strong>dado aberto de medicamentos registrados da ANVISA</strong>, baixado em {_DT} — 43.508 linhas, contando apenas situação <strong>Ativo</strong>.",
            "Duas linhas da tabela de evidência não entram aqui porque não são princípio ativo: a troca plasmática é procedimento e o anti-IL-11 é uma classe sem produto. As demais foram buscadas pelo nome em português do princípio ativo, inclusive as vendidas como suplemento — e é aí que a tabela mostra o que interessa: <strong>suplemento não aparece na base de medicamentos porque não é medicamento</strong>, e isso não é o mesmo que ser seguro.",
                ], tabela=dict(cap="Registro na ANVISA — geroprotetores", linhas=[
                    ["Princípio ativo", "Padrão buscado", "Registros ativos", "Classe terapêutica declarada", "Produtos"],
            ["<strong>Sirolimo</strong>", "<code>SIROLIMO</code>", "<strong>1</strong>", "<small>AGENTE IMUNOSUPRESSOR</small>", "RAPAMUNE"],
            ["<strong>Metformina</strong>", "<code>METFORMIN</code>", "<strong>78</strong>", "<small>ANTIDIABETICOS</small>", "CLORIDRATO DE METFORMINA, CLORIDRATO DE METFORMINA + BENZOATO DE ALOGLIPTINA, CLORIDRATO DE METFORMINA + FOSFATO DE SITAGLIPTINA, CLORIDRATO DE METFORMINA + GLIBENCLAMIDA, CLORIDRATO DE SITAGLIPTINA MONOIDRATADO + CLORIDRATO DE METFORMINA, DAPAGLIFLOZINA + CLORIDRATO DE METFORMINA"],
            ["<strong>Canaquinumabe</strong>", "<code>CANAQUINUMAB</code>", "<strong>1</strong>", "<small>IMUNOMODULADOR</small>", "ILARIS"],
            ["<strong>Dasatinibe</strong>", "<code>DASATINIB</code>", "<strong>10</strong>", "<small>ANTINEOPLASICO</small>", "DASATINIBE, DASATINIBE MONOIDRATADO, DASNAR, DAZANYN, LADIZAC, SPRYCEL"],
            ["<strong>Quercetina</strong>", "<code>QUERCETIN</code>", "<strong>0</strong>", "<small>—</small>", "—"],
            ["<strong>Fisetina</strong>", "<code>FISETIN</code>", "<strong>0</strong>", "<small>—</small>", "—"],
            ["<strong>Urolitina</strong>", "<code>UROLITIN</code>", "<strong>0</strong>", "<small>—</small>", "—"],
            ["<strong>Nicotinamida mononucleotideo</strong>", "<code>NICOTINAMIDA MONONUCLEOT</code>", "<strong>0</strong>", "<small>—</small>", "—"],
            ["<strong>Nicotinamida ribosideo</strong>", "<code>RIBOSID</code>", "<strong>0</strong>", "<small>—</small>", "—"],
            ["<strong>MitoQ</strong>", "<code>MITOQUINON</code>", "<strong>0</strong>", "<small>—</small>", "—"],
            ["<strong>PQQ</strong>", "<code>PIRROLOQUINOLIN</code>", "<strong>0</strong>", "<small>—</small>", "—"],
            ["<strong>Klotho</strong>", "<code>KLOTHO</code>", "<strong>0</strong>", "<small>—</small>", "—"],
            ["<strong>Acarbose</strong>", "<code>ACARBOSE</code>", "<strong>1</strong>", "<small>ANTIDIABETICOS</small>", "AGLUCOSE"],
                ])),
    ],
    nota_refs=(f"Todas as contagens desta página foram levantadas por mim em {_DT}, com a consulta declarada ao lado de cada número. As três ressalvas de método estão escritas na primeira seção, antes das tabelas. <strong>Esta página foi apurada em dia próprio</strong>, e por isso carrega data própria."),
    referencias=[
        ("API pública do ClinicalTrials.gov, versão 2 — a base de todas as contagens de estudo e de fase 3 desta página.",
         "https://clinicaltrials.gov/data-api/api"),
        ("E-utilities do PubMed (esearch) — a base de todas as contagens de artigo desta página.",
         "https://www.ncbi.nlm.nih.gov/books/NBK25501/"),
        ("Registro NCT05653258 no ClinicalTrials.gov — o único ensaio de fase 3 que a busca por dasatinibe com quercetina devolveu, patrocínio do Cedars-Sinai Medical Center.",
         "https://clinicaltrials.gov/study/NCT05653258"),
        ("Registro NCT06739720 no ClinicalTrials.gov — o único de fase 3 de nicotinamida mononucleotídeo que a busca devolveu, patrocínio da Universidade de Hong Kong.",
         "https://clinicaltrials.gov/study/NCT06739720"),
        ("Dado aberto de medicamentos registrados da ANVISA — a mesma base usada na página O que existe no Brasil.",
         "https://dados.anvisa.gov.br/dados/"),
    ],
),
}
