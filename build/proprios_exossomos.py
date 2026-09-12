# -*- coding: utf-8 -*-
"""Exossomos: levantamento de fonte primaria.

Apurado em 12 de setembro de 2026, num dia proprio -- por isso importa
DATA_EXOSSOMOS e nao DATA_APURACAO. Carimbar esta pagina com a data da
varredura de setembro seria afirmar uma conferencia que naquele dia nao houve.

Nome de arquivo descritivo, e nao proprios19/20, de proposito: este repo tem
sessoes paralelas criando modulos numerados ao mesmo tempo, e duas sessoes
escolhendo o proximo numero livre colidem.

Consultas rodadas:
  PubMed             exosome OR exosomes  (e o mesmo com filtro de ensaio)
  ClinicalTrials.gov intervencao: exosome OR exosomes, com recortes de tipo,
                     fase e resultado postado
  openFDA            openfda.generic_name:"exosome" e busca livre por exosome
  ANVISA             grep no dado aberto de medicamentos registrados
  FDA                notificacao de seguranca de 06/12/2019 e duas cartas de
                     advertencia, lidas na pagina da agencia
  ANVISA / SBD       pagina de cosmeticos para tratamentos esteticos e a nota
                     tecnica da Sociedade Brasileira de Dermatologia
"""

from datas import DATA_EXOSSOMOS as _DT

EXOSSOMOS = {
"proprio_exossomos": dict(
    secoes=[
        dict(h="O que é — e o nome já é o primeiro problema", tipo="p", corpo=[
            "Exossomo não é uma molécula. É uma <strong>vesícula extracelular de escala nanométrica</strong>, "
            "liberada por células — nas preparações vendidas, quase sempre células-tronco mesenquimais de cordão "
            "umbilical, placenta ou tecido adiposo, ou células da papila dérmica. O que se compra não é uma "
            "substância definida: é o material separado do meio em que essas células foram cultivadas.",
            "Isso põe os exossomos na mesma categoria de problema do "
            "<a href=\"proprio_thymalin.html\">Thymalin</a>, que é extrato de timo bovino: <strong>não existe "
            "sequência para citar, não existe pureza para conferir num laudo, e dois frascos com o mesmo nome "
            "podem não ser a mesma coisa</strong>. A diferença é que o Thymalin não finge ser molécula, e "
            "“exossomo” soa como se fosse.",
            "A dificuldade não é minha nem é de quem vende: é da própria área. O documento de consenso da "
            "<strong>International Society for Extracellular Vesicles</strong> — o MISEV2023, escrito com "
            "contribuição de mais de mil pesquisadores — lista, entre os obstáculos ainda abertos do campo, os "
            "<em>desafios de nomenclatura</em> e a <em>separação das vesículas em relação a partículas "
            "extracelulares não vesiculares</em>. Em português claro: a sociedade científica da área diz que "
            "nomear e purificar continuam sendo problemas não resolvidos.",
            "Esta página não veio da fonte secundária que originou a maior parte deste site. Foi montada do "
            "zero, no PubMed, no ClinicalTrials.gov, na base de rótulos da FDA e no dado aberto da ANVISA.",
        ]),
        dict(h="Quanta evidência existe, de verdade", tipo="p", corpo=[
            f"Os números abaixo foram levantados por mim em {_DT}. A consulta de cada linha está ao lado do "
            "número, para qualquer pessoa repetir e me contradizer.",
            "Cada consulta está escrita <strong>inteira</strong>, e não como “a mesma de cima mais um filtro”: "
            "assim cada linha reproduz sozinha, num só colar, e o script que reconfere as contagens deste site "
            "consegue rodar todas. Abreviar a consulta é o defeito que esta referência já cometeu uma vez e "
            "resolveu com uma trava.",
        ], tabela=dict(
            cap="Levantamento de evidência — exossomos",
            linhas=[
                ["Base", "Consulta", "Resultado"],
                ["PubMed", "<code>exosome OR exosomes</code>", "<strong>45.674 artigos</strong>"],
                ["PubMed", "<code>(exosome OR exosomes) AND (Clinical Trial[Publication Type] OR Randomized Controlled Trial[Publication Type])</code>",
                 "168 artigos"],
                ["PubMed", "<code>(exosome OR exosomes) AND Randomized Controlled Trial[Publication Type]</code>",
                 "<strong>83 artigos</strong>"],
                ["ClinicalTrials.gov", "campo de intervenção: <code>exosome OR exosomes</code>", "378 estudos registrados"],
                ["ClinicalTrials.gov", "campo de intervenção: <code>(exosome OR exosomes) AND AREA[StudyType]INTERVENTIONAL</code>", "235 estudos"],
                ["ClinicalTrials.gov", "campo de intervenção: <code>(exosome OR exosomes) AND AREA[StudyType]OBSERVATIONAL</code>", "<strong>142 estudos</strong>"],
                ["ClinicalTrials.gov", "campo de intervenção: <code>(exosome OR exosomes) AND AREA[Phase]PHASE3</code>", "9 registros"],
                ["ClinicalTrials.gov", "campo de intervenção: <code>(exosome OR exosomes) AND AREA[ResultsFirstPostDate]RANGE[MIN,MAX]</code>",
                 "<strong>9 estudos com resultado postado</strong>"],
            ])),
        dict(h="E nas duas agências", tipo="p", corpo=[
            "As duas bases regulatórias ficam fora da tabela acima porque não são contagem de literatura, e o "
            f"script que reconfere as contagens deste site só sabe repetir PubMed e ClinicalTrials.gov. Rodei as "
            f"duas à mão em {_DT}.",
            "Na base de rótulos da FDA, <code>openfda.generic_name:\"exosome\"</code> devolve "
            "<strong>NOT_FOUND</strong> — <strong>zero rótulos</strong>. A busca livre por <code>exosome</code> "
            "na mesma base devolve <strong>3 rótulos</strong>, e nenhum deles é produto aprovado; o que são está "
            "na seção da FDA, mais abaixo.",
            "No dado aberto de medicamentos registrados da ANVISA, <code>exossom</code> e <code>exosom</code> "
            "devolvem <strong>zero ocorrências</strong>. O que essa ausência significa — e o que ela não "
            "significa — está na seção sobre o Brasil.",
        ]),
        dict(h="Onde a conta não fecha", tipo="li", corpo=[
            "<strong>45.674 artigos e 83 ensaios randomizados.</strong> Os randomizados são menos de "
            "<strong>0,2%</strong> da literatura; com o filtro mais largo, de qualquer tipo de ensaio clínico, "
            "são 168 — menos de 0,4%. Nenhum outro composto deste site tem uma assimetria dessa ordem.",
            "<strong>142 dos 378 registros são observacionais</strong>, não intervencionais. A maior parte "
            "deles não dá exossomo a ninguém: <strong>mede</strong> exossomo no sangue como marcador de doença. "
            "É outro assunto, e é de onde vem boa parte do prestígio da palavra.",
            "<strong>9 dos 378 registros têm resultado postado na própria base.</strong> Registro sem resultado "
            "não é evidência: é intenção declarada.",
            "<strong>O tamanho da literatura mede a biologia, não o produto.</strong> Exossomo é um mecanismo "
            "celular real, estudado desde antes de existir clínica vendendo frasco — do mesmo modo que "
            "citocromo C tem centenas de artigos de bioquímica que nada dizem sobre o injetável. Contagem alta "
            "aqui não é sinal de tratamento validado.",
        ]),
        dict(h="Os nove “de fase 3”, um a um", tipo="p", corpo=[
            "“Nove ensaios de fase 3” é o tipo de número que circula em material de venda. Abri os nove. Quatro "
            "são fase 3 pura; cinco são <strong>fase 2/3</strong>, o rótulo combinado. E um deles não é terapia "
            "com exossomo nenhuma.",
        ], tabela=dict(
            cap="Os nove registros de fase 3 localizados",
            linhas=[
                ["Registro", "Desenho", "n", "Situação", "O que é"],
                ["<strong>NCT05354141</strong><br>EXTINGUISH ARDS", "Fase 3, ExoFlo por via intravenosa contra soro fisiológico, em SDRA",
                 "<strong>970</strong>", "Recrutando, conclusão prevista para 31/12/2027",
                 "<strong>O único grande.</strong> Patrocínio da Direct Biologics, a fabricante"],
                ["NCT07480161", "Fase 2/3, disfunção erétil no diabetes: células-tronco de cordão, exossomos delas e placebo intracavernoso",
                 "90", "Recrutando (Ankara City Hospital Bilkent)", "Braço de exossomo separado do braço de célula"],
                ["NCT05413148", "Fase 2/3, retinose pigmentar, injeção subtenoniana",
                 "135", "<strong>UNKNOWN</strong> — patrocinador parou de atualizar", "Célula e exossomo em braços distintos"],
                ["NCT05216562", "Fase 2/3, COVID-19 moderado, exossomo de célula mesenquimal por via intravenosa contra placebo",
                 "60", "<strong>UNKNOWN</strong>, conclusão estimada em dezembro de 2022", "Indonésia"],
                ["NCT02138331", "Fase 2/3, diabetes tipo 1, microvesículas e exossomos de célula mesenquimal",
                 "20", "<strong>UNKNOWN</strong>, conclusão estimada em setembro de 2014", "Egito. Doze anos sem resultado publicado que eu tenha encontrado"],
                ["NCT06539273", "Fase 3, alopecia androgenética, complexo de exossomo e RNA",
                 "30", "Concluído em 05/05/2024", "Yeditepe University Hospital"],
                ["NCT07281690", "Fase 3, laser Nd:YAG de 1064 nm com exossomo tópico de cordão umbilical",
                 "20", "Concluído em 17/07/2025", "Patrocínio de uma clínica de estética"],
                ["NCT07466953", "Fase 3, exossomo de célula mesenquimal intradérmico em qualidade da pele facial",
                 "40", "Ainda não recrutando, início estimado em 10/07/2026", "Investigador individual como patrocinador"],
                ["NCT03824275", "Fase 2/3, PET/CT com 18F-DCFPyL em câncer de próstata",
                 "129", "Ativo, sem recrutar", "<strong>Não é terapia com exossomo.</strong> Entrou na busca porque a descrição cita <code>exosome analysis</code> numa coleta de biópsia líquida"],
            ])),
        dict(h="O que a leitura dos nove mostra", tipo="li", corpo=[
            "<strong>Sem o estudo de PET/CT, sobram oito.</strong> Um falso positivo em nove é a razão pela qual "
            "eu trato os 378 registros como <strong>teto</strong>, e não como contagem de terapias com exossomo.",
            "<strong>Sete dos oito têm 135 participantes ou menos.</strong> Vinte, trinta, quarenta, sessenta, "
            "noventa, cento e trinta e cinco. “Fase 3” aqui não significa o que significa num programa de "
            "registro: significa o rótulo que o patrocinador escolheu no formulário.",
            "<strong>Três dos oito estão em UNKNOWN</strong> — a marca que o registro aplica quando o "
            "patrocinador para de atualizar. Um deles deveria ter terminado em 2014.",
            "<strong>Metade é estética.</strong> Pele facial, alopecia, laser. É onde está o mercado, e é onde "
            "os ensaios são menores.",
        ]),
        dict(h="O único programa grande, e o que ele achou", tipo="p", corpo=[
            "O ExoFlo, da Direct Biologics, é vesícula extracelular de célula mesenquimal de medula óssea. É o "
            "único exossomo deste levantamento com programa clínico sério, e o resultado publicado merece ser "
            "lido inteiro, não pela manchete.",
            "A <strong>fase 2</strong> saiu no <em>Chest</em> em dezembro de 2023 (NCT04493242): 102 pacientes "
            "com SDRA moderada a grave por COVID-19, em cinco centros nos Estados Unidos, randomizados para "
            "placebo, 10 mL ou 15 mL de ExoFlo nos dias 1 e 4. O <strong>desfecho primário era mortalidade por "
            "qualquer causa em 60 dias</strong>.",
            "<strong>O desfecho primário não bateu.</strong> A redução com 15 mL contra placebo veio "
            "<strong>não significante</strong> (χ², P = 0,1343). O que bateu foi <strong>análise de subgrupo "
            "post hoc</strong>: risco relativo de 0,385 (IC 95% 0,159–0,931; P = 0,0340; n = 50) e, entre 18 e "
            "65 anos, 0,423 (IC 95% 0,173–1,032; P = 0,0588; n = 24). Dias livres de ventilação melhoraram "
            "(P = 0,0455; n = 50). Nenhum evento adverso relacionado ao tratamento foi relatado.",
            "Subgrupo post hoc <strong>gera hipótese; não confirma efeito</strong> — é para isso que existe a "
            "fase 3, e é exatamente o que a EXTINGUISH ARDS, com 970 participantes, está rodando até o fim de "
            "2027. O artigo é assinado pelo diretor médico e por funcionários da fabricante, com o conflito "
            "declarado, e recebeu errata em 2024.",
            "O outro dado humano com desenho comparativo que encontrei é o EXO-CD24, vesícula inalada: 35 "
            "pacientes tratados em 2020 contra 105 controles pareados, seguimento retrospectivo de 4,6 anos, "
            "nenhuma morte no grupo tratado contra 14 (13,3%) nos controles. <strong>É retrospectivo e "
            "pareado, não randomizado</strong> — o desenho mais sujeito a seleção que existe entre os que "
            "comparam grupos.",
        ]),
        dict(h="Onde o mercado está: pele, cabelo e joelho", tipo="p", corpo=[
            "Quase tudo que se vende como exossomo no Brasil é estética. Fui ver o que a literatura sustenta "
            "nesses três terrenos.",
            "<strong>Cabelo.</strong> Uma revisão sistemática de 2026 reuniu 39 estudos publicados entre 2019 e "
            "2025 sobre exossomo em alopecia androgenética. Os estudos clínicos iniciais relatam ganho de "
            "<strong>8% a 20%</strong> em densidade capilar — e os próprios autores listam as limitações: "
            "amostras pequenas, desenho retrospectivo, <strong>ausência de grupo controle</strong> e desfechos "
            "medidos de formas diferentes em cada estudo. A conclusão pede ensaios randomizados grandes, com "
            "desfecho padronizado e produção em boas práticas de fabricação, antes de adoção clínica ampla.",
            "<strong>Joelho.</strong> A melhor síntese quantitativa que encontrei sobre exossomo em artrose de "
            "joelho é uma meta-análise em rede de 2026 com 27 ensaios randomizados — <strong>em 456 "
            "ratos</strong>. O efeito no dano histopatológico da cartilagem é grande (SMD de −3,78; IC 95% "
            "−4,76 a −2,80), e continua sendo rato. Os próprios autores dizem que serve para otimização "
            "pré-clínica e geração de hipótese clínica.",
            "<strong>Pele.</strong> Os ensaios que existem são pequenos e de face dividida, muitos comparando "
            "exossomo somado a laser ou a microagulhamento contra o procedimento sozinho — desenho que mede o "
            "acréscimo, e no qual o procedimento base já produz efeito.",
            "O contorno comercial disso foi medido. Um levantamento de 2023 analisou <strong>978 empresas</strong> "
            "que anunciavam célula-tronco e exossomo direto ao consumidor nos Estados Unidos; menos da metade "
            "fazia alguma afirmação identificável sobre segurança e eficácia do que vendia. No recorte de "
            "COVID-19, 38 empresas operando ou intermediando 60 clínicas, com preço de "
            "<strong>US$ 2.950 a US$ 25.000</strong> e média anunciada de US$ 11.322.",
        ]),
        dict(h="O que a FDA diz, com data", tipo="li", corpo=[
            "<strong>06/12/2019 — notificação pública de segurança.</strong> A agência informou "
            "<strong>múltiplos relatos de eventos adversos graves</strong> em pacientes de Nebraska tratados com "
            "produtos não aprovados vendidos como contendo exossomos. Os relatos chegaram à FDA pelo CDC, e as "
            "agências trabalharam com o departamento de saúde do estado.",
            "<strong>A frase central, literal: <em>“There are currently no FDA-approved exosome products.”</em></strong> "
            f"Reconferida por mim na página da agência em {_DT}.",
            "<strong>Exossomo para tratar doença é droga e produto biológico</strong>, sujeito a revisão e "
            "aprovação prévias, sob o Public Health Service Act e o Federal Food, Drug, and Cosmetic Act. A FDA "
            "registra que clínicas alegam que esses produtos escapam das regras de medicamento e responde que "
            "isso <em>“is simply untrue”</em>.",
            "<strong>O que a agência manda o paciente fazer:</strong> perguntar se a FDA revisou o tratamento e "
            "<strong>pedir o número do IND</strong> — a autorização de pesquisa — antes de aceitar a aplicação.",
            "<strong>As cartas de advertência continuam saindo.</strong> Conferi duas: Platinum Biologics, de "
            "Orlando, em <strong>15/08/2025</strong>, pelos produtos “NanoEx” e “Nano Xsomes”, com a frase "
            "<em>“Your products are not the subject of an approved BLA”</em>; e Dynamic Stem Cell Therapy, de "
            "Henderson, Nevada, em <strong>11/02/2026</strong>, que remete à mesma notificação de 2019. "
            "<strong>Não contei quantas existem</strong> — verifiquei estas duas.",
            "<strong>A pegadinha da base de rótulos.</strong> A busca livre por <code>exosome</code> devolve "
            "<strong>3 rótulos</strong>: uma solução de exossomo de placenta com alegação de antienvelhecimento, "
            "uma ampola contra queda de cabelo e um fluido de cicatrização. Nenhum tem número de aprovação, e "
            "<strong>estar listado na base de rótulos não é ser aprovado</strong> — a base recebe também produto "
            "sem aprovação. A busca por nome genérico não devolve nada.",
        ]),
        dict(h="O que existe no Brasil", tipo="p", corpo=[
            f"Baixei o dado aberto de medicamentos registrados da ANVISA em {_DT} e procurei "
            "<code>exossom</code> e <code>exosom</code>: <strong>zero ocorrências</strong>. Não há medicamento "
            "com exossomo registrado nessa base.",
            "<strong>E isso não fecha a pergunta.</strong> Essa base não cobre <strong>Produto de Terapia "
            "Avançada</strong>, que tem registro separado sob a RDC 505/2021 — a mesma armadilha descrita em "
            "<a href=\"proprio_casgevy.html\">Casgevy</a>. Se algum exossomo foi protocolado como terapia "
            "avançada, não é ali que apareceria. <strong>NÃO VERIFIQUEI</strong> a lista de produtos de terapia "
            "avançada: a página oficial que deveria exibi-la não renderiza produto nenhum.",
            "O que está verificado na ANVISA é o enquadramento, e ele é direto. Na página da agência sobre "
            "cosméticos para tratamentos estéticos, publicada em 16/11/2023: <em>“Produtos estéticos destinados "
            "a procedimentos injetáveis não podem ser regularizados como cosméticos.”</em> Injetável entra como "
            "medicamento ou produto para a saúde, e não existe cosmético injetável.",
            "A <strong>Sociedade Brasileira de Dermatologia</strong> tratou do assunto pelo nome em nota técnica "
            "de <strong>13/09/2024</strong>: <em>“tais produtos não podem ser aplicados em terapias injetáveis, "
            "independentemente da técnica, da indicação, da competência técnica do prescritor ou da qualidade do "
            "produto.”</em>",
            "A mesma nota afirma que a ANVISA classifica exossomos como cosméticos, de uso restrito ao tópico. "
            "<strong>Registro isso como afirmação da SBD, não como ato que eu tenha lido.</strong> Procurei e "
            "não encontrei a resolução ou nota da ANVISA que diga isso sobre exossomos pelo nome — e não vou "
            "afirmar pela agência o que li na sociedade.",
        ]),
        dict(h="Por que não há tabela de dose nesta página", tipo="p", corpo=[
            "Porque não existe unidade que atravesse os produtos. Uma dose de exossomo é anunciada às vezes em "
            "contagem de partículas, às vezes em microgramas de proteína, às vezes em mililitros, às vezes em "
            "“frascos” — e cada laboratório mede pelo método que escolheu, num campo cujo próprio consenso trata "
            "separação e caracterização como problema aberto.",
            "Montar uma tabela de diluição aqui daria aparência de protocolo a algo que não tem dose aprovada, "
            "apresentação registrada nem lote comparável. É a mesma decisão tomada nas páginas do "
            "<a href=\"proprio_thymalin.html\">Thymalin</a>, dos "
            "<a href=\"proprio_bioreguladores.html\">bioreguladores</a> e da "
            "<a href=\"proprio_mazdutida.html\">mazdutida</a>: <strong>onde não há número que signifique a mesma "
            "coisa duas vezes, a tabela é invenção com aparência de dado</strong>.",
        ]),
        dict(h="O que este levantamento não fez", tipo="li", corpo=[
            "<strong>Li resumos e registros, não artigos inteiros.</strong> As exceções são as páginas da FDA, "
            "da ANVISA e da SBD, que abri e li — e das quais as frases citadas são literais.",
            "<strong>Não consultei agência asiática nem europeia.</strong> O mercado cosmético de exossomo é "
            "maior na Coreia do Sul, no Japão e na China, e eu não tenho nada verificado sobre MFDS, PMDA, NMPA "
            "ou EMA. Ausência aqui não é ausência lá.",
            "<strong>Não achei descrição revisada por pares do surto de Nebraska.</strong> A única fonte é a "
            "notificação da FDA, que não nomeia a clínica, o produto, o número de pacientes nem o "
            "microrganismo. O que se sabe é o que a agência escreveu.",
            "<strong>Não cobri exossomo como diagnóstico.</strong> Os 142 registros observacionais são em boa "
            "parte biópsia líquida e marcador de doença — outro assunto, e fora do escopo deste site.",
            "<strong>A contagem do ClinicalTrials.gov é teto, não medida.</strong> A busca por campo de "
            "intervenção captura registro que apenas menciona exossomo, e o caso do PET/CT prova. Quem quiser "
            "número exato de terapias com exossomo tem que abrir os 378, um a um; eu abri os nove de fase 3.",
            "<strong>Não há tabela de reconstituição nesta página</strong>, por decisão, pela razão da seção "
            "acima.",
        ]),
    ],
    nota_refs=(f'Cada número desta página foi levantado por mim em {_DT} no PubMed, no ClinicalTrials.gov, na '
               'base de rótulos da FDA, no dado aberto da ANVISA e nas páginas da FDA, da ANVISA e da '
               'Sociedade Brasileira de Dermatologia, e a consulta usada está declarada acima. '
               '<strong>Esta página foi apurada em dia próprio</strong>, e por isso carrega data própria.'),
    referencias=[
        ("FDA. Public Safety Notification on Exosome Products, 6 de dezembro de 2019 — a origem da frase “There are currently no FDA-approved exosome products” e do relato dos eventos adversos graves em Nebraska.",
         "https://www.fda.gov/vaccines-blood-biologics/safety-availability-biologics/public-safety-notification-exosome-products"),
        ("FDA. Public Safety Alert Due to Marketing of Unapproved Stem Cell and Exosome Products — a versão em alerta ao consumidor, com a orientação de pedir o número do IND.",
         "https://www.fda.gov/safety/medical-product-safety-information/public-safety-alert-due-marketing-unapproved-stem-cell-and-exosome-products"),
        ("FDA. Carta de advertência a Platinum Biologics LLC, 15 de agosto de 2025 — produtos “NanoEx” e “Nano Xsomes”, sem BLA aprovado.",
         "https://www.fda.gov/inspections-compliance-enforcement-and-criminal-investigations/warning-letters/platinum-biologics-llc-705090-08152025"),
        ("FDA. Carta de advertência a Dynamic Stem Cell Therapy, 11 de fevereiro de 2026 — remete à notificação de 2019 sobre exossomos.",
         "https://www.fda.gov/inspections-compliance-enforcement-and-criminal-investigations/warning-letters/dynamic-stem-cell-therapy-712579-02112026"),
        ("Lightner AL et al. Bone Marrow Mesenchymal Stem Cell-Derived Extracellular Vesicle Infusion for the Treatment of Respiratory Failure From COVID-19: A Randomized, Placebo-Controlled Dosing Clinical Trial. Chest. 2023;164(6):1444-1453 — ExoFlo, fase 2, NCT04493242, 102 pacientes, desfecho primário não significante.",
         "https://doi.org/10.1016/j.chest.2023.06.024"),
        ("Registro da EXTINGUISH ARDS no ClinicalTrials.gov — fase 3 de ExoFlo, 970 participantes, conclusão prevista para o fim de 2027.",
         "https://clinicaltrials.gov/study/NCT05354141"),
        ("Shapira S et al. Reduced Mortality in COVID-19 Patients Treated With Inhaled Extracellular Vesicles Expressing CD24. J Extracell Vesicles. 2026;15(3):e70253 — 35 tratados contra 105 controles pareados, seguimento retrospectivo de 4,6 anos.",
         "https://doi.org/10.1002/jev2.70253"),
        ("Malih S et al. Exosome-driven treatments for hair regrowth in androgenetic alopecia: a systematic review of preclinical studies, clinical experiments, safety, and future prospects. Mol Biol Rep. 2026;53(1):1046 — 39 estudos, ganho relatado de 8% a 20% em densidade capilar e as limitações de desenho.",
         "https://doi.org/10.1007/s11033-026-12255-2"),
        ("Zhao Y et al. Exosome therapy for knee osteoarthritis: a network meta-analysis based on rat models. Stem Cells Transl Med. 2026;15(9):szag069 — 27 ensaios randomizados, 456 ratos.",
         "https://doi.org/10.1093/stcltm/szag069"),
        ("Turner L et al. Safety and efficacy claims made by US businesses marketing purported stem cell treatments and exosome therapies. Regen Med. 2023;18(10):781-793 — 978 empresas analisadas.",
         "https://doi.org/10.2217/rme-2023-0118"),
        ("Turner L et al. Businesses marketing purported stem cell treatments and exosome therapies for COVID-19: An analysis of direct-to-consumer online advertising claims. Stem Cell Reports. 2023;18(11):2010-2015 — 38 empresas, 60 clínicas, de US$ 2.950 a US$ 25.000.",
         "https://doi.org/10.1016/j.stemcr.2023.09.015"),
        ("Welsh JA et al. Minimal information for studies of extracellular vesicles (MISEV2023): From basic to advanced approaches. J Extracell Vesicles. 2024;13(2):e12404 — o consenso da ISEV, que lista nomenclatura e separação de partículas não vesiculares entre os obstáculos abertos.",
         "https://doi.org/10.1002/jev2.12404"),
        ("Registro do NCT03824275 no ClinicalTrials.gov — o estudo de PET/CT em câncer de próstata que entra na busca por “exosome analysis” na descrição, e não é terapia com exossomo.",
         "https://clinicaltrials.gov/study/NCT03824275"),
        ("ANVISA. Cosméticos para tratamentos estéticos, publicado em 16 de novembro de 2023 — “Produtos estéticos destinados a procedimentos injetáveis não podem ser regularizados como cosméticos”.",
         "https://www.gov.br/anvisa/pt-br/assuntos/cosmeticos/cosmeticos-para-tratamentos-esteticos"),
        ("Sociedade Brasileira de Dermatologia. Nota técnica sobre o uso dermatológico de exossomos, 13 de setembro de 2024.",
         "https://www.sbd.org.br/nota-tecnica-uso-dermatologico-de-exossomos-em-dermatologia/"),
        ("API pública de rótulos da FDA, usada para confirmar a ausência de produto aprovado e para achar os três rótulos listados.",
         "https://open.fda.gov/apis/drug/label/"),
        ("Dado aberto de medicamentos registrados da ANVISA, a mesma base usada na página O que existe no Brasil.",
         "https://dados.anvisa.gov.br/dados/"),
    ],
),
}
