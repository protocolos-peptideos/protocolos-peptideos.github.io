# -*- coding: utf-8 -*-
"""Anticorpos monoclonais: levantamento de fonte primaria.

Apurado em 12 de setembro de 2026, varios dias depois das outras paginas desta
secao. Por isso importa DATA_MABS, e nao DATA_APURACAO: carimbar esta pagina
com a data de uma varredura anterior seria afirmar uma conferencia que naquele
dia nao houve. Ver o cabecalho de datas.py.

Consultas rodadas:
  PubMed              bimagrumab / trevogrumab / garetosmab / "monoclonal antibody",
                      cada um tambem com o filtro de Clinical Trial e RCT
  ClinicalTrials.gov  campo de intervencao: bimagrumab, trevogrumab, garetosmab
  openFDA             openfda.generic_name para os tres, e description:"monoclonal antibody"
  OMS/INN             sumario executivo da 73a Consultacao (Working Doc. 21.533)

Nao cita a ANVISA de proposito: registro brasileiro desta classe nao foi
conferido nesta varredura, e o que nao foi conferido nao entra. A ausencia
esta declarada na secao final da propria pagina.
"""

from datas import DATA_MABS as _DT

MABS = {
"proprio_anticorpos": dict(
    titulo="Anticorpos monoclonais — por que não são peptídeo, e o que a evidência mostra",
    secoes=[
        dict(h="Anticorpo monoclonal não é peptídeo, e a diferença é de ordem de grandeza", tipo="p", corpo=[
            "Um <strong>anticorpo monoclonal</strong> é uma proteína grande, construída por célula viva, desenhada "
            "para grudar num alvo só. Um peptídeo é uma cadeia curta de aminoácidos, e a maior parte do que este "
            "site cobre sai de síntese química. A diferença entre os dois não é de grau — é de tamanho, de "
            "fabricação e de logística, e é ela que decide o que dá para fazer com um frasco.",
            "Para não discutir isso no abstrato, li as duas bulas na base de rótulos da FDA em "
            f"{_DT} e coloquei lado a lado o único anticorpo desta página que tem rótulo aprovado e o peptídeo "
            "mais conhecido deste site. O rótulo de semaglutida que li é o da <strong>apresentação em "
            "comprimido</strong> — RYBELSUS e OZEMPIC comprimidos, no mesmo documento —, e não o da caneta "
            "injetável; a molécula é a mesma, a forma de tomar é que muda.",
        ], tabela=dict(
            cap="As duas bulas, lado a lado",
            linhas=[
                ["", "Garetosmab (PASATRU)", "Semaglutida (RYBELSUS / OZEMPIC comprimidos)"],
                ["O que a própria bula diz que é",
                 "Anticorpo monoclonal IgG4 humano, produzido por tecnologia de DNA recombinante em cultura de "
                 "células de ovário de hamster chinês",
                 "Agonista do receptor de GLP-1; o esqueleto peptídico é produzido por fermentação em levedura"],
                ["Massa molecular declarada", "<strong>cerca de 146 kDa</strong>", "<strong>4.113,58 g/mol</strong>"],
                ["Via e frequência", "Infusão <strong>intravenosa</strong> de 60 minutos, uma vez a cada 4 semanas",
                 "<strong>Comprimido por via oral</strong>, uma vez ao dia, em jejum, engolido inteiro"],
                ["Dose que a bula recomenda", "10 mg/kg, podendo cair para 3 mg/kg se não for tolerada",
                 "3 mg, 7 mg ou 14 mg"],
            ])),
        dict(h="A conta que essa tabela esconde", tipo="li", corpo=[
            "<strong>146 kDa dividido por 4.113,58 g/mol dá cerca de 35.</strong> O anticorpo é 35 vezes mais "
            "pesado que a molécula de semaglutida. Não é uma variação dentro da mesma família de substâncias; é "
            "outra categoria de coisa.",
            "<strong>10 mg/kg numa pessoa de 80 kg são 800 mg por infusão.</strong> A conta é minha, feita sobre "
            "a dose por quilo que está na bula. O frasco de PASATRU tem 300 mg em 5 mL — então uma dose passa de "
            "dois frascos e meio. Compare com os 14 mg do comprimido de maior dose de semaglutida, e com os "
            "microgramas em que o resto deste site mede peptídeo.",
            "<strong>Um é engolido em jejum; o outro entra na veia por uma hora, num serviço de saúde.</strong> "
            "Essa linha da tabela é a razão pela qual não existe aqui tabela de reconstituição: não há nada para "
            "reconstituir, e o passo seguinte não é uma seringa de insulina.",
        ]),
        dict(h="O nome parou de entregar a classe", tipo="p", corpo=[
            "O mercado aprendeu a reconhecer anticorpo pela terminação <code>-mab</code>, de "
            "<em>monoclonal antibody</em>. Isso deixou de ser regra. No sumário executivo da <strong>73ª "
            "Consultação de Denominações Comuns Internacionais da OMS</strong> (Working Doc. 21.533, novembro de "
            "2021), o grupo de especialistas aprovou um esquema novo, que divide os anticorpos monoclonais em "
            "quatro grupos — e decidiu <strong>abandonar de vez o radical <code>-mab</code></strong>, para evitar "
            "confusão agora que os outros grupos ganharam sufixo próprio.",
            "Os nomes desta página são todos anteriores a essa decisão, e por isso ainda terminam em "
            "<code>-mab</code>. Escrevo-os aqui aportuguesados, com a terminação <em>-mabe</em>, quando o texto "
            "corre em português; nas consultas e nas tabelas uso a forma que a OMS publicou: "
            "<code>bimagrumab</code>, <code>trevogrumab</code> e <code>garetosmab</code>.",
        ], tabela=dict(
            cap="Os quatro grupos do esquema aprovado em 2021",
            linhas=[
                ["Grupo", "O que é", "Sufixo"],
                ["1", "Monoespecíficos e não modificados", "<code>-tug</code> — o <em>ug</em> foi definido como "
                 "<em>unmodified immunoglobulin</em>"],
                ["2", "Monoespecíficos de comprimento inteiro, com domínio constante modificado por engenharia",
                 "<code>-bart</code>, de <em>antibody artificial</em>"],
                ["3", "Bi ou multiespecíficos, em qualquer formato", "<code>-mig</code>, de "
                 "<em>multispecific-immunoglobulin</em>"],
                ["4", "Fragmentos monoespecíficos derivados do domínio variável de uma imunoglobulina",
                 "<code>-ment</code>, de <em>fragment</em>"],
            ])),
        dict(h="Quanta evidência existe, de verdade", tipo="p", corpo=[
            f"Os números abaixo foram levantados por mim em {_DT}. A consulta de cada linha está ao lado do "
            "número, para qualquer pessoa repetir e me contradizer. Os três anticorpos são os que aparecem na "
            "mesma conversa dos GLP-1 quando o assunto é massa magra: <strong>bimagrumabe</strong>, que bloqueia "
            "os receptores de activina do tipo II; <strong>trevogrumabe</strong>, dirigido à miostatina; e "
            "<strong>garetosmabe</strong>, dirigido à activina A.",
        ], tabela=dict(
            cap="Levantamento de evidência — os três anticorpos",
            linhas=[
                ["Base", "Consulta", "Resultado"],
                ["PubMed", "<code>bimagrumab</code>", "91 artigos"],
                ["PubMed", "<code>bimagrumab AND (Clinical Trial[Publication Type] OR Randomized Controlled "
                           "Trial[Publication Type])</code>", "17 artigos"],
                ["ClinicalTrials.gov", "campo de intervenção: <code>bimagrumab</code>", "17 estudos registrados"],
                ["openFDA", "<code>openfda.generic_name:\"bimagrumab\"</code>", "<strong>0 rótulos</strong>"],
                ["PubMed", "<code>trevogrumab</code>", "<strong>2 artigos</strong>"],
                ["PubMed", "<code>trevogrumab AND (Clinical Trial[Publication Type] OR Randomized Controlled "
                           "Trial[Publication Type])</code>", "<strong>0 artigos</strong>"],
                ["ClinicalTrials.gov", "campo de intervenção: <code>trevogrumab</code>",
                 "<strong>1 estudo registrado</strong>"],
                ["openFDA", "<code>openfda.generic_name:\"trevogrumab\"</code>", "<strong>0 rótulos</strong>"],
                ["PubMed", "<code>garetosmab</code>", "14 artigos"],
                ["PubMed", "<code>garetosmab AND (Clinical Trial[Publication Type] OR Randomized Controlled "
                           "Trial[Publication Type])</code>", "5 artigos"],
                ["ClinicalTrials.gov", "campo de intervenção: <code>garetosmab</code>", "6 estudos registrados"],
                ["openFDA", "<code>openfda.generic_name:\"garetosmab\"</code>", "<strong>1 rótulo</strong>"],
            ])),
        dict(h="A classe é enorme; estes três não são", tipo="p", corpo=[
            "Anticorpo monoclonal é das coisas mais estudadas da medicina, e é justamente esse contraste que "
            "interessa a quem chega aqui vindo de um fórum de treino: o tamanho da literatura da classe não se "
            "transfere para a molécula específica que alguém está considerando.",
        ], tabela=dict(
            cap="O tamanho da classe, medido nas mesmas bases",
            linhas=[
                ["Base", "Consulta", "Resultado"],
                ["PubMed", "<code>\"monoclonal antibody\"</code>", "<strong>424.965 artigos</strong>"],
                ["openFDA", "<code>description:\"monoclonal antibody\"</code>", "281 rótulos"],
                ["openFDA", "<code>description:\"monoclonal antibody\"</code>, agrupado por "
                            "<code>openfda.generic_name.exact</code>", "149 nomes genéricos distintos"],
            ])),
        dict(h="O que o único ensaio publicado mediu", tipo="p", corpo=[
            "Dos três, só o bimagrumabe tem ensaio de fase 2 publicado em revista sobre obesidade: o "
            "<strong>BELIEVE</strong>, saído na <strong>Nature Medicine</strong> em março de 2026 "
            "(<code>NCT05616013</code>). <strong>507 adultos</strong> com obesidade foram sorteados em nove "
            "grupos e tratados por <strong>48 semanas</strong>, com extensão aberta até a semana 72.",
            "O desenho é a informação mais importante da página, e quase nunca aparece quando o estudo é citado "
            "em rede social: o bimagrumabe foi dado por <strong>infusão intravenosa a cada 12 semanas</strong>, "
            "em 10 ou 30 mg/kg, enquanto a semaglutida era subcutânea semanal, em 1,0 ou 2,4 mg.",
            "As mudanças médias de peso na semana 48, como o próprio artigo as reporta: <strong>−9,3 kg</strong> "
            "com bimagrumabe 30 mg/kg sozinho, <strong>−14,2 kg</strong> com semaglutida 2,4 mg sozinha, "
            "<strong>−17,8 kg</strong> com os dois juntos na dose alta, contra <strong>−3,3 kg</strong> no "
            "placebo — todos com P &lt; 0,001 contra placebo. Os eventos adversos comuns do bimagrumabe foram "
            "espasmos musculares, diarreia e acne.",
            "<strong>Leia o que esse resultado não diz.</strong> O anticorpo sozinho perdeu menos peso que a "
            "semaglutida sozinha. O que a hipótese do campo sustenta é outra coisa — a composição do peso "
            "perdido —, e essa é a pergunta que o ensaio de fase 2 do trevogrumabe, o "
            "<strong>COURAGE</strong> (<code>NCT06299098</code>), colocou como desfecho primário: variação "
            "percentual de massa gorda, de massa magra e de peso. São <strong>1.005 participantes</strong>, "
            "início em 13 de março de 2024, conclusão primária prevista para 16 de junho de 2026, e "
            "<strong>nenhum resultado publicado</strong> que eu tenha localizado — o PubMed devolve dois artigos "
            "para o nome do fármaco, e nenhum é ensaio.",
        ]),
        dict(h="O único com bula é para uma doença que quase ninguém tem", tipo="p", corpo=[
            "O garetosmabe tem rótulo aprovado pela FDA sob a marca <strong>PASATRU</strong> (BLA 761508, "
            "Regeneron), com data de vigência de <strong>14 de agosto de 2026</strong> no registro que li. A "
            "indicação não tem nada a ver com peso: é reduzir a formação de novas lesões de ossificação "
            "heterotópica e as crises em adultos com <strong>fibrodisplasia ossificante progressiva</strong>, "
            "uma doença rara em que tecido mole vira osso.",
            "É o exemplo mais útil desta página inteira, porque mostra o que significa uma molécula desta classe "
            "<em>chegar</em> ao mercado: infusão de 60 minutos a cada quatro semanas, num serviço de saúde; "
            "frasco de dose única de 300 mg em 5 mL; guardar entre 2 °C e 8 °C, na embalagem original, protegido "
            "da luz, sem congelar e sem agitar. As reações adversas mais comuns, com incidência de 10% ou mais, "
            "são abscesso, acne, aumento de pelos, madarose, úlceras orais e epistaxe.",
            "A bula também traz o número que nenhum peptídeo de frasco tem: <strong>1,3% (1 de 76)</strong> dos "
            "pacientes tratados por até 76 semanas desenvolveram anticorpos contra o próprio fármaco. Proteína "
            "grande é vista pelo sistema imune; o rótulo mede isso e publica.",
        ]),
        dict(h="O que foi retirado antes de começar", tipo="li", corpo=[
            "<strong><code>NCT06901349</code> — bimagrumabe com tirzepatida, da Eli Lilly: retirado.</strong> "
            "O motivo registrado no ClinicalTrials.gov é <em>Study terminated for strategic business reasons</em>.",
            "<strong><code>NCT06970405</code> — garetosmabe em homens obesos saudáveis e mulheres na "
            "pós-menopausa, fase 1: retirado.</strong> Motivo registrado: <em>Sponsor Decision</em>. Era o único "
            "estudo que eu localizei do garetosmabe fora de doença rara.",
            "<strong>O que continua de pé</strong>: o <code>NCT06643728</code>, de bimagrumabe com tirzepatida "
            "em manejo de peso, com 252 participantes, está ativo e não recruta mais; e o <code>NCT05933499</code>, "
            "conduzido pelo Massachusetts General Hospital com 63 participantes, recruta.",
            "<strong>Ensaio retirado não é evidência de dano.</strong> É evidência de que a resposta não virá tão "
            "cedo — e, num campo em que o entusiasmo corre muito à frente do dado, saber quais perguntas "
            "deixaram de ser feitas vale tanto quanto saber as respostas que existem.",
        ]),
        dict(h="Antidoping: a classe já tem método de detecção", tipo="p", corpo=[
            "Quem treina para competir tem um dado concreto aqui, e ele é antigo. Segundo o artigo de "
            "Sakellariou e colegas na <strong>Scientific Reports</strong> em 2025, os inibidores das vias de "
            "sinalização do receptor de activina estão incluídos nas seções <strong>S2</strong> "
            "(<em>Peptide hormones, growth factors, related substances and mimetics</em>) e <strong>S4</strong> "
            "(<em>Hormone and metabolic modulators</em>) da Lista Proibida da Agência Mundial Antidoping.",
            "O mesmo trabalho descreve um método capaz de detectar nove dessas substâncias em soro e plasma de "
            "controle de dopagem, <strong>o garetosmabe entre elas</strong>, com limite de detecção entre 10 e "
            "50 ng/mL. E o bimagrumabe já tinha método próprio publicado em <strong>2018</strong>, na Proteomics "
            "Clinical Applications, pelo mesmo grupo de Colônia.",
            "Ou seja: a detecção não está atrás da molécula. Está na frente dela.",
        ]),
        dict(h="O que este levantamento não fez", tipo="li", corpo=[
            "<strong>Não conferi registro no Brasil para nenhum dos três.</strong> A varredura brasileira deste "
            "site é de 4 de setembro e não cobriu esta classe. Qualquer afirmação minha sobre registro brasileiro "
            "destes anticorpos hoje seria chute. O que está verificado é o rótulo da FDA: um dos três tem, dois "
            "não têm.",
            "<strong>Não conferi se algum deles é vendido como material de pesquisa.</strong> Este site nasceu de "
            "uma fonte que cataloga frasco de peptídeo; não fui a nenhum vendedor conferir se anticorpo circula "
            "pelo mesmo canal, e não vou afirmar nem que circula, nem que não circula.",
            "<strong>Li resumos e bulas, não os artigos inteiros.</strong> Os números do BELIEVE são os que o "
            "próprio resumo publica. Não fui ao material suplementar, não separei análise por protocolo de "
            "intenção de tratar e não avaliei risco de viés.",
            "<strong>Não cobri a classe.</strong> A mesma consulta que devolveu 149 nomes genéricos distintos na "
            "base da FDA mostra o tamanho do que ficou de fora: esta página trata de três anticorpos, escolhidos "
            "por aparecerem na conversa de composição corporal, e não diz nada sobre os outros.",
            "<strong>Não há tabela de reconstituição, dose de comunidade nem estrutura de ciclo nesta página</strong>, "
            "e é deliberado. Publicar um esquema caseiro para molécula que só existe como infusão hospitalar daria "
            "a ela uma aparência de protocolo que a evidência e a própria farmacotécnica não sustentam.",
        ]),
    ],
    nota_refs=(f'Cada número desta página foi levantado por mim em {_DT} no PubMed, no ClinicalTrials.gov e na '
               'base de rótulos da FDA, e a consulta usada está declarada acima. <strong>Esta página é mais nova '
               'que as outras desta seção</strong>, apurada em outro dia, e por isso carrega data própria. O '
               'registro brasileiro desta classe não foi conferido e está declarado como lacuna no corpo da '
               'página.'),
    referencias=[
        ("Heymsfield SB et al. Bimagrumab plus semaglutide alone or in combination for the treatment of obesity: "
         "a randomized phase 2 trial. Nat Med. 2026;32(3):869-882 — BELIEVE, NCT05616013, 507 participantes, "
         "48 semanas. PMID 41772149.",
         "https://doi.org/10.1038/s41591-026-04204-0"),
        ("Registro do BELIEVE no ClinicalTrials.gov, com o desenho de nove grupos e as doses intravenosas de "
         "bimagrumabe a cada 12 semanas.",
         "https://clinicaltrials.gov/study/NCT05616013"),
        ("Registro do COURAGE no ClinicalTrials.gov — trevogrumabe, com ou sem garetosmabe, somado à semaglutida; "
         "1.005 participantes; massa gorda e massa magra entre os desfechos primários.",
         "https://clinicaltrials.gov/study/NCT06299098"),
        ("Registro do estudo de bimagrumabe com tirzepatida retirado pela Eli Lilly, com o motivo declarado.",
         "https://clinicaltrials.gov/study/NCT06901349"),
        ("Registro do estudo de fase 1 de garetosmabe em pessoas obesas saudáveis, retirado por decisão do "
         "patrocinador.",
         "https://clinicaltrials.gov/study/NCT06970405"),
        ("Rótulo aprovado de PASATRU (garetosmab-grts), BLA 761508, na base pública de rótulos da FDA — classe, "
         "massa molecular, via, dose, armazenamento, reações adversas e imunogenicidade.",
         "https://open.fda.gov/apis/drug/label/"),
        ("Sakellariou P, Walpurgis K, Thomas A et al. Combined detection of inhibitors of the activin receptor "
         "signaling pathways (IASPs) by means of LC-HRMS/MS for human doping control. Sci Rep. 2025;15:19887 — "
         "as seções S2 e S4 da Lista Proibida e o método para nove substâncias. PMID 40481031.",
         "https://doi.org/10.1038/s41598-025-03562-y"),
        ("Walpurgis K, Thomas A, Dellanna F, Schänzer W, Thevis M. Detection of the Human Anti-ActRII Antibody "
         "Bimagrumab in Serum by Means of Affinity Purification, Tryptic Digestion, and LC-HRMS. Proteomics Clin "
         "Appl. 2018;12(3):1700120. PMID 29226558.",
         "https://doi.org/10.1002/prca.201700120"),
        ("Sumário executivo da 73ª Consultação de INN da OMS, Working Doc. 21.533, novembro de 2021 — os quatro "
         "grupos de anticorpo monoclonal e a decisão de abandonar o radical -mab.",
         "https://cdn.who.int/media/docs/default-source/international-nonproprietary-names-(inn)/73rd_executive_summary.pdf"),
        ("Lista Proibida da Agência Mundial Antidoping, a mesma fonte usada nas outras páginas deste site.",
         "https://www.wada-ama.org/en/prohibited-list"),
        ("API pública de rótulos da FDA, usada para as contagens da classe e para confirmar a ausência de "
         "registro do bimagrumabe e do trevogrumabe.",
         "https://open.fda.gov/apis/drug/label/"),
    ],
),
}
