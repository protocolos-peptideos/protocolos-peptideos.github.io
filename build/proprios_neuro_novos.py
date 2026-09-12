# -*- coding: utf-8 -*-
"""Neuro e cognição — o bloco russo e o que tem bula: levantamento de fonte primaria.

Apurado em 12 de setembro de 2026, num dia proprio -- por isso importa
DATA_NOVAS_CLASSES e nao DATA_APURACAO.

Nome de arquivo descritivo, e nao proprios20/21, de proposito: este repo
tem sessoes paralelas criando modulos numerados ao mesmo tempo.
"""

from datas import DATA_NOVAS_CLASSES as _DT

NEURO_NOVOS = {
"proprio_neuro_novos": dict(
    secoes=[
        dict(h="Duas metades que a conversa costuma juntar", tipo="p", corpo=[
                    "A conversa sobre cognição junta, na mesma lista, um pó russo comprado pela internet e um anticorpo monoclonal aprovado por agência. A tabela abaixo mede os dois com a mesma régua — número de artigos, número de estudos registrados, número de ensaios de fase 3 — e a régua separa sozinha.",
            "Quatro ressalvas de método, escritas antes dos números. <strong>Uma:</strong> a busca do KarXT usa <code>xanomeline AND trospium</code>, os dois princípios ativos, porque é assim que o registro escreve. <strong>Duas:</strong> <code>\"P021\"</code> entre aspas devolve artigos que usam o código para outras coisas — o número é teto. <strong>Três:</strong> o único registro de fase 3 do XPro1595 que a busca devolve é de COVID-19, não de Alzheimer. <strong>Quatro:</strong> a esketamina aparece na ANVISA sob a grafia <code>ESCETAMINA</code>, que é a que a base usa.",
            "Nenhum número desta página veio da fonte secundária do site.",
                ]),
        dict(h="Quanta evidência existe, composto a composto", tipo="p", corpo=[
                    f"Os números abaixo foram levantados por mim em {_DT}, no PubMed e no ClinicalTrials.gov. A consulta de cada linha está escrita <strong>inteira</strong>, ao lado do número, para qualquer pessoa repetir e me contradizer — e para o script que reconfere as contagens deste site conseguir rodar todas.",
            "A coluna de condição <strong>não é afirmação de mecanismo</strong>: é o campo <em>Condition</em> copiado dos registros de fase 3 que a própria busca devolveu. Quando não há registro de fase 3, a célula diz isso.",
                ], tabela=dict(cap="Levantamento de evidência — neuro e cognição", linhas=[
                    ["Composto", "Condição nos registros de fase 3", "Consulta", "Artigos no PubMed", "Estudos no ClinicalTrials.gov"],
            ["<strong>Noopept</strong>", "<small>nenhum registro de fase 3 nesta busca</small>", "<code>noopept OR \"GVS-111\"</code>", "113", "0"],
            ["<strong>Fenilpiracetam</strong>", "<small>nenhum registro de fase 3 nesta busca</small>", "<code>phenylpiracetam OR fonturacetam</code>", "31", "0"],
            ["<strong>Bromantano</strong>", "<small>nenhum registro de fase 3 nesta busca</small>", "<code>bromantane OR ladasten</code>", "74", "0"],
            ["<strong>Cortexina</strong>", "<small>nenhum registro de fase 3 nesta busca</small>", "<code>cortexin</code>", "217", "0"],
            ["<strong>Dihexa</strong>", "<small>nenhum registro de fase 3 nesta busca</small>", "<code>dihexa</code>", "18", "0"],
            ["<strong>P021</strong>", "<small>nenhum registro de fase 3 nesta busca</small>", "<code>\"P021\"</code>", "45", "0"],
            ["<strong>Modafinila</strong>", "<small>Cocaine Addiction; Cocaine Dependence; Narcolepsy; Attention Deficit Hyperactivity Disorder</small>", "<code>modafinil</code>", "2.412", "216"],
            ["<strong>Lecanemabe</strong>", "<small>Alzheimer's Disease; Preclinical Alzheimer's Disease; Early Preclinical Alzheimer's Disease; Early Alzheimer's Disease</small>", "<code>lecanemab</code>", "919", "34"],
            ["<strong>Donanemabe</strong>", "<small>Mild Cognitive Impairment (MCI); Alzheimer Disease; Dementia; Plaque</small>", "<code>donanemab</code>", "464", "19"],
            ["<strong>KarXT</strong>", "<small>Schizophrenia</small>", "<code>xanomeline AND trospium</code>", "159", "45"],
            ["<strong>Zuranolona</strong>", "<small>Major Depressive Disorder; Depressive Disorder; Major; Insomnia</small>", "<code>zuranolone</code>", "190", "17"],
            ["<strong>Esketamina</strong>", "<small>Treatment Resistant Depression; Major Depressive Disorder; Depressive Disorder; Major</small>", "<code>esketamine</code>", "2.420", "353"],
            ["<strong>XPro1595</strong>", "<small>COVID-19</small>", "<code>XPro1595</code>", "75", "5"],
                ])),
        dict(h="O que existe de fase 3, e de quem é", tipo="p", corpo=[
                    "Contagem de artigo mede atenção acadêmica, não evidência de desfecho. A tabela abaixo separa o que tem <strong>ensaio de fase 3 registrado</strong> — e mostra o maior registro que a busca devolveu em cada linha, com o número de participantes declarado e o patrocinador.",
            "Registro não é resultado. Um ensaio de fase 3 recrutando é intenção declarada com dinheiro atrás, e nada mais que isso.",
                ], tabela=dict(cap="Ensaios de fase 3 registrados — neuro e cognição", linhas=[
                    ["Composto", "Consulta", "Ensaios registrados de fase 3", "O maior registro que abri"],
            ["<strong>Noopept</strong>", "<code>(noopept OR \"GVS-111\") AND AREA[Phase]PHASE3</code>", "0", "—"],
            ["<strong>Fenilpiracetam</strong>", "<code>(phenylpiracetam OR fonturacetam) AND AREA[Phase]PHASE3</code>", "0", "—"],
            ["<strong>Bromantano</strong>", "<code>(bromantane OR ladasten) AND AREA[Phase]PHASE3</code>", "0", "—"],
            ["<strong>Cortexina</strong>", "<code>(cortexin) AND AREA[Phase]PHASE3</code>", "0", "—"],
            ["<strong>Dihexa</strong>", "<code>(dihexa) AND AREA[Phase]PHASE3</code>", "0", "—"],
            ["<strong>P021</strong>", "<code>(\"P021\") AND AREA[Phase]PHASE3</code>", "0", "—"],
            ["<strong>Modafinila</strong>", "<code>(modafinil) AND AREA[Phase]PHASE3</code>", "52", "<strong>NCT00343811</strong> · n = 120 · Cephalon<br><small>Attention Deficit Hyperactivity Disorder</small>"],
            ["<strong>Lecanemabe</strong>", "<code>(lecanemab) AND AREA[Phase]PHASE3</code>", "6", "<strong>NCT03887455</strong> · n = 1.906 · Eisai Inc.<br><small>Early Alzheimer's Disease</small>"],
            ["<strong>Donanemabe</strong>", "<code>(donanemab) AND AREA[Phase]PHASE3</code>", "8", "<strong>NCT05508789</strong> · n = 1.500 · Eli Lilly and Company<br><small>Alzheimer Disease, Dementia, Brain Diseases</small>"],
            ["<strong>KarXT</strong>", "<code>(xanomeline AND trospium) AND AREA[Phase]PHASE3</code>", "23", "<strong>NCT05304767</strong> · n = 290 · Karuna Therapeutics, Inc., a Bristol Myers Squibb company<br><small>Schizophrenia</small>"],
            ["<strong>Zuranolona</strong>", "<code>(zuranolone) AND AREA[Phase]PHASE3</code>", "8", "<strong>NCT03672175</strong> · n = 581 · Biogen<br><small>Major Depressive Disorder</small>"],
            ["<strong>Esketamina</strong>", "<code>(esketamine) AND AREA[Phase]PHASE3</code>", "30", "<strong>NCT03039192</strong> · n = 226 · Janssen Research & Development, LLC<br><small>Depressive Disorder, Major</small>"],
            ["<strong>XPro1595</strong>", "<code>(XPro1595) AND AREA[Phase]PHASE3</code>", "1", "<strong>NCT04370236</strong> · n = 79 · Inmune Bio, Inc.<br><small>COVID-19</small>"],
                ])),
        dict(h="Onde a conta não fecha", tipo="li", corpo=[
                    "<strong>Os quatro do bloco russo somam 0 estudos registrados.</strong> Noopept (0), fenilpiracetam (0), bromantano (0) e cortexina (0). A literatura existe — 217 artigos só de cortexina — e o registro de ensaio, na base internacional, não.",
            "<strong>Dihexa e P021 são pré-clínicos, e a base mostra.</strong> 18 e 45 artigos, 0 e 0 estudos registrados. Quem vende os dois como “nootrópico de nova geração” está vendendo bancada.",
            "<strong>Lecanemabe e donanemabe têm registro ativo no Brasil.</strong> LEQEMBI e KISUNLA, os dois na categoria biológico. É o contraste mais duro desta página: dois anticorpos de infusão hospitalar entraram no sistema de registro brasileiro enquanto nootrópico nenhum entrou.",
            "<strong>A esketamina tem 8 registros ativos</strong>, em duas classes — anestésico geral injetável e antidepressivo. A modafinila tem 2. São os dois únicos estimulantes/psicoativos desta lista com produto legal aqui, e os dois são de prescrição controlada.",
            "<strong>O único registro de fase 3 do XPro1595 é de COVID-19.</strong> 75 artigos, 5 estudos registrados, 1 de fase 3 — e esse é o de complicação pulmonar. A promessa que circula é neuroinflamação; o registro de fase 3 é outro assunto.",
                ]),
        dict(h="No Brasil", tipo="p", corpo=[
                    f"Busquei cada princípio ativo no <strong>dado aberto de medicamentos registrados da ANVISA</strong>, baixado em {_DT} — 43.508 linhas, contando apenas situação <strong>Ativo</strong>. A coluna de classe terapêutica é a que a própria base declara.",
            "O padrão é limpo: os quatro do bloco russo, mais a xanomelina do KarXT e a zuranolona, voltam vazios. Modafinila, esketamina, lecanemabe e donanemabe têm produto. Não estar na base não é proibição — é ausência de produto legal com aquele princípio ativo.",
                ], tabela=dict(cap="Registro na ANVISA — neuro e cognição", linhas=[
                    ["Princípio ativo", "Padrão buscado", "Registros ativos", "Classe terapêutica declarada", "Produtos"],
            ["<strong>Noopept</strong>", "<code>NOOPEPT</code>", "<strong>0</strong>", "<small>—</small>", "—"],
            ["<strong>Fenilpiracetam</strong>", "<code>FENILPIRACETAM</code>", "<strong>0</strong>", "<small>—</small>", "—"],
            ["<strong>Bromantano</strong>", "<code>BROMANTAN</code>", "<strong>0</strong>", "<small>—</small>", "—"],
            ["<strong>Cortexina</strong>", "<code>CORTEXIN</code>", "<strong>0</strong>", "<small>—</small>", "—"],
            ["<strong>Modafinila</strong>", "<code>MODAFINIL</code>", "<strong>2</strong>", "<small>OUTROS PRODUTOS QUE ATUAM SOBRE O SISTEMA NERVOSO</small>", "NUVIGIL, STAVIGILE"],
            ["<strong>Lecanemabe</strong>", "<code>LECANEMAB</code>", "<strong>1</strong>", "<small>OUTROS PRODUTOS QUE ATUAM SOBRE O SISTEMA NERVOSO</small>", "LEQEMBI"],
            ["<strong>Donanemabe</strong>", "<code>DONANEMAB</code>", "<strong>1</strong>", "<small>OUTROS MEDICAMENTOS ANTI-DEMÊNCIA</small>", "KISUNLA"],
            ["<strong>Xanomelina</strong>", "<code>XANOMELIN</code>", "<strong>0</strong>", "<small>—</small>", "—"],
            ["<strong>Zuranolona</strong>", "<code>ZURANOLON</code>", "<strong>0</strong>", "<small>—</small>", "—"],
            ["<strong>Escetamina</strong>", "<code>ESCETAMIN</code>", "<strong>8</strong>", "<small>ANESTESICOS GERAIS INJETAVEIS; ANTIDEPRESSIVOS</small>", "CLORIDRATO DE ESCETAMINA, KETAH, KETAH LC, KETAMIN, SPRAVATO"],
                ])),
    ],
    nota_refs=(f"Todas as contagens desta página foram levantadas por mim em {_DT}, com a consulta declarada ao lado de cada número. As quatro ressalvas de método estão escritas antes das tabelas. <strong>Esta página foi apurada em dia próprio</strong>, e por isso carrega data própria."),
    referencias=[
        ("API pública do ClinicalTrials.gov, versão 2 — a base de todas as contagens de estudo e de fase 3 desta página.",
         "https://clinicaltrials.gov/data-api/api"),
        ("E-utilities do PubMed (esearch) — a base de todas as contagens de artigo desta página.",
         "https://www.ncbi.nlm.nih.gov/books/NBK25501/"),
        ("Registro NCT04370236 no ClinicalTrials.gov — INB03/XPro1595 em complicação pulmonar de COVID-19, o único de fase 3 que a busca devolve.",
         "https://clinicaltrials.gov/study/NCT04370236"),
        ("Registro NCT04468659 no ClinicalTrials.gov — lecanemabe, patrocínio da Eisai, um dos ensaios de fase 3 que a busca devolve.",
         "https://clinicaltrials.gov/study/NCT04468659"),
        ("Dado aberto de medicamentos registrados da ANVISA — a mesma base usada na página O que existe no Brasil.",
         "https://dados.anvisa.gov.br/dados/"),
    ],
),
}
