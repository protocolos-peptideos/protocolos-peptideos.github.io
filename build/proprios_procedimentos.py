# -*- coding: utf-8 -*-
"""Tratamentos que não são substância: levantamento de fonte primaria.

Apurado em 12 de setembro de 2026, num dia proprio -- por isso importa
DATA_NOVAS_CLASSES e nao DATA_APURACAO.

Nome de arquivo descritivo, e nao proprios20/21, de proposito: este repo
tem sessoes paralelas criando modulos numerados ao mesmo tempo.
"""

from datas import DATA_NOVAS_CLASSES as _DT

PROCEDIMENTOS = {
"proprio_procedimentos": dict(
    secoes=[
        dict(h="Por que um site de peptídeos precisa desta página", tipo="p", corpo=[
                    "Porque o comparador muda a conclusão. Um composto que faz perder cinco quilos parece muito ao lado de nada e parece pouco ao lado de uma cirurgia com décadas de seguimento. Este site passa o tempo inteiro medindo distância entre promessa e evidência; sem os procedimentos, a régua fica curta de um lado.",
            "Duas ressalvas de método. A busca da <strong>oxigenoterapia hiperbárica</strong> é cruzada com <code>aging</code> de propósito: sem isso, o número seria o da indicação clínica estabelecida, que é outro assunto. E a <strong>fotobiomodulação</strong> foi buscada pelo nome puro — o número inclui odontologia, dor e cicatrização, e é <strong>teto</strong> para o uso cognitivo que aparece em fórum.",
            "As três primeiras linhas foram buscadas pelo nome do procedimento, sem cruzamento, porque o nome já delimita o assunto.",
            "Nenhum número desta página veio da fonte secundária do site.",
                ]),
        dict(h="Quanta evidência existe, composto a composto", tipo="p", corpo=[
                    f"Os números abaixo foram levantados por mim em {_DT}, no PubMed e no ClinicalTrials.gov. A consulta de cada linha está escrita <strong>inteira</strong>, ao lado do número, para qualquer pessoa repetir e me contradizer — e para o script que reconfere as contagens deste site conseguir rodar todas.",
            "A coluna de condição <strong>não é afirmação de mecanismo</strong>: é o campo <em>Condition</em> copiado dos registros de fase 3 que a própria busca devolveu. Quando não há registro de fase 3, a célula diz isso.",
                ], tabela=dict(cap="Levantamento de evidência — tratamentos que não são substância", linhas=[
                    ["Composto", "Condição nos registros de fase 3", "Consulta", "Artigos no PubMed", "Estudos no ClinicalTrials.gov"],
            ["<strong>Cirurgia bariatrica</strong>", "<small>Obesity; Overweight; Severe Obesity; BMI Greater Than 30</small>", "<code>\"bariatric surgery\"</code>", "36.916", "2.039"],
            ["<strong>Transplante de microbiota fecal</strong>", "<small>Irritable Bowel Syndrome; Covid19; Carbapenem-Resistant Enterobacteriaceae Infection</small>", "<code>\"fecal microbiota transplantation\"</code>", "9.104", "644"],
            ["<strong>tDCS</strong>", "<small>Chronic Migraine Headache; Chronic Migraine; Headache; Healthy Volunteers</small>", "<code>\"transcranial direct current stimulation\"</code>", "11.183", "2.080"],
            ["<strong>Fotobiomodulacao</strong>", "<small>Mild Cognitive Impairment; Dementia; Mild; Chronic Knee Pain</small>", "<code>photobiomodulation</code>", "12.222", "584"],
            ["<strong>Oxigenoterapia hiperbarica</strong>", "<small>Aging</small>", "<code>\"hyperbaric oxygen\" AND aging</code>", "168", "2"],
                ])),
        dict(h="O que existe de fase 3, e de quem é", tipo="p", corpo=[
                    "Contagem de artigo mede atenção acadêmica, não evidência de desfecho. A tabela abaixo separa o que tem <strong>ensaio de fase 3 registrado</strong> — e mostra o maior registro que a busca devolveu em cada linha, com o número de participantes declarado e o patrocinador.",
            "Registro não é resultado. Um ensaio de fase 3 recrutando é intenção declarada com dinheiro atrás, e nada mais que isso.",
                ], tabela=dict(cap="Ensaios de fase 3 registrados — tratamentos que não são substância", linhas=[
                    ["Composto", "Consulta", "Ensaios registrados de fase 3", "O maior registro que abri"],
            ["<strong>Cirurgia bariatrica</strong>", "<code>(\"bariatric surgery\") AND AREA[Phase]PHASE3</code>", "76", "<strong>NCT02154763</strong> · n = 120 · Ottawa Hospital Research Institute<br><small>Bariatric Surgery Candidate</small>"],
            ["<strong>Transplante de microbiota fecal</strong>", "<code>(\"fecal microbiota transplantation\") AND AREA[Phase]PHASE3</code>", "61", "<strong>NCT04824222</strong> · n = 366 · Medical University of Warsaw<br><small>Covid19</small>"],
            ["<strong>tDCS</strong>", "<code>(\"transcranial direct current stimulation\") AND AREA[Phase]PHASE3</code>", "52", "<strong>NCT02315807</strong> · n = 60 · Federal University of Paraíba<br><small>Stroke, Cognitive Impairment, Cerebral Infarction</small>"],
            ["<strong>Fotobiomodulacao</strong>", "<code>(photobiomodulation) AND AREA[Phase]PHASE3</code>", "6", "<strong>NCT05894954</strong> · n = 73 · Alzheimer's Prevention and Reversal Project, Inc.<br><small>Mild Cognitive Impairment, Dementia, Mild</small>"],
            ["<strong>Oxigenoterapia hiperbarica</strong>", "<code>(\"hyperbaric oxygen\" AND aging) AND AREA[Phase]PHASE3</code>", "1", "<strong>NCT05297019</strong> · n = 30 · TruDiagnostic<br><small>Aging</small>"],
                ])),
        dict(h="Onde a conta não fecha", tipo="li", corpo=[
                    "<strong>A bariátrica sozinha tem 36.916 artigos e 2.039 estudos registrados.</strong> É a base de comparação que quase nunca aparece do lado dos frascos.",
            "<strong>O transplante de microbiota tem 644 estudos registrados e 61 de fase 3.</strong> A indicação com evidência consolidada é infecção intestinal recorrente; os registros que abri incluem síndrome do intestino irritável e COVID-19. Campo grande, alvo ainda disperso.",
            "<strong>A hiperbárica cruzada com envelhecimento tem 168 artigos e 2 estudos registrados.</strong> O único de fase 3 que a busca devolve tem 30 participantes e mede idade epigenética. É o tamanho real da evidência por trás de uma promessa vendida como estabelecida.",
            "<strong>tDCS e fotobiomodulação têm volume e dispersão.</strong> 2.080 e 584 estudos registrados, espalhados por dezenas de indicações. Muito estudo pequeno não vira um estudo grande.",
                ]),
    ],
    nota_refs=(f"Todas as contagens desta página foram levantadas por mim em {_DT}, com a consulta declarada ao lado de cada número. Esta página não tem tabela da ANVISA porque procedimento não tem princípio ativo para procurar no dado aberto de medicamentos. <strong>Esta página foi apurada em dia próprio</strong>, e por isso carrega data própria."),
    referencias=[
        ("API pública do ClinicalTrials.gov, versão 2 — a base de todas as contagens de estudo e de fase 3 desta página.",
         "https://clinicaltrials.gov/data-api/api"),
        ("E-utilities do PubMed (esearch) — a base de todas as contagens de artigo desta página.",
         "https://www.ncbi.nlm.nih.gov/books/NBK25501/"),
        ("Registro NCT05297019 no ClinicalTrials.gov — o único ensaio de fase 3 que a busca por oxigenoterapia hiperbárica cruzada com envelhecimento devolve, 30 participantes, patrocínio da TruDiagnostic.",
         "https://clinicaltrials.gov/study/NCT05297019"),
        ("Registro NCT06433180 no ClinicalTrials.gov — transplante de microbiota fecal em síndrome do intestino irritável grave, Assistance Publique – Hôpitaux de Paris.",
         "https://clinicaltrials.gov/study/NCT06433180"),
    ],
),
}
