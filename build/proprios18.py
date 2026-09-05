# -*- coding: utf-8 -*-
"""Mazdutida: levantamento de fonte primaria.

Apurado em 5 de setembro de 2026 -- um dia depois da varredura que produziu as
outras paginas desta secao. Por isso importa DATA_MAZDUTIDA, e nao
DATA_APURACAO: carimbar esta pagina com a data da varredura anterior seria
afirmar uma conferencia que naquele dia nao houve.

Consultas rodadas:
  PubMed             mazdutide OR IBI362 OR LY3305677
  ClinicalTrials.gov intervencao: mazdutide OR IBI362  (e o mesmo com fase 3)
  openFDA            openfda.generic_name:"mazdutide" e busca livre por mazdutide
  ANVISA             grep no dado aberto de medicamentos registrados
"""

from datas import DATA_MAZDUTIDA as _DT

MAZDUTIDA = {
"proprio_mazdutida": dict(
    secoes=[
        dict(h="O que é", tipo="p", corpo=[
            "Mazdutida é um <strong>agonista duplo de GLP-1 e de glucagon</strong>, semanal e subcutâneo. "
            "É a mesma dupla de alvos da survodutida, e diferente da tirzepatida, que atinge GLP-1 e GIP. "
            "Circula com três nomes: <strong>mazdutida</strong>, <strong>IBI362</strong> (o código da Innovent "
            "Biologics, que a desenvolve na China) e <strong>LY3305677</strong> (o código da Eli Lilly, de onde "
            "a molécula veio). Buscar por um só dos três devolve menos do que existe.",
            "Ela não estava neste site até agora, e a ausência tinha uma razão: a fonte secundária que originou "
            "a maior parte das páginas daqui não traz a mazdutida. Esta página não veio dessa fonte. Foi montada "
            "do zero, do PubMed e do ClinicalTrials.gov.",
        ]),
        dict(h="Quanta evidência existe, de verdade", tipo="p", corpo=[
            f"Os números abaixo foram levantados por mim em {_DT}. A consulta de cada linha está ao lado do "
            "número, para qualquer pessoa repetir.",
        ], tabela=dict(
            cap="Levantamento de evidência — mazdutida",
            linhas=[
                ["Base", "Consulta", "Resultado"],
                ["PubMed", "<code>mazdutide OR IBI362 OR LY3305677</code>", "51 artigos"],
                ["ClinicalTrials.gov", "campo de intervenção: <code>mazdutide OR IBI362</code>", "43 estudos registrados"],
                ["ClinicalTrials.gov", "a mesma consulta, filtrada em <code>PHASE3</code>", "<strong>12 ensaios de fase 3</strong>"],
                ["openFDA", "<code>openfda.generic_name:\"mazdutide\"</code> e busca livre por <code>mazdutide</code>",
                 "<strong>0 rótulos</strong> — sem registro na FDA"],
                ["ANVISA", "<code>mazdutida</code> no dado aberto de medicamentos registrados",
                 "<strong>0 registros</strong>"],
            ])),
        dict(h="Isto é raro neste site", tipo="li", corpo=[
            "<strong>12 ensaios de fase 3 é mais do que quase tudo aqui tem.</strong> A maior parte dos compostos "
            "desta referência não passou de modelo animal. A mazdutida está do outro lado da escala: tem programa "
            "clínico completo, com desfecho primário definido, comparador ativo e resultado publicado em "
            "<strong>NEJM, JAMA e Nature</strong>.",
            "<strong>E mesmo assim não tem bula em lugar nenhum onde eu procurei.</strong> Zero na FDA, zero na "
            "ANVISA. Quem compra mazdutida hoje está comprando um fármaco que passou na fase 3 e não passou por "
            "agência nenhuma que eu tenha conferido.",
            "<strong>Isso é o oposto do padrão do site.</strong> O padrão daqui é evidência fraca e alegação "
            "forte. Aqui a evidência é forte — e o que falta é o carimbo.",
        ]),
        dict(h="As fases 2 e 3 publicadas, com os números", tipo="p", corpo=[
            "Cinco estudos com resultado publicado em periódico indexado. Li o resumo de cada um; os percentuais "
            "abaixo são os que o próprio artigo reporta.",
        ], tabela=dict(
            cap="Ensaios de mazdutida com resultado publicado",
            linhas=[
                ["Estudo", "Desenho", "n", "Resultado principal"],
                ["Fase 1b<br>NCT04466904", "12 semanas, DM2, contra placebo e dulaglutida aberta, 3 a 6 mg", "43 randomizados<br>42 tratados",
                 "Reduções de HbA1c e glicemia; desfecho primário era segurança. Eventos mais comuns: diarreia (29,2%), apetite reduzido (25,0%), náusea (16,7%)"],
                ["Fase 2<br>NCT04904913", "24 semanas, sobrepeso/obesidade, 3 / 4,5 / 6 mg contra placebo", "248",
                 "Peso: <strong>−6,7%</strong>, <strong>−10,4%</strong> e <strong>−11,3%</strong> contra <strong>+1,0%</strong> no placebo"],
                ["<strong>GLORY-1</strong><br>NCT05607680", "Fase 3, 48 semanas, sobrepeso/obesidade, 4 e 6 mg contra placebo", "610",
                 "Semana 32: <strong>−10,09%</strong> e <strong>−12,55%</strong> contra <strong>+0,45%</strong>. Semana 48: <strong>−11,00%</strong> e <strong>−14,01%</strong> contra <strong>+0,30%</strong>. Perda de 15% ou mais em 35,7% e 49,5%, contra 2,0% no placebo"],
                ["<strong>GLORY-2</strong><br>NCT06164873", "Fase 3, 60 semanas, obesidade com IMC ≥ 30, dose única de 9 mg contra placebo", "461 tratados<br>(307 e 154)",
                 "Peso: <strong>−16,65%</strong> contra <strong>−1,50%</strong>. Perda de 5% ou mais em <strong>84,3%</strong> contra 33,1%. Vômito em <strong>53,1%</strong>, náusea em 46,9%, diarreia em 39,4%"],
                ["<strong>DREAMS-1</strong><br>NCT05628311", "Fase 3, 24 semanas em monoterapia, DM2, 4 e 6 mg contra placebo", "320",
                 "HbA1c: <strong>−1,57%</strong> e <strong>−2,15%</strong> contra <strong>−0,14%</strong>. Peso: −5,61% e −7,81% contra −1,26%"],
                ["<strong>DREAMS-2</strong><br>NCT05606913", "Fase 3, 28 semanas, DM2, 4 e 6 mg contra dulaglutida 1,5 mg", "731",
                 "Superior à dulaglutida em HbA1c (diferença de <strong>−0,24%</strong> e <strong>−0,30%</strong>) e em peso (<strong>−3,78%</strong> e <strong>−5,76%</strong>)"],
            ])),
        dict(h="A meta-análise diz menos do que os ensaios parecem dizer", tipo="p", corpo=[
            "Uma revisão sistemática reuniu <strong>9 ensaios randomizados, 2.292 participantes</strong>, com busca "
            "até 20 de fevereiro de 2026. Os números de perda de peso que ela agrupa são grandes: −6,56%, −9,92% e "
            "−11,1% para 3, 4 e 6 mg contra placebo em obesidade sem diabetes.",
            "E logo em seguida ela classifica <strong>a certeza dessa evidência como MUITO BAIXA</strong>, pelo "
            "método GRADE, por heterogeneidade substancial e por poucos ensaios. No diabetes tipo 2 a certeza é "
            "<strong>moderada</strong> — melhor, e ainda assim não alta.",
            "Vale ler as duas coisas juntas, porque elas costumam ser separadas na hora de vender: <strong>o efeito "
            "é grande e a confiança no tamanho dele é baixa</strong>. Não são frases contraditórias. A primeira é "
            "sobre a média observada; a segunda, sobre quanto essa média deve mudar quando entrarem mais estudos.",
        ]),
        dict(h="Toda a fase 3 é chinesa", tipo="p", corpo=[
            "Este é o achado que muda a leitura de tudo o que está acima. <strong>Nos 12 ensaios de fase 3 "
            "registrados, o patrocinador é chinês e a população declarada é chinesa</strong> — os títulos dizem "
            "\"Chinese participants\", \"Chinese adults\", \"Chinese adolescents\". Os artigos do NEJM, da JAMA e "
            "da Nature repetem isso no próprio título.",
            "A meta-análise reconhece a limitação e pede, na conclusão, estudos mais longos e "
            "<strong>multiétnicos</strong> para confirmar durabilidade, generalização e segurança cardiovascular.",
            "O que isso significa na prática, para quem lê daqui: <strong>o IMC médio dos participantes era baixo "
            "para o padrão ocidental</strong> — 31,1 na GLORY-1 e 34,3 na GLORY-2, contra os 38 que os grandes "
            "ensaios ocidentais de obesidade costumam ter. Resposta a incretina varia com composição corporal e "
            "com o ponto de partida. Não estou dizendo que o resultado não se transporta; estou dizendo que "
            "<strong>ninguém testou se ele se transporta</strong>.",
        ]),
        dict(h="Onde o registro e o artigo não batem", tipo="p", corpo=[
            "A GLORY-2 é o caso. O artigo saiu na <strong>JAMA em agosto de 2026</strong>, com resultado completo "
            "de 461 participantes tratados, e descreve o estudo rodando em <strong>27 hospitais</strong>, de "
            "dezembro de 2023 a novembro de 2025.",
            "No ClinicalTrials.gov, o mesmo NCT06164873 continua com situação <strong>UNKNOWN</strong> — a marca "
            "que o registro aplica quando o patrocinador parou de atualizar — e traz <strong>uma única "
            "localização</strong> cadastrada.",
            "Não é fraude nem erro de resultado: é registro desatualizado, e é comum. Mas é a razão pela qual eu "
            "não confio em uma base só. <strong>Quem consultasse apenas o ClinicalTrials.gov concluiria que a "
            "GLORY-2 está parada e sem resultado.</strong> Quem consultasse apenas o PubMed não saberia que "
            "existem outros sete ensaios de fase 3 ainda correndo.",
        ]),
        dict(h="O que ainda está correndo", tipo="li", corpo=[
            "<strong>GLORY-3</strong> (NCT06884293): fase 3 contra semaglutida em doença hepática esteatótica "
            "associada a disfunção metabólica, 479 participantes, ativo e sem recrutar.",
            "<strong>DREAMS-3</strong> (NCT06184568): fase 3 aberta contra semaglutida em DM2 inicial com "
            "obesidade, 349 participantes, <strong>concluído em setembro de 2025 e ainda sem publicação que eu "
            "tenha encontrado</strong>.",
            "<strong>GLORY-OSA</strong> (NCT06931028): apneia obstrutiva do sono moderada a grave, 260 "
            "participantes, recrutando.",
            "<strong>GLORY-YOUNG</strong> (NCT07255209): adolescentes chineses com obesidade ou sobrepeso, 180 "
            "participantes, recrutando.",
            "<strong>Hipertensão leve a moderada</strong> (NCT07469800) com sobrepeso, 336 participantes, sem "
            "tratamento anti-hipertensivo prévio, recrutando.",
            "<strong>Função cognitiva em DM2</strong> (NCT07083154): 420 participantes, patrocinador acadêmico e "
            "não a fabricante, com conclusão prevista só para 2029.",
            "<strong>Um concorrente já usa a mazdutida como régua</strong>: o HDM1005 (NCT07417306) foi registrado "
            "como fase 3 <em>contra</em> mazdutida, com 912 participantes. Virar comparador ativo é o sinal de que "
            "um fármaco passou a ser o padrão a bater — naquele mercado.",
        ]),
        dict(h="Sem bula, sem dose aprovada, sem lista de contraindicação", tipo="p", corpo=[
            f"Procurei na base de rótulos da FDA em {_DT}, pelo nome genérico e por busca livre: "
            "<strong>a mazdutida não tem registro</strong>. No dado aberto da ANVISA, também não.",
            "Isso não a torna mais segura que a semaglutida ou a tirzepatida, que têm tarja preta. Torna-a "
            "<strong>menos documentada</strong>: não existe escada de titulação aprovada por agência, não existe "
            "dose máxima definida e <strong>não existe lista oficial de contraindicação</strong> para comparar.",
            "As doses que os ensaios usaram foram <strong>3, 4, 4,5, 6 e 9 mg por semana</strong>, por via "
            "subcutânea, sempre com escalonamento. O teto testado em fase 3 é <strong>9 mg</strong>, e foi testado "
            "num único ensaio.",
            "Os análogos aparentados que já têm bula carregam advertência de tumor de células C da tireoide, e a "
            "tirzepatida é contraindicada em carcinoma medular de tireoide e neoplasia endócrina múltipla tipo 2 "
            "nas bulas dos dois países. Não afirmo que isso vale para a mazdutida — <strong>não há bula dela para "
            "ler</strong>. Afirmo que o leitor não tem, aqui, o documento que teria para as outras duas. O que as "
            "agências dizem sobre a classe está em "
            "<a href=\"proprio_glp1_bula.html\">Os GLP-1 contra a bula</a>.",
        ]),
        dict(h="O que este levantamento não fez", tipo="li", corpo=[
            "<strong>Não conferi se a mazdutida tem registro na China.</strong> Todo o programa clínico é chinês, "
            "e a agência que naturalmente decidiria primeiro é a NMPA — que eu não consultei. Qualquer afirmação "
            "minha sobre aprovação chinesa seria chute. O que está verificado é a ausência na FDA e na ANVISA.",
            "<strong>Li resumos, não os artigos inteiros.</strong> Os percentuais reproduzidos aqui são os que "
            "cada resumo publica. Não fui ao material suplementar, não confiri análise por protocolo contra "
            "intenção de tratar, e não avaliei risco de viés estudo a estudo.",
            "<strong>Não busquei literatura chinesa fora do PubMed.</strong> Um programa inteiramente chinês "
            "provavelmente tem publicação em periódico nacional que este levantamento não alcança.",
            "<strong>Não há tabela de reconstituição nesta página</strong>, e é deliberado: sem dose aprovada e "
            "sem apresentação registrada, uma tabela de diluição daria à mazdutida uma aparência de protocolo que "
            "a evidência não sustenta.",
            "<strong>Não comparei mazdutida com tirzepatida ou retatrutida cabeça a cabeça.</strong> Nenhum ensaio "
            "fez isso. As comparações publicadas são contra placebo, dulaglutida e semaglutida.",
        ]),
    ],
    nota_refs=(f'Cada número desta página foi levantado por mim em {_DT} no PubMed, no '
               'ClinicalTrials.gov, na base de rótulos da FDA e no dado aberto da ANVISA, e a consulta usada '
               'está declarada acima. <strong>Esta página é um dia mais nova que as outras desta seção</strong>, '
               'e por isso carrega data própria.'),
    referencias=[
        ("Ji L et al. Once-Weekly Mazdutide in Chinese Adults with Obesity or Overweight. N Engl J Med. 2025;392(22):2215-2225 — GLORY-1, NCT05607680, 610 participantes.",
         "https://doi.org/10.1056/NEJMoa2411528"),
        ("Gao L et al. Treatment With 9-mg Mazdutide for Weight Reduction in Chinese Adults With Obesity: The GLORY-2 Randomized Clinical Trial. JAMA. 2026;336(5):377-388 — NCT06164873, 461 tratados, 60 semanas.",
         "https://doi.org/10.1001/jama.2026.8142"),
        ("Zhu D et al. Mazdutide versus placebo in Chinese adults with type 2 diabetes. Nature. 2025;652(8108):174-180 — DREAMS-1, NCT05628311, 320 participantes.",
         "https://doi.org/10.1038/s41586-025-10026-w"),
        ("Guo L et al. Mazdutide versus dulaglutide in Chinese adults with type 2 diabetes. Nature. 2025;652(8108):181-188 — DREAMS-2, NCT05606913, 731 participantes.",
         "https://doi.org/10.1038/s41586-025-10031-z"),
        ("Ji L et al. A phase 2 randomised controlled trial of mazdutide in Chinese overweight adults or adults with obesity. Nat Commun. 2023;14(1):8289 — NCT04904913, 248 participantes.",
         "https://doi.org/10.1038/s41467-023-44067-4"),
        ("Jiang H et al. A phase 1b randomised controlled trial of a glucagon-like peptide-1 and glucagon receptor dual agonist IBI362 (LY3305677) in Chinese patients with type 2 diabetes. Nat Commun. 2022;13(1):3613 — NCT04466904.",
         "https://doi.org/10.1038/s41467-022-31328-x"),
        ("Kamrul-Hasan ABM et al. Efficacy and Safety of the Dual GLP-1 and Glucagon Receptor Agonist Mazdutide. Diabetes Obes Metab. 2026;28(10):8777-8794 — meta-análise de 9 ensaios, 2.292 participantes, e a classificação GRADE de certeza muito baixa em obesidade.",
         "https://doi.org/10.1111/dom.71058"),
        ("Registro da GLORY-2 no ClinicalTrials.gov, ainda com situação UNKNOWN e uma única localização, contra os 27 hospitais descritos no artigo da JAMA.",
         "https://clinicaltrials.gov/study/NCT06164873"),
        ("Registro da GLORY-1 no ClinicalTrials.gov, com 23 localizações cadastradas.",
         "https://clinicaltrials.gov/study/NCT05607680"),
        ("Registro da DREAMS-3 no ClinicalTrials.gov — concluída em setembro de 2025, contra semaglutida, sem publicação localizada.",
         "https://clinicaltrials.gov/study/NCT06184568"),
        ("API pública de rótulos da FDA, usada para confirmar a ausência de registro da mazdutida.",
         "https://open.fda.gov/apis/drug/label/"),
        ("Dado aberto de medicamentos registrados da ANVISA, a mesma base usada na página O que existe no Brasil.",
         "https://dados.anvisa.gov.br/dados/"),
    ],
),
}
