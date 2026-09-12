# -*- coding: utf-8 -*-
"""Metadados PT-BR de cada composto.

campos: nome, categoria, tagline, resumo, alerta (opcional)
'aprovado' controla o selo: 'nao' | 'parcial' | 'sim'
"""

CATEGORIAS = {
    "reparo": ("Reparo e tecido", "Compostos estudados em cicatrização, tendão, pele e inflamação local."),
    "metabolico": ("Metabólico e peso", "Agonistas de incretina e correlatos estudados em peso e glicemia."),
    "gh": ("Eixo do hormônio do crescimento", "Análogos de GHRH e secretagogos que pedem ao próprio corpo que libere GH."),
    "neuro": ("Neuro e cognição", "Compostos estudados em atenção, memória, ansiedade e sono."),
    "longevidade": ("Longevidade e mitocôndria", "Alvos ligados a senescência, NAD+ e função mitocondrial."),
    "hormonal": ("Hormonal e sexual", "Eixo reprodutivo, libido, pigmentação e vasodilatação."),
    "imune": ("Imune", "Modulação da resposta imune."),
    "combinacao": ("Combinações", "Protocolos que juntam dois ou mais compostos no mesmo ciclo."),
    "primaria": ("Verificado em fonte primária", "Páginas montadas direto do PubMed e do ClinicalTrials.gov, não da fonte secundária. Trazem a contagem de evidência e a consulta usada."),
}

COMPOSTOS = {
"protocol_5-amino-1mq": dict(
    nome="5-Amino-1MQ", categoria="metabolico", aprovado="nao",
    tagline="Molécula pequena, não é peptídeo, estudada em gordura e NNMT",
    resumo="Abreviação de 5-amino-1-metilquinolínio. É uma molécula pequena, não um peptídeo de verdade, ainda que seja vendida junto com peptídeos de pesquisa. O interesse se concentra em dois alvos: reduzir o tamanho de células de gordura e a inibição da enzima NNMT. Existe em cápsula oral e em formato injetável, e a maior parte do que circula como protocolo vem de relatos de comunidade, não de ensaio clínico.",
),
"protocol_adamax": dict(
    nome="Adamax", categoria="neuro", aprovado="nao",
    tagline="Parente experimental do Semax, quase sem pesquisa publicada",
    resumo="Peptídeo experimental aparentado ao Semax, com praticamente nenhuma pesquisa publicada própria. Os padrões de dose que circulam são transposições do Semax feitas pela comunidade — o que é uma extrapolação, não um dado. Aparece nas vias nasal e subcutânea.",
    alerta="Quase toda a base de dose é emprestada do Semax por analogia. Não há farmacocinética própria publicada.",
),
"protocol_aod-9604": dict(
    nome="AOD-9604", categoria="metabolico", aprovado="nao",
    tagline="Fragmento do GH estudado em lipólise",
    resumo="Fragmento sintético da porção 176–191 do hormônio do crescimento, estudado pelo efeito lipolítico sem a ação de crescimento da molécula inteira. Os planos de comunidade citam 300–500 mcg por dia, o que não é um protocolo clínico aprovado. Num frasco de 5 mg reconstituído com 3 mL de água bacteriostática, essa faixa corresponde a cerca de 18–30 unidades numa seringa U-100.",
),
"protocol_ara-290": dict(
    nome="ARA-290 (cibinetida)", categoria="reparo", aprovado="nao",
    tagline="Fragmento da EPO sem o efeito sobre hemácias",
    resumo="Peptídeo de 11 aminoácidos construído a partir de um trecho da molécula de eritropoetina (EPO). Foi desenhado para preservar a sinalização de reparo tecidual e anti-inflamatória da EPO, retirando a parte que estimula a produção de hemácias. A pesquisa mais consistente está em neuropatia de fibras finas.",
),
"protocol_bpc-157": dict(
    nome="BPC-157", categoria="reparo", aprovado="nao",
    tagline="O peptídeo de reparo mais discutido — e quase só em modelo animal",
    resumo="Sigla de Body Protection Compound 157. Peptídeo sintético de 15 aminoácidos derivado de uma sequência identificada no suco gástrico humano nos anos 1990. A maior parte da pesquisa está em modelos animais de tendão, ligamento e trato digestivo. É o componente de reparo mais presente nas combinações (GLOW, KLOW, Wolverine).",
    alerta="A base de evidência é quase inteiramente pré-clínica. Ensaio humano controlado é escasso.",
),
"protocol_bremelanotide-pt-141": dict(
    nome="PT-141 (bremelanotida)", categoria="hormonal", aprovado="parcial",
    tagline="Agonista MC3R/MC4R — aprovado nos EUA como Vyleesi",
    resumo="Peptídeo cíclico sintético que ativa dois receptores de melanocortina no cérebro, MC3R e MC4R. É o princípio ativo do Vyleesi, injeção aprovada pela FDA para desejo sexual hipoativo em mulheres na pré-menopausa. Fora dessa indicação, o uso é off-label e os esquemas vêm da comunidade.",
),
"protocol_cagrilintide": dict(
    nome="Cagrilintida", categoria="metabolico", aprovado="nao",
    tagline="Análogo de amilina semanal, em investigação",
    resumo="Peptídeo semanal em investigação, desenvolvido pela Novo Nordisk. É um análogo de ação longa da amilina, o hormônio que o pâncreas libera junto com a insulina para sinalizar saciedade após comer. Em linguagem direta: prolonga o sinal de estar satisfeito. Aparece isolada e em combinação com semaglutida (CagriSema), tirzepatida e retatrutida.",
),
"protocol_cartalax": dict(
    nome="Cartalax", categoria="reparo", aprovado="nao",
    tagline="Bioregulador curto estudado em cartilagem",
    resumo="Peptídeo curto estudado em células de cartilagem e em modelos celulares de envelhecimento. Há uma distância grande entre a pesquisa laboratorial publicada e os esquemas injetáveis que circulam nas comunidades — a página separa as duas coisas.",
),
"protocol_cerebrolysin": dict(
    nome="Cerebrolisina", categoria="neuro", aprovado="parcial",
    tagline="Mistura injetável de peptídeos de origem suína",
    resumo="Mistura injetável pronta para uso, de peptídeos e aminoácidos derivados de cérebro suíno. Tem registro em alguns países (não nos EUA) e é usada em contextos de AVC e demência. Não é um peptídeo único: é um preparado biológico, o que muda completamente a lógica de dose e de controle de qualidade.",
),
"protocol_cjc-1295-dac": dict(
    nome="CJC-1295 com DAC", categoria="gh", aprovado="nao",
    tagline="Análogo de GHRH de ação longa, ligado à albumina",
    resumo="Análogo de GHRH de 30 aminoácidos com uma modificação chamada DAC (Drug Affinity Complex) na posição 30, que permite ao peptídeo se ligar à albumina circulante. Essa ligação o protege da degradação e estende muito a meia-vida — daí a frequência semanal ou quinzenal, em vez de diária.",
),
"protocol_cjc-1295-no-dac": dict(
    nome="CJC-1295 sem DAC (Mod GRF 1-29)", categoria="gh", aprovado="nao",
    tagline="Pulso curto de GHRH, sem acúmulo",
    resumo="Também chamado de GRF Modificado 1-29. É uma cópia de ação curta do hormônio liberador de GH do próprio corpo. Sinaliza à hipófise que libere um pulso breve de hormônio do crescimento e é eliminado rápido. É a metade 'GHRH' da dupla clássica com ipamorelina.",
),
"protocol_dsip": dict(
    nome="DSIP", categoria="neuro", aprovado="nao",
    tagline="Peptídeo indutor de sono delta — nome maior que a evidência",
    resumo="Delta sleep-inducing peptide, um peptídeo de nove aminoácidos isolado nos anos 1970 do sangue venoso cerebral de coelhos adormecidos. O nome vem da observação inicial de aumento de atividade delta. A pesquisa humana subsequente é escassa e inconsistente com a promessa do nome.",
),
"protocol_epitalon": dict(
    nome="Epitalon (epithalon, AEDG)", categoria="longevidade", aprovado="nao",
    tagline="Tetrapeptídeo russo associado a telomerase",
    resumo="Peptídeo de quatro aminoácidos em sequência: Ala-Glu-Asp-Gly, também escrito AEDG. Vem da escola russa de bioreguladores curtos e é associado a telomerase e ritmo circadiano. Os protocolos são curtos e cíclicos, repetidos poucas vezes por ano.",
),
"protocol_foxo4-dri": dict(
    nome="FOXO4-DRI", categoria="longevidade", aprovado="nao",
    tagline="Senolítico experimental — o de menor margem desta lista",
    resumo="Peptídeo sintético estudado como senolítico: um composto que pretende eliminar células senescentes, aquelas células velhas e danificadas que param de se dividir mas não morrem, e passam a liberar sinais inflamatórios no tecido vizinho. É dos compostos com menos dados humanos de toda esta referência.",
    alerta="Mecanismo desenhado para matar células. A margem entre o alvo pretendido e o dano colateral não está estabelecida em humanos.",
),
"protocol_ghk-cu": dict(
    nome="GHK-Cu", categoria="reparo", aprovado="nao",
    tagline="Peptídeo de cobre — o acúmulo é a variável que manda no ciclo",
    resumo="Glicil-L-histidil-L-lisina cobre: pequeno peptídeo ligante de cobre que ocorre naturalmente no plasma humano. Os níveis ficam em torno de 200 ng/mL aos 20 anos e caem para cerca de 80 ng/mL aos 60 — parte de por que atrai interesse. É o componente dominante das blends GLOW e KLOW, em massa.",
    alerta="Carrega cobre. O acúmulo de cobre é o que define a necessidade de pausa entre ciclos, não o cansaço do receptor.",
),
"protocol_ghrp-6": dict(
    nome="GHRP-6", categoria="gh", aprovado="nao",
    tagline="Secretagogo que imita a grelina — e abre a fome junto",
    resumo="Peptídeo sintético de seis aminoácidos que copia parte do funcionamento da grelina, o hormônio da fome. Em vez de acrescentar GH externo, sinaliza ao corpo que libere o próprio. O aumento marcado de apetite é um efeito esperado, não um acidente.",
),
"protocol_glutathione": dict(
    nome="Glutationa", categoria="longevidade", aprovado="parcial",
    tagline="O antioxidante que o corpo já fabrica",
    resumo="Frequentemente escrita GSH, é o antioxidante mais abundante produzido pelo próprio corpo. É um tripeptídeo, formado por três aminoácidos: cisteína, glicina e glutamato. Praticamente toda célula depende dela. As formas de uso vão de oral (absorção discutível) a intravenosa.",
),
"protocol_humanin": dict(
    nome="Humanina (HNG)", categoria="longevidade", aprovado="nao",
    tagline="Peptídeo codificado na mitocôndria, não no núcleo",
    resumo="Pequeno peptídeo derivado da mitocôndria — um dos primeiros mostrados como codificados no DNA mitocondrial em vez de no núcleo da célula. O interesse está em sobrevivência celular, função mitocondrial e neuroproteção. HNG é uma variante mais potente usada em pesquisa.",
),
"protocol_igf-1-lr3": dict(
    nome="IGF-1 LR3", categoria="gh", aprovado="nao",
    tagline="Análogo de IGF-1 de ação longa — o de maior risco do grupo do GH",
    resumo="Análogo sintético e de ação mais longa do fator de crescimento semelhante à insulina tipo 1. O IGF-1 do próprio corpo leva sinais de crescimento do fígado ao músculo e ao osso; o LR3 faz o mesmo, mas resiste às proteínas de ligação, o que estende muito sua atividade.",
    alerta="Sinal de crescimento sistêmico e sustentado. Hipoglicemia e a questão de crescimento tecidual indesejado são as preocupações centrais.",
),
"protocol_ipamorelin": dict(
    nome="Ipamorelina", categoria="gh", aprovado="nao",
    tagline="Secretagogo seletivo, sem o disparo de fome do GHRP-6",
    resumo="Peptídeo pequeno que pede ao corpo que libere o próprio hormônio do crescimento em pulsos curtos e naturais. Também aparece como NNC 26-0161; foi estudado pela Novo Nordisk no fim dos anos 1990. É mais seletivo que o GHRP-6 — menos efeito sobre cortisol, prolactina e apetite.",
),
"protocol_kisspeptin": dict(
    nome="Kisspeptina", categoria="hormonal", aprovado="nao",
    tagline="A chave a montante do eixo reprodutivo",
    resumo="Peptídeo sinalizador que ativa a via hormonal reprodutiva. Avisa o cérebro para liberar GnRH, que por sua vez faz a hipófise liberar LH e FSH. Nos homens, o LH sinaliza aos testículos que produzam testosterona. Age acima do eixo, não dentro dele.",
),
"protocol_kpv": dict(
    nome="KPV", categoria="reparo", aprovado="nao",
    tagline="Tripeptídeo anti-inflamatório, fragmento do α-MSH",
    resumo="Peptídeo curto estudado sobretudo em pesquisa laboratorial e animal. É o fragmento terminal do α-MSH e o componente que diferencia a blend KLOW da GLOW. O interesse está em inflamação intestinal e cutânea. Aparece em frascos de 5 mg e 10 mg.",
),
"protocol_lipo-c": dict(
    nome="Lipo-C", categoria="metabolico", aprovado="parcial",
    tagline="Injeção lipotrópica manipulada — não é um peptídeo",
    resumo="Não é um peptídeo: é uma injeção lipotrópica manipulada, com aminoácidos (metionina, inositol, colina) e vitaminas do complexo B. Por ser fórmula de manipulação, a composição varia de farmácia para farmácia — o que torna a comparação entre protocolos pouco confiável.",
),
"protocol_ll-37": dict(
    nome="LL-37", categoria="reparo", aprovado="nao",
    tagline="O único peptídeo antimicrobiano catelicidina humano",
    resumo="Único peptídeo antimicrobiano da família catelicidina produzido por humanos. Deriva de uma proteína maior, a hCAP-18, e participa da resposta do corpo a micróbios, inflamação e reparo de ferida. No mercado de peptídeos de pesquisa costuma aparecer em frasco liofilizado.",
),
"protocol_melanotan-ii": dict(
    nome="Melanotan II (MT-2)", categoria="hormonal", aprovado="nao",
    tagline="Bronzeamento por via de melanocortina — e uma lista de efeitos",
    resumo="Peptídeo sintético desenvolvido na Universidade do Arizona entre os anos 1980 e 1990. O objetivo era induzir bronzeamento sem exposição solar prolongada. Ativa receptores de melanocortina de forma ampla, o que traz junto náusea, escurecimento de pintas e efeito sobre a ereção.",
    alerta="Escurecimento e alteração de nevos é um efeito relatado. Qualquer mudança em pinta pede avaliação dermatológica, não observação.",
),
"protocol_methylene-blue": dict(
    nome="Azul de metileno", categoria="neuro", aprovado="parcial",
    tagline="Corante de 1876 que virou medicamento hospitalar",
    resumo="Corante sintético azul que também é medicamento. Foi criado em 1876 como corante têxtil e se tornou um dos fármacos mais antigos ainda em uso. Nome químico: cloreto de metiltionínio. Em hospital é usado no tratamento de metemoglobinemia. O interesse nootrópico é de dose muito menor.",
    alerta="Interage com serotonérgicos (ISRS, IMAO) — risco de síndrome serotoninérgica. É a interação mais importante desta lista inteira.",
),
"protocol_mots-c": dict(
    nome="MOTS-c", categoria="longevidade", aprovado="nao",
    tagline="Peptídeo mitocondrial ligado à via AMPK",
    resumo="Sigla de mitochondrial open reading frame of the 12S rRNA-c. Peptídeo de 16 aminoácidos que a própria mitocôndria produz. O interesse está em sinalização de AMPK, sensibilidade à insulina e metabolismo — e por isso aparece combinado com agonistas de GLP-1.",
),
"protocol_nad-plus": dict(
    nome="NAD+", categoria="longevidade", aprovado="nao",
    tagline="Coenzima central — a via de administração muda tudo",
    resumo="Nicotinamida adenina dinucleotídeo: coenzima presente em toda célula viva. O corpo a usa para converter comida em energia celular (ATP), para reparo de DNA e para alimentar as sirtuínas. Existe em subcutâneo, intravenoso, intramuscular, oral e caneta — e a biodisponibilidade entre essas vias é muito diferente.",
),
"protocol_oxytocin": dict(
    nome="Ocitocina", categoria="hormonal", aprovado="parcial",
    tagline="Hormônio aprovado em obstetrícia, usado off-label em cognição social",
    resumo="Pequeno hormônio peptídico produzido no cérebro e liberado pela hipófise. Na medicina é fármaco aprovado, por via IV ou IM, para indução de parto, controle de sangramento pós-parto e lactação. O uso intranasal em cognição social e vínculo é off-label e de dose única na maior parte dos estudos.",
),
"protocol_pinealon": dict(
    nome="Pinealon (EDR)", categoria="neuro", aprovado="nao",
    tagline="Bioregulador curto da escola de Khavinson",
    resumo="Peptídeo sintético de três aminoácidos, sequência Glu-Asp-Arg — daí o nome peptídeo EDR. É um dos bioreguladores curtos desenvolvidos pelo grupo de Vladimir Khavinson, em São Petersburgo. A base publicada é majoritariamente russa e pré-clínica.",
),
"protocol_retatrutide": dict(
    nome="Retatrutida", categoria="metabolico", aprovado="nao",
    tagline="Agonista triplo em fase 3 — GIP, GLP-1 e glucagon",
    resumo="Agonista triplo de receptor, semanal, em investigação e em ensaios de fase 3. Ativa receptores de GIP, GLP-1 e glucagon ao mesmo tempo. É importante separar o desenho de escalonamento do programa TRIUMPH, que é público, dos esquemas que circulam na comunidade — não são a mesma coisa.",
    alerta="Não aprovado em lugar nenhum. O que existe no mercado cinza não passou por controle regulatório.",
),
"protocol_selank": dict(
    nome="Selank (TP-7)", categoria="neuro", aprovado="parcial",
    tagline="Ansiolítico peptídico russo, par do Semax",
    resumo="Peptídeo desenvolvido na Rússia, estudado em alívio de ansiedade e suporte leve de foco. Também chamado TP-7. Tem registro na Rússia. É o par do Semax na chamada dupla nootrópica russa: o Semax puxa para ativação, o Selank para contenção.",
),
"protocol_semaglutide": dict(
    nome="Semaglutida", categoria="metabolico", aprovado="sim",
    tagline="Ozempic, Wegovy e Rybelsus — a mesma molécula",
    resumo="Um dos fármacos de perda de peso e diabetes mais estudados do mundo. Aparece como Ozempic (diabetes tipo 2), Wegovy (manejo de peso) e Rybelsus (comprimido oral diário). São a mesma molécula em apresentações e doses diferentes. Aqui é o composto com a base clínica mais sólida da referência inteira.",
),
"protocol_semax": dict(
    nome="Semax", categoria="neuro", aprovado="parcial",
    tagline="Heptapeptídeo russo derivado do ACTH, ligado a BDNF",
    resumo="Peptídeo sintético de sete aminoácidos, sequência Met-Glu-His-Phe-Pro-Gly-Pro. Foi desenhado na Rússia a partir de um fragmento do hormônio adrenocorticotrófico (ACTH) somado a uma cauda estabilizadora Pro-Gly-Pro. Tem registro russo em AVC isquêmico e neurologia. A meia-vida plasmática é curtíssima, mas o efeito sobre BDNF é tardio e prolongado — o que explica a dose matinal.",
),
"protocol_sermorelin": dict(
    nome="Sermorelina (GRF 1-29)", categoria="gh", aprovado="parcial",
    tagline="Cópia dos 29 primeiros aminoácidos do GHRH",
    resumo="Peptídeo que copia os 29 primeiros aminoácidos do hormônio liberador de GH natural do corpo. Também chamado GRF 1-29 ou acetato de sermorelina. A cópia curta ainda encaixa no receptor de GHRH da hipófise. Já teve aprovação nos EUA como teste diagnóstico, depois retirada do mercado.",
),
"protocol_slu-pp-332": dict(
    nome="SLU-PP-332", categoria="metabolico", aprovado="nao",
    tagline="Agonista pan-ERR vendido como 'mimético de exercício'",
    resumo="Agonista pan-ERR frequentemente descrito como mimético de exercício. A dose publicada é murina — de camundongo — e a conversão para humano não está estabelecida. Difere dos peptídeos mitocondriais por ser molécula pequena, com planejamento oral e injetável.",
    alerta="A dose publicada é de camundongo. Não existe equivalente humano estabelecido.",
),
"protocol_ss-31": dict(
    nome="SS-31 (elamipretida)", categoria="longevidade", aprovado="nao",
    tagline="Peptídeo que se liga à cardiolipina mitocondrial",
    resumo="Peptídeo sintético de quatro aminoácidos. Migra para a membrana mitocondrial interna e se liga a um fosfolipídio chamado cardiolipina, que é o andaime estrutural onde a mitocôndria organiza sua maquinaria de produção de energia. Chegou a ensaios clínicos como elamipretida.",
),
"protocol_survodutide": dict(
    nome="Survodutida", categoria="metabolico", aprovado="nao",
    tagline="Agonista duplo GLP-1/glucagon, código BI 456906",
    resumo="Peptídeo de 29 aminoácidos desenvolvido pela Boehringer Ingelheim com a Zealand Pharma. Código de pesquisa BI 456906. Semanal e subcutâneo, age em dois alvos: receptores de GLP-1 e de glucagon. Ainda em investigação, com dados relevantes em esteato-hepatite.",
),
"protocol_tb-500": dict(
    nome="TB-500", categoria="reparo", aprovado="nao",
    tagline="Fragmento da timosina beta-4 — migração celular",
    resumo="Fragmento sintético de 7 aminoácidos da timosina beta-4, um peptídeo maior presente em todo o corpo. A sequência é Ac-LKKTETQ, que corresponde aos aminoácidos 17–23 da Tβ4. O prefixo 'Ac' indica acetilação numa das pontas. O interesse está em migração celular e reparo sistêmico, e não local como o BPC-157.",
),
"protocol_tesamorelin": dict(
    nome="Tesamorelina", categoria="gh", aprovado="sim",
    tagline="O único análogo de GHRH aprovado pela FDA",
    resumo="Único peptídeo GHRH aprovado pela FDA. Sinaliza à hipófise que libere mais do próprio hormônio do crescimento, no ritmo natural. Vendido como Egrifta SV e Egrifta WR para lipodistrofia associada ao HIV. É o composto do grupo do GH com maior lastro regulatório.",
),
"protocol_tesofensine": dict(
    nome="Tesofensina", categoria="metabolico", aprovado="nao",
    tagline="Inibidor triplo de recaptação, em comprimido oral",
    resumo="Comprimido oral desenvolvido originalmente para doença de Parkinson e Alzheimer. Naqueles ensaios iniciais, os participantes perderam peso sem tentar — achado que redirecionou o programa para obesidade. Age no cérebro bloqueando a recaptação de noradrenalina, dopamina e serotonina.",
    alerta="Mecanismo estimulante central. Pressão arterial, frequência cardíaca e sono são os pontos de atenção.",
),
"protocol_thymosin-alpha-1": dict(
    nome="Timosina alfa-1 (TA1)", categoria="imune", aprovado="parcial",
    tagline="Modulador imune com registro fora dos EUA",
    resumo="Peptídeo de 28 aminoácidos produzido naturalmente pelo timo. Ajuda a treinar e coordenar as células imunes que combatem vírus e outras infecções. A versão sintética, timalfasina, é vendida como Zadaxin e tem registro em vários países para hepatite B e C.",
),
"protocol_tirzepatide": dict(
    nome="Tirzepatida", categoria="metabolico", aprovado="sim",
    tagline="Agonista duplo GLP-1/GIP — Mounjaro e Zepbound",
    resumo="Agonista duplo de GLP-1 e GIP, semanal, aprovado como Mounjaro (diabetes tipo 2) e Zepbound (obesidade). A titulação vai de 2,5 mg a 15 mg por semana, subindo a cada quatro semanas. Os dados de efeito e de eventos adversos vêm dos programas SURPASS e SURMOUNT.",
),
"protocol_vip": dict(
    nome="VIP (peptídeo intestinal vasoativo)", categoria="hormonal", aprovado="nao",
    tagline="Neuropeptídeo de 28 aminoácidos, meia-vida muito curta",
    resumo="Peptídeo intestinal vasoativo: molécula sinalizadora natural (um neuropeptídeo) de 28 aminoácidos. O corpo o produz no intestino, cérebro, pulmões e outros tecidos, onde relaxa musculatura lisa, dilata vasos e modula inflamação. A meia-vida muito curta é o principal limitador prático.",
),

# ------------------------------------------------------------ combinações
"stacks_advanced-recomp-stack": dict(
    nome="Advanced Recomp", categoria="combinacao", aprovado="nao",
    tagline="Retatrutida + CJC-1295 sem DAC + ipamorelina",
    resumo="Combina três peptídeos num protocolo só: retatrutida, CJC-1295 (sem DAC) e ipamorelina. A lógica declarada é direta — perder gordura rápido com a retatrutida e tentar preservar massa magra com a dupla CJC-1295 + ipamorelina. É a combinação mais carregada desta referência, com três compostos não aprovados ao mesmo tempo.",
    alerta="Três compostos não aprovados simultaneamente. Se algo der errado, não há como saber qual dos três foi.",
),
"stacks_cagrilintide-retatrutide": dict(
    nome="Cagrilintida + Retatrutida", categoria="combinacao", aprovado="nao",
    tagline="Agonista triplo somado a análogo de amilina",
    resumo="Combina dois peptídeos de perda de peso em investigação. A retatrutida é o agonista triplo da Eli Lilly — uma injeção semanal que atinge três receptores ao mesmo tempo (GLP-1, GIP, glucagon). A cagrilintida é um análogo de amilina de ação longa. A ordem importa: estabiliza-se a retatrutida antes de acrescentar a cagrilintida.",
),
"stacks_cagrilintide-tirzepatide": dict(
    nome="Cagrilintida + Tirzepatida", categoria="combinacao", aprovado="nao",
    tagline="Dupla semanal de apetite",
    resumo="Junta dois peptídeos semanais de perda de peso. A tirzepatida é agonista duplo GLP-1/GIP, aprovada como Mounjaro e Zepbound. A cagrilintida entra como acréscimo para saciedade, na menor dose, com a tirzepatida já estável.",
),
"stacks_cagrisema": dict(
    nome="CagriSema", categoria="combinacao", aprovado="nao",
    tagline="Cagrilintida 2,4 mg + semaglutida 2,4 mg, dose fixa",
    resumo="Combinação semanal de dose fixa entre cagrilintida 2,4 mg (análogo de amilina de ação longa) e semaglutida 2,4 mg (agonista de receptor de GLP-1), desenvolvida pela Novo Nordisk para manejo crônico de peso. Diferente das outras combinações desta seção, é um produto único em desenvolvimento formal, não uma junção feita pelo usuário.",
),
"stacks_cjc-1295-ipamorelin-gh-pulse-stack": dict(
    nome="CJC-1295 sem DAC + Ipamorelina", categoria="combinacao", aprovado="nao",
    tagline="A dupla de GH mais planejada da comunidade",
    resumo="A combinação de GH mais difundida na comunidade de pesquisa. O CJC-1295 imita o sinal de GHRH do corpo, dizendo à hipófise que produza GH. A ipamorelina age por outra porta, a via da grelina. Como usam receptores diferentes, o efeito somado sobre o pulso de GH é maior que o de cada um isolado.",
),
"stacks_glow-stack": dict(
    nome="GLOW", categoria="combinacao", aprovado="nao",
    tagline="BPC-157 + TB-500 + GHK-Cu num frasco",
    resumo="Blend de pesquisa que reúne três compostos num único frasco: BPC-157, TB-500 e GHK-Cu. A comunidade agrupa os três porque cada um atinge uma parte diferente de como o tecido se repara — reparo local, migração celular e remodelamento. É a KLOW sem o KPV.",
),
"stacks_klow-stack": dict(
    nome="KLOW", categoria="combinacao", aprovado="nao",
    tagline="GHK-Cu + KPV + BPC-157 + TB-500, frasco de 80 mg",
    resumo="Nome de comunidade para uma blend de quatro peptídeos que junta GHK-Cu (peptídeo ligante de cobre, ligado à pesquisa de pele e tecido conjuntivo) com KPV (tripeptídeo anti-inflamatório), BPC-157 (estudado em reparo de tecido mole) e TB-500 (fragmento sintético da timosina beta-4, usado em pesquisa de migração celular). O frasco padrão discutido é de 80 mg no total, com 50 mg de GHK-Cu e 10 mg de cada um dos outros três. É a GLOW acrescida de KPV — e o KPV é justamente o motivo que a maioria cita para escolher a KLOW.",
    alerta="Nenhum ensaio publicado avaliou a combinação de quatro peptídeos junta. O acúmulo de cobre do GHK-Cu é o que determina a pausa.",
),
"stacks_retatrutide-mots-c": dict(
    nome="Retatrutida + MOTS-c", categoria="combinacao", aprovado="nao",
    tagline="Apetite por uma via, mitocôndria por outra",
    resumo="Junta dois compostos que agem em partes diferentes do metabolismo. A retatrutida é o agonista triplo em investigação da Eli Lilly, agindo em GLP-1, GIP e glucagon para reduzir apetite. O MOTS-c entra pela via mitocondrial e AMPK. Em geral o MOTS-c é usado em pulsos, e não continuamente.",
),
"stacks_russian-nootropic-stack": dict(
    nome="Dupla nootrópica russa", categoria="combinacao", aprovado="nao",
    tagline="Semax + Selank",
    resumo="Combina dois peptídeos de cadeia curta desenvolvidos no mesmo instituto de pesquisa russo: Semax e Selank. A comunidade também chama de dupla Semax-Selank ou NeuroFocus. A lógica é de contrapeso: o Semax puxa para ativação e foco, o Selank contém a ansiedade que essa ativação pode trazer.",
),
"stacks_tesamorelin-ipamorelin": dict(
    nome="Tesamorelina + Ipamorelina", categoria="combinacao", aprovado="nao",
    tagline="Duas portas diferentes para o mesmo pulso de GH",
    resumo="Junta dois compostos que elevam o hormônio do crescimento por portas diferentes. A tesamorelina é análogo sintético de GHRH: copia o hormônio liberador e diz à hipófise que produza. A ipamorelina age pela via da grelina. As blends comerciais aparecem em proporções 10/3 e 5/5.",
),
"stacks_wolverine-stack": dict(
    nome="Wolverine", categoria="combinacao", aprovado="nao",
    tagline="BPC-157 + TB-500, a base de reparo",
    resumo="Apelido de comunidade para a dupla BPC-157 + TB-500 num protocolo focado em reparo tecidual. O nome vem do personagem de quadrinhos conhecido pela cicatrização rápida — e não é uma descrição do que o par faz. É a base mais simples: GLOW e KLOW são ela com acréscimos.",
),

"proprio_thymalin": dict(
    nome="Thymalin", categoria="primaria", aprovado="parcial",
    tagline="Extrato tímico russo — 293 artigos, 13 ensaios, zero registros",
    resumo="Extrato polipeptídico de timo bovino desenvolvido na União Soviética nos anos 1970 pelo grupo de Vladimir Khavinson. Não é peptídeo único: é mistura, sem sequência definida e sem pureza conferível em laudo. É o composto mais estudado de toda a escola de bioreguladores curtos — e mesmo assim não tem um único ensaio registrado no ClinicalTrials.gov. Esta página traz o levantamento completo, com a consulta usada e a ressalva de cada estudo.",
    alerta="O estudo mais citado sobre longevidade é assinado pelo próprio desenvolvedor do composto. Isso não invalida o trabalho, mas muda o peso que se dá a ele.",
),
"proprio_bioreguladores": dict(
    nome="Bioreguladores curtos de Khavinson", categoria="primaria", aprovado="nao",
    tagline="Onze peptídeos, cinco estudos clínicos, zero ensaios registrados",
    resumo="Vilon, Vesugen, Livagen, Cortagen, Pancragen, Prostamax, Testagen, Chonluten, Bronchogen, Crystagen e Ovagen: peptídeos de dois a quatro aminoácidos da escola russa de bioregulação. Estão numa página só, e não em onze, porque o levantamento no PubMed e no ClinicalTrials.gov não sustenta onze. Oito dos onze não têm nenhum estudo clínico, e nenhum tem ensaio registrado.",
    alerta="Nenhum dos onze tem ensaio registrado no ClinicalTrials.gov. Oito não têm sequer um artigo de ensaio clínico no PubMed. Sete não têm nem a sequência química indexada.",
),
"proprio_meldonium": dict(
    nome="Meldonium (mildronato)", categoria="primaria", aprovado="parcial",
    tagline="357 artigos, 7 ensaios registrados — e uma janela de detecção de meses",
    resumo="Cardioprotetor desenvolvido no Instituto Letão de Síntese Orgânica, em Riga, e registrado na Letônia e na Rússia. É o composto mais bem documentado de todo o bloco do leste europeu desta referência: 357 artigos, 35 ensaios clínicos e 7 registros no ClinicalTrials.gov. Inibe a biossíntese de L-carnitina — e não o contrário — deslocando o metabolismo cardíaco da gordura para a glicose. Está na lista de proibidos da WADA desde 1º de janeiro de 2016.",
    alerta="A janela de detecção urinária medida chega a 117 dias após seis dias de uso, e a vários meses após três semanas. Quem faz exame antidoping deve tratá-lo como indisponível, não como algo a suspender com antecedência.",
),
}

from compostos2 import EXTRA_CATEGORIAS as _XC, EXTRA_COMPOSTOS as _XCOMP
CATEGORIAS.update(_XC)
COMPOSTOS.update(_XCOMP)

from compostos3 import EXTRA2 as _X2
COMPOSTOS.update(_X2)

from compostos4 import EXTRA3 as _X3
COMPOSTOS.update(_X3)

from compostos5 import EXTRA4 as _X4
COMPOSTOS.update(_X4)

from compostos6 import EXTRA5 as _X5
COMPOSTOS.update(_X5)

from compostos7 import EXTRA6 as _X6
COMPOSTOS.update(_X6)

from compostos8 import EXTRA7 as _X7
COMPOSTOS.update(_X7)

from compostos9 import EXTRA8 as _X8
COMPOSTOS.update(_X8)

from compostos10 import EXTRA9 as _X9
COMPOSTOS.update(_X9)

from compostos11 import EXTRA10 as _X10
COMPOSTOS.update(_X10)

from compostos12 import EXTRA11 as _X11
COMPOSTOS.update(_X11)

from compostos13 import EXTRA12 as _X12
COMPOSTOS.update(_X12)

from compostos14 import EXTRA13 as _X13
COMPOSTOS.update(_X13)

from compostos15 import EXTRA14 as _X14
COMPOSTOS.update(_X14)

from compostos16 import EXTRA15 as _X15
COMPOSTOS.update(_X15)

from compostos17 import EXTRA16 as _X16
COMPOSTOS.update(_X16)

from compostos_exossomos import EXTRA_EXOSSOMOS as _XEXO
COMPOSTOS.update(_XEXO)

from compostos_incretinas import EXTRA_INCRETINAS as _XINC
COMPOSTOS.update(_XINC)

from compostos_eixo_gh import EXTRA_EIXO_GH as _XGH
COMPOSTOS.update(_XGH)

from compostos_geroprotetores import EXTRA_GEROPROTETORES as _XGERO
COMPOSTOS.update(_XGERO)

from compostos_figado_lipidio import EXTRA_FIGADO_LIPIDIO as _XFIG
COMPOSTOS.update(_XFIG)

from compostos_calvicie import EXTRA_CALVICIE as _XCALV
COMPOSTOS.update(_XCALV)

from compostos_reparo_novos import EXTRA_REPARO_NOVOS as _XREP
COMPOSTOS.update(_XREP)

from compostos_neuro_novos import EXTRA_NEURO_NOVOS as _XNEU
COMPOSTOS.update(_XNEU)

from compostos_musculo_hpg import EXTRA_MUSCULO_HPG as _XMUS
COMPOSTOS.update(_XMUS)

from compostos_procedimentos import EXTRA_PROCEDIMENTOS as _XPROC
COMPOSTOS.update(_XPROC)
