# -*- coding: utf-8 -*-
"""Paginas escritas a partir de fonte primaria, nao da fonte secundaria.

Diferente do resto do site: aqui nao ha tabela importada. Cada numero foi
conferido no PubMed ou no ClinicalTrials.gov em 04/09/2026, e a consulta
usada esta declarada na propria pagina.

Excecao: proprios18 (mazdutida) foi apurado em 05/09/2026 e carrega data
propria, importada de datas.py. Ver o cabecalho daquele modulo.
"""

from datas import DATA_APURACAO as _DT

PROPRIOS = {

# ---------------------------------------------------------------- Thymalin
"proprio_thymalin": dict(
    secoes=[
        dict(h="O que é", tipo="p", corpo=[
            "Thymalin não é um peptídeo único. É um <strong>extrato polipeptídico de timo bovino</strong>, "
            "obtido por extração ácida — uma mistura, não uma molécula definida. Isso importa mais do que parece: "
            "não existe sequência para citar, não existe pureza para conferir num laudo, e dois lotes podem não ser "
            "a mesma coisa.",
            "Foi desenvolvido na União Soviética nos anos 1970 pelo grupo de Vladimir Khavinson, no que viria a ser "
            "o Instituto de Bioregulação e Gerontologia de São Petersburgo. É o composto mais antigo e mais estudado "
            "de toda a escola de bioreguladores curtos — o mesmo grupo que originou o Epitalon, o Pinealon e o "
            "Cartalax, que já estão nesta referência.",
        ]),
        dict(h="Quanta evidência existe, de verdade", tipo="p", corpo=[
            "Esta é a parte que nenhum site de venda mostra. Os números abaixo foram levantados diretamente no "
            f"PubMed e no ClinicalTrials.gov em {_DT}.",
        ], tabela=dict(
            cap="Levantamento de evidência — Thymalin",
            linhas=[
                ["Base", "Consulta", "Resultado"],
                ["PubMed", "<code>Thymalin</code>", "293 artigos"],
                ["PubMed", "<code>Thymalin AND (Clinical Trial[Publication Type] OR Randomized Controlled Trial[Publication Type])</code>", "13 artigos"],
                ["ClinicalTrials.gov", "intervenção contendo Thymalin", "<strong>0 registros</strong>"],
            ])),
        dict(h="Leitura honesta desses números", tipo="li", corpo=[
            "<strong>293 artigos é muita coisa</strong> para um composto desta família. O Prostamax tem 6. "
            "O Thymalin é o outlier, não a regra.",
            "<strong>Zero ensaios registrados.</strong> Nenhum estudo de Thymalin foi registrado no "
            "ClinicalTrials.gov. Registro prévio é o que impede que um desfecho ruim vire um desfecho diferente "
            "depois — sem ele, não há como saber quantos estudos não foram publicados.",
            "<strong>Os 13 ensaios vão de 1999 a 2015</strong> e são, na maioria, em russo ou ucraniano, "
            "publicados em periódicos regionais.",
            "<strong>O estudo mais citado é do próprio inventor.</strong> Isso não invalida o trabalho, mas é "
            "informação que o leitor precisa ter para calibrar o peso que dá a ele.",
        ]),
        dict(h="Os estudos que sustentam as alegações", tipo="p", corpo=[
            "Segundo o PubMed, estes são os trabalhos clínicos concretos por trás do que se diz sobre o Thymalin. "
            "Leia o que cada um mediu, e em quantas pessoas.",
        ], tabela=dict(
            cap="Estudos clínicos localizados",
            linhas=[
                ["Estudo", "N", "Contexto", "O que relatou", "Ressalva"],
                ["Khavinson &amp; Morozov, 2003<br><small>Neuro Endocrinol Lett 24(3-4):233-40 · PMID 14523363</small>",
                 "266", "Idosos, acompanhados por 6–8 anos",
                 "Mortalidade 2,0–2,1× menor no grupo Thymalin; 4,1× menor no grupo que usou Thymalin + Epitalamina anualmente por 6 anos",
                 "<strong>Assinado pelo desenvolvedor do composto.</strong> É a fonte de praticamente toda alegação de longevidade que circula"],
                ["Maslennikov et al., 2007<br><small>Probl Tuberk Bolezn Legk (9):30-3 · PMID 18038603</small>",
                 "154", "Tuberculose pulmonar progressiva",
                 "Cura clínica de 61,1% no esquema padrão contra 94,7% no esquema individualizado com correção imunológica",
                 "Em russo. O braço de comparação mistura duas variáveis: individualização do esquema e imunocorreção"],
                ["Kopchak et al., 2004<br><small>Klin Khir (9):5-7 · PMID 15560588</small>",
                 "18", "Pancreatite necrosante aguda",
                 "Regressão da doença em 12 de 18; todos sobreviveram",
                 "Em ucraniano. Série pequena, sem grupo controle descrito"],
                ["Litvinenko et al., 2015<br><small>Bull Exp Biol Med 159(1):62-5 · PMID 26033592</small>",
                 "n/d", "Salpingite e ooforite crônicas",
                 "Melhora clínica e imunológica quando a dose foi sincronizada com a reação da succinato desidrogenase linfocitária",
                 "O desfecho depende de um teste de cronobiologia que não é feito na prática comum"],
                ["Musienko, 1999<br><small>Lik Sprava (1):119-22 · PMID 10424021</small>",
                 "15", "Doença de Parkinson idiopática",
                 "Melhora no tremor, rigidez e hipocinesia, com alteração no mapeamento de EEG",
                 "Em russo. Quinze pacientes, sem controle descrito"],
            ])),
        dict(h="Status regulatório", tipo="li", corpo=[
            "<strong>Rússia:</strong> registrado como medicamento imunomodulador, com décadas de uso.",
            "<strong>Brasil:</strong> sem registro na ANVISA.",
            "<strong>Estados Unidos e União Europeia:</strong> sem aprovação.",
            "É importado como medicamento estrangeiro ou vendido como material de pesquisa, conforme o fornecedor.",
        ]),
        dict(h="Por que não há tabela de dose nesta página", tipo="p", corpo=[
            "Porque não achei uma fonte primária que sustente uma. As doses que circulam vêm de bula russa "
            "traduzida por revendedor ou de relato de comunidade — e esta página existe justamente para não "
            "reproduzir isso como se fosse dado.",
            "Se você tem em mãos a bula russa original, ela é a referência válida. Um profissional que leia russo "
            "ou tenha acesso ao registro do Ministério da Saúde da Rússia vale mais que qualquer tabela que eu "
            "montasse aqui por analogia.",
        ]),
    ],
    referencias=[
        ("Khavinson VKh, Morozov VG. Peptides of pineal gland and thymus prolong human life. Neuro Endocrinol Lett. 2003;24(3-4):233-40. PMID 14523363", "https://pubmed.ncbi.nlm.nih.gov/14523363/"),
        ("Maslennikov AA et al. [Immunological correction in progressive pulmonary tuberculosis]. Probl Tuberk Bolezn Legk. 2007;(9):30-3. PMID 18038603", "https://pubmed.ncbi.nlm.nih.gov/18038603/"),
        ("Kopchak VM et al. [The application efficacy of immunomodulators in complex of treatment of an acute necrotic pancreatitis]. Klin Khir. 2004;(9):5-7. PMID 15560588", "https://pubmed.ncbi.nlm.nih.gov/15560588/"),
        ("Litvinenko GI et al. Chrono- and Immunocorrection of Inflammatory Disorders of Internal Reproductive Organs in Women of Reproductive Age. Bull Exp Biol Med. 2015;159(1):62-5. doi:10.1007/s10517-015-2890-0", "https://doi.org/10.1007/s10517-015-2890-0"),
        ("Musienko GV. [Thymalin in the combined treatment of parkinsonism patients]. Lik Sprava. 1999;(1):119-22. PMID 10424021", "https://pubmed.ncbi.nlm.nih.gov/10424021/"),
    ],
),

# ------------------------------------------- familia dos bioreguladores (11)
"proprio_bioreguladores": dict(
    secoes=[
        dict(h="O que são", tipo="p", corpo=[
            "São peptídeos de dois a quatro aminoácidos, desenvolvidos pelo grupo de Vladimir Khavinson no "
            "Instituto de Bioregulação e Gerontologia de São Petersburgo. A tese do grupo é que cada peptídeo "
            "curto se liga a regiões específicas do DNA e regula a expressão gênica de um órgão-alvo — daí cada "
            "um levar o nome do tecido a que se destina: Bronchogen para brônquio, Testagen para testículo, "
            "Prostamax para próstata, e assim por diante.",
            "Esta página cobre onze deles de uma vez. O motivo está na seção seguinte: separá-los em onze páginas "
            "com tabela de dose daria a impressão de que existe base para isso, e não existe.",
        ]),
        dict(h="O levantamento", tipo="p", corpo=[
            f"Consultei o PubMed e o ClinicalTrials.gov em {_DT}, um a um. O resultado está abaixo.",
            "A coluna <strong>Consulta</strong> traz o termo exato que produziu o número ao lado. Copie no PubMed e o resultado tem que ser o mesmo — se não for, o número aqui está velho, e o que vale é o que a base devolver a você.",
            "A coluna <strong>Ensaios clínicos</strong> é a mesma consulta somada ao filtro "
            "<code>Clinical Trial[Publication Type] OR Randomized Controlled Trial[Publication Type]</code>. "
            "No ClinicalTrials.gov a busca foi por intervenção, com o mesmo termo.",
        ], tabela=dict(
            cap="Evidência por composto",
            linhas=[
                ["Composto", "Sequência", "Consulta no PubMed", "Artigos no PubMed", "Ensaios clínicos", "ClinicalTrials.gov"],
                ["Vilon", "Lys-Glu (KE)", "<code>vilon</code>", "80", "3", "0"],
                ["Vesugen / Vezugen", "Lys-Glu-Asp (KED)", "<code>vesugen OR vezugen</code>", "29", "2", "0"],
                ["Livagen", "não indexada", "<code>livagen</code>", "19", "0", "0"],
                ["Cortagen", "Ala-Glu-Asp-Pro (AEDP)", "<code>cortagen</code>", "15", "0", "0"],
                ["Pancragen", "Lys-Glu-Asp-Trp (KEDW)", "<code>pancragen</code>", "9", "0", "0"],
                ["Prostamax", "não indexada", "<code>prostamax</code>", "6", "0", "0"],
                ["Testagen", "não indexada", "<code>testagen</code>", "2", "0", "1"],
                ["Chonluten", "não indexada", "<code>chonluten</code>", "1", "0", "0"],
                ["Bronchogen", "não indexada", "<code>bronchogen</code>", "12", "0", "1"],
                ["Crystagen", "não indexada", "<code>crystagen</code>", "1", "0", "0"],
                ["Ovagen", "não indexada", "<code>ovagen</code>", "34", "2", "0"],
            ])),
        dict(h="Três coisas que esse levantamento revela", tipo="li", corpo=[
            "<strong>Nenhum dos onze tem um único ensaio registrado no ClinicalTrials.gov.</strong> A busca por "
            "intervenção devolveu zero, com contagem total zero.",
            "<strong>Oito dos onze não têm nenhum artigo de ensaio clínico no PubMed.</strong> Toda a literatura "
            "clínica da família se concentra em dois compostos: Vilon e Vesugen.",
            "<strong>As sequências de sete deles não estão sequer indexadas</strong> como conceito químico no "
            "PubMed — o que significa que, para a base biomédica de referência do mundo, esses compostos não têm "
            "identidade química estabelecida.",
        ]),
        dict(h="Os cinco estudos clínicos que existem", tipo="p", corpo=[
            "Segundo o PubMed, é isto — e só isto — que sustenta clinicamente a família inteira. Todos em russo, "
            "quase todos no mesmo periódico, e três com o desenvolvedor entre os autores.",
        ], tabela=dict(
            cap="Todos os ensaios clínicos localizados",
            linhas=[
                ["Composto", "Estudo", "N", "Contexto", "Ressalva"],
                ["Vesugen", "Kitachev et al., 2014 · Adv Gerontol 27(1):156-9 · PMID 25051774", "41",
                 "Disfunção erétil vasculogênica", "<strong>Khavinson entre os autores.</strong> Em russo"],
                ["Vesugen + Pinealon", "Bashkireva &amp; Artamonova, 2012 · Adv Gerontol 25(4):718-28 · PMID 23734521",
                 "150 + 150", "Transtornos neuróticos em caminhoneiros profissionais", "Em russo. Efeito relatado da combinação, não de um composto isolado"],
                ["Vilon", "Kuznik et al., 2007 · Adv Gerontol 20(2):106-15 · PMID 18306698", "n/d",
                 "Diabetes tipo 1: imunidade e coagulação", "Em russo"],
                ["Vilon", "Kuznik et al., 2006 · Adv Gerontol 19:107-15 · PMID 17152731", "n/d",
                 "Diabetes tipo 1: coagulação e fibrinólise", "Em russo. Confirma a sequência Lys-Glu"],
                ["Vilon", "Ias'kevich et al., 2005 · Adv Gerontol 16:97-100 · PMID 16075684", "n/d",
                 "Câncer colorretal em idosos, como adjuvante", "<strong>Khavinson entre os autores.</strong> Em russo. Os próprios autores chamam de experiência pioneira e resultado preliminar"],
            ])),
        dict(h="A armadilha do nome Ovagen", tipo="p", corpo=[
            "Ao levantar isto, a busca trouxe um ensaio randomizado que parecia ser de Ovagen. Não era: é um "
            "estudo de superovulação em <strong>vacas</strong>, publicado em Animal Reproduction Science, no qual "
            "Ovagen é a marca de um produto veterinário de FSH — nada a ver com o peptídeo de Khavinson.",
            "Registro isto porque é exatamente o tipo de erro que infla contagem de evidência quando alguém "
            "pesquisa pelo nome comercial e não confere o que achou.",
        ]),
        dict(h="Status regulatório", tipo="li", corpo=[
            "<strong>Rússia:</strong> vários são vendidos como suplemento alimentar (parafarmacêutico), não como medicamento registrado.",
            "<strong>Brasil:</strong> nenhum tem registro na ANVISA.",
            "<strong>Estados Unidos e União Europeia:</strong> nenhum é aprovado.",
        ]),
        dict(h="Por que esta página não traz dose", tipo="p", corpo=[
            "Porque não há fonte primária de onde tirar. Com zero ensaios registrados e oito dos onze compostos "
            "sem nenhum estudo clínico, qualquer tabela de dose aqui seria uma transcrição de rótulo de "
            "fornecedor — apresentada com a mesma aparência de autoridade das tabelas do resto do site, que ao "
            "menos vêm de protocolos documentados.",
            "É a diferença entre dizer <em>não sei</em> e preencher a lacuna com algo que parece resposta.",
        ]),
    ],
    referencias=[
        ("Kitachev KV et al. [The efficacy of peptide bioregulators of vessels in lower limbs chronic arterial insufficiency treatment in old and elderly people]. Adv Gerontol. 2014;27(1):156-9. PMID 25051774", "https://pubmed.ncbi.nlm.nih.gov/25051774/"),
        ("Bashkireva AS, Artamonova VG. [The peptide correction of neurotic disorders among professional truck-drivers]. Adv Gerontol. 2012;25(4):718-28. PMID 23734521", "https://pubmed.ncbi.nlm.nih.gov/23734521/"),
        ("Kuznik BI et al. [Effect of vilon on the immunity status and coagulation hemostasis in patients of different age with diabetes mellitus]. Adv Gerontol. 2007;20(2):106-15. PMID 18306698", "https://pubmed.ncbi.nlm.nih.gov/18306698/"),
        ("Kuznik BI et al. [Effect of thymomimetic vilon on blood coagulation system and fibrinolisis in diabetes mellitus type 1 patients of different age]. Adv Gerontol. 2006;19:107-15. PMID 17152731", "https://pubmed.ncbi.nlm.nih.gov/17152731/"),
        ("Ias'kevich LS et al. [Application of peptide bioregulator in complex treatment of elderly cancer patients]. Adv Gerontol. 2005;16:97-100. PMID 16075684", "https://pubmed.ncbi.nlm.nih.gov/16075684/"),
        ("Aller JF et al. Transvaginal follicular aspiration and embryo development in superstimulated early postpartum beef cows. Anim Reprod Sci. 2009;119(1-2):1-8. doi:10.1016/j.anireprosci.2009.11.009 — o falso positivo do nome Ovagen", "https://doi.org/10.1016/j.anireprosci.2009.11.009"),
    ],
),
}

from proprios2 import MELDONIUM as _MELD
PROPRIOS.update(_MELD)

from proprios3 import SUPLEMENTOS as _SUP3
from proprios4 import SUPS as _SUP4
PROPRIOS.update(_SUP3)
PROPRIOS.update(_SUP4)

from proprios5 import LESTE as _LESTE
PROPRIOS.update(_LESTE)

from proprios6 import KLOW_SEMAX as _KS
PROPRIOS.update(_KS)

from proprios7 import NOOT as _NOOT
PROPRIOS.update(_NOOT)

from proprios8 import EFEITO as _EFEITO
PROPRIOS.update(_EFEITO)

from proprios9 import GLP1 as _GLP1
PROPRIOS.update(_GLP1)

from proprios10 import ANV as _ANV
PROPRIOS.update(_ANV)

from proprios11 import SARM as _SARM
PROPRIOS.update(_SARM)

from proprios12 import CRISPR as _CRISPR
PROPRIOS.update(_CRISPR)

from proprios13 import CASGEVY as _CASG
PROPRIOS.update(_CASG)

from proprios14 import RIM as _RIM
PROPRIOS.update(_RIM)

from proprios15 import DOSE_RENAL as _DOSER
PROPRIOS.update(_DOSER)

from proprios16 import HEPATICA as _HEP
PROPRIOS.update(_HEP)

from proprios17 import ALCOOL as _ALC
PROPRIOS.update(_ALC)

from proprios18 import MAZDUTIDA as _MAZD
PROPRIOS.update(_MAZD)
