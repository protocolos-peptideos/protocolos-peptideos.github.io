# -*- coding: utf-8 -*-
"""Metadado das paginas de alegacoes (indice, cartao, resumo e alerta).

Selo 'aprovado' pela indicacao de que a pagina trata (decisao de 16/10/2026):
  sim     -- medicamento aprovado para aquele uso;
  parcial -- a aprovacao cobre so parte do uso tratado, ou e alegacao
             autorizada de suplemento para aquele uso;
  nao     -- a aprovacao existente e para outra coisa, ou nao existe.

Gerado por build/json/gera_paginas_alegacoes.py a partir dos textos de
build/json/alegacoes/md/ (local, fora do git). Editar o Markdown e rodar o
gerador de novo, nunca este arquivo.

As datas nao aparecem aqui: os marcadores {DATA} e {DATA_C} sao trocados no
import por datas.DATA_ALEGACOES e datas.DATA_ALEGACOES_CONTAGEM, como manda a
trava de datas.
"""

from datas import DATA_ALEGACOES as _DT
from datas import DATA_ALEGACOES_CONTAGEM as _DTC
from datas import DATA_APURACAO as _DTA


def _d(x):
    if isinstance(x, str):
        return x.replace("{DATA_C}", _DTC).replace("{DATA_APURACAO}", _DTA).replace("{DATA}", _DT)
    if isinstance(x, list):
        return [_d(i) for i in x]
    if isinstance(x, tuple):
        return tuple(_d(i) for i in x)
    if isinstance(x, dict):
        return {k: _d(v) for k, v in x.items()}
    return x


EXTRA_ALEGACOES = _d({'proprio_acafrao_crocus_sativus': {'nome': 'Açafrão verdadeiro (Crocus sativus, extrato do estigma)',
                                    'categoria': 'primaria',
                                    'aprovado': 'nao',
                                    'tagline': 'Contra antidepressivo, 8 ensaios pequenos não acharam '
                                               'diferença, o que não prova empate; contra placebo, o efeito '
                                               'aparece na escala do paciente, não na do avaliador.',
                                    'resumo': 'O açafrão verdadeiro é o estigma seco da flor Crocus sativus, '
                                              'não a cúrcuma. Em depressão, o PubMed devolve 46 ensaios '
                                              'randomizados, a maioria com autores do Irã. Contra placebo, '
                                              'uma meta-análise de 2026 com 34 ensaios achou queda nos '
                                              'escores que o próprio paciente preenche, mas não na escala '
                                              'aplicada por avaliador. Contra antidepressivos, 8 ensaios '
                                              'pequenos e curtos não acharam diferença, e isso não é o mesmo '
                                              'que demonstrar empate. Em TDAH, há um ensaio piloto de 54 '
                                              'crianças. Uma diretriz internacional de 2022 dá ao açafrão '
                                              'recomendação provisória em depressão. No Brasil, ele não '
                                              'consta da lista de constituintes de suplemento.',
                                    'alerta': 'Depressão é doença séria. Os estudos de açafrão são em '
                                              'depressão leve a moderada e curtos (os que li duraram de 4 a '
                                              '6 semanas), e nenhum sustenta trocar ou suspender '
                                              'antidepressivo por conta própria. Doses altas de açafrão '
                                              'foram associadas a estímulo do útero e aborto, e a dose de '
                                              '400 mg baixou a pressão em voluntários. Entre 20% e 30% do '
                                              'açafrão comercial é adulterado, segundo uma revisão de 2026. '
                                              'No Brasil, o Crocus sativus não consta da lista de '
                                              'constituintes autorizados em suplemento.'},
 'proprio_acido_d_aspartico': {'nome': 'Ácido D-aspártico (D-aspartato, DAA)',
                               'categoria': 'primaria',
                               'aprovado': 'nao',
                               'tagline': 'Os "+42% em 12 dias" vêm de 23 homens saudáveis com testosterona '
                                          'normal, não baixa; quatro ensaios depois disso não repetiram o '
                                          'efeito, e 6 g por dia derrubaram a testosterona.',
                               'resumo': 'O ácido D-aspártico é a forma "D" de um aminoácido presente na '
                                         'hipófise e no testículo. O número que circula, testosterona de 4,5 '
                                         'para 6,4 ng/mL (+42%) em 12 dias, é de um estudo italiano de 2009 '
                                         'com 23 homens saudáveis de 27 a 37 anos, testosterona média normal '
                                         'e um produto comercial; o placebo era água com sal. Depois disso, '
                                         'quatro ensaios com placebo em homens treinados, com 3 ou 6 g por '
                                         'dia de 2 semanas a 3 meses, não acharam aumento; num deles, 6 g '
                                         'por dia reduziram a testosterona total e a livre. Nenhum estudo '
                                         'testou a ideia de que o efeito aparece só em quem tem testosterona '
                                         'baixa. No Brasil, a forma D não consta da lista de constituintes '
                                         'de suplemento; só a forma L é autorizada.',
                               'alerta': 'No Brasil, só o ácido L-aspártico é fonte autorizada de aspartato '
                                         'em suplemento; o ácido D-aspártico não consta da lista. Num ensaio '
                                         'controlado, 6 g por dia por duas semanas reduziram a testosterona '
                                         'total e a livre em homens treinados. Não localizei estudo de '
                                         'segurança de uso por mais de 3 meses nem estudo em homens com '
                                         'hipogonadismo diagnosticado.'},
 'proprio_acido_ursolico': {'nome': 'Ácido ursólico (casca de maçã)',
                            'categoria': 'primaria',
                            'aprovado': 'nao',
                            'tagline': 'O estudo da PLOS ONE citado como prova de "−40% de gordura" foi '
                                       'feito em camundongos e não traz esse número; em homens que treinam, '
                                       '400 mg por dia não somaram músculo.',
                            'resumo': 'O ácido ursólico é uma substância da cera da casca da maçã e de '
                                      'várias folhas, como alecrim e nêspera. Em camundongos, aumentou '
                                      'músculo e gordura marrom e reduziu a obesidade. O artigo de 2012 da '
                                      'PLOS ONE citado nos vídeos é esse estudo em camundongos, e o número '
                                      'de 40% não aparece no texto. Em pessoas, o PubMed devolve 5 ensaios '
                                      'randomizados sobre músculo ou gordura, e os 4 que testam o ácido '
                                      'ursólico têm de 9 a 26 participantes. O ensaio com placebo em homens '
                                      'treinados não achou músculo a mais, e uma meta-análise de 2024 com 6 '
                                      'estudos não achou efeito em peso, gordura ou massa magra. No Brasil, '
                                      'o ácido ursólico não é constituinte autorizado de suplemento '
                                      'alimentar.',
                            'alerta': 'O ácido ursólico não consta da lista de constituintes autorizados '
                                      'para suplemento alimentar no Brasil (IN 28/2018, consolidada até a IN '
                                      '470, de 16 de setembro de 2026). Os ensaios por boca duraram no '
                                      'máximo 12 semanas e não trazem perfil de segurança de uso prolongado. '
                                      'Em infusão na veia, em estudos de câncer, a dose máxima tolerada teve '
                                      'como toxicidade limitante dano ao fígado e diarreia; isso não se '
                                      'transfere automaticamente para cápsula, mas é o único dado de '
                                      'toxicidade em humanos que localizei.'},
 'proprio_akarkara_anacyclus_pyrethrum': {'nome': 'Akarkara (Anacyclus pyrethrum)',
                                          'categoria': 'primaria',
                                          'aprovado': 'nao',
                                          'tagline': 'Os "+150%" e "+100%" de testosterona livre não '
                                                     'aparecem em nenhum estudo; tudo o que existe sobre '
                                                     'hormônio e ereção com essa raiz foi feito em ratos.',
                                          'resumo': 'Akarkara é o nome ayurvédico da raiz de Anacyclus '
                                                    'pyrethrum, planta do norte da África classificada como '
                                                    'vulnerável pela lista vermelha da IUCN; o mesmo nome '
                                                    'também é usado na Índia para plantas do gênero '
                                                    'Spilanthes. O PubMed tem 69 artigos sobre a planta e '
                                                    'nenhum marcado como ensaio clínico ou meta-análise; o '
                                                    'ClinicalTrials.gov não tem nenhum registro. Os estudos '
                                                    'que os vídeos citam são de um mesmo grupo indiano, em '
                                                    'ratos, por 28 dias. O "Planta Medica" citado é uma '
                                                    'análise química, não um teste de efeito. O "efeito que '
                                                    'persiste 15 dias" foi medido em ratos. A evidência em '
                                                    'humanos é zero. No Brasil, a planta não consta da lista '
                                                    'de constituintes de suplemento.',
                                          'alerta': 'Não há nenhum estudo em humanos com akarkara para '
                                                    'testosterona, ereção ou fertilidade, nem estudo de '
                                                    'segurança em pessoas. Em camundongos, extratos da raiz '
                                                    'elevaram enzimas do fígado em dose de 300 mg/kg e '
                                                    'causaram alterações no fígado, nos rins e no baço em '
                                                    'dose alta. Remédios ayurvédicos vendidos nos EUA tinham '
                                                    'chumbo, mercúrio ou arsênio em cerca de um a cada cinco '
                                                    'produtos analisados. O nome "akarkara" é usado para '
                                                    'mais de uma planta, e o que se compra pode não ser a '
                                                    'espécie dos estudos.'},
 'proprio_albumina': {'nome': 'Albumina (clara de ovo desidratada)',
                      'categoria': 'primaria',
                      'aprovado': 'parcial',
                      'tagline': 'O único estudo de Phillips com ovo que localizei usou ovo inteiro, em 6 '
                                 'homens, sem carne nem whey; e a proteína do ovo cru teve digestibilidade '
                                 'de 51,3%, contra 90,9% cozida.',
                      'resumo': 'Albumina, no balcão de suplementos, é clara de ovo desidratada: segundo a '
                                'tabela do USDA, 81,1 g de proteína em 100 g de pó, sem gordura e sem '
                                'lactose. É proteína completa, de pontuação máxima no PDCAAS. Mas tem menos '
                                'aminoácidos essenciais e menos leucina por grama que o whey, e o único '
                                'ensaio que comparou as duas no treino, com 30 pessoas por 6 semanas, não '
                                'achou efeito de nenhuma. O único estudo de Phillips com proteína de ovo que '
                                'localizei usou ovo inteiro, em 6 homens, e não comparou com carne nem soro. '
                                'Crua, a proteína do ovo teve digestibilidade de 51,3%. Nenhum estudo testou '
                                'clara antes de dormir.',
                      'alerta': 'Ovo é alérgeno alimentar, e há relato de alergia a ovo que começou na idade '
                                'adulta. Clara não desnaturada contém avidina, que prende a biotina: bebidas '
                                'de clara induziram deficiência leve de biotina em 28 dias num estudo. A '
                                'tabela do USDA registra 1.280 mg de sódio em 100 g de clara desidratada. A '
                                '"albumina" proibida pela agência antidoping é a albumina humana na veia, '
                                'outra coisa.'},
 'proprio_alfa_gpc': {'nome': 'Alfa-GPC antes do treino ("GH 44 vezes")',
                      'categoria': 'primaria',
                      'aprovado': 'nao',
                      'tagline': 'O "GH 44 vezes" veio de um resumo de congresso com 7 homens em que o GH de '
                                 'partida do dia da alfa-GPC era dez vezes menor que o do placebo; com o '
                                 'mesmo treino, em 20 homens, o GH não mudou.',
                      'resumo': 'A alfa-GPC, ou colina alfoscerato, é uma molécula com colina que o corpo '
                                'usa para fabricar acetilcolina. O "GH 44 vezes" existe: está num resumo de '
                                'congresso de 2008, com 7 homens, 600 mg e financiamento de um fabricante. '
                                'Mas o GH de partida no dia da alfa-GPC era 0,19 ng/mL e no dia do placebo, '
                                '1,9 ng/mL; em valor absoluto, o pico foi 8,4 contra 5,0. Em 2024, um ensaio '
                                'com 20 homens e o mesmo treino de agachamento não achou diferença no GH nem '
                                'no desempenho físico. Em força, os estudos são pequenos e discordam. Em '
                                'idosos com comprometimento cognitivo, há ensaios positivos. No Brasil, a '
                                'alfa-GPC não é fonte de colina autorizada em suplemento e não tem '
                                'medicamento registrado.',
                      'alerta': 'A alfa-GPC não está entre as fontes de colina autorizadas em suplemento '
                                'alimentar no Brasil (IN 28/2018, consolidada até setembro de 2026) e não há '
                                'medicamento com ela registrado na ANVISA. Uma coorte coreana de mais de 12 '
                                'milhões de pessoas com 50 anos ou mais associou o uso de alfa-GPC a mais '
                                'AVC em 10 anos, com risco maior quanto maior o uso; é estudo observacional, '
                                'que não prova causa. Num ensaio, 500 mg por dia por 7 dias baixaram o TSH, '
                                'hormônio que regula a tireoide.'},
 'proprio_alho_preto_s_alil_cisteina': {'nome': 'Alho preto e S-alil-cisteína',
                                        'categoria': 'primaria',
                                        'aprovado': 'nao',
                                        'tagline': 'O estudo japonês de 2021 deu S-alil-cisteína por injeção '
                                                   'na barriga de 8 camundongos; em pessoas, ninguém mediu '
                                                   'testosterona, e a queda de pressão foi de 1,8 mmHg.',
                                        'resumo': 'A S-alil-cisteína é um composto de enxofre que existe em '
                                                  'pouca quantidade no alho cru e aumenta muito no alho '
                                                  'preto, feito com calor e umidade por dias ou semanas. O '
                                                  'estudo da Universidade de Tohoku de 2021 existe: uma dose '
                                                  'de 50 mg/kg, injetada na cavidade abdominal de 8 '
                                                  'camundongos, subiu a testosterona no sangue e no '
                                                  'testículo 6 horas depois, e em células de tumor de '
                                                  'testículo dobrou a produção. Não foi em rato nem injeção '
                                                  'no testículo. O PubMed devolve 0 ensaios de alho ou '
                                                  'S-alil-cisteína com testosterona em pessoas. O estudo '
                                                  'humano de "quase nada de dose" também existe: 0,25 mg por '
                                                  'dia de S-alil-cisteína baixou a pressão em 1,8 mmHg em '
                                                  'hipertensos que já tomavam remédio, num ensaio pago pelo '
                                                  'fabricante do extrato.',
                                        'alerta': 'O alho em suplemento pode reduzir o nível de remédios no '
                                                  'sangue: num estudo com 10 voluntários, a exposição ao '
                                                  'antirretroviral saquinavir caiu 51%. O alho tem efeito '
                                                  'sobre plaquetas e pressão, e quem usa anticoagulante ou '
                                                  'anti-hipertensivo deve falar com o médico antes de tomar '
                                                  'extrato concentrado. A S-alil-cisteína isolada não é '
                                                  'constituinte autorizado de suplemento alimentar no '
                                                  'Brasil. Em ratos, frações de alho dadas por longo tempo '
                                                  'baixaram a testosterona.'},
 'proprio_apneia_do_sono': {'nome': 'Ronco e apneia obstrutiva do sono (testosterona, CPAP e perda de peso)',
                            'categoria': 'primaria',
                            'aprovado': 'nao',
                            'tagline': 'Homens com apneia têm testosterona mais baixa, e o CPAP sozinho não '
                                       'a sobe nas meta-análises. Mas o CPAP trata a apneia; somar perda de '
                                       'peso subiu a testosterona em 77,6 ng/dL.',
                            'resumo': 'Apneia obstrutiva do sono é a garganta que fecha repetidas vezes '
                                      'durante o sono. Em São Paulo, 32,8% dos adultos examinados tinham a '
                                      'síndrome, e o excesso de peso foi o fator mais forte. Duas '
                                      'meta-análises acham testosterona mais baixa em homens com apneia, '
                                      'também depois de ajustar por idade e peso, sobretudo na apneia grave. '
                                      'O vídeo acerta num ponto: nas meta-análises, o CPAP sozinho não mudou '
                                      'a testosterona. Erra no resto: o CPAP não é oxigênio, trata a apneia, '
                                      'reduz sonolência e ronco e é recomendado pelas diretrizes. Num ensaio '
                                      'com 89 homens já em CPAP, somar 8 semanas de perda de peso e mudança '
                                      'de hábitos subiu a testosterona e tirou 45% deles do aparelho. A '
                                      'tirzepatida reduziu o índice de apneia em 20 a 24 eventos por hora a '
                                      'mais que o placebo e foi aprovada para isso nos EUA e no Brasil.',
                            'alerta': 'Ronco alto com pausas na respiração, engasgos à noite e sonolência de '
                                      'dia pedem exame do sono, não protocolo de suplemento. Apneia moderada '
                                      'ou grave sem tratamento é contraindicação para começar reposição de '
                                      'testosterona, e a testosterona injetada piorou a oxigenação noturna '
                                      'de homens obesos com apneia grave nas primeiras semanas. Não abandone '
                                      'o CPAP por conta própria: a perda de peso que tirou pacientes do '
                                      'aparelho foi feita com acompanhamento e novo exame. Tirzepatida é '
                                      'remédio de prescrição.'},
 'proprio_ashwagandha_ksm_66': {'nome': 'Ashwagandha (Withania somnifera; extrato KSM-66)',
                                'categoria': 'primaria',
                                'aprovado': 'nao',
                                'tagline': 'O "+17% de testosterona" não está no estudo de 57 homens citado '
                                           'nos vídeos; vem de 46 homens inférteis. No Brasil, a ANVISA '
                                           'manda apreender produtos irregulares com ashwagandha.',
                                'resumo': 'A ashwagandha é uma raiz da medicina ayurvédica vendida como '
                                          'redutora de cortisol e de estresse e como reforço de testosterona '
                                          'e força. Meta-análises acham queda de cortisol e alta pequena de '
                                          'testosterona em homens, mas a força tem evidência de certeza '
                                          'baixa, que depende de um estudo. Os números dos vídeos misturam '
                                          'estudos: o +17% de testosterona é de homens inférteis, o +14,7% é '
                                          'de outro extrato, e o −27,9% de cortisol é a queda desde o '
                                          'início, não contra o placebo. A maior parte dos estudos do KSM-66 '
                                          'foi feita com extrato fornecido ou financiado pelo fabricante. Há '
                                          'casos publicados de lesão no fígado, inclusive mortes em quem já '
                                          'tinha doença hepática.',
                                'alerta': 'A ashwagandha não é constituinte autorizado de suplemento no '
                                          'Brasil, e a ANVISA determinou em 2022 a apreensão e a proibição '
                                          'de venda e uso de todos os produtos irregulares que a contenham. '
                                          'Há casos publicados de lesão no fígado, em geral com icterícia e '
                                          'coceira semanas depois do início; em pessoas com doença hepática '
                                          'prévia, houve mortes. A agência francesa recomenda que gestantes, '
                                          'lactantes, menores de 18 anos, quem tem doença da tireoide, do '
                                          'fígado ou do coração e quem usa sedativos não consumam.'},
 'proprio_atp_oral': {'nome': 'ATP oral (ATP dissódico, PEAK ATP)',
                      'categoria': 'primaria',
                      'aprovado': 'nao',
                      'tagline': 'O "+147% de força" é a diferença entre os ganhos de 11 e 10 homens num '
                                 'estudo pago em parte pela fabricante e questionado por discrepâncias; '
                                 'tomado por boca, o ATP não aparece no sangue.',
                      'resumo': 'O ATP dissódico vendido como PEAK ATP é a molécula de energia das células, '
                                'em cápsula. Tomado por boca, mesmo protegido contra o ácido do estômago ou '
                                'posto direto no intestino, não aumentou o ATP no sangue em estudos de '
                                'Maastricht; só subiu o ácido úrico. O estudo de Tampa de 2013, com 21 '
                                'homens, achou força total +55,3 kg contra +22,4 kg; o "147%" é a diferença '
                                'entre esses ganhos. A fabricante pagou parte do estudo, e dois '
                                'pesquisadores publicaram em 2017 dúvidas sobre o placebo e a homogeneidade '
                                'dos dados. Outros ensaios, menores, acharam efeito pequeno ou nenhum.',
                      'alerta': 'O ATP não é constituinte autorizado de suplemento alimentar no Brasil. Os '
                                'estudos de efeito são quase todos ligados à fabricante. Em dose alta (5.000 '
                                'mg por dia), o ATP oral subiu o ácido úrico no sangue: quem tem gota ou '
                                'ácido úrico alto deve falar com o médico antes (inferência minha a partir '
                                'desse dado). Não há estudo de ATP oral em disfunção erétil.'},
 'proprio_atrazina_agua': {'nome': 'Atrazina na água (herbicida)',
                           'categoria': 'primaria',
                           'aprovado': 'nao',
                           'tagline': 'Os sapos que "viraram fêmeas" eram 4 de 40, a 2,5 ppb; na água '
                                      'tratada de 22 capitais, a atrazina medida ficou entre 2 e 6 '
                                      'nanogramas por litro.',
                           'resumo': 'A atrazina é um herbicida de milho e cana, o 7º agrotóxico mais '
                                     'vendido no Brasil em 2024, e aparece em rio e em água tratada. Em '
                                     'sapos, o laboratório de Tyrone Hayes viu machos virarem fêmeas '
                                     'funcionais (4 de 40, a 2,5 ppb); uma repetição exigida pela agência '
                                     'americana, paga pela fabricante, não viu efeito. Em homens, não achei '
                                     'estudo de testosterona; há um estudo de sêmen com 86 homens e '
                                     'associações fracas com peso ao nascer e menarca. O limite brasileiro '
                                     'na água potável é 2 µg/L. O tratamento convencional não remove a '
                                     'atrazina; carvão ativado remove.',
                           'alerta': 'Esta página trata de exposição, não de suplemento. Filtrar a água não '
                                     'é tratamento de testosterona baixa, e nenhum estudo mediu se filtrar '
                                     'muda a testosterona. Quem tem poço perto de lavoura de milho ou cana e '
                                     'gestantes são os grupos com mais motivo para saber o que há na água. '
                                     'Queixa de libido, ereção ou fertilidade pede avaliação médica, não só '
                                     'filtro.'},
 'proprio_azeite_extravirgem': {'nome': 'Azeite de oliva extravirgem (oleuropeína)',
                                'categoria': 'primaria',
                                'aprovado': 'nao',
                                'tagline': 'O "+17,4% de testosterona" vem de um estudo marroquino de 3 '
                                           'semanas sem grupo controle, que não mediu oleuropeína; e acidez '
                                           'de 0,2% não separa extravirgem de refinado.',
                                'resumo': 'O estudo citado nos vídeos existe: 60 homens marroquinos de 23 a '
                                          '40 anos trocaram manteiga por óleo de argan ou por azeite '
                                          'extravirgem durante 3 semanas, e a testosterona subiu 17,4% no '
                                          'grupo do azeite e 19,9% no do argan. Não houve grupo controle '
                                          'paralelo, o resumo não informa a quantidade de óleo, e ninguém '
                                          'mediu oleuropeína. É o único ensaio em humanos de azeite e '
                                          'testosterona que o PubMed devolve. O efeito da oleuropeína no '
                                          'testículo foi visto em ratos. Das três "regras" para escolher '
                                          'azeite, o vidro escuro tem apoio; a acidez de 0,2% não é critério '
                                          'legal, e o refinado tem acidez máxima ainda menor.',
                                'alerta': 'Azeite é alimento, e esta página não trata de risco do azeite '
                                          'comum. O alerta é sobre a troca de alvo: o único estudo humano '
                                          'não mediu oleuropeína, e o suplemento de oleuropeína vendido no '
                                          'Brasil vem de extrato de folha de oliveira, não de azeite. Esse '
                                          'suplemento é autorizado com faixa estreita, de 150 a 161 mg por '
                                          'dia para adultos, e o rótulo tem de dizer que gestantes, '
                                          'lactantes e crianças não devem consumir. Nenhum estudo mediu '
                                          'testosterona com ele.'},
 'proprio_banho_frio_lh': {'nome': 'Banho frio e imersão em água fria (LH e testosterona)',
                           'categoria': 'primaria',
                           'aprovado': 'nao',
                           'tagline': 'Nos estudos que mediram, o frio não subiu o LH nem a testosterona: '
                                      'ficaram iguais ou caíram. O "14 °C por 11 minutos" junta dois estudos '
                                      'que não mediram nenhum dos dois.',
                           'resumo': 'Banho frio e imersão em água fria aparecem em vídeos como o jeito de '
                                     '"religar" o sinal da hipófise (o LH) que manda o testículo fabricar '
                                     'testosterona. Os estudos em homens que mediram LH ou testosterona '
                                     'durante ou depois do frio não acharam subida: 2 horas a 10 °C não '
                                     'mudaram nenhum dos dois, nadar no inverno não mudou o LH, e uma '
                                     'imersão abaixo de 4 °C baixou a testosterona de 21,22 para 17,27 '
                                     'nmol/L. Depois do treino de força, a água fria atenuou a subida da '
                                     'testosterona e, em 12 semanas, o ganho de força e de massa. O "38,7%" '
                                     'vem de um estudo de 2006 que não mediu LH. O que o frio faz, medido, é '
                                     'outra coisa: solta noradrenalina e, num ensaio com 3.018 pessoas, o '
                                     'banho frio diário reduziu faltas ao trabalho.',
                           'alerta': 'Esta página trata de hábito, não de suplemento. Água fria provoca a '
                                     'resposta de choque ao frio: respiração ofegante involuntária, coração '
                                     'acelerado e pressão alta nos primeiros minutos. Ela aumenta o risco de '
                                     'afogamento em água aberta e pode desencadear arritmia em quem tem '
                                     'predisposição. Quem tem doença do coração, arritmia ou pressão alta '
                                     'deve conversar com o médico antes. Testosterona baixa com sintomas '
                                     'pede exame e investigação da causa, não banho frio.'},
 'proprio_berberina': {'nome': 'Berberina (cloridrato de berberina)',
                       'categoria': 'primaria',
                       'aprovado': 'nao',
                       'tagline': 'O estudo de 2008 que "empatou com a metformina" tinha 36 pacientes por 3 '
                                  'meses; nenhum ensaio comparou berberina com semaglutida, e ela inibe '
                                  'enzimas que metabolizam remédios.',
                       'resumo': 'A berberina é um alcaloide de plantas como a Coptis, usado na China contra '
                                 'diarreia e diabetes. Em diabetes tipo 2, meta-análises de ensaios acham '
                                 'queda modesta da glicose e da hemoglobina glicada contra placebo. O estudo '
                                 'de 2008 citado nos vídeos existe: 36 pacientes recém-diagnosticados, 3 '
                                 'meses, efeito parecido com o da metformina, num piloto. Nenhum ensaio a '
                                 'comparou com semaglutida. Em 2 semanas, ela inibiu em pessoas três enzimas '
                                 'que metabolizam remédios e elevou a ciclosporina de transplantados. No '
                                 'Brasil, não consta da lista de constituintes de suplemento.',
                       'alerta': 'Quem tem diabetes não deve trocar nem somar remédio por conta própria: '
                                 'berberina com antidiabéticos baixa mais a glicose, e em pessoas ela inibiu '
                                 'as enzimas CYP3A4, CYP2D6 e CYP2C9, que metabolizam muitos remédios, e '
                                 'elevou a ciclosporina de transplantados. A berberina desloca a bilirrubina '
                                 'da albumina, e o autor desse estudo recomenda evitá-la em gestantes e '
                                 'recém-nascidos com icterícia. Diarreia e prisão de ventre são comuns.'},
 'proprio_beta_alanina': {'nome': 'Beta-alanina (carnosina muscular)',
                          'categoria': 'primaria',
                          'aprovado': 'nao',
                          'tagline': 'A beta-alanina funciona de verdade, mas o ganho médio é de cerca de '
                                     '3%, não 80%; e os 3 a 6 g por dia dos vídeos passam do teto de 2 g da '
                                     'ANVISA.',
                          'resumo': 'A beta-alanina é um aminoácido que o músculo usa para fabricar '
                                    'carnosina, um tampão contra a acidez do esforço intenso. Isso está bem '
                                    'estudado: com 4 a 6 g por dia por 4 semanas, a carnosina sobe até 64%, '
                                    'e o ganho de desempenho aparece em esforços de 30 segundos a 10 '
                                    'minutos. O tamanho do ganho é pequeno: mediana de 2,85% numa '
                                    'meta-análise e de 0,2% a 3% segundo o Comitê Olímpico Internacional. O '
                                    'formigamento é real, inofensivo e não prova que a carnosina subiu. No '
                                    'Brasil, a beta-alanina é constituinte autorizado de suplemento, com '
                                    'máximo de 2 g por dia em doses de até 300 mg.',
                          'alerta': 'No Brasil, o rótulo de suplemento com beta-alanina tem de trazer a '
                                    'advertência: "Quantidade diária máxima de 2 g com doses divididas de, '
                                    'no máximo, 300 mg, com intervalo de duas horas entre as doses." Os 3 a '
                                    '6 g por dia que circulam nos vídeos passam desse teto. O único efeito '
                                    'colateral consistente nos estudos é o formigamento na pele, que cresce '
                                    'com a dose. Não há estudo publicado da combinação com tadalafila.'},
 'proprio_betaina': {'nome': 'Betaína (betaína anidra, trimetilglicina)',
                     'categoria': 'primaria',
                     'aprovado': 'nao',
                     'tagline': 'O estudo de 2013 existe e tem os números do vídeo, mas foi pago pela '
                                'fornecedora da betaína; no Brasil, a betaína não está na lista de '
                                'constituintes de suplemento.',
                     'resumo': 'A betaína é um derivado da glicina que o corpo usa como osmólito e doador de '
                               'metil. O estudo de 2013 citado nos vídeos existe: 23 homens treinados, 2,5 g '
                               'por dia, 6 semanas, braço 4,6 cm² maior pela fita e pela dobra cutânea, sem '
                               'ganho de força máxima, financiado pela empresa que forneceu a betaína. A '
                               'meta-análise de 2024 acha ganho pequeno de força, sobretudo nas pernas; a de '
                               '2022 não acha efeito na composição corporal. Dois estudos curtos viram a '
                               'testosterona subir. A betaína baixa a homocisteína, mas em doses de 4 g ou '
                               'mais sobe o colesterol. No Brasil, não é constituinte autorizado de '
                               'suplemento alimentar.',
                     'alerta': 'A betaína não consta da lista de constituintes autorizados em suplemento '
                               'alimentar no Brasil (IN 28/2018, consolidada até setembro de 2026). Em doses '
                               'de 4 g por dia ou mais, as meta-análises acharam alta do colesterol total e '
                               'do LDL. Nos Estados Unidos, a betaína anidra é medicamento para '
                               'homocistinúria, e a bula alerta para alta da metionina e edema cerebral em '
                               'pacientes com deficiência de CBS. Náusea e desconforto gastrintestinal são '
                               'os efeitos mais relatados.'},
 'proprio_beterraba_nitrato': {'nome': 'Beterraba em pó e nitrato dietético',
                               'categoria': 'primaria',
                               'aprovado': 'nao',
                               'tagline': 'O "+33% de ereção noturna" não aparece em nenhum estudo publicado '
                                          'que localizei; no treino, o nitrato da beterraba tem efeito real, '
                                          'mas pequeno.',
                               'resumo': 'A beterraba é rica em nitrato, que bactérias da boca transformam '
                                         'em nitrito e o corpo, depois, em óxido nítrico. Esse caminho está '
                                         'bem descrito, e o enxaguante bucal o atrapalha. No treino, uma '
                                         'revisão de 20 meta-análises achou ganhos pequenos em resistência '
                                         'muscular e tempo até a exaustão, e nada na maioria dos outros '
                                         'desfechos. Na pressão, a queda média é de alguns mmHg. O estudo de '
                                         'ereção noturna com "10 homens e +33%" não foi localizado, e os '
                                         'dois ensaios registrados sobre nitrato e ereção não têm resultado. '
                                         'O teor de nitrato varia até 50 vezes entre produtos.',
                               'alerta': 'O nitrato da beterraba baixa a pressão alguns mmHg; quem usa '
                                         'remédio de pressão, nitrato de farmácia ou tadalafila pode somar '
                                         'efeitos, e isso é inferência minha, sem estudo que eu tenha achado '
                                         'sobre a soma. Revisões registram que o suco concentrado pode '
                                         'passar da ingestão diária aceitável de nitrato e que nitrato e '
                                         'nitrito se associam a risco de câncer gastrointestinal e a '
                                         'meta-hemoglobinemia em bebês. No Brasil, o nitrato não consta da '
                                         'lista de constituintes autorizados em suplemento alimentar.'},
 'proprio_bicarbonato_de_sodio': {'nome': 'Bicarbonato de sódio (como suplemento de treino)',
                                  'categoria': 'primaria',
                                  'aprovado': 'nao',
                                  'tagline': 'O "+27% até a exaustão" é de uma meta-análise de 1993; as '
                                             'análises mais novas acham cerca de 2%, e os "7 g" que circulam '
                                             'ficam abaixo da dose mínima eficaz para quase todo adulto.',
                                  'resumo': 'O bicarbonato de sódio é um tampão do sangue com efeito real em '
                                            'esforços intensos de 30 segundos a 12 minutos, segundo o '
                                            'posicionamento de 2021 da International Society of Sports '
                                            'Nutrition. A dose estudada é por peso: 0,2 a 0,5 g por quilo, '
                                            'com 0,3 g/kg como a mais eficaz. O "+27% de tempo até a '
                                            'exaustão" existe, numa meta-análise de 1993; uma de 2011 achou '
                                            '1,7% de potência média num sprint de um minuto. Melhora a '
                                            'resistência muscular, não a força máxima. A dose eficaz traz '
                                            'mais sódio do que os 2.300 mg diários das referências '
                                            'americanas e, num estudo, causou diarreia em 10 de 11 pessoas. '
                                            'No Brasil, bicarbonato de sódio é medicamento antiácido e só '
                                            'entra em suplemento como fonte de sódio em bebida eletrolítica.',
                                  'alerta': 'Uma dose de 0,3 g por quilo tem cerca de 27% de sódio e passa '
                                            'sozinha dos 2.300 mg diários de sódio acima dos quais as '
                                            'referências americanas recomendam reduzir; num estudo, 10 de 11 '
                                            'pessoas tiveram diarreia. Há relatos raros de ruptura do '
                                            'estômago após bicarbonato tomado com o estômago cheio. Quem tem '
                                            'pressão alta, doença renal, insuficiência cardíaca ou dieta com '
                                            'restrição de sódio não deve usar sem médico. No Brasil, o '
                                            'bicarbonato de sódio não é autorizado como suplemento de treino '
                                            'em cápsula ou pó.'},
 'proprio_body_balance_peptideos': {'nome': 'Peptídeos de colágeno para músculo (Body Balance)',
                                    'categoria': 'primaria',
                                    'aprovado': 'nao',
                                    'tagline': 'O estudo de Freiburg de 2015 existe, mas a gordura caiu 5,4 '
                                               'kg contra 3,5 kg no placebo, não o triplo; e só em 2025 o '
                                               'artigo declarou que um autor tem pedido de patente do '
                                               'ingrediente.',
                                    'resumo': 'Body Balance é a marca de um hidrolisado de colágeno de cerca '
                                              'de 3 kDa de uma fabricante alemã, testado com 15 g por dia '
                                              'junto com musculação. Em ensaios financiados total ou '
                                              'parcialmente pela fabricante ou por um instituto ligado a um '
                                              'coautor com patente, a massa livre de gordura subiu mais que '
                                              'com placebo sem proteína. Mas o colágeno tem pouca leucina, e '
                                              'nos quatro estudos que mediram a síntese de proteína muscular '
                                              'diretamente ele não a aumentou; contra whey, deu menos '
                                              'músculo. A gordura caiu 5,4 kg contra 3,5 kg, não o triplo. '
                                              'Nenhum estudo mediu colágeno "vascular", e a ANVISA autoriza '
                                              'alegação só para pele e articulações.',
                                    'alerta': 'A ANVISA autoriza peptídeos de colágeno em suplemento com '
                                              'alegação para pele e articulações, nunca para músculo, '
                                              'gordura ou sarcopenia, e exige no rótulo do de 3 kDa a '
                                              'advertência de que não deve ser consumido por gestantes, '
                                              'lactantes e crianças. Os estudos de músculo positivos são '
                                              'quase todos do mesmo grupo e pagos pela fabricante ou por um '
                                              'instituto de pesquisa em que trabalha um coautor com '
                                              'patentes. Quem tem sarcopenia precisa de avaliação médica, '
                                              'não de um suplemento específico.'},
 'proprio_boro_shbg_testosterona_livre': {'nome': 'Boro (SHBG e testosterona livre)',
                                          'categoria': 'primaria',
                                          'aprovado': 'nao',
                                          'tagline': 'O "+28% de testosterona livre" é atribuído a um estudo '
                                                     'de 8 homens sem grupo placebo; no Brasil, 10 mg por '
                                                     'dia passa do máximo permitido em suplemento.',
                                          'resumo': 'O boro é um oligoelemento que a autoridade europeia '
                                                    'classifica como não essencial. A alegação de que ele '
                                                    'derruba a SHBG e sobe a testosterona livre se apoia num '
                                                    'estudo iraniano de 2011 com 8 homens, 10 mg por dia por '
                                                    'uma semana e sem grupo placebo paralelo. Os dois '
                                                    'artigos com placebo em homens, com 2,5 mg por dia por 7 '
                                                    'semanas, não acharam efeito na testosterona. Um estudo '
                                                    'de 1997 com 10 mg por dia por 4 semanas viu o estradiol '
                                                    'subir, não cair. No Brasil, o máximo em suplemento para '
                                                    'adultos é 8,866 mg por dia, e boro em suplemento não é '
                                                    'autorizado para gestantes, lactantes, crianças e '
                                                    'adolescentes.',
                                          'alerta': 'Os 10 mg por dia que circulam passam do máximo que a '
                                                    'ANVISA permite por dia em suplemento para adultos '
                                                    '(8,866 mg) e igualam o limite superior de ingestão '
                                                    'total fixado na Europa, que soma comida, água e '
                                                    'suplemento. Na União Europeia, o ácido bórico e os '
                                                    'boratos são classificados como tóxicos à reprodução, '
                                                    'com base em estudos em animais. No Brasil, o rótulo de '
                                                    'suplemento com boro tem de dizer que gestantes, '
                                                    'lactantes e crianças não devem consumir.'},
 'proprio_bpa_ftalatos_plasticos': {'nome': 'BPA, ftalatos e microplástico (exposição a plástico)',
                                    'categoria': 'primaria',
                                    'aprovado': 'nao',
                                    'tagline': 'Em homens, mais BPA na urina andou junto com testosterona '
                                               'mais alta, não mais baixa; com ftalatos há associação. Três '
                                               'dias sem comida embalada cortaram o BPA da urina em 66%.',
                                    'resumo': 'BPA, ftalatos e microplástico estão no corpo de quase todo '
                                              'mundo: o BPA apareceu na urina de 92,6% dos americanos '
                                              'testados em 2003–2004. A queda da testosterona e da contagem '
                                              'de espermatozoides ao longo das décadas é real, mas a causa '
                                              'não foi estabelecida. Em homens adultos, dois estudos acharam '
                                              'testosterona mais alta, não mais baixa, em quem tinha mais '
                                              'BPA; para os ftalatos DEHP e DBP, uma revisão sistemática '
                                              'achou evidência robusta de associação com desfechos '
                                              'reprodutivos. Várias alegações que circulam não existem nas '
                                              'fontes citadas. O que reduz a exposição foi medido: trocar '
                                              'comida enlatada e embalada por comida fresca derrubou o BPA '
                                              'da urina em dias.',
                                    'alerta': 'Esta página trata de exposição, não de suplemento. Reduzir '
                                              'plástico não é tratamento de testosterona baixa, disfunção '
                                              'erétil ou infertilidade, e nenhum ensaio que localizei mediu '
                                              'se reduzir a exposição muda a testosterona. Gestantes e '
                                              'crianças pequenas são o grupo que a regulação mais protege. '
                                              'Queixa de libido, ereção ou fertilidade pede avaliação '
                                              'médica, não só troca de pote.'},
 'proprio_bulbine_natalensis': {'nome': 'Bulbine natalensis (Bulbine latifolia)',
                                'categoria': 'primaria',
                                'aprovado': 'nao',
                                'tagline': 'O "+346% de testosterona" vem de ratos, e as mesmas doses que '
                                           'subiram o hormônio alteraram fígado e rim. Em homens, não há um '
                                           'único estudo de eficácia publicado.',
                                'resumo': 'A Bulbine natalensis é uma planta sul-africana vendida como '
                                          'reforço de testosterona. Toda a evidência de efeito vem de ratos, '
                                          'num grupo de pesquisa da África do Sul: 25 e 50 mg/kg por 7 a 14 '
                                          'dias subiram a testosterona, e 100 mg/kg a derrubou. As mesmas '
                                          'doses elevaram enzimas do fígado, alteraram a arquitetura do '
                                          'fígado e do rim, baixaram o HDL e pioraram o índice aterogênico. '
                                          'Em humanos, o PubMed não tem nenhum ensaio; o único dado que '
                                          'localizei é um resumo de congresso de 28 dias, sobre segurança, '
                                          'apoiado por empresa do setor. A planta não é constituinte '
                                          'autorizado de suplemento no Brasil.',
                                'alerta': 'A Bulbine natalensis não é constituinte autorizado de suplemento '
                                          'alimentar no Brasil e não tem medicamento registrado na ANVISA. '
                                          'Em ratos, as doses que aumentaram a testosterona também alteraram '
                                          'enzimas e tecido do fígado e do rim e pioraram o perfil de '
                                          'colesterol. Em laboratório, extratos da planta mexeram em enzimas '
                                          'que metabolizam remédios. Não existe "dose segura" estabelecida '
                                          'em humanos.'},
 'proprio_butea_superba': {'nome': 'Butea superba (kwao krua vermelho)',
                           'categoria': 'primaria',
                           'aprovado': 'nao',
                           'tagline': 'O único ensaio publicado perdeu todo o grupo placebo em três semanas, '
                                      'e o único estudo contra o sildenafil achou o remédio misturado no '
                                      'lote "natural".',
                           'resumo': 'A Butea superba é uma trepadeira tailandesa cuja raiz tuberosa é '
                                     'vendida como estimulante sexual masculino. O PubMed tem 34 artigos com '
                                     'o nome da planta; só um é ensaio clínico, e o ClinicalTrials.gov não '
                                     'tem nenhum registro. Nesse ensaio de 2003, 39 homens foram sorteados, '
                                     'mas os 14 do grupo placebo abandonaram o estudo e só 17 do grupo da '
                                     'planta terminaram: sobrou uma comparação de antes e depois, sem '
                                     'controle. Em 2010, um estudo mexicano viu a planta empatar com o '
                                     'sildenafil e depois descobriu que o primeiro lote tinha um inibidor de '
                                     'fosfodiesterase-5 misturado; o lote limpo não teve efeito. Nenhum '
                                     'estudo testou a planta contra a ADMA nem junto com o extrato de '
                                     'pinheiro.',
                           'alerta': 'Há um relato de caso de um homem de 35 anos com di-hidrotestosterona '
                                     'acima da faixa de referência depois de algumas semanas de cápsulas da '
                                     'planta, que voltou ao normal uma semana após parar. Em ratos, doses '
                                     'altas por 90 dias baixaram a testosterona e mexeram em enzimas do '
                                     'fígado, e doses muito altas induziram micronúcleos, um marcador de '
                                     'dano ao material genético. Um lote vendido como produto natural tinha '
                                     'remédio de prescrição misturado. A planta não é autorizada em '
                                     'suplemento no Brasil.'},
 'proprio_cafeina': {'nome': 'Cafeína (anidra pré-treino e energético diário)',
                     'categoria': 'primaria',
                     'aprovado': 'parcial',
                     'tagline': 'O "+16% de força" é a velocidade da barra numa só carga, em 14 homens; a '
                                'força máxima subiu de 4% a 7%. No Brasil, suplemento pode ter até 200 mg '
                                'por dose.',
                     'resumo': 'A cafeína é o suplemento de desempenho com mais estudo: melhora força e '
                               'potência em pouco (meta-análise com efeito de 0,20) e resistência aeróbia de '
                               'forma mais consistente, com 3 a 6 mg por quilo uma hora antes. O estudo '
                               'citado nos vídeos existe: 14 homens, 4 mg/kg, força máxima +4,1% no supino e '
                               '+6,9% no agachamento; os 16% são a velocidade de pico numa carga. Não há '
                               'diferença de molécula entre "anidra" e a do café. Do energético diário, '
                               'metade do alerta se sustenta: perda de sono, tolerância parcial em duas a '
                               'três semanas e abstinência de 2 a 9 dias estão documentadas; o "paladar '
                               'viciado em 16 dias" e o "rim trabalhando dobrado" não.',
                     'alerta': 'No Brasil, suplemento de cafeína para adultos pode ter no máximo 200 mg por '
                               'dia, ou 400 mg por dia só para atletas com dose individual de até 200 mg, e '
                               'o rótulo deve dizer que gestantes, lactantes e crianças não devem consumir. '
                               'Para um homem de 80 kg, 3 a 6 mg/kg dão 240 a 480 mg (conta minha), acima da '
                               'dose única do suplemento. Com 9 mg/kg, os efeitos colaterais apareceram em '
                               '15% a 62% dos participantes de um ensaio. Cafeína perto da hora de dormir '
                               'reduz o sono total, e parar de repente dá dor de cabeça e cansaço por até 9 '
                               'dias.'},
 'proprio_calor_testicular': {'nome': 'Calor nos testículos (cueca de poliéster, banco aquecido e notebook '
                                      'no colo)',
                              'categoria': 'primaria',
                              'aprovado': 'nao',
                              'tagline': 'O estudo dos 14 homens de poliéster existe, mas usou uma funda '
                                         'anticoncepcional, foi reversível e não mexeu nos hormônios; o '
                                         'calor derruba espermatozoide, não testosterona.',
                              'resumo': 'O testículo trabalha alguns graus abaixo do resto do corpo, e '
                                        'esquentá-lo reduz a produção de espermatozoides. Isso está bem '
                                        'medido. O que não aparece nos estudos é a queda de testosterona: na '
                                        'sauna, no banho quente, na funda de poliéster e na temperatura do '
                                        'dia a dia, os hormônios não mudaram ou não se associaram ao calor. '
                                        'O banco aquecido (+0,6 °C) e o notebook no colo (+2,8 °C) têm os '
                                        'números nos artigos; a soma de "quase 5 °C" não. O estudo de 1992 '
                                        'com 14 homens usou uma funda de poliéster como anticoncepcional, e '
                                        'a produção voltou depois que ela foi retirada. Em todos os '
                                        'experimentos, o efeito do calor foi reversível.',
                              'alerta': 'Esta página trata de exposição, não de suplemento. O calor no '
                                        'escroto é fator conhecido para a produção de espermatozoides, não '
                                        'para a testosterona: testosterona baixa ou disfunção erétil pedem '
                                        'investigação médica, e trocar de cueca não substitui isso. Febre, '
                                        'varicocele e trabalho em ambiente quente pesam mais que roupa '
                                        'íntima. Casal que não engravida depois de um ano de tentativa '
                                        'precisa de avaliação dos dois.'},
 'proprio_castanha_do_para_selenio': {'nome': 'Castanha-do-pará e selênio',
                                      'categoria': 'primaria',
                                      'aprovado': 'nao',
                                      'tagline': 'Duas castanhas renderam 53 µg de selênio num ensaio, mas o '
                                                 'teor vai de 2,07 a 68,15 mg por kg conforme a região do '
                                                 'Brasil.',
                                      'resumo': 'A castanha-do-pará é a comida mais rica em selênio, e o '
                                                'selênio faz parte das enzimas que convertem o hormônio T4 '
                                                'da tireoide em T3. O ensaio da Nova Zelândia citado nos '
                                                'vídeos existe: 59 adultos, 2 castanhas por dia por 12 '
                                                'semanas, selênio no sangue igual ao do comprimido de 100 '
                                                'µg. Mas em pessoas com tireoide normal, três ensaios com '
                                                '100 a 300 µg por dia não aumentaram o T3, e dois ensaios em '
                                                'homens não mudaram a testosterona. O ensaio que mostrou '
                                                'selênio subindo a testosterona e melhorando o sêmen recebeu '
                                                'nota de preocupação da revista em 2023. O teor na castanha '
                                                'varia de 2,07 a 68,15 mg por kg conforme a região.',
                                      'alerta': 'O selênio tem margem estreita. A autoridade europeia fixou '
                                                'em 2023 o limite superior para adultos em 255 µg por dia e '
                                                'cita quem come castanha-do-pará com regularidade entre os '
                                                'que podem passar dele; duas castanhas de lote muito rico '
                                                'podem chegar perto de 400 µg (conta minha a partir do teor '
                                                'publicado). Excesso causa queda de cabelo, unhas frágeis, '
                                                'diarreia e cansaço. Em ensaios com 200 µg por dia de '
                                                'selênio, houve mais diabetes tipo 2 num deles. No Brasil, '
                                                'suplemento pode ter no máximo 319,75 µg de selênio por dia '
                                                'para adultos.'},
 'proprio_cerveja_lupulo_fitoestrogeno': {'nome': 'Lúpulo, 8-prenilnaringenina e cerveja sem álcool '
                                                  '(fitoestrógeno)',
                                          'categoria': 'primaria',
                                          'aprovado': 'nao',
                                          'tagline': 'O 8-PN do lúpulo é potente no tubo de ensaio, mas a '
                                                     'maioria das cervejas nem tem quantidade detectável; no '
                                                     'único ensaio comparado, a testosterona caiu com a '
                                                     'cerveja com álcool, não com a sem álcool.',
                                          'resumo': 'A 8-prenilnaringenina (8-PN) é um fitoestrógeno do '
                                                    'lúpulo, e é dos mais potentes já medidos em '
                                                    'laboratório. Na cerveja, a quantidade é de microgramas '
                                                    'por litro, e a maioria das cervejas analisadas em 1999 '
                                                    'não tinha nível detectável. O único efeito hormonal '
                                                    'medido em gente veio de 750 mg de 8-PN puro, numa dose '
                                                    'só, em mulheres na pós-menopausa. Não achei estudo de '
                                                    'cerveja sem álcool com testosterona em homens. No '
                                                    'ensaio que comparou cerveja com e sem álcool, a '
                                                    'testosterona caiu 6,8% no período com álcool. A cerveja '
                                                    'estimula a prolactina, mas o responsável apontado é a '
                                                    'cevada, não o lúpulo.',
                                          'alerta': 'Esta página trata de bebida, não de suplemento. Trocar '
                                                    'a cerveja comum pela sem álcool tira o álcool, que é o '
                                                    'componente com efeito medido sobre a testosterona. A '
                                                    'cerveja sem álcool pode ter até 0,5% de álcool no '
                                                    'Brasil, o que importa para quem não pode beber nada, '
                                                    'como gestantes, pessoas em tratamento de dependência ou '
                                                    'quem toma remédio que interage com álcool. Extrato de '
                                                    'lúpulo concentrado é outra coisa: foi estudado em '
                                                    'mulheres, e a dose que mexeu em hormônio é muito maior '
                                                    'do que a contida numa cerveja.'},
 'proprio_cha_verde_com_mucuna': {'nome': 'Chá verde (adjuvante da mucuna)',
                                  'categoria': 'primaria',
                                  'aprovado': 'nao',
                                  'tagline': 'O chá verde entra no protocolo da mucuna "para o fluxo", sem '
                                             'dose; o que existe são catequinas que melhoram pouco a '
                                             'dilatação das artérias, e extrato concentrado que mexe no '
                                             'fígado.',
                                  'resumo': 'Num vídeo sobre mucuna, o chá verde aparece como adjuvante '
                                            '"para o fluxo", sem dose nem explicação. Não há estudo de chá '
                                            'verde com mucuna em pessoas. As catequinas do chá melhoraram a '
                                            'dilatação das artérias numa meta-análise, com efeito pequeno. '
                                            'Sobre testosterona em homens, a evidência é quase nula: um '
                                            'estudo nigeriano sem placebo achou alta, um estudo espanhol não '
                                            'achou mudança no perfil de esteroides, e em células de rato o '
                                            'principal composto do chá inibiu a produção de testosterona. O '
                                            'risco real está no extrato concentrado: a partir de 800 mg de '
                                            'EGCG por dia, as enzimas do fígado sobem.',
                                  'alerta': 'O chá como bebida é considerado seguro nas quantidades '
                                            'habituais; o risco está no extrato concentrado. Num ensaio com '
                                            'mais de mil mulheres, o extrato de chá verde multiplicou por 7 '
                                            'a chance de alteração das enzimas do fígado, e a autoridade '
                                            'europeia concluiu que 800 mg ou mais de EGCG por dia, em '
                                            'suplemento, sobem as transaminases. No Brasil, o extrato de chá '
                                            'verde não é constituinte autorizado de suplemento. Quem tem '
                                            'doença do fígado não deve tomar extrato de chá verde.'},
 'proprio_cipionato_de_testosterona_trt': {'nome': 'Cipionato de testosterona (Deposteron) e reposição '
                                                   'hormonal (TRT)',
                                           'categoria': 'primaria',
                                           'aprovado': 'parcial',
                                           'tagline': 'A cronologia de 30 dias que circula não bate com os '
                                                      'estudos: o interesse sexual começa em 3 semanas e a '
                                                      'massa magra muda em 12 a 16, e no Brasil é vedado '
                                                      'prescrever testosterona para estética.',
                                           'resumo': 'O cipionato de testosterona é uma forma injetável de '
                                                     'testosterona, registrada no Brasil e nos Estados '
                                                     'Unidos para tratar hipogonadismo comprovado. Os vídeos '
                                                     'descrevem 30 dias de uso para músculo com uma '
                                                     'cronologia dia a dia. Os estudos mostram outro '
                                                     'relógio: efeito no desejo sexual a partir de 3 '
                                                     'semanas, mudança de massa magra e força em 12 a 16 '
                                                     'semanas, estabilização em 6 a 12 meses. Doses acima do '
                                                     'fisiológico aumentam músculo, e também derrubam o HDL '
                                                     'e sobem a hemoglobina conforme a dose. Em 100 usuários '
                                                     'de academia acompanhados por um ano, todos tiveram '
                                                     'algum efeito adverso. Em 2023, o Conselho Federal de '
                                                     'Medicina vedou a prescrição de anabolizantes para '
                                                     'estética e desempenho.',
                                           'alerta': 'Testosterona é anabolizante da lista C5 da Portaria '
                                                     '344/98 e só sai com receita de controle especial. O '
                                                     'Conselho Federal de Medicina veda prescrevê-la sem '
                                                     'deficiência comprovada ou com finalidade estética ou '
                                                     'esportiva. A testosterona de fora suprime a produção '
                                                     'de espermatozoides: num estudo da OMS, 65% dos homens '
                                                     'ficaram sem espermatozoides em 6 meses. A bula '
                                                     'contraindica o uso em câncer de mama ou próstata e em '
                                                     'doença grave do coração, fígado ou rim, e manda vigiar '
                                                     'hematócrito e pressão.'},
 'proprio_cistanche': {'nome': 'Cistanche (Cistanche deserticola e Cistanche tubulosa)',
                       'categoria': 'primaria',
                       'aprovado': 'nao',
                       'tagline': 'O estudo dos "636 para 773 ng/dL" existe, mas os dois números são placebo '
                                  'e cistanche no fim do teste, não antes e depois; o "+44,6%" não está '
                                  'nele.',
                       'resumo': 'A cistanche é uma planta parasita do deserto usada na medicina chinesa. '
                                 'Para testosterona e força, há um único ensaio em homens: 48 voluntários de '
                                 'Wuhan, 8 semanas de musculação, extrato de C. deserticola contra placebo, '
                                 'patrocinado pela empresa que forneceu o extrato. Ele relata testosterona e '
                                 'agachamento maiores que no placebo, mas os 636 e 773 ng/dL que circulam '
                                 'são a comparação entre os grupos ao fim do estudo, e o "+44,6%" não '
                                 'aparece no artigo. Enzimas do testículo, espermatozoides e bisfenol são '
                                 'dados de rato. Em 2021, a agência europeia concluiu que a segurança de um '
                                 'extrato de C. tubulosa não está estabelecida.',
                       'alerta': 'A cistanche não consta da lista de constituintes autorizados para '
                                 'suplemento alimentar no Brasil (IN 28/2018, consolidada até setembro de '
                                 '2026). Em 2021, a agência europeia de segurança alimentar (EFSA) concluiu '
                                 'que a segurança de um extrato de C. tubulosa não está estabelecida, depois '
                                 'de examinar 12 eventos adversos relacionados ao extrato em 1.076 pacientes '
                                 'com demência, dois deles graves (hemorragia cerebral e epilepsia). Em '
                                 'camundongos, um estudo coreano viu a erva baixar espermatozoides e '
                                 'testosterona. Gestantes e lactantes ficaram fora até do pedido de '
                                 'autorização europeu.'},
 'proprio_cjc_1295_ipamorelina': {'nome': 'CJC-1295 + ipamorelina (o "GH sem colateral")',
                                  'categoria': 'primaria',
                                  'aprovado': 'nao',
                                  'tagline': 'Nenhum estudo publicado testou CJC-1295 e ipamorelina juntos '
                                             'em pessoas; o "+1000% de GH" vem de um ensaio de 2006 com o '
                                             'CJC-1295 sozinho, e a ANVISA diz que nenhum dos dois tem '
                                             'registro.',
                                  'resumo': 'CJC-1295 e ipamorelina são dois peptídeos injetáveis que pedem '
                                            'à hipófise que solte hormônio do crescimento, por receptores '
                                            'diferentes. Nenhum dos dois virou remédio em lugar nenhum. No '
                                            'PubMed, a busca pelos dois juntos devolve 11 artigos, e nenhum '
                                            'é estudo em pessoas: são revisões e um método antidoping. O '
                                            '"aumento de até 10 vezes" existe, mas foi medido em 2006 com o '
                                            'CJC-1295 sozinho, na versão de ação longa, em voluntários '
                                            'saudáveis, e no estudo seguinte o tamanho dos pulsos de GH não '
                                            'mudou. Massa muscular, gordura, tendão, sono e recuperação '
                                            'nunca foram medidos em humanos com esses peptídeos. A ANVISA '
                                            'informou em julho de 2026 que não estão registrados, e a '
                                            'Agência Mundial Antidoping proíbe os dois.',
                                  'alerta': 'CJC-1295 e ipamorelina não têm registro na ANVISA nem aprovação '
                                            'na FDA, e o que se vende com esses nomes não tem garantia de '
                                            'origem, pureza ou esterilidade. Material apreendido pela '
                                            'alfândega dinamarquesa continha versões modificadas dessas '
                                            'moléculas. A FDA registra eventos adversos graves com CJC-1295, '
                                            'como aceleração do coração e reação vasodilatadora, e com '
                                            'ipamorelina na veia, inclusive morte, segundo a leitura da '
                                            'agência. Os dois estão na Lista Proibida da WADA, em competição '
                                            'e fora dela.'},
 'proprio_clembuterol': {'nome': 'Clembuterol',
                         'categoria': 'primaria',
                         'aprovado': 'nao',
                         'tagline': 'Nos dois ensaios randomizados em humanos, o clembuterol aumentou massa '
                                    'magra e não reduziu gordura mais que o placebo; o estudo de 2025 citado '
                                    'como prova de "queima de gordura" diz o contrário.',
                         'resumo': 'O clembuterol é um broncodilatador da família dos agonistas beta-2, sem '
                                   'nenhum registro de medicamento na ANVISA e sem aplicação humana na FDA. '
                                   'Ele circula como queimador de gordura com cronologia de 30 dias. Uma '
                                   'dose única subiu o gasto de energia em repouso em 21% em 6 homens. Mas '
                                   'nos dois ensaios randomizados com uso contínuo, de 2 e de 8 semanas, a '
                                   'massa gorda não caiu mais que com placebo; a massa magra subiu cerca de '
                                   '1 a 2 kg, e o fôlego máximo caiu 7%. A sinalização do remédio perdeu '
                                   'força em duas semanas. Os relatos de intoxicação trazem taquicardia, '
                                   'potássio baixo, infarto, miocardite e morte.',
                         'alerta': 'O clembuterol não tem registro como medicamento no Brasil e não é '
                                   'aprovado para uso humano nos Estados Unidos. Os centros de intoxicação '
                                   'registram taquicardia, tremor, potássio baixo, glicose alta e lesão do '
                                   'músculo do coração, com efeitos que duram mais de 24 horas; há relatos '
                                   'de infarto, miocardite, cardiomiopatia, parada cardíaca e morte em '
                                   'jovens. Quem tem doença do coração, arritmia ou pressão alta corre risco '
                                   'maior: isso é inferência minha a partir dos relatos. É proibido pela '
                                   'WADA o tempo todo.'},
 'proprio_clomifeno': {'nome': 'Clomifeno (citrato de clomifeno, Clomid)',
                       'categoria': 'primaria',
                       'aprovado': 'nao',
                       'tagline': 'O "+146%" existe, em estudos pequenos e sem grupo controle; no homem, o '
                                  'clomifeno não tem indicação em bula, e a versão purificada teve o '
                                  'registro recusado na Europa.',
                       'resumo': 'O clomifeno é um modulador seletivo do receptor de estrogênio aprovado '
                                 'para induzir ovulação em mulheres. Em homens com testosterona baixa, ele é '
                                 'usado fora da bula e sobe a testosterona produzida pelo próprio testículo: '
                                 'uma meta-análise de 2025 só com ensaios randomizados achou +273,76 ng/dL '
                                 'em relação ao placebo. Os números dos vídeos vêm de estudos reais, mas '
                                 'pequenos e sem controle, e duas fontes foram citadas com revista ou autor '
                                 'trocados. Subir o exame não é o mesmo que melhorar sintomas: a Europa '
                                 'recusou o enclomifeno em 2018 por falta de prova de benefício clínico e '
                                 'por risco de trombose. Não há estudo de desempenho em academia. É proibido '
                                 'pela WADA o tempo todo.',
                       'alerta': 'O clomifeno pode causar sintomas visuais que a bula americana descreve '
                                 'como possivelmente irreversíveis, e quem tiver qualquer sintoma visual '
                                 'deve parar e passar por avaliação oftalmológica. A bula contraindica o uso '
                                 'em doença do fígado e na presença de tumor de hipófise, e registra '
                                 'ginecomastia e tumores de testículo relatados em homens. O estradiol sobe '
                                 'junto com a testosterona. O zuclomifeno, um dos dois componentes, fica no '
                                 'corpo por meses e aparece no antidoping por pelo menos quatro meses depois '
                                 'de um uso de 30 dias.'},
 'proprio_colostro_bovino': {'nome': 'Colostro bovino',
                             'categoria': 'primaria',
                             'aprovado': 'nao',
                             'tagline': 'No Brasil, suplemento de colostro pode ter no máximo 4 g por dia; '
                                        'os estudos de treino usaram de 10 a 60 g, e na maioria o IGF-1 do '
                                        'sangue não subiu.',
                             'resumo': 'O colostro bovino é a primeira secreção da mama da vaca depois do '
                                       'parto, rica em imunoglobulinas, lactoferrina e fatores de '
                                       'crescimento como o IGF-1. Em treino de força, os ensaios compararam '
                                       'colostro com whey: um viu mais massa magra com colostro, os outros '
                                       'não viram diferença no músculo. Em vários ensaios, o IGF-1 do sangue '
                                       'não mudou, e o IGF-1 tomado por boca chega ao sangue fragmentado. O '
                                       'efeito mais consistente é em marcadores de permeabilidade do '
                                       'intestino. A WADA não proíbe o colostro, mas desaconselha seu uso '
                                       'por atletas, e no Brasil essa advertência é obrigatória no rótulo, '
                                       'com máximo de 4 g por dia.',
                             'alerta': 'A WADA não proíbe o colostro, mas desaconselha seu uso por atletas '
                                       'porque ele contém IGF-1 e outros fatores de crescimento, que estão '
                                       'na Lista Proibida. No Brasil, o rótulo do suplemento de colostro tem '
                                       'de trazer essa advertência, e o máximo permitido é 4 g por dia para '
                                       'adultos; os estudos de desempenho usaram de 10 a 60 g por dia. O '
                                       'colostro é derivado de leite: quem tem alergia à proteína do leite '
                                       'deve evitar. O pó de colostro contém estrógenos naturais da vaca, em '
                                       'microgramas por quilo.'},
 'proprio_cominho_preto': {'nome': 'Cominho-preto (Nigella sativa; timoquinona)',
                           'categoria': 'primaria',
                           'aprovado': 'nao',
                           'tagline': 'O estudo iraquiano existe, mas durou 3 meses, não 6, e a testosterona '
                                      'subiu 29%; os 59% eram da motilidade dos espermatozoides.',
                           'resumo': 'O cominho-preto (Nigella sativa) é uma semente usada como tempero; a '
                                     'timoquinona é o composto mais estudado dela. O estudo citado nos '
                                     'vídeos existe: 40 homens inférteis em Tikrit, no Iraque, 2 g por dia '
                                     'por 3 meses, com contagem de espermatozoides +39% e motilidade +60% no '
                                     'próprio grupo, e testosterona +29%. Ele não está no PubMed, não '
                                     'descreve sorteio e mal descreve o grupo placebo. Um ensaio iraniano '
                                     'randomizado, com óleo, também melhorou o sêmen. Não existe '
                                     'meta-análise de testosterona ou sêmen com a planta, e nenhum estudo '
                                     'testou microplástico no testículo.',
                           'alerta': 'O cominho-preto não consta da lista de constituintes autorizados para '
                                     'suplemento alimentar no Brasil (IN 28/2018, consolidada até setembro '
                                     'de 2026). Há relatos de lesão renal aguda, rabdomiólise, lesão do '
                                     'fígado e reação grave de pele depois de tomar o óleo ou o suplemento, '
                                     'e de hematoma com plaquetas baixas em paciente que também usava dois '
                                     'antiagregantes. Quem usa anticoagulante, antiagregante ou tem doença '
                                     'renal não deveria usar sem médico.'},
 'proprio_compostos_do_brocolis_estrogenio': {'nome': '"Dois compostos do brócolis" contra o estrogênio '
                                                      '(indol-3-carbinol, DIM e sulforafano)',
                                              'categoria': 'primaria',
                                              'aprovado': 'nao',
                                              'tagline': 'Os vídeos não dizem quais são os "dois compostos"; '
                                                         'nos candidatos mais estudados, o DIM não mexeu na '
                                                         'testosterona de homens e, no laboratório, bloqueou '
                                                         'o receptor de androgênio.',
                                              'resumo': 'Os vídeos prometem "dois compostos do brócolis" '
                                                        'contra a "dominância estrogênica", mas não os '
                                                        'nomeiam. Os candidatos mais estudados são o '
                                                        'indol-3-carbinol, o DIM, que se forma a partir dele '
                                                        'no estômago, e o sulforafano. O indol-3-carbinol '
                                                        'desvia o metabolismo do estrogênio para a via de '
                                                        '2-hidroxilação em homens e mulheres, em estudos de '
                                                        'uma semana. Em 45 homens com câncer de próstata, o '
                                                        'DIM por 3 a 4 semanas não mudou a testosterona de '
                                                        'forma significativa. No laboratório, o DIM se '
                                                        'comportou como antagonista do receptor de '
                                                        'androgênio. No Brasil, nenhum dos três é '
                                                        'constituinte autorizado de suplemento alimentar.',
                                              'alerta': 'Os vídeos não nomeiam os compostos; esta página '
                                                        'discute os candidatos mais estudados e não afirma '
                                                        'que são os mesmos. Nenhum deles foi testado para '
                                                        'subir testosterona em homens, e o DIM bloqueou o '
                                                        'receptor de androgênio em células de próstata. O '
                                                        'indol-3-carbinol aumentou em 4 vezes a atividade de '
                                                        'uma enzima hepática que metaboliza remédios. Quem '
                                                        'usa medicação contínua ou trata câncer '
                                                        'hormônio-dependente deve conversar com o médico '
                                                        'antes.'},
 'proprio_cordyceps': {'nome': 'Cordyceps (Ophiocordyceps sinensis e Cordyceps militaris)',
                       'categoria': 'primaria',
                       'aprovado': 'nao',
                       'tagline': 'Nenhum ensaio humano testou o cordyceps em ereção ou testosterona; no '
                                  'treino, a meta-análise de 2025 achou ganho aeróbio pequeno, com p = 0,05 '
                                  'na resistência.',
                       'resumo': '"Cordyceps" nomeia dois fungos diferentes: o Ophiocordyceps sinensis '
                                 'selvagem do planalto tibetano, que custa dezenas de milhares de dólares o '
                                 'quilo, e o Cordyceps militaris cultivado, que está na maior parte dos '
                                 'estudos recentes e dos suplementos. Para ereção, o PubMed não tem nenhum '
                                 'ensaio randomizado; o que existe é rato e estudo chinês antigo fora do '
                                 'PubMed. Para testosterona, só células e camundongos, e num deles o fungo '
                                 'fez crescer câncer de próstata. No treino, uma meta-análise de 2025 achou '
                                 'melhora pequena no limiar ventilatório e no VO2 pico, com p = 0,05 na '
                                 'resistência; ensaios bem feitos em ciclistas não acharam nada.',
                       'alerta': 'O cordyceps não consta da lista de constituintes autorizados para '
                                 'suplemento alimentar no Brasil (IN 28/2018, consolidada até setembro de '
                                 '2026). O fungo selvagem acumula arsênio: em 2016 a autoridade chinesa '
                                 'encerrou um programa piloto de alimentos com cordyceps depois de encontrar '
                                 '4,4–9,9 mg/kg, contra limite de 1,0 mg/kg. Uma revisão associa o C. '
                                 'sinensis, de forma fraca, a sangramento cirúrgico. Em camundongos, o fungo '
                                 'subiu a testosterona e acelerou tumor de próstata; homem com câncer de '
                                 'próstata ou PSA alterado não deveria usá-lo sem o urologista saber.'},
 'proprio_creatina': {'nome': 'Creatina (monoidratada)',
                      'categoria': 'primaria',
                      'aprovado': 'parcial',
                      'tagline': 'O "8% a 14% a mais de força" existe e vem de uma revisão de 2003; a '
                                 'saturação de 15 a 20 g por dia passa de 3 a 4 vezes o máximo diário '
                                 'permitido em suplemento no Brasil.',
                      'resumo': 'A creatina é uma molécula que o próprio corpo fabrica e que a dieta com '
                                'carne fornece em parte. É o suplemento esportivo com mais evidência: no '
                                'PubMed, 868 artigos sobre suplementação de creatina estão marcados como '
                                'ensaio randomizado ou meta-análise. O "8% a 14%" citado nos vídeos existe, '
                                'numa revisão de 22 estudos de 2003, mas o 14% é de repetições, não de '
                                'força. Meta-análises recentes acham ganho real e pequeno: 1,43 kg a mais no '
                                'supino e 5,64 kg no agachamento, com treino. A saturação funciona, mas não '
                                'é necessária: 3 g por dia por 28 dias chegam ao mesmo nível no músculo. No '
                                'Brasil, o máximo em suplemento é 5 g por dia.',
                      'alerta': 'A fase de saturação de 15 a 20 g por dia passa do máximo de 5 g por dia que '
                                'a ANVISA permite na recomendação de um suplemento para adultos, e uma dose '
                                'única de 10 g dobrou a frequência de diarreia num ensaio. A creatina eleva '
                                'a creatinina do sangue sem lesar o rim em pessoas saudáveis, o que pode '
                                'fazer um exame parecer pior do que é. No Brasil, suplemento de creatina não '
                                'é autorizado para gestantes, lactantes, crianças e adolescentes. Quem tem '
                                'doença renal deve conversar com o médico antes.'},
 'proprio_ddt_dde_dieta': {'nome': 'DDT e DDE na dieta (os jacarés do Lago Apopka)',
                           'categoria': 'primaria',
                           'aprovado': 'nao',
                           'tagline': 'Os jacarés do Lago Apopka tiveram pênis 24% menor e testosterona 70% '
                                      'mais baixa; em homens expostos ao DDE, a testosterona apareceu mais '
                                      'baixa, igual ou até mais alta, conforme o estudo.',
                           'resumo': 'O DDT é um inseticida proibido no Brasil desde 2009, e o DDE é o '
                                     'resíduo que ele deixa na gordura de animais e de pessoas por décadas. '
                                     'Os números dos jacarés estão no artigo de 1996: pênis 24% menor e '
                                     'testosterona 70% mais baixa num lago contaminado. Em laboratório e em '
                                     'ratos, o DDE bloqueia o receptor de andrógeno. Em homens, os estudos '
                                     'são de observação e não concordam: alguns acham pior motilidade dos '
                                     'espermatozoides, e um estudo sul-africano achou testosterona mais alta '
                                     'em quem tinha mais DDE. A associação com diabetes tipo 2 aparece em '
                                     'meta-análises, e a agência de câncer da OMS classifica o DDT como '
                                     'provável cancerígeno. A comida é a principal via de exposição.',
                           'alerta': 'Esta página trata de exposição, não de suplemento. Não existe exame de '
                                     'rotina nem protocolo testado para "limpar" o DDE do corpo; ele sai '
                                     'devagar, e perder peso rápido pode até aumentar a concentração no '
                                     'sangue por um tempo. Testosterona baixa ou infertilidade pedem '
                                     'investigação médica das causas comuns antes de culpar o DDT. Peixe tem '
                                     'benefícios conhecidos, e trocar a dieta por medo de resíduo pode fazer '
                                     'mais mal que bem.'},
 'proprio_dhea': {'nome': 'DHEA (deidroepiandrosterona, prasterona)',
                  'categoria': 'primaria',
                  'aprovado': 'nao',
                  'tagline': 'O DHEA sobe o IGF-1, mas em homens jovens que treinavam não aumentou força nem '
                             'massa magra além do placebo, e num ensaio de 2 anos em idosos não melhorou '
                             'músculo, desempenho nem qualidade de vida.',
                  'resumo': 'O DHEA é um hormônio que a suprarrenal produz e que o corpo converte em '
                            'andrógenos e estrogênios. No Brasil, está na lista C5 de anabolizantes da '
                            'Portaria 344/98 e não tem medicamento registrado nem autorização como '
                            'suplemento. Os vídeos o chamam de "santo graal da regeneração" que bloqueia o '
                            'cortisol e sobe o IGF-1. O IGF-1 sobe de fato. Mas em 19 homens jovens com '
                            'treino, 150 mg por dia não melhoraram força nem massa magra além do placebo; '
                            'num ensaio de 2 anos em idosos, o DHEA não mudou composição corporal, força nem '
                            'qualidade de vida. O estudo da Universidade de Washington citado não trata de '
                            'cortisol no resumo. É proibido pela WADA o tempo todo.',
                  'alerta': 'No Brasil, o DHEA é substância anabolizante da lista C5 da Portaria 344/98, '
                            'sujeita a receita de controle especial, e o Conselho Federal de Medicina veda '
                            'prescrever anabolizantes ou hormônios androgênicos com finalidade estética ou '
                            'de desempenho. O corpo transforma o DHEA em testosterona e estrogênio: em '
                            'mulheres, os andrógenos passaram da faixa de adultas jovens num ensaio. A bula '
                            'americana do único produto aprovado com prasterona lembra que o estrogênio é um '
                            'de seus metabólitos. Que isso pese para quem tem câncer sensível a hormônio é '
                            'inferência minha.'},
 'proprio_dim_di_indolilmetano': {'nome': "DIM (3,3'-di-indolilmetano)",
                                  'categoria': 'primaria',
                                  'aprovado': 'nao',
                                  'tagline': 'O "−76% de estrogênio" não aparece em nenhum estudo de DIM que '
                                             'localizei; no maior ensaio, o DIM subiu a SHBG, a proteína que '
                                             'prende a testosterona no sangue.',
                                  'resumo': 'O DIM se forma no estômago a partir de um composto do brócolis '
                                            'e de outras crucíferas e é vendido concentrado como suplemento. '
                                            'Os estudos em humanos medem metabólitos de estrogênio na urina, '
                                            'quase sempre em mulheres com câncer ou risco de câncer de mama. '
                                            'Nenhum traz os 76% citados nos vídeos. Em homens, o DIM não '
                                            'mudou a testosterona; na próstata, empurrou o receptor de '
                                            'androgênio para fora do núcleo da célula, um efeito '
                                            'antiandrogênico. No maior ensaio, a SHBG subiu e os metabólitos '
                                            'ativos do tamoxifeno caíram. No Brasil, o DIM não é '
                                            'constituinte autorizado de suplemento alimentar.',
                                  'alerta': 'O DIM não é constituinte autorizado de suplemento no Brasil. Em '
                                            'homens com câncer de próstata, ele agiu contra o androgênio, '
                                            'não a favor, e na dose de 300 mg duas vezes ao dia dois de '
                                            'quatro pacientes tiveram sódio muito baixo no sangue. Em '
                                            'mulheres que tomavam tamoxifeno, o DIM reduziu os metabólitos '
                                            'ativos do remédio. Quem usa tamoxifeno, trata câncer '
                                            'hormônio-dependente ou usa medicação contínua não deve tomar '
                                            'DIM sem falar com o médico.'},
 'proprio_ecdisterona': {'nome': 'Ecdisterona (20-hidroxiecdisona; inclui turquesterona)',
                         'categoria': 'primaria',
                         'aprovado': 'nao',
                         'tagline': 'O estudo alemão que deu fama à ecdisterona usou 12 e 48 mg por dia, '
                                    'melhorou o supino e não o agachamento; a agência antidoping a monitora, '
                                    'não a proíbe.',
                         'resumo': 'A ecdisterona é um hormônio de muda de insetos que algumas plantas '
                                   'também fabricam, inclusive o espinafre. A fama de "anabolizante natural" '
                                   'vem de ratos e de um estudo alemão de 2019, financiado pela agência '
                                   'antidoping: 46 homens em quatro grupos, 12 ou 48 mg por dia por 10 '
                                   'semanas. O supino subiu mais com ecdisterona; o agachamento, não. Uma '
                                   'meta-análise de 2026 com 4 ensaios e 150 pessoas achou efeito pequeno só '
                                   'na força das pernas e nenhum na massa magra. A turquesterona não tem '
                                   'ensaio controlado publicado. Em 2026, a ecdisterona está no programa de '
                                   'monitoramento da WADA, não na lista proibida.',
                         'alerta': 'A ecdisterona não consta da lista de constituintes autorizados para '
                                   'suplemento alimentar no Brasil (IN 28/2018, consolidada até setembro de '
                                   '2026). Nos produtos analisados por laboratórios, o conteúdo real costuma '
                                   'ficar muito abaixo do rótulo: 6 mg em cápsula rotulada com 100 mg, menos '
                                   'de 1% em outro produto, turquesterona indetectável em metade das '
                                   'amostras de um estudo americano. A segurança do uso prolongado como '
                                   'suplemento não foi estudada. Atleta testado: é substância monitorada '
                                   'pela WADA em 2026.'},
 'proprio_epicatequina_cacau': {'nome': 'Epicatequina ((−)-epicatequina; extrato de cacau)',
                                'categoria': 'primaria',
                                'aprovado': 'nao',
                                'tagline': 'O estudo de 2013 que "derrubou a miostatina" tratou 6 pessoas '
                                           'por 7 dias, sem placebo; num ensaio de 4 semanas, a epicatequina '
                                           'não mexeu na miostatina do músculo.',
                                'resumo': 'A (−)-epicatequina é o flavanol mais citado do cacau. A fama de '
                                          '"desligar a miostatina" vem de um piloto de 2013 em 6 pessoas, 50 '
                                          'mg por dia por 7 dias, sem placebo, com preensão 7% maior e a '
                                          'razão folistatina/miostatina subindo em dado não mostrado. Num '
                                          'ensaio de 4 semanas em 20 ciclistas, ela não mudou a miostatina '
                                          'do músculo e atrapalhou a adaptação aeróbia. Em idosos com '
                                          'sarcopenia, somada à musculação, a força subiu mais. Os efeitos '
                                          'mais sólidos do cacau são vasculares e pequenos. No Brasil, o '
                                          'extrato de cacau é permitido em suplemento até 300 mg por dia.',
                                'alerta': 'O extrato de cacau é constituinte autorizado de suplemento no '
                                          'Brasil, mas só para maiores de 19 anos e até 300 mg por dia, e '
                                          'sem nenhuma alegação de músculo permitida no rótulo. A '
                                          'epicatequina isolada não consta da lista. Num ensaio controlado, '
                                          '200 mg por dia de epicatequina bloquearam o ganho de VO2 do '
                                          'treino aeróbio. A agência antidoping proíbe "agentes que reduzem '
                                          'a expressão da miostatina"; a epicatequina não é citada, mas o '
                                          'atleta que a toma justamente para isso corre um risco que não foi '
                                          'esclarecido.'},
 'proprio_epimedium_icariina': {'nome': 'Epimedium (icariina, "horny goat weed")',
                                'categoria': 'primaria',
                                'aprovado': 'nao',
                                'tagline': 'A prova de que a icariina age como a tadalafila vem de enzima '
                                           'isolada e de ratos; tomada por boca, ela ficou abaixo do limite '
                                           'de detecção no sangue em dois estudos humanos.',
                                'resumo': 'A icariina é o flavonoide mais citado do Epimedium, planta usada '
                                          'na medicina tradicional chinesa. Em tubo de ensaio, ela inibe a '
                                          'mesma enzima que a sildenafila e a tadalafila, com potência bem '
                                          'menor. Os efeitos sobre ereção e testosterona citados nos vídeos '
                                          'vêm de ratos. Não localizei nenhum ensaio em homens com icariina '
                                          'ou Epimedium sozinhos para disfunção erétil; o único ensaio '
                                          'clínico da busca testa uma mistura de quatro plantas. Em dois '
                                          'estudos humanos, a icariina ficou abaixo do limite de detecção no '
                                          'sangue depois de tomada por boca. No Brasil, não consta da lista '
                                          'de suplementos nem tem registro de medicamento.',
                                'alerta': 'A icariina não tem ensaio em homens com disfunção erétil, e a '
                                          'dose de 200 a 500 mg que circula não vem de estudo clínico de '
                                          'ereção. Há relatos de caso de arritmia com hipomania, de espasmos '
                                          'musculares com alteração renal e de psicose associados ao uso de '
                                          'Epimedium. Somar Epimedium a remédio de pressão, nitrato ou '
                                          'inibidor de PDE5 pode, em tese, somar efeitos: é inferência '
                                          'minha, sem estudo humano que eu tenha localizado.'},
 'proprio_fadogia_agrestis': {'nome': 'Fadogia agrestis (Vangueria agrestis)',
                              'categoria': 'primaria',
                              'aprovado': 'nao',
                              'tagline': 'Nenhum estudo em humanos; o artigo do mesmo grupo nigeriano na '
                                         'revista citada nos vídeos mostra efeito adverso no testículo de '
                                         'ratos, não aumento de testosterona.',
                              'resumo': 'A Fadogia agrestis é um arbusto da África Ocidental. O PubMed tem '
                                        '11 artigos sobre a espécie, nenhum ensaio clínico, e o '
                                        'ClinicalTrials.gov não tem nenhum registro. Toda a base para '
                                        '"testosterona" é de ratos: um estudo de 2005 da Universidade de '
                                        'Ilorin, na Nigéria, viu a testosterona subir em 5 dias. O mesmo '
                                        'grupo publicou depois, na revista que os vídeos citam, que 28 dias '
                                        'do extrato causaram alterações adversas na função do testículo de '
                                        'ratos, e em 2009 descreveu dano às células do fígado e dos rins. O '
                                        'LH, que os vídeos dizem que a planta "dispara", não foi medido. Em '
                                        '17 suplementos vendidos com a planta, 5 não tinham os compostos '
                                        'marcadores. No Brasil, a planta não consta da lista de '
                                        'constituintes de suplemento.',
                              'alerta': 'Não existe nenhum estudo em humanos com Fadogia agrestis, nem de '
                                        'efeito nem de segurança. Em ratos, 28 dias do extrato alteraram '
                                        'marcadores da função do testículo, e o próprio grupo que estuda a '
                                        'planta classificou essas alterações como efeitos adversos; o '
                                        'extrato também lesou membranas de células do fígado e dos rins. '
                                        'Plantas do mesmo gênero causam doença cardíaca em ruminantes, e '
                                        'parte dos suplementos vendidos com o nome da planta não tinha os '
                                        'compostos dela.'},
 'proprio_farinha_de_arroz': {'nome': 'Farinha de arroz no shake (carboidrato pós-treino)',
                              'categoria': 'primaria',
                              'aprovado': 'nao',
                              'tagline': 'Farinha de arroz é carboidrato comum e funciona como caloria; o '
                                         '"pico de insulina que joga aminoácidos na fibra" não aumentou a '
                                         'síntese de músculo quando já havia proteína suficiente.',
                              'resumo': 'A farinha de arroz aparece em vídeo como um carboidrato barato para '
                                        'o shake, que faria "supercompensação de glicogênio", subiria a '
                                        'força e, pelo pico de insulina, levaria os aminoácidos para dentro '
                                        'do músculo. Não há estudo com farinha de arroz. Sobre carboidrato '
                                        'em geral, a literatura é clara em dois pontos: ele repõe o '
                                        'glicogênio depois do treino e pode aumentar o volume de treino em '
                                        'sessões longas ou em jejum; mas somado a uma dose suficiente de '
                                        'proteína, não aumentou a síntese de músculo em dois ensaios, mesmo '
                                        'com insulina cinco vezes maior. A farinha é densa em energia, o que '
                                        'ajuda quem quer comer mais.',
                              'alerta': 'A farinha de arroz é alimento comum, sem risco especial em '
                                        'quantidade de cozinha. O arroz é a principal fonte de arsênio '
                                        'inorgânico na dieta de muitas populações, inclusive a brasileira; '
                                        'quem passa a somar farinha de arroz todos os dias ao arroz das '
                                        'refeições aumenta essa exposição. Como qualquer carboidrato '
                                        'concentrado, ela sobe a glicose do sangue: quem tem diabetes deve '
                                        'contar essas gramas com o profissional que o acompanha.'},
 'proprio_fascia_de_buck': {'nome': 'Fáscia de Buck e o "protocolo de perfusão"',
                            'categoria': 'primaria',
                            'aprovado': 'nao',
                            'tagline': 'O vídeo não descreve a técnica. A fáscia de Buck existe e envolve os '
                                       'corpos do pênis, mas nenhum artigo a liga a bloquear vasos, e nenhum '
                                       'ensaio testou manipulação manual para ereção ou tamanho.',
                            'resumo': 'Um vídeo curto diz que a fáscia de Buck, uma camada fibrosa do pênis, '
                                      '"bloqueia completamente" a formação de vasos e limita o tamanho, e '
                                      'que um "protocolo de perfusão documentado" resolveria isso. O vídeo '
                                      'não descreve a técnica. A fáscia existe: envolve os dois corpos '
                                      'cavernosos e o corpo esponjoso, e por dentro dela passam nervos e '
                                      'vasos. A busca por fáscia de Buck e formação de vasos devolve zero '
                                      'artigos. Não há ensaio clínico de manipulação manual do pênis para '
                                      'ereção ou tamanho; nos artigos, manipulação do pênis aparece como '
                                      'causa de fratura. O estudo de Amsterdã de 2019 não foi localizado.',
                            'alerta': 'Esta página trata de uma técnica que o vídeo não descreve, por isso '
                                      'não há o que avaliar dela além das alegações. Forçar ou dobrar o '
                                      'pênis ereto pode romper a túnica albugínea, a chamada fratura de '
                                      'pênis, que é urgência cirúrgica. Curvatura nova, dor ou caroço no '
                                      'pênis pedem avaliação de urologista. A única técnica mecânica com '
                                      'ensaios para comprimento é a tração, que tem página própria.'},
 'proprio_feno_grego': {'nome': 'Feno-grego (fenogreco, Trigonella foenum-graecum)',
                        'categoria': 'primaria',
                        'aprovado': 'nao',
                        'tagline': 'O "+37% acima do placebo" é testosterona na saliva; no sangue, o mesmo '
                                   'ensaio de 95 homens não diferiu do placebo. O "+46%" vem de estudo sem '
                                   'grupo controle.',
                        'resumo': 'O feno-grego é uma semente de tempero com 9 artigos no PubMed marcados '
                                  'como ensaio randomizado ou meta-análise sobre testosterona e 35 sobre '
                                  'glicemia. É, entre as ervas vendidas para testosterona, uma das poucas '
                                  'com efeito positivo em revisão sistemática, mas pequeno: SMD 0,32 na '
                                  'testosterona total e efeito não significativo na livre, segundo a '
                                  'meta-análise de 2023. O "+37% acima do placebo" de 95 homens é '
                                  'testosterona salivar; no sangue, o ensaio não achou diferença contra o '
                                  'placebo. O "+46% em 90%" vem de estudo de um braço só, feito pelo '
                                  'desenvolvedor do extrato. Na glicemia, a base é mais antiga e mais ampla, '
                                  'com qualidade baixa. No Brasil, o extrato de semente é fonte autorizada '
                                  'de saponinas furostanólicas em suplemento, até 450 mg por dia para '
                                  'adultos e sem nenhuma alegação de rótulo.',
                        'alerta': 'No Brasil, o suplemento com saponinas furostanólicas do extrato de '
                                  'feno-grego tem limite de 450 mg por dia, só para maiores de 19 anos, e o '
                                  'rótulo tem de dizer que gestantes, lactantes e crianças não devem '
                                  'consumir. O feno-grego pode baixar a glicose e somar efeito com remédios '
                                  'para diabetes, pode interagir com a varfarina e tem reação cruzada com '
                                  'amendoim e grão-de-bico em pessoas alérgicas.'},
 'proprio_fluor_agua_pineal': {'nome': 'Flúor na água e glândula pineal (filtros de água e de chuveiro)',
                               'categoria': 'primaria',
                               'aprovado': 'nao',
                               'tagline': 'O flúor se acumula na calcificação da pineal de idosos, num '
                                          'estudo de 11 cadáveres; nenhum estudo em gente mediu melatonina, '
                                          'e o filtro de carvão de fato não tira fluoreto.',
                               'resumo': 'A pineal calcifica com a idade em boa parte das pessoas, e o flúor '
                                         'se acumula nessa calcificação: num estudo de 11 cadáveres, a '
                                         'pineal tinha 297 mg de flúor por quilo, contra 0,5 no músculo. Daí '
                                         'a dizer que o flúor "destrói" a glândula, cria os cristais ou '
                                         'derruba a melatonina há um salto que nenhum estudo em humanos deu. '
                                         'Dois estudos de população acharam associação entre mais flúor na '
                                         'água e sono mais curto ou mais tardio, não com sonolência. A '
                                         'preocupação mais estudada com flúor é outra: QI de crianças, com '
                                         'associação clara acima de 1,5 mg/L. No Brasil, a fluoretação é '
                                         'recomendada entre 0,6 e 1,2 mg/L conforme o clima, com máximo de '
                                         '1,5. Osmose reversa e destilação tiram a maior parte do fluoreto; '
                                         'carvão comum, não.',
                               'alerta': 'Esta página trata de exposição, não de suplemento. Tirar o flúor '
                                         'da água de beber tira também o efeito contra a cárie, que existe, '
                                         'embora menor que no passado; quem filtra a água deve conversar com '
                                         'o dentista sobre outras fontes de flúor, sobretudo para crianças. '
                                         'Insônia e cansaço persistentes pedem avaliação médica, porque têm '
                                         'causas comuns e tratáveis. Filtro de chuveiro contra flúor não tem '
                                         'estudo que o sustente.'},
 'proprio_forskolina': {'nome': 'Forskolina (Coleus forskohlii)',
                        'categoria': 'primaria',
                        'aprovado': 'nao',
                        'tagline': 'O "+33,77% de testosterona" é o desvio padrão do estudo de Kansas, não o '
                                   'efeito: a média subiu 16,77%, sem diferença estatística contra o '
                                   'placebo, em 15 homens.',
                        'resumo': 'A forskolina é a substância da raiz de Coleus forskohlii que ativa a '
                                  'enzima adenilato ciclase e eleva o AMP cíclico, uma ferramenta clássica '
                                  'de laboratório. O estudo citado nos vídeos existe: Universidade de '
                                  'Kansas, 2005, 30 homens com sobrepeso, 12 semanas, 250 mg 2×/dia de '
                                  'extrato a 10%. A gordura caiu mais que no placebo e a testosterona livre '
                                  'subiu; a total subiu 16,77 ± 33,77%, sem diferença entre grupos — o '
                                  '"33,77%" dos vídeos é o desvio padrão. Em mulheres, outro estudo não '
                                  'achou perda de gordura. Em camundongos, o extrato causou fígado gorduroso '
                                  'e alterou o metabolismo de remédios, por outros componentes além da '
                                  'forskolina.',
                        'alerta': 'A forskolina e o extrato de Coleus forskohlii não são constituintes '
                                  'autorizados de suplemento no Brasil. Em camundongos, o extrato '
                                  'padronizado a 10% causou lesão e gordura no fígado dependentes da dose e '
                                  'acelerou enzimas que metabolizam remédios, a ponto de reduzir o efeito da '
                                  'varfarina; em células humanas, induziu a enzima CYP3A4. Quem usa '
                                  'anticoagulante, remédio de uso contínuo ou tem doença do fígado não tem '
                                  'estudo de segurança em que se apoiar.'},
 'proprio_fosfatidilserina': {'nome': 'Fosfatidilserina (cortisol e testosterona)',
                              'categoria': 'primaria',
                              'aprovado': 'nao',
                              'tagline': 'O "+37% de testosterona" é de 10 homens pedalando 15 minutos, numa '
                                         'medida em que o pico da testosterona não diferiu do placebo; a '
                                         'pesquisa foi paga pela empresa de dois autores.',
                              'resumo': 'A fosfatidilserina é um fosfolipídio das membranas das células, '
                                        'vendida como suplemento de memória. O estudo de 2008 citado nos '
                                        'vídeos existe: 10 homens, 600 mg por dia por 10 dias, 15 minutos de '
                                        'bicicleta em intensidade moderada. A área sob a curva do cortisol '
                                        'caiu 35% e a da testosterona subiu 37%, mas o pico da testosterona '
                                        'não diferiu do placebo, e a pesquisa foi financiada pela empresa em '
                                        'que trabalham dois dos autores. Outro ensaio, com 750 mg de '
                                        'fosfatidilserina de soja, não mudou o cortisol, e um terceiro achou '
                                        'efeito com 400 mg e não com 600 ou 800 mg. Em idosos, a de soja não '
                                        'melhorou a memória. No Brasil, o máximo em suplemento é 400 mg por '
                                        'dia.',
                              'alerta': 'Os 600 mg por dia dos vídeos passam do máximo que a ANVISA permite '
                                        'em suplemento para adultos (400 mg por dia), e no Brasil só a '
                                        'fosfatidilserina de soja é autorizada; a de origem bovina, a '
                                        'primeira estudada, foi abandonada pelo risco de transmissão de '
                                        'doenças infecciosas. O rótulo deve dizer que gestantes, lactantes e '
                                        'crianças não devem consumir. Quem tem alergia a soja deve '
                                        'considerar a origem do produto. Não há estudo de uso por meses para '
                                        'subir testosterona.'},
 'proprio_gaba_hormonio_do_crescimento': {'nome': 'GABA oral e o "+400% de GH"',
                                          'categoria': 'primaria',
                                          'aprovado': 'nao',
                                          'tagline': 'O "+400% de GH" existe: veio de 11 homens que tomaram '
                                                     '3 g de GABA uma vez, em jejum; no Brasil, o máximo '
                                                     'permitido em suplemento é 300 mg por dia.',
                                          'resumo': 'O GABA é o principal neurotransmissor inibitório do '
                                                    'cérebro e é vendido como suplemento. O número que '
                                                    'circula, pico de GH 400% maior que com placebo, é real '
                                                    'e vem de um ensaio de 2008 com 11 homens treinados, 3 g '
                                                    'numa dose só, sangue colhido por 90 minutos. É um pico '
                                                    'agudo e relativo, contra um placebo de açúcar, e o '
                                                    'estudo não mediu músculo, gordura nem sono. Um estudo '
                                                    'de 1980 mostrou que 18 g por dia por 4 dias reduziram a '
                                                    'resposta do GH, em vez de aumentar. Para sono e '
                                                    'estresse, uma revisão sistemática achou evidência muito '
                                                    'limitada. No Brasil, o GABA é constituinte autorizado '
                                                    'de suplemento desde junho de 2025, até 300 mg por dia '
                                                    'para adultos: os 3 a 5 g dos vídeos passam dez vezes ou '
                                                    'mais desse limite.',
                                          'alerta': 'Os 3 a 5 g por dia que circulam passam de dez vezes o '
                                                    'máximo que a ANVISA permite em suplemento (300 mg por '
                                                    'dia, só para maiores de 19 anos). Pela regra '
                                                    'brasileira, suplemento com GABA não é autorizado para '
                                                    'gestantes, lactantes, crianças e adolescentes, e o '
                                                    'rótulo tem de dizer isso. A revisão de segurança da '
                                                    'Farmacopeia americana registra queda transitória de '
                                                    'pressão e recomenda cautela com remédio para pressão, '
                                                    'na gravidez e na amamentação, porque o GABA mexe com GH '
                                                    'e prolactina.'},
 'proprio_gengibre_fertilidade': {'nome': 'Gengibre e fertilidade masculina (Zingiber officinale)',
                                  'categoria': 'primaria',
                                  'aprovado': 'nao',
                                  'tagline': 'O "LH +43%" existe, num estudo iraquiano sem placebo que não '
                                             'diz dose nem forma; o único ensaio com placebo, em 100 homens, '
                                             'não mudou contagem nem motilidade.',
                                  'resumo': 'O gengibre é tempero e fitoterápico registrado no Brasil, para '
                                            'enjoo e má digestão. A alegação de que ele sobe LH, FSH e '
                                            'testosterona vem de um estudo de 2012 de uma revista médica '
                                            'iraquiana, fora do PubMed: 75 homens inférteis, 3 meses de '
                                            'gengibre, sem grupo placebo, sem dose nem forma declaradas, e '
                                            'com médias diferentes no texto e na tabela. O único ensaio '
                                            'randomizado com placebo, iraniano, deu 250 mg de pó 2 vezes ao '
                                            'dia por 3 meses a 100 homens inférteis: a fragmentação do DNA '
                                            'do espermatozoide caiu, mas contagem e motilidade não mudaram, '
                                            'e os hormônios, registrados como desfecho, não aparecem no '
                                            'artigo. Uma revisão de 2018 conclui que o efeito na '
                                            'testosterona não está confirmado em humanos.',
                                  'alerta': 'O Formulário de Fitoterápicos da Farmacopeia Brasileira '
                                            'contraindica o gengibre para quem tem cálculo na vesícula, '
                                            'irritação gástrica e hipertensão, na gestação e na lactação, e '
                                            'manda não usar junto com anticoagulantes. Quem toma '
                                            'anticoagulante ou antiagregante deve falar com o médico antes '
                                            'de usar gengibre em dose de suplemento. Infertilidade masculina '
                                            'tem causas tratáveis que um chá não resolve, e adiar a '
                                            'investigação custa tempo ao casal.'},
 'proprio_ginseng_vermelho_coreano': {'nome': 'Ginseng vermelho coreano (Panax ginseng; ginsenosídeos)',
                                      'categoria': 'primaria',
                                      'aprovado': 'nao',
                                      'tagline': 'A revisão Cochrane de 9 ensaios e 587 homens achou efeito '
                                                 'trivial do ginseng na ereção; a "fibrose desfeita" e o '
                                                 '"+230% de óxido nítrico" não têm estudo humano.',
                                      'resumo': 'O ginseng vermelho é a raiz de Panax ginseng cozida no '
                                                'vapor e seca. Para disfunção erétil, a revisão Cochrane de '
                                                '2021, com 9 ensaios e 587 homens, achou melhora pequena '
                                                'demais para ser clinicamente relevante, com certeza baixa a '
                                                'moderada, e nenhuma comparação com remédios do tipo '
                                                'tadalafila. O mecanismo citado nos vídeos existe em tecido '
                                                'de coelho: os ginsenosídeos liberam óxido nítrico, o que '
                                                'não é o mesmo mecanismo da tadalafila. Não localizei o '
                                                'estudo de 2021 com 847 amostras nem estudo humano de '
                                                'ginseng desfazendo fibrose no pênis. No Brasil, há '
                                                'fitoterápicos de ginseng registrados, nenhum para ereção.',
                                      'alerta': 'No Brasil, o Panax ginseng não está na lista de '
                                                'constituintes autorizados para suplemento alimentar; existe '
                                                'como medicamento fitoterápico registrado, para fadiga, e '
                                                'não para disfunção erétil. A monografia europeia limita o '
                                                'uso tradicional a 3 meses, não o recomenda na gravidez e na '
                                                'lactação e registra insônia, desconforto gástrico e '
                                                'alergia. Quem tem disfunção erétil pode ter doença vascular '
                                                'por trás: o ginseng não substitui avaliação médica.'},
 'proprio_glicerol': {'nome': 'Glicerol em pó (hiper-hidratação)',
                      'categoria': 'primaria',
                      'aprovado': 'nao',
                      'tagline': 'A agência antidoping tirou o glicerol da lista em 2018 porque o efeito no '
                                 'volume de sangue era "mínimo", não porque a detecção melhorou; e o estudo '
                                 'de 1990 do grupo citado viu suor maior, não menor.',
                      'resumo': 'Glicerol tomado com bastante água faz o corpo reter mais líquido: uma '
                                'meta-análise achou 7,7 mL por kg a mais que com água pura. A revisão citada '
                                'nos vídeos é da Universidade do Novo México, e o estudo de 1990 do mesmo '
                                'grupo mostrou, em 6 pessoas, suor maior e temperatura menor. No desempenho, '
                                'a meta-análise achou +2,62% com 4 estudos, e três ensaios de 2023 a 2025 '
                                'não acharam ganho. A agência antidoping o proibiu como expansor de plasma '
                                'em 2010 e o liberou em 2018 por considerar o efeito mínimo. Nenhum estudo '
                                'testou "pump", hipertrofia ou "pele seca". No Brasil, glicerol não é '
                                'constituinte autorizado de suplemento.',
                      'alerta': 'Glicerol não está na lista de constituintes autorizados para suplemento '
                                'alimentar no Brasil; no país, ele é princípio ativo de enemas, de nutrição '
                                'na veia e de colírios. Em dose alta, já foi remédio para edema cerebral e '
                                'glaucoma, porque puxa água por osmose. Os efeitos colaterais relatados são '
                                'náusea, desconforto intestinal, tontura e dor de cabeça. Quem tem doença do '
                                'coração, dos rins ou controla sódio não deve fazer hiper-hidratação com '
                                'glicerol e sal sem médico (inferência minha; não achei estudo nesses '
                                'grupos).'},
 'proprio_glicina_sono_gh': {'nome': 'Glicina antes de dormir (sono e GH)',
                             'categoria': 'primaria',
                             'aprovado': 'nao',
                             'tagline': 'O "70% do GH" não é aumento: é a parte do GH do homem que sai no '
                                        'começo do sono; nenhum estudo de glicina antes de dormir mediu GH.',
                             'resumo': 'A glicina é o aminoácido mais simples, fabricado pelo próprio corpo. '
                                       'Dois estudos japoneses, feitos com pesquisadores de uma fabricante '
                                       'de glicina, deram 3 g antes de dormir e viram adormecer mais rápido, '
                                       'chegar antes ao sono profundo e menos sonolência no dia seguinte. A '
                                       'explicação pela queda de temperatura e pelo núcleo supraquiasmático '
                                       'vem de ratos. O "70%" dos vídeos é um dado de fisiologia: em homens, '
                                       'cerca de 70% do GH diário sai no começo do sono. Nenhum estudo mediu '
                                       'GH no sono depois de glicina. O estudo de 1978 citado para o "pico '
                                       'que quase triplica" existe, mas não traz 22 g nem a palavra triplica '
                                       'no resumo. No Brasil, o máximo de glicina em suplemento é 2.980 mg '
                                       'por dia, só para adultos.',
                             'alerta': 'Os 3 g por dia que circulam ficam um pouco acima do máximo que a '
                                       'ANVISA permite em suplemento (2.980 mg por dia, só para maiores de '
                                       '19 anos), e os 22 g ficam muito acima. Pela regra brasileira, '
                                       'suplemento de glicina não é autorizado para crianças, adolescentes, '
                                       'gestantes e lactantes. A evidência de sono vem de estudos pequenos, '
                                       'assinados pelo mesmo grupo de autores, que inclui um pesquisador de '
                                       'uma fabricante de glicina.'},
 'proprio_glifosato_transgenicos': {'nome': 'Glifosato e alimentos transgênicos',
                                    'categoria': 'primaria',
                                    'aprovado': 'nao',
                                    'tagline': 'O "−35% de testosterona" vem de células de rato numa placa '
                                               'de cultura; em homens, nenhum estudo ligou glifosato ou '
                                               'transgênico a testosterona baixa.',
                                    'resumo': 'O selo amarelo com "T" avisa que o alimento tem mais de 1% de '
                                              'ingrediente transgênico; não diz nada sobre glifosato. O '
                                              'glifosato é o agrotóxico mais vendido no Brasil (231.888 '
                                              'toneladas em 2024) e aparece na urina de 4 em cada 5 '
                                              'americanos testados. Em células de testículo de rato, a '
                                              'formulação comercial matou células e, em concentração baixa, '
                                              'derrubou a testosterona em 35%. Em gente, os estudos são '
                                              'transversais e não acham a queda de testosterona em homens. A '
                                              'IARC chamou o glifosato de provável cancerígeno; as agências '
                                              'do Brasil, da Europa e dos EUA não. Comer orgânico baixou o '
                                              'glifosato da urina em dias.',
                                    'alerta': 'Esta página trata de exposição, não de suplemento. Evitar o '
                                              'selo transgênico ou comprar orgânico não é tratamento de '
                                              'testosterona baixa, e nenhum estudo mediu se isso muda a '
                                              'testosterona. Quem tem mais risco real com o glifosato é quem '
                                              'o aplica: a ANVISA registrou intoxicações agudas graves, '
                                              'sobretudo em trabalhadores rurais. Queixa de libido, ereção '
                                              'ou fertilidade pede avaliação médica.'},
 'proprio_gordura_corporal_penis_enterrado': {'nome': 'Gordura corporal, "pênis enterrado" e aromatase',
                                              'categoria': 'primaria',
                                              'aprovado': 'nao',
                                              'tagline': 'Em 778 homens, o IMC só se associou ao comprimento '
                                                         'medido a partir da pele, não do osso: a gordura '
                                                         'esconde, não encolhe. Os "2,3 cm" e "1 a 3 cm a '
                                                         'cada 10 kg" não estão nas fontes citadas.',
                                              'resumo': 'A gordura sobre o osso púbico esconde parte do '
                                                        'pênis, e isso tem nome e medida. Num estudo com 778 '
                                                        'homens, o IMC se associou ao comprimento ereto '
                                                        'medido da pele até a ponta, mas não ao medido do '
                                                        'osso até a ponta. O pênis enterrado adquirido do '
                                                        'adulto é uma condição real, ligada sobretudo à '
                                                        'obesidade grave, e tratada com cirurgia. Os números '
                                                        'dos vídeos — 2,3 cm escondidos, 1 a 3 cm a cada 10 '
                                                        'a 12 kg, 1,5 a 3 cm perdidos por ereção incompleta '
                                                        '— não estão nas fontes citadas. A obesidade é o '
                                                        'maior fator de risco de testosterona baixa no '
                                                        'homem, e perder peso sobe a testosterona numa '
                                                        'meta-análise de 24 estudos. A ideia de atacar a '
                                                        'aromatase com suplementos não tem apoio, e os '
                                                        'inibidores de aromatase estão na Lista Proibida da '
                                                        'WADA.',
                                              'alerta': 'Esta página trata de gordura corporal, não de '
                                                        'suplemento. O pênis enterrado de verdade, que '
                                                        'dificulta urinar e higienizar e causa feridas na '
                                                        'pele, é condição médica tratada por urologista, '
                                                        'muitas vezes com cirurgia. Inibidores de aromatase '
                                                        'são remédios de prescrição, não recomendados para a '
                                                        'testosterona baixa da obesidade, e proibidos no '
                                                        'esporte; alguns "bloqueadores de aromatase" '
                                                        'vendidos como suplemento estão na mesma lista. '
                                                        'Queixa de pênis pequeno com medida dentro do normal '
                                                        'pede conversa com profissional, não procedimento.'},
 'proprio_gordura_na_dieta_1977': {'nome': 'Gordura na dieta e testosterona (a "diretriz de 1977")',
                                   'categoria': 'primaria',
                                   'aprovado': 'nao',
                                   'tagline': 'Em ensaios pequenos, dietas com 25% de gordura ou menos '
                                              'deixaram a testosterona 12% a 13% menor; o "21% em 1996" não '
                                              'está no estudo de 1996, e a meta de 1977 era 30% de gordura, '
                                              'não zero.',
                                   'resumo': 'Os vídeos dizem que uma diretriz de 1977 mandou cortar '
                                             'gordura, que isso cortou a "matéria-prima" da testosterona e '
                                             'que um estudo de 1996 mediu queda de 21%. O documento de 1977 '
                                             'existe: é um relatório de uma comissão do Senado americano que '
                                             'propôs baixar a gordura de cerca de 40% para cerca de 30% das '
                                             'calorias. O estudo de 1996 também existe, com 43 homens, e '
                                             'achou testosterona total 13% maior na dieta rica em gordura, '
                                             'sem significância estatística. Outro ensaio achou queda de '
                                             '12%. Uma meta-análise de 6 estudos achou queda; outra, de 11 '
                                             'ensaios, não achou diferença. Nenhum estudo liga a diretriz à '
                                             'testosterona de uma geração.',
                                   'alerta': 'Esta página trata de alimentação, não de suplemento. Mudar a '
                                             'gordura da dieta não é tratamento de testosterona baixa, e uma '
                                             'dieta de corte com pouca comida também baixa o hormônio, por '
                                             'outro caminho. Reduzir gordura saturada diminuiu eventos '
                                             'cardiovasculares em ensaios longos; quem tem colesterol alto, '
                                             'doença do coração ou usa estatina não deve trocar a dieta ou '
                                             'parar o remédio por causa de vídeo. Queixa de libido, ereção '
                                             'ou cansaço pede avaliação médica.'},
 'proprio_huperzina_a': {'nome': 'Huperzina A ("dobro de força" em 7 dias)',
                         'categoria': 'primaria',
                         'aprovado': 'nao',
                         'tagline': 'Nenhum estudo mediu força com huperzina A; o ensaio financiado pelo '
                                    'instituto americano do envelhecimento, com 210 pacientes de Alzheimer, '
                                    'falhou no desfecho principal.',
                         'resumo': 'A huperzina A é um alcaloide da planta Huperzia serrata que bloqueia a '
                                   'enzima que destrói a acetilcolina, como os remédios de Alzheimer. É '
                                   'medicamento licenciado na China e vendida como suplemento nos Estados '
                                   'Unidos. Em Alzheimer, ensaios chineses pequenos e de qualidade baixa '
                                   'sugerem melhora; o maior ensaio ocidental, com 210 pacientes e '
                                   'financiamento público americano, não achou efeito na dose principal. Em '
                                   'pessoas saudáveis, não melhorou a cognição num estudo com militares. '
                                   'Nenhum estudo mediu força muscular. A meia-vida em pessoas é de cerca de '
                                   '12 horas e o pico no sangue vem em cerca de uma hora, não em 2 a 4. No '
                                   'Brasil, não é constituinte autorizado de suplemento e não tem '
                                   'medicamento registrado.',
                         'alerta': 'A huperzina A é inibidora de acetilcolinesterase, a mesma classe da '
                                   'donepezila, da rivastigmina e da galantamina. Junto com esses remédios, '
                                   'pode somar efeitos colaterais. Nos ensaios, os efeitos foram leves: '
                                   'náusea, tontura, dor de cabeça, visão turva. Pela farmacologia da '
                                   'classe, quem tem frequência cardíaca baixa, asma ou doença obstrutiva '
                                   'dos pulmões deve falar com o médico antes — isso é inferência minha, '
                                   'porque não há bula de huperzina para ler. No Brasil, ela não é '
                                   'ingrediente autorizado de suplemento.'},
 'proprio_ioimbina': {'nome': 'Ioimbina (cloridrato de ioimbina; casca de Pausinystalia)',
                      'categoria': 'primaria',
                      'aprovado': 'parcial',
                      'tagline': 'O estudo de 86 homens com 71% contra 45% existe; o que não se diz é que, '
                                 'na disfunção de causa orgânica, a ioimbina mal supera o placebo.',
                      'resumo': 'A ioimbina é um alcaloide da casca de uma árvore africana que bloqueia '
                                'receptores alfa-2 adrenérgicos. O ensaio citado nos vídeos existe: 86 '
                                'homens sem causa orgânica clara, 30 mg por dia por 8 semanas, resposta de '
                                '71% contra 45%. A meta-análise de 1998, com 7 ensaios, achou vantagem sobre '
                                'o placebo. Mas na disfunção de causa orgânica os resultados foram marginais '
                                'ou nulos, e a associação americana de urologia não a recomendou em 1996. Em '
                                'suplementos, o teor variou de nada a 12,1 mg por dose, e há mortes e um '
                                'derrame cerebral relatados.',
                      'alerta': 'A ioimbina sobe a pressão e pode causar ansiedade, sobretudo em doses '
                                'altas. Há relatos de morte por intoxicação e de hemorragia cerebral depois '
                                'de um suplemento com ioimbina em uma pessoa que usava clonidina e '
                                'antidepressivos. Em suplementos vendidos nos EUA, o teor real variou de '
                                'zero a 12,1 mg por dose e raramente batia com o rótulo. No Brasil, a '
                                'ioimbina não é constituinte autorizado de suplemento; existe como '
                                'medicamento registrado.'},
 'proprio_jejum_gh_autofagia': {'nome': 'Jejum de 24 horas e jejum intermitente de 16 horas (GH, autofagia e '
                                        'testosterona)',
                                'categoria': 'primaria',
                                'aprovado': 'nao',
                                'tagline': 'O "+2.000% de GH" veio de uma notícia sobre um congresso; o '
                                           'estudo publicado tinha 30 voluntários, só 10 homens, e o GH '
                                           'deles partia de quase zero.',
                                'resumo': 'O jejum aumenta o GH: isso está medido desde os anos 1980, em '
                                          'jejuns de 1 a 5 dias. O "2.000%" dos vídeos saiu de uma notícia '
                                          'de 2011 sobre uma apresentação em congresso; no ensaio publicado, '
                                          'eram 30 voluntários, 20 mulheres e 10 homens, e o GH basal dos '
                                          'homens tinha mediana de 0,04 ng/mL, o que faz qualquer subida '
                                          'virar um percentual enorme. Durante o jejum, o IGF-1, que é o '
                                          'braço anabólico do GH, cai. A autofagia rendeu o Nobel de 2016 '
                                          'por trabalhos em levedura; em gente, um ensaio de 2025 diz que o '
                                          'efeito do jejum nunca tinha sido mostrado. O jejum de 16 horas '
                                          'não emagreceu mais que comer em horário normal em dois ensaios, '
                                          'não reduziu gordura visceral em outro e baixou a testosterona de '
                                          'homens treinados.',
                                'alerta': 'Jejum é intervenção com risco para quem usa insulina ou remédio '
                                          'que baixa a glicose: num ensaio com diabéticos tipo 2, o jejum '
                                          'dobrou a taxa de hipoglicemia mesmo com redução do remédio. Quem '
                                          'tem ou teve transtorno alimentar não foi estudado. Em homens '
                                          'magros e treinados, o jejum de 16 horas baixou a testosterona. '
                                          'Nenhum ensaio mediu morte ou infarto com jejum intermitente.'},
 'proprio_l_arginina': {'nome': 'L-arginina (inclui aspartato e cloridrato de arginina)',
                        'categoria': 'primaria',
                        'aprovado': 'nao',
                        'tagline': 'As doses de 5 a 9 g que circulam passam do máximo de 3,81 g por dia que '
                                   'a ANVISA permite em suplemento, e o GH extra não virou músculo em nenhum '
                                   'estudo que localizei.',
                        'resumo': 'A L-arginina é o aminoácido que a enzima do óxido nítrico usa como '
                                  'matéria-prima. Tomada por boca, só cerca de 20% de uma dose de 10 g chega '
                                  'ao sangue. Em disfunção erétil leve a moderada, uma meta-análise de 10 '
                                  'ensaios achou benefício, e os inibidores de PDE5 continuam melhores. O '
                                  'estudo de 1981 citado para o "GH 2,7 vezes maior" usou lisina com '
                                  'arginina, não ornitina, e o resumo não traz esse número. Os ensaios de '
                                  'força com 6 g antes do treino não acharam ganho. No Brasil, o máximo em '
                                  'suplemento é 3.810 mg por dia, só para adultos.',
                        'alerta': 'Doses de 5 a 9 g por dia passam do limite de 3.810 mg que a ANVISA fixa '
                                  'para suplemento, e a arginina em suplemento não é autorizada para '
                                  'gestantes, lactantes e menores de 19 anos. Num ensaio em pessoas que '
                                  'tinham acabado de infartar, 6 dos que tomavam arginina morreram em 6 '
                                  'meses, contra nenhum no placebo, e o estudo foi interrompido. A arginina '
                                  'baixa alguns mmHg da pressão; somar isso a tadalafila, nitrato ou remédio '
                                  'de pressão é inferência minha, sem estudo que eu tenha achado sobre essa '
                                  'soma.'},
 'proprio_l_citrulina': {'nome': 'L-citrulina (inclui citrulina malato)',
                         'categoria': 'primaria',
                         'aprovado': 'nao',
                         'tagline': 'O único ensaio de L-citrulina sozinha em disfunção erétil tem 24 '
                                    'homens, usou 1,5 g por dia e não mediu o tamanho do pênis.',
                         'resumo': 'A L-citrulina é um aminoácido que o próprio corpo fabrica e que vira '
                                   'arginina e, depois, óxido nítrico. Em disfunção erétil, o PubMed devolve '
                                   '42 artigos e só um marcado como ensaio randomizado ou meta-análise, e '
                                   'ele testa uma mistura, não a citrulina sozinha. O estudo de 2011 citado '
                                   'nos vídeos existe: 24 homens com disfunção leve, 1,5 g por dia, metade '
                                   'melhorou a dureza da ereção, contra 8,3% com placebo. Ele não mediu '
                                   'centímetros. No treino, as meta-análises acham efeito pequeno ou nenhum. '
                                   'No Brasil, a L-citrulina não consta da lista de constituintes '
                                   'autorizados em suplemento alimentar.',
                         'alerta': 'A L-citrulina e a citrulina malato não aparecem na lista de '
                                   'constituintes autorizados para suplemento alimentar no Brasil (IN '
                                   '28/2018, consolidada até setembro de 2026). Uma meta-análise de 2025 '
                                   'achou queda de pressão em adultos de meia-idade e idosos. Quem usa '
                                   'tadalafila, nitrato ou remédio de pressão pode somar efeitos: isso é '
                                   'inferência minha, e não achei estudo publicado que tenha medido essa '
                                   'soma.'},
 'proprio_l_glutamina_gh': {'nome': 'L-glutamina e hormônio do crescimento',
                            'categoria': 'primaria',
                            'aprovado': 'nao',
                            'tagline': 'O estudo de 1995 existe: 9 pessoas, 2 g num refrigerante, sem bebida '
                                       'placebo; o resumo diz só que o GH estava "elevado" aos 90 minutos, e '
                                       'o efeito nunca virou músculo em quem treina.',
                            'resumo': 'O estudo citado é real: em 1995, 9 voluntários saudáveis tomaram 2 g '
                                      'de glutamina num refrigerante de cola, 45 minutos depois de um café '
                                      'da manhã leve, e aos 90 minutos o GH e o bicarbonato estavam mais '
                                      'altos que numa medida feita uma semana antes. O resumo não traz "4 '
                                      'vezes", "400%" nem faixa de idade, e não consegui abrir o texto '
                                      'completo. Não achei repetição com glutamina sozinha. Com mais '
                                      'glutamina e por semanas, o treino de força não rendeu mais, e a dose '
                                      'de bicarbonato da glutamina não mudou o desempenho num teste de '
                                      'esforço máximo. No Brasil, o máximo em suplemento é 5 g por dia.',
                            'alerta': 'A ANVISA permite glutamina em suplemento só para maiores de 19 anos, '
                                      'até 5.000 mg por dia; para gestantes, lactantes e crianças, não é '
                                      'autorizada. No maior ensaio em pacientes de UTI, glutamina em dose '
                                      'alta, na veia e por sonda, aumentou a mortalidade. Um pico isolado de '
                                      'GH não é tratamento nem aumenta músculo; quem suspeita de falta de GH '
                                      'precisa de médico.'},
 'proprio_l_ornitina': {'nome': 'L-ornitina (cloridrato de L-ornitina)',
                        'categoria': 'primaria',
                        'aprovado': 'nao',
                        'tagline': 'O estudo de 1990 citado nos vídeos deu a dose em jejum de manhã, não à '
                                   'noite; o "2,7 vezes" de 1981 é de arginina com lisina, sem ornitina.',
                        'resumo': 'A L-ornitina é um aminoácido que o corpo usa no ciclo da ureia. A '
                                  'promessa de que ela "dispara" o hormônio do crescimento vem de um estudo '
                                  'de 1990 com 12 fisiculturistas: só a dose de 170 mg por quilo subiu o GH, '
                                  'e só aos 90 minutos. O estudo de 1981 citado ao lado dela testou arginina '
                                  'com lisina. Uma revisão de 2002 concluiu que doses orais capazes de subir '
                                  'o GH tendem a dar desconforto no estômago e diarreia, e que nenhum estudo '
                                  'adequado mostrou mais músculo por isso. Subidas de GH depois do treino '
                                  'não aumentaram a síntese de proteína muscular. No Brasil, a L-ornitina '
                                  'não consta da lista de constituintes autorizados de suplemento.',
                        'alerta': 'A L-ornitina não consta da lista de constituintes autorizados em '
                                  'suplemento alimentar no Brasil (IN 28/2018, consolidada até setembro de '
                                  '2026). Os cerca de 13 g por dose que circulam ficam acima dos 12.000 mg '
                                  'por dia que uma revisão de segurança de 2025 estimou como nível sem '
                                  'efeito adverso observado, e o efeito colateral mais relatado é '
                                  'gastrointestinal. Pessoas com doença genética do metabolismo da ornitina, '
                                  'como a atrofia girata, têm ornitina alta no sangue.'},
 'proprio_lactobacillus_reuteri': {'nome': 'Limosilactobacillus reuteri (cepa ATCC PTA 6475)',
                                   'categoria': 'primaria',
                                   'aprovado': 'nao',
                                   'tagline': 'Os testículos maiores e a testosterona alta são de '
                                              'camundongos; no único ensaio com placebo em homens de 55 a 65 '
                                              'anos, a mesma cepa não mudou a testosterona.',
                                   'resumo': 'Limosilactobacillus reuteri é uma bactéria do intestino e do '
                                             'leite humano, vendida como probiótico. A cepa ATCC PTA 6475 '
                                             'ficou famosa por um estudo de 2014 do MIT, em camundongos: os '
                                             'que beberam a bactéria na água tiveram testículos maiores, '
                                             'mais células de Leydig e testosterona mais alta na velhice, e '
                                             'bloquear a interleucina-17A reproduziu o efeito. Em pessoas, o '
                                             'resultado foi outro. Num ensaio randomizado de 12 semanas em '
                                             'homens de 55 a 65 anos, a cepa não mudou a testosterona, em '
                                             'dose alta nem baixa; um piloto japonês com 10 pessoas também '
                                             'não viu mudança notável. No Brasil, a cepa entrou em 2026 na '
                                             'lista de suplementos, só associada a outra e só com alegação '
                                             'intestinal.',
                                   'alerta': 'No Brasil, a única forma autorizada da cepa ATCC PTA 6475 em '
                                             'suplemento é a associação com a DSM 17938, para adultos, e o '
                                             'rótulo deve dizer que gestantes, lactantes, lactentes, '
                                             'crianças, pessoas imunocomprometidas e pessoas com doença '
                                             'debilitante grave não devem consumir. A única alegação '
                                             'permitida é a de contribuir com a saúde do trato '
                                             'gastrointestinal. Iogurte caseiro "cultivado" com a bactéria '
                                             'não tem dose nem controle de contaminação, e não há estudo '
                                             'dele.'},
 'proprio_luz_vermelha_fotobiomodulacao': {'nome': 'Luz vermelha (fotobiomodulação, 660–670 nm) e luz azul '
                                                   'de LED',
                                           'categoria': 'primaria',
                                           'aprovado': 'nao',
                                           'tagline': 'O "+33,5% de testosterona" com laser não foi '
                                                      'localizado; no único ensaio randomizado que mediu '
                                                      'testosterona após luz no corpo inteiro, ela não '
                                                      'mudou.',
                                           'resumo': 'A fotobiomodulação usa luz vermelha ou infravermelha '
                                                     'de baixa potência, e a hipótese mais aceita é que ela '
                                                     'age na enzima citocromo c oxidase da mitocôndria. Para '
                                                     'testosterona em homens, a evidência é quase nula: o '
                                                     'único ensaio randomizado localizado, com 13 atletas e '
                                                     'luz no corpo inteiro, não mudou a testosterona. Em '
                                                     'camundongos com testículo lesado pelo calor, a luz '
                                                     'recuperou espermatogênese e testosterona. Os estudos '
                                                     'citados nos vídeos, de 2013 em ratos e de 2018 em '
                                                     'homens com "+33,5%", não foram localizados. A luz azul '
                                                     'suprime a melatonina à noite, mas de dia, em jovens '
                                                     'privados de sono, ela devolveu a testosterona ao '
                                                     'normal.',
                                           'alerta': 'Esta página trata de luz e aparelhos, não de '
                                                     'suplemento. Luz vermelha não é tratamento aprovado de '
                                                     'testosterona baixa, e não há estudo em homens '
                                                     'mostrando que ela suba o hormônio. Aparelhos de laser '
                                                     'e de LED intenso podem lesar os olhos; não aponte para '
                                                     'o rosto sem proteção. Queixa de libido, ereção ou '
                                                     'testosterona baixa pede dosagem e avaliação médica.'},
 'proprio_maca_peruana': {'nome': 'Maca peruana (Lepidium meyenii)',
                          'categoria': 'primaria',
                          'aprovado': 'nao',
                          'tagline': 'Aqui o vídeo acerta o principal: em ensaios controlados, a maca '
                                     'melhorou o desejo sem mexer na testosterona. Mas os ciclistas não '
                                     'bateram o placebo, e a fertilidade não se confirmou.',
                          'resumo': 'A maca é a raiz de uma planta dos Andes peruanos. Ao contrário da '
                                    'maioria dos suplementos vendidos para homens, ela não promete hormônio, '
                                    'e os ensaios confirmam: em homens saudáveis, 1,5 a 3 g por dia por 12 '
                                    'semanas melhoraram o desejo sexual a partir da 8ª semana sem alterar '
                                    'testosterona, estradiol, LH ou FSH. A base é pequena: uma revisão de '
                                    '2010 achou 4 ensaios e chamou a evidência de "limitada". Os ciclistas '
                                    'melhoraram contra a própria linha de base, não contra o placebo. Na '
                                    'fertilidade, os ensaios com placebo são mistos, e uma meta-análise de '
                                    '2022 não achou efeito na concentração de espermatozoides. As diferenças '
                                    'entre maca amarela, vermelha e preta vêm de estudos em ratos.',
                          'alerta': 'A maca não tem efeito comprovado sobre testosterona e não substitui '
                                    'tratamento de disfunção erétil, que os estudos com maca mostraram '
                                    'melhorar pouco. As alegações sobre cores (vermelha para a próstata, '
                                    'preta para os espermatozoides) vêm de estudos em ratos. Há um relato de '
                                    'síndrome das pernas inquietas na combinação de maca com o '
                                    'antidepressivo mianserina. No Brasil, a maca não consta da lista de '
                                    'constituintes de suplemento alimentar.'},
 'proprio_magnesio': {'nome': 'Magnésio (treonato e cloreto P.A.)',
                      'categoria': 'primaria',
                      'aprovado': 'nao',
                      'tagline': 'O "+24% de testosterona livre" não está no resumo do estudo citado, o '
                                 '"P.A." do cloreto é grau de reagente e, no Brasil, o máximo em suplemento '
                                 'é 350 mg por dia.',
                      'resumo': 'O magnésio é um mineral essencial, cofator de centenas de reações. Daí não '
                                'se segue que tomar mais dê mais testosterona. O estudo turco citado nos '
                                'vídeos existe, mas o resumo não traz percentual, não menciona SHBG e '
                                'descreve 10 mg por quilo por dia, dose que, para um adulto, passa do teto '
                                'brasileiro. A meta-análise de força não achou efeito em atletas, a revisão '
                                'Cochrane não achou efeito em câimbra de idosos e as revisões sobre sono '
                                'classificam a evidência como de certeza baixa ou muito baixa. O treonato '
                                'foi desenvolvido em estudo com ratos e não consta da lista brasileira de '
                                'fontes de magnésio. No Brasil, o máximo em suplemento é 350 mg por dia para '
                                'adultos.',
                      'alerta': 'O magnésio de suplemento tem teto: 350 mg por dia para adultos no Brasil, o '
                                'mesmo valor do limite superior americano para magnésio que não vem da '
                                'comida, porque acima disso o primeiro efeito é diarreia. Quem tem doença '
                                'renal pode acumular magnésio no sangue, situação que pode ser grave. '
                                'Antiácidos com magnésio reduzem muito a absorção dos antibióticos do grupo '
                                'das quinolonas. "P.A." quer dizer "para análise", o grau de reagente de '
                                'laboratório; a norma de suplemento exige fonte que cumpra especificação de '
                                'farmacopeia ou de código alimentar.'},
 'proprio_maitake_glicose': {'nome': 'Maitake (Grifola frondosa) e glicose',
                             'categoria': 'primaria',
                             'aprovado': 'nao',
                             'tagline': 'Os "30% a 63%" vêm de 7 voluntários sem grupo controle, que também '
                                        'tomavam remédio para diabetes; não há ensaio randomizado de maitake '
                                        'em diabetes no PubMed.',
                             'resumo': 'O maitake é um cogumelo comestível (Grifola frondosa). A promessa de '
                                       'baixar a glicose "em até 63%" vem de uma série de 7 voluntários com '
                                       'diabetes tipo 2 descrita por um pesquisador de Nova York: um '
                                       'comprimido de uma fração do cogumelo três vezes ao dia por 4 '
                                       'semanas, sem grupo controle, em pessoas que também tomavam remédio '
                                       'oral para diabetes. O "−25% em 4 dias" é de camundongos. No PubMed, '
                                       'nenhum ensaio randomizado de maitake mediu glicose, e no '
                                       'ClinicalTrials.gov não há registro em diabetes. No Brasil, o maitake '
                                       'não consta da lista de constituintes de suplemento.',
                             'alerta': 'Quem tem diabetes e usa remédio não deve somar ou trocar tratamento '
                                       'por maitake por conta própria: na série de casos que deu origem aos '
                                       'números, todos tomavam remédio oral, e o primeiro paciente usava uma '
                                       'sulfonilureia, classe que causa hipoglicemia. Um relato de caso de '
                                       '2010 descreve aumento do INR com extrato de maitake em quem usava '
                                       'varfarina. O maitake não consta da lista de constituintes '
                                       'autorizados em suplemento no Brasil.'},
 'proprio_moringa': {'nome': 'Moringa (folha de Moringa oleifera)',
                     'categoria': 'primaria',
                     'aprovado': 'nao',
                     'tagline': 'No Brasil, alimento com moringa é proibido desde 2019, e a ANVISA reafirmou '
                                'isso em setembro de 2026; a meta-análise de 9 ensaios não achou benefício '
                                'consistente.',
                     'resumo': 'A moringa é uma árvore de origem indiana cujas folhas têm proteína, '
                               'vitaminas, flavonoides e glucosinolatos. No Brasil, a ANVISA proibiu em 2019 '
                               'a fabricação, a venda e a propaganda de qualquer alimento com Moringa '
                               'oleifera, porque a segurança do uso como alimento não foi comprovada, e '
                               'citou essa proibição numa apreensão de 15 de setembro de 2026. Em gente, a '
                               'meta-análise de 2025 com 9 ensaios randomizados não achou efeito na maioria '
                               'dos desfechos cardiometabólicos, com certeza muito baixa. Para músculo, há '
                               'um piloto chinês com 44 homens jovens: mais flexões e mais tempo na esteira '
                               'em 30 dias. Ninguém mediu síntese proteica, e a ação diurética vem de '
                               'semente, em rato.',
                     'alerta': 'No Brasil, a venda de chá, cápsula, pó ou qualquer alimento com moringa é '
                               'proibida desde 2019; a ANVISA diz que a segurança do uso como alimento não '
                               'foi comprovada. Em ratos, o extrato da folha foi genotóxico na dose de 3.000 '
                               'mg/kg. Há relatos de síndrome de Stevens-Johnson, anafilaxia e erupção na '
                               'pele depois de consumir a folha. Em 2026, um suplemento importado de moringa '
                               'foi proibido no Brasil por estar ligado a um surto de Salmonella nos Estados '
                               'Unidos.'},
 'proprio_mucuna_pruriens_l_dopa': {'nome': 'Mucuna pruriens (feijão-veludo; fonte de L-dopa), com vitamina '
                                            'B6 e chá verde',
                                    'categoria': 'primaria',
                                    'aprovado': 'nao',
                                    'tagline': 'O "+878% de GH" é de 15 homens, sem placebo, com uma mistura '
                                               'de duas plantas, e o pico não passou de 2 ng/mL. E a '
                                               'vitamina B6 junto anula o efeito da L-dopa.',
                                    'resumo': 'A semente de Mucuna pruriens contém levodopa (L-dopa), o '
                                              'mesmo remédio usado no Parkinson e num teste hospitalar '
                                              'antigo de hormônio do crescimento (GH). O "+878%" dos vídeos '
                                              'existe: é de um estudo de 2011 com 15 homens, sem grupo '
                                              'placebo, com uma mistura de mucuna e outra planta, financiado '
                                              'em parte por uma empresa de suplementos; o GH foi de 0,18 '
                                              'para 1,76 ng/mL. A vitamina B6 vendida como protetora faz o '
                                              'contrário: sem um bloqueador como a carbidopa, ela acelera a '
                                              'destruição da L-dopa fora do cérebro e, num estudo de 1975, '
                                              'inibiu a subida do GH. Mucuna é L-dopa, com as mesmas '
                                              'interações e efeitos adversos.',
                                    'alerta': 'A mucuna contém levodopa, um medicamento de prescrição com '
                                              'interações graves: é contraindicada com inibidores não '
                                              'seletivos da MAO e em glaucoma de ângulo fechado, e pode '
                                              'causar náusea, queda de pressão, alucinações, sonolência '
                                              'súbita e compulsões. A vitamina B6 em doses de 10 a 25 mg '
                                              'pode reverter o efeito da levodopa sem carbidopa. A mucuna '
                                              'não é constituinte autorizado de suplemento no Brasil. Quem '
                                              'tem Parkinson não deve trocar o remédio por mucuna sem o '
                                              'neurologista.'},
 'proprio_muira_puama': {'nome': 'Muira puama (Ptychopetalum olacoides, marapuama)',
                         'categoria': 'primaria',
                         'aprovado': 'nao',
                         'tagline': 'O "62% em 14 dias" vem de uma apresentação em congresso de 1990 que não '
                                    'está no PubMed; nenhum ensaio com placebo testou a raiz sozinha, e no '
                                    'Brasil não há produto ativo.',
                         'resumo': 'A muira puama, ou marapuama, é uma árvore amazônica cuja raiz é usada '
                                   'como tônico e afrodisíaco. O PubMed tem 51 artigos com o nome da planta '
                                   'no título ou no resumo, nenhum ensaio randomizado e nenhuma '
                                   'meta-análise; quase tudo é química e teste em camundongo. O estudo '
                                   'francês com 262 homens e "62% de efeito na libido" é uma apresentação em '
                                   'congresso de 1990, aberta e sem placebo, que não consegui ler. Os '
                                   'estudos humanos indexados testaram misturas: com ginkgo em 202 mulheres, '
                                   'sem grupo controle, e com gengibre, guaraná e citrulina em 54 homens, '
                                   'dos quais 16 chegaram ao fim. No Brasil, onze medicamentos já tiveram a '
                                   'planta na fórmula; todos estão com registro inativo, e ela não é '
                                   'constituinte autorizado de suplemento.',
                         'alerta': 'Não há estudo de segurança da muira puama sozinha em pessoas. Em '
                                   'camundongos, o extrato teve efeito ansiogênico e inibiu a enzima que '
                                   'degrada a acetilcolina, o que sugere ação no sistema nervoso central. O '
                                   'nome popular marapuama cobre plantas diferentes: no Nordeste, ele é '
                                   'usado para espécies de Croton, e dois fitoterápicos ativos no Brasil '
                                   'trazem Croton, não Ptychopetalum. Comprar "marapuama" não garante qual '
                                   'raiz vem no pacote.'},
 'proprio_nac_n_acetilcisteina': {'nome': 'NAC (N-acetilcisteína)',
                                  'categoria': 'primaria',
                                  'aprovado': 'nao',
                                  'tagline': 'A FDA mandou cartas a 7 empresas de produtos "contra ressaca" '
                                             'em 2020, não a centenas; no Brasil, NAC é remédio e também '
                                             'fonte de cisteína em suplemento.',
                                  'resumo': 'A N-acetilcisteína é um remédio antigo: mucolítico e antídoto '
                                            'da intoxicação por paracetamol, porque repõe a glutationa do '
                                            'fígado. Nos vídeos, ela "blinda o eixo hormonal". Em homens '
                                            'inférteis, três ensaios somados mostraram sêmen um pouco '
                                            'melhor, mas sem mudança na testosterona; o maior ensaio a '
                                            'favor, iraniano, recebeu nota de preocupação da revista em '
                                            '2023. No esporte, o ganho médio foi de 0,29%, sem '
                                            'significância. A história americana é real em parte: a FDA '
                                            'aprovou a NAC como remédio em 1963 e, por isso, a excluiu da '
                                            'definição de suplemento; em 2022 passou a tolerar a venda. No '
                                            'Brasil, é remédio registrado e consta da lista de fontes de '
                                            'cisteína para suplemento.',
                                  'alerta': 'A NAC é medicamento: a bula americana lista náusea, vômito, '
                                            'estomatite, febre, coriza, sonolência e broncoconstrição, e '
                                            'pede vigilância em asmáticos. No Brasil, o comprimido '
                                            'efervescente e o granulado de até 600 mg são vendidos sem '
                                            'receita como expectorante; isso não faz deles tratamento para '
                                            'testosterona ou fertilidade. Em homens inférteis, procurar '
                                            'urologista ou andrologista antes de tomar antioxidante por '
                                            'conta própria: a revisão Cochrane classifica a evidência como '
                                            'de certeza muito baixa.'},
 'proprio_niacina_gh': {'nome': 'Niacina (ácido nicotínico) e hormônio do crescimento',
                        'categoria': 'primaria',
                        'aprovado': 'nao',
                        'tagline': 'O estudo de 2008 existe: 7 homens, 2 g de ácido nicotínico em 4 horas, e '
                                   'o GH do segundo sprint triplicou em relação ao primeiro. No Brasil, o '
                                   'máximo diário em suplemento é 35 mg.',
                        'resumo': 'O ácido nicotínico, uma forma da vitamina B3, trava por algumas horas a '
                                  'liberação de gordura do tecido adiposo, e com menos gordura livre no '
                                  'sangue o GH sobe. O estudo citado nos vídeos existe: 7 homens, dois '
                                  'sprints de 30 segundos separados por 4 horas, 2 g de ácido nicotínico no '
                                  'total. Com ele, o pico de GH depois do segundo sprint foi de 23,3 contra '
                                  '7,7 µg/L no primeiro. Os "4,5 vezes" e "mais de 5 vezes" só aparecem '
                                  'comparando com o segundo sprint sem niacina. A dose do estudo é de '
                                  'remédio, não de vitamina. Nas formas de liberação lenta, metade dos '
                                  'pacientes de um ensaio teve lesão no fígado.',
                        'alerta': 'A dose usada no estudo, 2 g em 4 horas, é dose de remédio para colesterol '
                                  'e passa de 50 vezes o máximo de 35 mg por dia permitido em suplemento no '
                                  'Brasil; a autoridade europeia fixou em 10 mg por dia o limite seguro de '
                                  'ácido nicotínico. Nas formas de liberação lenta, 52% dos pacientes de um '
                                  'ensaio tiveram lesão no fígado. Em dois grandes ensaios, a niacina não '
                                  'reduziu infarto nem derrame e aumentou diabetes, infecções e '
                                  'sangramentos. Quem tem doença do fígado, diabetes ou usa estatina não '
                                  'deve tomar ácido nicotínico sem médico.'},
 'proprio_nofap_pornografia': {'nome': 'NoFap: abstinência de pornografia e masturbação ("jejum de '
                                       'dopamina")',
                               'categoria': 'primaria',
                               'aprovado': 'nao',
                               'tagline': 'Num ensaio de 7 dias sem pornografia, ninguém teve sintoma de '
                                          'abstinência; o estudo do "pico de testosterona no 7º dia" foi '
                                          'retratado em 2021.',
                               'resumo': 'A abstinência de pornografia e masturbação aparece em vídeos '
                                         'curtos como um "reinício" de 30 dias para o cérebro, a ereção e a '
                                         'testosterona. O estudo de 1986 sobre preferência por conteúdo mais '
                                         'incomum existe e diz o que se afirma, num desenho de laboratório '
                                         'da era do videocassete. O resto não se sustenta como foi dito: os '
                                         'receptores de dopamina D2 não estavam reduzidos em homens com uso '
                                         'compulsivo, num estudo de PET; 7 dias de abstinência, num ensaio '
                                         'randomizado, não deram sintoma de abstinência; o "sêmen reciclado '
                                         'que devolve nutrientes ao sangue" não tem base. Uso problemático '
                                         'de pornografia se associa a disfunção erétil em estudos '
                                         'transversais, mas o uso em si não, e não se demonstrou causa. O '
                                         'estudo chinês do pico de testosterona no 7º dia de abstinência foi '
                                         'retratado.',
                               'alerta': 'Esta página trata de comportamento, não de suplemento. Disfunção '
                                         'erétil em homem jovem tem causas médicas que precisam ser '
                                         'investigadas: doença cardiovascular, diabetes, remédios, '
                                         'depressão. Perder o controle sobre o uso de pornografia, com '
                                         'sofrimento e prejuízo por 6 meses ou mais, é um diagnóstico com '
                                         'tratamento (transtorno do comportamento sexual compulsivo, CID-11 '
                                         '6C72), e não se resolve com contagem de dias. Sofrimento que vem '
                                         'só de julgamento moral sobre o próprio desejo não é critério desse '
                                         'diagnóstico.'},
 'proprio_oleo_de_semente_de_abobora': {'nome': 'Óleo de semente de abóbora (Cucurbita pepo) e '
                                                'beta-sitosterol',
                                        'categoria': 'primaria',
                                        'aprovado': 'nao',
                                        'tagline': 'O "+40% de fios contra +10% no placebo" existe, num '
                                                   'único ensaio coreano de 76 homens pago pelo fornecedor '
                                                   'da cápsula; a DHT não foi medida e a extração não foi '
                                                   'descrita.',
                                        'resumo': 'O óleo de semente de abóbora é vendido contra a calvície '
                                                  'com base num ensaio de 2014 da Universidade Nacional de '
                                                  'Pusan: 76 homens com calvície de padrão masculino, 400 mg '
                                                  'por dia ou placebo por 24 semanas. A contagem de fios '
                                                  'subiu 40% contra 10%, como se diz; o avaliador cego '
                                                  'classificou 44,1% como melhores, contra 7,7% no placebo. '
                                                  'O estudo foi financiado pela empresa que forneceu as '
                                                  'cápsulas, não mediu DHT, não descreveu a extração e não '
                                                  'foi repetido em homens. O efeito sobre a enzima '
                                                  '5-alfa-redutase foi visto em rato e em célula, e num tipo '
                                                  'de abóbora estudado os fitosteróis do óleo são quase '
                                                  'todos de outro grupo, não o beta-sitosterol. No Brasil, o '
                                                  'óleo é fonte autorizada de lipídios em suplemento, sem '
                                                  'alegação para cabelo.',
                                        'alerta': 'O óleo é tomado por boca e, se age no folículo, chega lá '
                                                  'pelo sangue: a promessa de agir "sem entrar na '
                                                  'circulação" não se sustenta. Não há dado de segurança de '
                                                  'longo prazo nem de interação com finasterida ou '
                                                  'dutasterida. A calvície de padrão masculino tem '
                                                  'tratamentos aprovados com evidência muito maior; trocar '
                                                  'um deles por um único ensaio pequeno é uma escolha que '
                                                  'vale fazer com o dermatologista.'},
 'proprio_oximetolona_hemogenin': {'nome': 'Oximetolona (Hemogenin, Anadrol-50)',
                                   'categoria': 'primaria',
                                   'aprovado': 'nao',
                                   'tagline': 'O Hemogenin é um anabolizante oral feito para anemia, sem '
                                              'registro ativo na ANVISA desde 2020; nos estudos, até 43% dos '
                                              'pacientes tiveram enzimas do fígado acima de cinco vezes o '
                                              'basal.',
                                   'resumo': 'A oximetolona é um esteroide anabolizante oral, derivado da '
                                             'testosterona, aprovado nos Estados Unidos para anemias por '
                                             'falta de produção de glóbulos vermelhos. Os vídeos descrevem '
                                             '30 dias de força, pump, recordes e glóbulos vermelhos em duas '
                                             'semanas. Os estudos mostram outra coisa: a bula pede pelo '
                                             'menos 3 a 6 meses para avaliar a resposta na anemia; em '
                                             'idosos, 12 semanas deram cerca de 3 a 4 kg de massa magra, com '
                                             'queda do HDL e alta das enzimas do fígado; em pacientes com '
                                             'HIV, até 43% tiveram enzimas hepáticas acima de cinco vezes o '
                                             'basal. A bula avisa de peliose hepática e de tumores de '
                                             'fígado. No Brasil, o único registro, o do Hemogenin, está '
                                             'inativo.',
                                   'alerta': 'A oximetolona é anabolizante da lista C5 da Portaria 344/98. A '
                                             'bula americana traz advertência em destaque para peliose '
                                             'hepática, tumores de fígado, inclusive malignos fatais, e '
                                             'alteração de colesterol ligada a aterosclerose. Nos ensaios, a '
                                             'toxicidade no fígado foi o principal efeito adverso. Em '
                                             'mulheres, a virilização pode ser irreversível. Interage com '
                                             'anticoagulantes como a varfarina. No Brasil, não há registro '
                                             'ativo do medicamento no dado aberto da ANVISA, e é proibida '
                                             'pela WADA o tempo todo.'},
 'proprio_parabenos_cosmeticos': {'nome': 'Parabenos e ftalatos em shampoo e cosméticos',
                                  'categoria': 'primaria',
                                  'aprovado': 'nao',
                                  'tagline': 'O "99,1%" existe, mas é de urina de americanos de todas as '
                                             'idades, não de sangue de homens; o butilparabeno baixou '
                                             'testosterona em ratos, e em homens os estudos não concordam.',
                                  'resumo': 'Os parabenos são conservantes de cosméticos, remédios e '
                                            'alimentos, e aparecem na urina de quase todo mundo: '
                                            'metilparabeno em 99,1% de 2.548 americanos testados em '
                                            '2005–2006. Eles agem como estrogênio fraco, de 10 mil a 100 mil '
                                            'vezes menos potente que o estradiol nos testes de laboratório, '
                                            'e o corpo os quebra e elimina em horas, sem acúmulo. Em ratos, '
                                            'doses altas de butilparabeno baixaram testosterona e '
                                            'espermatozoides em alguns estudos e em outros não. Em homens, '
                                            'há estudos com associação e estudos sem. A regra não ficou '
                                            'parada: a Europa proibiu cinco parabenos em 2014, e o Brasil '
                                            'limita butil e propilparabeno a 0,14%. Trocar de produto baixou '
                                            'parabenos na urina em 3 dias.',
                                  'alerta': 'Esta página trata de exposição, não de suplemento. Trocar de '
                                            'shampoo não é tratamento de testosterona baixa, de '
                                            'infertilidade ou de queda de libido, e nenhum estudo mediu '
                                            'testosterona depois da troca. "Sem parabeno" não quer dizer sem '
                                            'conservante: o produto precisa de outro, que também pode causar '
                                            'alergia. Bebês são o grupo que a regra mais protege, com '
                                            'proibição de butil e propilparabeno em produto sem enxágue para '
                                            'a área da fralda.'},
 'proprio_peptistrong_peptideo_de_fava': {'nome': 'Hidrolisado de proteína de fava (PeptiStrong, NPN_1)',
                                          'categoria': 'primaria',
                                          'aprovado': 'nao',
                                          'tagline': 'Os três ensaios em humanos têm funcionários da '
                                                     'fabricante entre os autores; 47%, 136% e "4 vezes o '
                                                     'whey" não aparecem neles, e 24,5% e 21,6% não tiveram '
                                                     'significância.',
                                          'resumo': 'O ingrediente vendido como PeptiStrong é um hidrolisado '
                                                    'de proteína de fava (Vicia faba), código NPN_1, '
                                                    'desenvolvido por uma empresa irlandesa que diz tê-lo '
                                                    'achado com inteligência artificial. Há três ensaios em '
                                                    'humanos, com 30, 30 e 72 participantes, todos com '
                                                    'funcionários da empresa entre os autores. Com 2,4 g por '
                                                    'dia, um deles achou melhor recuperação de força em 72 '
                                                    'horas, outro mais força na perna aos 28 dias. Com 20 g '
                                                    'por dia, o ensaio de Maastricht não achou diferença da '
                                                    'proteína do leite no tamanho do músculo. Nenhum mediu '
                                                    'ganho de massa muscular com diferença do placebo, e a '
                                                    'miostatina não mudou em 8 semanas.',
                                          'alerta': 'Fava contém vicina e convicina, que causam hemólise em '
                                                    'quem tem deficiência de G6PD (favismo). Não achei dado '
                                                    'sobre a presença dessas substâncias no hidrolisado. '
                                                    'Quem tem deficiência de G6PD ou alergia a fava deve '
                                                    'conversar com um médico antes. No Brasil, a proteína de '
                                                    'fava é constituinte autorizado de suplemento, mas o '
                                                    'hidrolisado de fava não aparece pelo nome na lista.'},
 'proprio_peptopro': {'nome': 'Hidrolisado de caseína (PeptoPro)',
                      'categoria': 'primaria',
                      'aprovado': 'parcial',
                      'tagline': 'O estudo de Maastricht citado existe: o hidrolisado chegou ao sangue 27% '
                                 'mais rápido que a caseína inteira, mas a síntese muscular não diferiu, e '
                                 'em outro estudo do mesmo grupo o whey ganhou dos dois.',
                      'resumo': 'PeptoPro é a marca de um hidrolisado de caseína, a proteína do leite já '
                                'quebrada em pedaços pequenos. É comida pré-digerida, não um peptídeo com '
                                'ação hormonal. O estudo de 2009 do grupo de van Loon, citado nos vídeos, '
                                'mostrou absorção mais rápida que a da caseína inteira em 10 idosos, mas sem '
                                'diferença estatística na síntese muscular. Em 48 idosos, o whey estimulou '
                                'mais a síntese que a caseína e que o hidrolisado. A ressíntese de '
                                'glicogênio "sem carboidrato" não aparece em nenhum estudo: nos que existem, '
                                'a proteína veio sempre junto com carboidrato. Não localizei estudo que '
                                'medisse cortisol com hidrolisado de caseína.',
                      'alerta': 'É proteína do leite: quem tem alergia à proteína do leite não deve usar sem '
                                'orientação médica (inferência minha; não achei estudo de alergia com este '
                                'ingrediente). Um dos coautores dos estudos de 2009 aparece em outras '
                                'publicações como funcionário da empresa que vende o ingrediente. Absorção '
                                'mais rápida não significou mais músculo nos estudos que localizei.'},
 'proprio_pfaffia_paniculata': {'nome': 'Pfaffia paniculata ("ginseng brasileiro", Hebanthe eriantha)',
                                'categoria': 'primaria',
                                'aprovado': 'nao',
                                'tagline': 'Nenhum estudo em gente testou o "ginseng brasileiro" para '
                                           'músculo, libido ou diabetes; em camundongos, uma Pfaffia baixou '
                                           'a testosterona e piorou o sêmen.',
                                'resumo': 'Pfaffia paniculata é o nome antigo da planta brasileira hoje '
                                          'chamada Hebanthe eriantha, vendida como "ginseng brasileiro" '
                                          'junto com outra espécie, a Pfaffia glomerata. A evidência é rala: '
                                          'o PubMed tem 100 artigos e o ClinicalTrials.gov, zero registros; '
                                          'o único ensaio clínico é em anemia falciforme, com certeza muito '
                                          'baixa. O composto típico da P. paniculata é o ácido pfáffico, '
                                          'descrito por químicos japoneses em 1983; a ecdisterona é a marca '
                                          'da P. glomerata. Em ratos, a P. glomerata não teve efeito '
                                          'anabólico; em camundongos, baixou a testosterona e piorou o '
                                          'sêmen. Não há registro de uso por atletas soviéticos.',
                                'alerta': 'A Pfaffia não consta da lista de constituintes autorizados para '
                                          'suplemento alimentar no Brasil (IN 28/2018, consolidada até '
                                          'setembro de 2026), e o único fitoterápico de "ginseng brasileiro" '
                                          'que a ANVISA registrou está inativo desde 2012. Em camundongos, o '
                                          'extrato de P. glomerata reduziu a testosterona por morte de '
                                          'células de Leydig, diminuiu a produção de espermatozoides e '
                                          'aumentou a perda de embriões; a β-ecdisona pura foi genotóxica em '
                                          'roedores. O pó da raiz já causou asma ocupacional. Quem quer ter '
                                          'filhos ou está tentando engravidar a parceira tem motivo concreto '
                                          'para não usar sem médico.'},
 'proprio_pinheiro_maritimo': {'nome': 'Extrato de casca de pinheiro-marítimo (procianidinas)',
                               'categoria': 'primaria',
                               'aprovado': 'nao',
                               'tagline': 'O "+230% de óxido nítrico" não aparece em nenhum estudo que '
                                          'localizei, e o 92,5% vem de um estudo de 2003 sem grupo controle '
                                          'e com arginina junto.',
                               'resumo': 'O extrato padronizado da casca do pinheiro-marítimo francês é rico '
                                         'em procianidinas. Em laboratório e num ensaio com 16 homens, ele '
                                         'aumentou a dilatação dos vasos por um caminho que depende do óxido '
                                         'nítrico. Em disfunção erétil, quase todos os estudos usaram o '
                                         'extrato junto com arginina, e a revisão Cochrane de 2020 '
                                         'classifica a evidência como de certeza muito baixa. O 92,5% citado '
                                         'nos vídeos é de um estudo de 40 homens, sem controle, com arginina '
                                         'nos três meses. O "+230%" e a meta-análise com "cinco ensaios" não '
                                         'batem com as fontes. No Brasil, há dois fitoterápicos registrados, '
                                         'para varizes.',
                               'alerta': 'Os estudos de ereção testaram quase sempre o extrato junto com '
                                         'arginina; o efeito do extrato sozinho é incerto. Em laboratório, '
                                         'ele inibiu plaquetas e somou efeito à aspirina; que isso importe '
                                         'para quem usa anticoagulante ou antiagregante é inferência minha. '
                                         'No Brasil, procianidinas de pinho marítimo em suplemento têm '
                                         'máximo de 262,5 mg por dia, só para adultos, e o rótulo tem de '
                                         'dizer que gestantes, lactantes e crianças não devem consumir.'},
 'proprio_placebo_nocebo_reprogramacao_de_crenca': {'nome': 'Placebo, nocebo e a "reprogramação de crença"',
                                                    'categoria': 'primaria',
                                                    'aprovado': 'nao',
                                                    'tagline': 'Em 63 ensaios com 12.564 homens, o placebo '
                                                               'melhorou a ereção com efeito pequeno a '
                                                               'moderado, e o remédio com efeito grande. O '
                                                               'nocebo é real. O "protocolo de Harvard em 4 '
                                                               'etapas" é um roteiro publicado inteiro.',
                                                    'resumo': 'Os vídeos dizem que 35% dos doentes "se '
                                                              'curam" com pílula de açúcar, que a indústria '
                                                              'esconde isso e que um protocolo de Harvard de '
                                                              '"reprogramação de crença" teve etapas '
                                                              'apagadas. O 35% vem de um artigo de 1955, não '
                                                              'de 1961, e foi contestado por uma reanálise. '
                                                              'Revisões Cochrane acharam efeito pequeno do '
                                                              'placebo em sintomas relatados, como dor, e '
                                                              'nenhum efeito claro em desfechos objetivos. '
                                                              'Na disfunção erétil, o placebo melhorou a '
                                                              'ereção com efeito pequeno a moderado em 63 '
                                                              'ensaios; o remédio teve efeito grande. O '
                                                              'nocebo é bem medido: avisar sobre efeito '
                                                              'sexual subiu a queixa de 15,3% para 43,6%. O '
                                                              'roteiro de Harvard existe, tem quatro pontos '
                                                              'e está publicado inteiro.',
                                                    'alerta': 'Esta página trata de expectativa e '
                                                              'informação, não de suplemento. Placebo não '
                                                              'trata doença grave, e acreditar não substitui '
                                                              'remédio. Também não é verdade que todo efeito '
                                                              'colateral seja "da cabeça": os mesmos estudos '
                                                              'mostram efeitos reais dos remédios. Quem tem '
                                                              'disfunção erétil deve ser avaliado, porque '
                                                              'ela pode ser sinal de doença do coração, e '
                                                              'tratamento psicológico tem evidência própria. '
                                                              'Não pare remédio por causa de vídeo.'},
 'proprio_pre_treino_caseiro': {'nome': 'Pré-treino caseiro (guaraná, canela, gengibre e cafeína anidra)',
                                'categoria': 'primaria',
                                'aprovado': 'nao',
                                'tagline': 'Pela própria receita, uma medida de 10 g leva de 345 a 481 mg de '
                                           'cafeína, e o saco de 20 g de cafeína pura passa da faixa que a '
                                           'FDA considera potencialmente letal.',
                                'resumo': 'A receita mistura 700 g de guaraná em pó, 200 g de canela, 70 g '
                                          'de gengibre e 20 g de cafeína anidra. Pelas proporções dela e '
                                          'pelo teor de cafeína do guaraná medido no Brasil, uma medida de '
                                          '10 g leva de 345 a 481 mg de cafeína, conta minha; o vídeo diz '
                                          '350 mg. Isso é cerca de duas vezes a medida média de pré-treino '
                                          'comercial e passa dos 200 mg por dose que a ANVISA permite em '
                                          'suplemento. O efeito vem da cafeína. Gengibre e canela não '
                                          'aumentaram o gasto de energia em ensaios, e a enzima que o vídeo '
                                          'diz que eles "ligam" é a da inflamação, não a que dilata os '
                                          'vasos.',
                                'alerta': 'A receita manda comprar 20 g de cafeína anidra pura a granel. '
                                          'Segundo a FDA, uma colher de chá desse pó pode ter cerca de 3.200 '
                                          'mg, efeitos tóxicos aparecem perto de 1.200 mg e a dose que '
                                          'ameaça a vida fica entre 10 e 14 g. Misturar em casa não garante '
                                          'que cada medida tenha a mesma quantidade. Canela do tipo cássia '
                                          'pode ter muita cumarina, que é tóxica para o fígado. Não use com '
                                          'outra fonte de cafeína, perto da hora de dormir, nem se tiver '
                                          'doença cardíaca, gestação ou ansiedade sem falar com médico.'},
 'proprio_radiofrequencia_celular_notebook': {'nome': 'Celular no bolso e notebook no colo (radiofrequência '
                                                      'e calor)',
                                              'categoria': 'primaria',
                                              'aprovado': 'nao',
                                              'tagline': 'O "−21% de concentração" do estudo suíço não está '
                                                         'no artigo, e o celular no bolso não se associou a '
                                                         'sêmen pior; o que o notebook no colo '
                                                         'comprovadamente faz é esquentar o escroto.',
                                              'resumo': 'Celular e Wi-Fi emitem radiofrequência; notebook no '
                                                        'colo também esquenta. São duas exposições '
                                                        'diferentes. As revisões sistemáticas encomendadas '
                                                        'pela OMS em 2024 classificaram como muito incerta a '
                                                        'evidência de efeito da radiofrequência sobre o '
                                                        'esperma em homens; carregar o celular no bolso da '
                                                        'frente teve pouco ou nenhum efeito. O estudo suíço '
                                                        'de 2.886 jovens achou associação entre usar o '
                                                        'celular mais de 20 vezes por dia e contagem menor, '
                                                        'que diminuiu com os anos. O estudo do notebook com '
                                                        'Wi-Fi expôs o sêmen numa placa, não homens. Com o '
                                                        'notebook no colo, a temperatura do escroto subiu '
                                                        '2,6 a 2,8 °C em uma hora.',
                                              'alerta': 'Esta página trata de exposição, não de suplemento. '
                                                        'Afastar o celular do corpo não é tratamento de '
                                                        'testosterona baixa ou de infertilidade, e nenhum '
                                                        'estudo mediu se isso muda a testosterona. O efeito '
                                                        'mais bem medido do notebook no colo é o calor, e a '
                                                        'almofada embaixo dele não protegeu. Quem tenta '
                                                        'engravidar sem conseguir há um ano precisa de '
                                                        'avaliação médica do casal, não só de mudar o '
                                                        'celular de bolso.'},
 'proprio_red_spinach_nitrato': {'nome': 'Espinafre vermelho (red spinach, Amaranthus) e nitrato',
                                 'categoria': 'primaria',
                                 'aprovado': 'nao',
                                 'tagline': 'Na única meta-análise que separou as fontes, a beterraba '
                                            'melhorou o desempenho e o espinafre vermelho não; o extrato '
                                            'usado nos estudos tem cerca de 90 mg de nitrato por grama.',
                                 'resumo': 'O espinafre vermelho é um amaranto (Amaranthus dubius e espécies '
                                           'próximas) com folhas ricas em nitrato, o mesmo composto que faz '
                                           'o efeito da beterraba. O caminho do nitrato até o óxido nítrico '
                                           'é o mesmo para as duas: passa pelo sangue, pela saliva e pelas '
                                           'bactérias da boca, e o nitrito, passo seguinte, chega ao pico 2 '
                                           'a 3 horas depois. Os ensaios com extrato de espinafre vermelho '
                                           'são pequenos, com 10 a 16 pessoas, e usaram 90 a 400 mg de '
                                           'nitrato. Três não acharam ganho em repetições, força ou '
                                           'adaptação ao treino (um deles viu só a barra mais rápida), um '
                                           'achou limiar ventilatório maior sem mudar o tempo até a '
                                           'exaustão, e uma meta-análise de 2021 não achou efeito do '
                                           'espinafre vermelho em endurance. A faixa publicada para as '
                                           'folhas vai até cerca de 3,5 vezes a da beterraba, não 5 vezes.',
                                 'alerta': 'Nitrato baixa a pressão; quem usa remédio de pressão, nitrato de '
                                           'farmácia, tadalafila ou sildenafila pode somar efeitos, e isso é '
                                           'inferência minha, sem estudo de soma que eu tenha achado. Uma '
                                           'revisão de 2024 registra uma ingestão diária aceitável de '
                                           'nitrato de 3,7 mg por quilo de peso; alguns estudos com extrato '
                                           'deram 400 mg de nitrato de uma vez. No Brasil, nem o nitrato nem '
                                           'o amaranto constam da lista de constituintes autorizados em '
                                           'suplemento alimentar. Enxaguante bucal atrapalha a conversão do '
                                           'nitrato.'},
 'proprio_respiracao_diafragmatica': {'nome': 'Respiração lenta e diafragmática (hipocapnia, efeito Bohr e '
                                              'ereção)',
                                      'categoria': 'primaria',
                                      'aprovado': 'nao',
                                      'tagline': 'Respiração lenta reduz estresse e ansiedade em ensaios, '
                                                 'com efeito pequeno. O "40% a menos de oxigênio" é do fluxo '
                                                 'do cérebro em hiperventilação forte, não do pênis.',
                                      'resumo': 'Respirar rápido demais baixa o gás carbônico do sangue '
                                                '(hipocapnia), e isso faz a hemoglobina segurar mais o '
                                                'oxigênio e contrai os vasos do cérebro: é fisiologia real. '
                                                'A queda de 40% a 50% citada vale para o fluxo de sangue do '
                                                'cérebro com o CO2 entre 20 e 25 mmHg, não para o pênis. '
                                                'Hipocapnia persistente foi medida em pacientes com '
                                                'transtorno de pânico, não na população geral. Nenhum estudo '
                                                'localizado mediu o efeito da respiração sobre a ereção, o '
                                                'tamanho do pênis, o óxido nítrico pélvico ou a '
                                                'testosterona. O que a respiração lenta tem: uma '
                                                'meta-análise de 12 ensaios com 785 adultos achou menos '
                                                'estresse (efeito pequeno a médio), e um ensaio com 62 '
                                                'homens relatou ganho maior no tempo até a ejaculação quando '
                                                'ela foi somada a fisioterapia do assoalho pélvico, embora o '
                                                'resumo traga P = 0,12 para essa diferença.',
                                      'alerta': 'Esta página trata de hábito, não de suplemento. Respiração '
                                                'lenta é de baixo risco, mas não trata disfunção erétil, que '
                                                'depende de nervos e vasos saudáveis e merece investigação. '
                                                'Crises de falta de ar podem vir de ansiedade, mas o CO2 '
                                                'baixo também acompanha doenças do pulmão e do coração, e '
                                                'isso pede avaliação médica. Técnicas que mandam respirar '
                                                'muito rápido e fundo por minutos produzem a própria '
                                                'hipocapnia que o vídeo diz combater.'},
 'proprio_respiracao_nasal_sono': {'nome': 'Respiração nasal no sono (óxido nítrico, testosterona e fita na '
                                           'boca)',
                                   'categoria': 'primaria',
                                   'aprovado': 'nao',
                                   'tagline': 'O nariz entrega 4 a 6 vezes mais óxido nítrico que a boca, '
                                              'não 25, e a boca não chega a zero. Esse gás age no pulmão; '
                                              'nenhum estudo o liga à testosterona.',
                                   'resumo': 'O óxido nítrico do nariz vem sobretudo dos seios paranasais. '
                                             'Medido, o ar que sai pelo nariz tem cerca de 56 partes por '
                                             'bilhão, contra 14 pela boca: 4 vezes, não 25, e a boca não '
                                             'chega a zero. Inalado pelo nariz, esse gás melhora um pouco a '
                                             'oxigenação e baixa a resistência dos vasos do pulmão; mesmo em '
                                             'dose centenas de vezes maior, o óxido nítrico inalado não '
                                             'dilatou vasos fora do pulmão. A ereção depende do óxido '
                                             'nítrico feito nos nervos e vasos do próprio pênis. Respirar '
                                             'pela boca no sono, por outro lado, tem efeito medido: em 12 '
                                             'adultos saudáveis forçados a respirar pela boca, o índice de '
                                             'apneias foi de 1,5 para 43 por hora. Nenhum estudo localizado '
                                             'mediu testosterona conforme a via da respiração. A fita na '
                                             'boca tem 10 estudos com 213 pacientes, resultados mistos e '
                                             'risco descrito com nariz entupido.',
                                   'alerta': 'Esta página trata de hábito, não de suplemento. Quem dorme de '
                                             'boca aberta porque o nariz não passa ar precisa tratar o '
                                             'nariz, não fechar a boca: tapar a boca com nariz obstruído tem '
                                             'risco de sufocação descrito na literatura. Ronco alto, pausas '
                                             'na respiração e cansaço ao acordar podem ser apneia do sono, '
                                             'que pede exame. Fita na boca não substitui o tratamento da '
                                             'apneia.'},
 'proprio_retatrutida': {'nome': 'Retatrutida (LY3437943)',
                         'categoria': 'primaria',
                         'aprovado': 'nao',
                         'tagline': 'O primeiro artigo de fase 3 da retatrutida publica −25,0% de peso em 80 '
                                    'semanas, não 28%; ela não é aprovada em lugar nenhum e, no Brasil, a '
                                    'ANVISA proibiu e mandou apreender toda retatrutida à venda.',
                         'resumo': 'A retatrutida é uma molécula experimental da Eli Lilly que ativa ao '
                                   'mesmo tempo os receptores de GLP-1, GIP e glucagon, em injeção semanal. '
                                   'Os resultados de peso são grandes e reais: −24,2% em 48 semanas na fase '
                                   '2 e −25,0% em 80 semanas no primeiro artigo de fase 3, publicado em 29 '
                                   'de setembro de 2026. O "28%" dos vídeos vem de um comunicado da empresa, '
                                   'não de artigo revisado. Também houve menos dor no joelho, menos apneia e '
                                   'menos gordura no fígado. Os efeitos adversos mais comuns são '
                                   'gastrointestinais, e a disestesia, uma sensação anormal na pele, '
                                   'apareceu mais com a dose alta. Nenhum país aprovou. No Brasil, a ANVISA '
                                   'proibiu e mandou apreender toda retatrutida vendida.',
                         'alerta': 'A retatrutida não tem registro na ANVISA nem aprovação da FDA, e a '
                                   'empresa planeja pedir a aprovação americana em 2027. Em janeiro de 2026, '
                                   'a ANVISA proibiu a venda, a importação e o uso de retatrutida de todas '
                                   'as marcas e lotes, por serem produtos de origem desconhecida, sem '
                                   'garantia de conteúdo. Nos ensaios, o que se aplicou foi o produto do '
                                   'fabricante, com dose subida aos poucos e acompanhamento. Na fase 3, a '
                                   'dose alta teve mais náusea, diarreia, pressão baixa e disestesia, e mais '
                                   'abandono do tratamento por efeito adverso.'},
 'proprio_rhodiola_e_ginseng_siberiano': {'nome': 'Rhodiola e ginseng siberiano (Rhodiola rosea e '
                                                  'Eleutherococcus senticosus)',
                                          'categoria': 'primaria',
                                          'aprovado': 'nao',
                                          'tagline': 'O "+12% de VO2 máximo" do ginseng siberiano vem de 9 '
                                                     'homens em Taiwan, não de Moscou; os estudos mais '
                                                     'rigorosos com a planta não acharam ganho no exercício.',
                                          'resumo': 'Rhodiola e ginseng siberiano são duas plantas '
                                                    'diferentes que a medicina soviética estudou como '
                                                    '"adaptógenos". A rhodiola tem a base mais sólida: uma '
                                                    'meta-análise de 2025 com 26 ensaios achou efeito '
                                                    'pequeno no VO2 máximo (tamanho de efeito 0,32), com '
                                                    'heterogeneidade, e uma dose única reduziu um pouco a '
                                                    'percepção de esforço num estudo de 18 pessoas. O '
                                                    'ginseng siberiano tem um estudo de 9 homens com +12% no '
                                                    'VO2 pico e cinco estudos rigorosos sem efeito. Nenhum '
                                                    'estudo testou a combinação com ecdisterona, e o '
                                                    '"cortisol −21%" não aparece nos ensaios da revista '
                                                    'citada. Na Europa, as duas têm monografia de uso '
                                                    'tradicional para fadiga, com limite de tempo de uso.',
                                          'alerta': 'Rhodiola e ginseng siberiano não constam da lista de '
                                                    'constituintes autorizados para suplemento alimentar no '
                                                    'Brasil (IN 28/2018, consolidada até setembro de 2026). '
                                                    'A agência europeia recomenda a rhodiola só para adultos '
                                                    'e por no máximo duas semanas sem orientação médica, e o '
                                                    'ginseng siberiano por no máximo dois meses. O ginseng '
                                                    'siberiano já elevou o resultado do exame de digoxina '
                                                    'num paciente cardíaco. Num teste de DNA no Reino Unido, '
                                                    'metade dos produtos de rhodiola com DNA da planta não '
                                                    'era Rhodiola rosea.'},
 'proprio_sal_e_potassio_pre_treino': {'nome': 'Sal e potássio pré-treino (inclui sal rosa, sal integral e '
                                               'glicerol)',
                                       'categoria': 'primaria',
                                       'aprovado': 'nao',
                                       'tagline': 'Nenhum estudo mediu "pump" com sal antes do treino de '
                                                  'força; o sal rosa precisaria de mais de 30 g por dia para '
                                                  'dar potássio que conte, e a pressão sobe com sal em quem '
                                                  'treina também.',
                                       'resumo': 'Sódio e potássio são essenciais para a contração muscular, '
                                                 'mas isso não transforma 1 ou 2 g de sal antes do treino em '
                                                 'pré-treino. Não localizei nenhum estudo sobre sal e "pump" '
                                                 'no treino de força; num estudo com lutadores, sal antes do '
                                                 'exercício intenso não melhorou o desempenho. O que existe '
                                                 'é a hiper-hidratação antes de exercício longo no calor, '
                                                 'com muito líquido e sódio ou glicerol. A câimbra do '
                                                 'exercício parece depender mais de controle neuromuscular '
                                                 'do que de falta de sal. O sal rosa tem minerais em '
                                                 'quantidade irrisória. Mais de 70% dos adultos brasileiros '
                                                 'já passam do limite de sódio, e reduzir sal baixa a '
                                                 'pressão em quem tem ou não hipertensão.',
                                       'alerta': 'Quem tem pressão alta, doença renal, insuficiência '
                                                 'cardíaca ou usa remédio para pressão não deve somar sal ao '
                                                 'dia sem médico. Potássio em excesso é perigoso para quem '
                                                 'tem doença renal ou usa remédios que retêm potássio, como '
                                                 'alguns anti-hipertensivos e diuréticos. No Brasil, o sal '
                                                 'para consumo humano tem de ser iodado; sódio e potássio só '
                                                 'entram em suplemento na forma de bebida eletrolítica, com '
                                                 'limites por litro. O glicerol não é constituinte '
                                                 'autorizado de suplemento no Brasil.'},
 'proprio_schisandra': {'nome': 'Schisandra (Schisandra chinensis, wu wei zi)',
                        'categoria': 'primaria',
                        'aprovado': 'nao',
                        'tagline': 'A visão noturna e a fome suprimida dos caçadores são tradição; os dois '
                                   'ensaios com a fruta sozinha mediram força de perna em mulheres e idosos, '
                                   'e o maior risco documentado é interação com remédio.',
                        'resumo': 'A Schisandra chinensis é uma trepadeira do nordeste da Ásia cuja fruta '
                                  'seca é usada na medicina chinesa e foi estudada na União Soviética como '
                                  'adaptógeno. O PubMed tem 13 ensaios randomizados ou meta-análises com o '
                                  'nome da espécie, mas a maior parte testa fórmulas com várias plantas. Com '
                                  'a fruta sozinha, dois ensaios coreanos de 12 semanas, com 1 g por dia de '
                                  'extrato, acharam ganho de força no joelho: 10,2 Nm a mais que o placebo '
                                  'em idosos que caminhavam, e mais força com menos lactato em repouso em 45 '
                                  'mulheres. Nenhum estudo localizado testou visão noturna, frio, fome ou '
                                  '"oxigenação neural" em pessoas. Em voluntários, o extrato aumentou em 47% '
                                  'a exposição a um remédio que depende da glicoproteína P.',
                        'alerta': 'O extrato de Schisandra chinensis aumentou em 47% a área sob a curva de '
                                  'um betabloqueador em 12 voluntários, por inibir a glicoproteína P. Uma '
                                  'espécie aparentada, a Schisandra sphenanthera, mais que dobrou a '
                                  'exposição ao tacrolimo e ao midazolam, e na China é usada de propósito '
                                  'para economizar tacrolimo em transplantados. Quem usa imunossupressor, '
                                  'anticoagulante, antiarrítmico ou outro remédio de margem estreita não '
                                  'deve tomar a fruta sem falar com o médico. Ela não é constituinte '
                                  'autorizado de suplemento no Brasil.'},
 'proprio_shilajit': {'nome': 'Shilajit (mumijo, resina mineral)',
                      'categoria': 'primaria',
                      'aprovado': 'nao',
                      'tagline': 'O "+23,5%" não é do ensaio controlado que os vídeos descrevem: é de um '
                                 'estudo sem placebo com homens inférteis. E parte das amostras analisadas '
                                 'tinha chumbo, arsênio e mercúrio acima do limite.',
                      'resumo': 'Shilajit é uma resina mineral que escorre de rochas de montanha, usada no '
                                'Ayurveda. Para testosterona, há um ensaio controlado: em homens de 45 a 55 '
                                'anos, 250 mg duas vezes ao dia por 90 dias de um extrato purificado '
                                'elevaram a testosterona total e a livre contra placebo, sem mexer em LH e '
                                'FSH. O resumo não traz percentual nem número de participantes. O "+23,5%" '
                                'vem de outro estudo do mesmo grupo, de 2010, sem placebo, com 28 homens com '
                                'poucos espermatozoides, e é de testosterona total. O PubMed tem 7 artigos '
                                'de shilajit marcados como ensaio ou meta-análise; o ClinicalTrials.gov, '
                                'nenhum de fase 3. A literatura de contaminação mostra variação grande: '
                                'estudos acharam chumbo, arsênio e mercúrio acima do permitido em amostras '
                                'da Índia e do Paquistão, e tálio em suplementos.',
                      'alerta': 'O shilajit é um material de rocha, e sua composição muda com a origem: '
                                'análises acharam chumbo, arsênio, mercúrio e tálio, em alguns casos acima '
                                'dos limites permitidos. Há relato de hipertensão com potássio baixo numa '
                                'grávida que tomava mumijo por 6 meses e de anafilaxia em que o shilajit foi '
                                'apontado como cofator. No Brasil, o shilajit não consta da lista de '
                                'constituintes de suplemento alimentar.'},
 'proprio_solidao_isolamento_social': {'nome': 'Solidão e isolamento social (cortisol, testosterona, músculo '
                                               'e mortalidade)',
                                       'categoria': 'primaria',
                                       'aprovado': 'nao',
                                       'tagline': 'Isolamento social anda junto com 32% mais mortalidade em '
                                                  '90 coortes. Sobre testosterona, o dado humano é escasso, '
                                                  'e homens com parceira fixa têm testosterona mais baixa, '
                                                  'não mais alta.',
                                       'resumo': 'Solidão e isolamento social são fatores de risco de morte '
                                                 'com tamanho parecido ao de fatores clássicos: em 90 '
                                                 'coortes com 2,2 milhões de pessoas, o isolamento se '
                                                 'associou a 32% mais mortalidade e a solidão, a 14% mais. A '
                                                 'Organização Mundial da Saúde estima que 1 em cada 6 '
                                                 'pessoas no mundo se sente sozinha. O que os vídeos '
                                                 'acrescentam tem pouca base: a solidão se associa a uma '
                                                 'resposta de cortisol maior ao acordar no dia seguinte, mas '
                                                 'não a um cortisol que "inunda" o sangue; o isolamento se '
                                                 'associa a sarcopenia em idosos, mas viver sozinho não teve '
                                                 'associação significativa em homens. Sobre testosterona, há '
                                                 'um estudo de 1983 com 60 idosos em que um programa de '
                                                 'convivência a subiu, e uma meta-análise em que homens com '
                                                 'parceira fixa e pais têm testosterona mais baixa que os '
                                                 'solteiros.',
                                       'alerta': 'Esta página trata de condição social, não de suplemento. '
                                                 'Solidão persistente se associa a depressão, e pensamento '
                                                 'de morte é emergência: no Brasil, o CVV atende pelo '
                                                 'telefone 188, 24 horas por dia, sem custo. Perda de massa '
                                                 'muscular, cansaço e queda de libido têm muitas causas e '
                                                 'pedem avaliação médica. Nenhum suplemento trata solidão.'},
 'proprio_sono_higiene_e_gh': {'nome': 'Sono: temperatura do quarto, horário e telas (GH e testosterona)',
                               'categoria': 'primaria',
                               'aprovado': 'nao',
                               'tagline': 'Uma semana dormindo 5 horas baixou a testosterona diurna de 10 '
                                          'jovens em 10% a 15%; o "60% da recuperação hormonal" e a "janela '
                                          'de 40 minutos" não aparecem em estudo.',
                               'resumo': 'Em homens, cerca de 70% do GH do dia sai num grande pulso logo '
                                         'depois que se adormece, ligado ao primeiro sono profundo, e a '
                                         'testosterona sobe durante a noite. Isso é fisiologia documentada '
                                         'desde 1968. O que os vídeos acrescentam não está nos estudos: o '
                                         'pulso de GH não se perde quando se demora a dormir, ele se desloca '
                                         'junto com o início do sono. Dormir pouco tem efeito medido: 1 '
                                         'semana com 5 horas por noite baixou a testosterona diurna de 10 '
                                         'jovens em 10% a 15%, e a privação total de 24 horas ou mais baixa '
                                         'a testosterona numa meta-análise, mas a restrição parcial de curto '
                                         'prazo, não. Quarto quente tira sono profundo; tela antes de deitar '
                                         'atrasa o sono e corta a melatonina. Nenhum estudo mediu GH ou '
                                         'testosterona depois de mudar a temperatura do quarto, o colchão ou '
                                         'a tela.',
                               'alerta': 'Esta página trata de hábito, não de suplemento. Ajustar quarto, '
                                         'horário e tela não trata testosterona baixa, disfunção erétil, '
                                         'insônia nem apneia. Ronco alto, pausas na respiração durante o '
                                         'sono, sonolência forte de dia ou insônia que dura meses pedem '
                                         'avaliação médica, não só um quarto mais fresco. Um dos estudos '
                                         'citados aqui usou um fármaco (gama-hidroxibutirato) para '
                                         'aprofundar o sono; ele aparece como prova de mecanismo, não como '
                                         'sugestão.'},
 'proprio_tadalafila_diaria': {'nome': 'Tadalafila de uso diário (5 mg)',
                               'categoria': 'primaria',
                               'aprovado': 'sim',
                               'tagline': 'A tadalafila diária é remédio aprovado e funciona, mas não "limpa '
                                          'artéria", não supera com folga o uso sob demanda e não previne '
                                          'encolhimento fora da cirurgia de próstata.',
                               'resumo': 'A tadalafila é um inibidor da fosfodiesterase tipo 5, aprovado '
                                         'para disfunção erétil e para sintomas de aumento benigno da '
                                         'próstata. Em uso diário, a bula americana registra melhora da '
                                         'ereção em ensaios de 12 e 24 semanas e menos dor de cabeça que a '
                                         'dose alta sob demanda. A meta-análise que comparou os dois '
                                         'esquemas achou 1,82 ponto a mais no escore de ereção com o diário, '
                                         'diferença que os autores dizem talvez não ser clinicamente '
                                         'relevante. O efeito contra encolhimento do pênis foi medido só '
                                         'depois de cirurgia de próstata. É remédio de receita e é proibido '
                                         'junto com nitratos.',
                               'alerta': 'A tadalafila é proibida para quem usa nitrato em qualquer forma e '
                                         'para quem usa riociguate, e pede cuidado com bloqueadores alfa, '
                                         'remédios de pressão e álcool em quantidade, pelo risco de queda de '
                                         'pressão. A bula americana manda procurar socorro em ereção que '
                                         'dure mais de 4 horas, perda súbita de visão ou de audição. Nos '
                                         'Estados Unidos, é de venda sob prescrição. Nenhum dos vídeos '
                                         'analisados menciona receita, contraindicação ou avaliação '
                                         'cardiovascular.'},
 'proprio_tirzepatida_mounjaro': {'nome': 'Tirzepatida (Mounjaro) semana a semana',
                                  'categoria': 'primaria',
                                  'aprovado': 'sim',
                                  'tagline': 'No estudo citado nos vídeos, quem trocou a tirzepatida por '
                                             'placebo voltou a ganhar peso mesmo recebendo orientação de '
                                             'dieta e exercício; o "14%" é do peso corporal, não do peso '
                                             'perdido.',
                                  'resumo': 'A tirzepatida é um remédio injetável semanal que age em dois '
                                            'receptores, o de GIP e o de GLP-1, registrado no Brasil como '
                                            'MOUNJARO e vendido só com retenção da receita. Os grandes '
                                            'números que circulam vêm de ensaios reais e grandes: no '
                                            'SURMOUNT-1, com 2.539 adultos, a dose de 15 mg tirou 20,9% do '
                                            'peso em 72 semanas, ou 22,5% contando só quem seguiu tomando. O '
                                            'que os vídeos erram é o resto: a perda de "até 5%" no primeiro '
                                            'mês não é regra, a náusea não some "em 48 horas" e o reganho do '
                                            'SURMOUNT-4 aconteceu em quem parou o remédio mesmo seguindo '
                                            'dieta e atividade orientadas.',
                                  'alerta': 'Tirzepatida é medicamento de prescrição. No Brasil, a farmácia '
                                            'só vende com retenção da receita desde abril de 2025. A bula '
                                            'americana traz tarja preta por tumor de tireoide em ratos e '
                                            'contraindica o uso por quem tem história pessoal ou familiar de '
                                            'carcinoma medular de tireoide ou NEM 2. Pancreatite, doença da '
                                            'vesícula e desidratação com lesão renal estão entre os riscos '
                                            'descritos. Em mulheres, o anticoncepcional oral pode falhar nas '
                                            'semanas de início e de aumento de dose.'},
 'proprio_tongkat_ali_long_jack': {'nome': 'Tongkat ali (Long Jack, Eurycoma longifolia)',
                                   'categoria': 'primaria',
                                   'aprovado': 'nao',
                                   'tagline': 'O "+581% de testosterona livre" não aparece em nenhum estudo '
                                              'que localizei; no ensaio com 600 mg, a SHBG e o LH não '
                                              'mudaram e o estradiol subiu.',
                                   'resumo': 'Tongkat ali é a raiz da Eurycoma longifolia, planta do Sudeste '
                                             'Asiático. Há 8 artigos no PubMed marcados como ensaio '
                                             'randomizado ou meta-análise e 5 estudos registrados no '
                                             'ClinicalTrials.gov, nenhum de fase 3. Uma meta-análise de 2022 '
                                             'achou aumento da testosterona total, com 5 ensaios pequenos; '
                                             'boa parte dos estudos usa o extrato de um mesmo fabricante, '
                                             'que financiou pelo menos dois deles. O ensaio duplo-cego com '
                                             '600 mg por dia em jovens viu a testosterona subir sem mudança '
                                             'de SHBG e de LH, o contrário do mecanismo que se promete, e o '
                                             'estradiol subiu junto. Em 2021, a autoridade europeia concluiu '
                                             'que a segurança do extrato não está estabelecida, por sinal de '
                                             'dano ao DNA. No Brasil, a planta não consta da lista de '
                                             'constituintes permitidos em suplemento.',
                                   'alerta': 'A autoridade europeia de segurança alimentar (EFSA) concluiu '
                                             'em 2021 que a segurança de um extrato padronizado de tongkat '
                                             'ali não foi estabelecida em nenhuma condição de uso, porque '
                                             'ele causou dano ao DNA em teste de laboratório e em animal. Há '
                                             'relato de lesão no fígado e de arritmia associados ao uso, e o '
                                             'extrato reduziu a absorção do propranolol. Levantamentos na '
                                             'Malásia acharam mercúrio e chumbo acima do limite local em '
                                             'parte dos produtos vendidos com a raiz.'},
 'proprio_tracao_peniana_e_vacuo': {'nome': 'Tração peniana e aparelho de vácuo (e "soltar o ligamento '
                                            'suspensor")',
                                    'categoria': 'primaria',
                                    'aprovado': 'nao',
                                    'tagline': 'Tração diária ganhou em média 1,3 a 2,3 cm em estudos com '
                                               'Peyronie, pós-prostatectomia e queixa de pênis curto; o '
                                               'vácuo não aumentou o tamanho. Os "2 a 5 cm" e o "37%" não '
                                               'estão em estudo.',
                                    'resumo': 'A tração peniana tem estudos de verdade, mas quase todos em '
                                              'homens com doença de Peyronie ou depois de retirar a '
                                              'próstata, e com uso diário longo. Em homens com queixa de '
                                              'pênis curto, o ganho médio de comprimento esticado foi de 1,7 '
                                              'cm em 6 meses com 4 horas ou mais por dia, num estudo de '
                                              'Turim, e uma revisão sistemática resume os aparelhos de '
                                              'tração como ganho de menos de 2 cm no pênis flácido. O '
                                              'aparelho de vácuo, usado 20 minutos 3 vezes por semana por 6 '
                                              'meses, não mudou o comprimento. Cortar o ligamento suspensor '
                                              'deu, em média, 1,3 cm, com 35% de satisfação e casos de '
                                              'perda. A maioria dos homens que buscam aumento tem pênis de '
                                              'tamanho normal.',
                                    'alerta': 'Tração e vácuo causaram desconforto, dormência da glande e '
                                              'hematoma em parte dos usuários dos estudos. Os ganhos '
                                              'dependem de horas de uso por dia durante meses e foram '
                                              'medidos sobretudo em doença de Peyronie e depois da retirada '
                                              'da próstata, não em homens saudáveis. Cortar o ligamento '
                                              'suspensor é cirurgia, com satisfação baixa e risco de perder '
                                              'comprimento; revisões chamam de antiético fazer cirurgia e '
                                              'injeção de aumento fora de pesquisa. Quem acha o pênis '
                                              'pequeno deve começar pela medida feita por profissional e por '
                                              'aconselhamento.'},
 'proprio_treino_limiar_de_lactato_gh': {'nome': 'Treino acima do limiar de lactato ("finisher") e GH',
                                         'categoria': 'primaria',
                                         'aprovado': 'nao',
                                         'tagline': 'Os 10 minutos acima do limiar de lactato subiram o GH '
                                                    'de 10 homens em 1992; o estudo de 1999 citado nos '
                                                    'vídeos achou subida em linha reta com a intensidade, '
                                                    'sem limiar.',
                                         'resumo': 'Exercício intenso aumenta o GH: está medido desde os '
                                                   'anos 1990. O estudo de 1992 citado nos vídeos existe e '
                                                   'bate nos números: 10 minutos acima do limiar de lactato '
                                                   'subiram o GH em 7,7 µg/L; abaixo, 1,5, sem '
                                                   'significância. Mas o estudo de 1999, também citado, '
                                                   'mostra o contrário da ideia de "linha": o GH subiu em '
                                                   'linha reta com a intensidade, já abaixo do limiar, e os '
                                                   'próprios autores escreveram que a ideia de um limiar '
                                                   'estava errada. A subida é passageira e não aumenta o GH '
                                                   'do dia inteiro depois de uma sessão. E dois ensaios '
                                                   'mostraram que o pico de hormônio do treino não aumenta a '
                                                   'hipertrofia nem a força. O "4 vezes mais GH" e os '
                                                   'números "por pulso" do estudo de 1997 não estão nos '
                                                   'resumos.',
                                         'alerta': 'Esta página trata de treino, não de suplemento. Esforço '
                                                   'máximo repetido aumenta, de forma passageira, o risco de '
                                                   'evento cardíaco em quem tem doença do coração, ainda que '
                                                   'o risco absoluto seja baixo em reabilitação '
                                                   'supervisionada. Quem é sedentário, tem doença '
                                                   'cardiovascular, metabólica ou renal, ou sente dor no '
                                                   'peito, falta de ar ou tontura no esforço deve passar por '
                                                   'avaliação antes de treino intenso. Subir o GH no treino '
                                                   'não é objetivo de saúde em si.'},
 'proprio_ultraprocessados_acucar_alcool': {'nome': 'Ultraprocessados, açúcar e álcool (dieta e '
                                                    'testosterona)',
                                            'categoria': 'primaria',
                                            'aprovado': 'nao',
                                            'tagline': 'O álcool frequente baixa a testosterona em '
                                                       'meta-análise; o "40% de queda" da toxina intestinal '
                                                       'é de outro estudo; e não há ensaio que teste "zerar" '
                                                       'açúcar para subir hormônio.',
                                            'resumo': 'Os vídeos juntam açúcar, ultraprocessados e álcool '
                                                      'numa só causa de "estrogênio bloqueando a '
                                                      'testosterona". Separados, os dados são outros. O '
                                                      'álcool consumido com frequência baixou a testosterona '
                                                      'total e subiu o estradiol numa meta-análise de 21 '
                                                      'estudos. Uma dose de 75 g de glicose baixou a '
                                                      'testosterona em 25%, e ela seguia baixa duas horas '
                                                      'depois. Num ensaio cruzado com 43 jovens, a dieta de '
                                                      'ultraprocessados aumentou o peso e baixou o FSH. A '
                                                      '"toxina que vaza do intestino" baixou a testosterona '
                                                      'por horas num experimento, e o número de 40% vem de '
                                                      'outro estudo. Perder peso subiu a testosterona em '
                                                      'meta-análise; "zerar" nunca foi testado.',
                                            'alerta': 'Esta página trata de alimentação e bebida, não de '
                                                      'suplemento. Cortar álcool e ultraprocessados não é '
                                                      'tratamento de hipogonadismo, e "dominância '
                                                      'estrogênica" não é diagnóstico que um exame de rotina '
                                                      'dê em homem. Quem bebe muito e para de repente pode '
                                                      'ter abstinência grave e precisa de acompanhamento. '
                                                      'Queixa de libido, ereção ou testosterona baixa pede '
                                                      'avaliação médica.'},
 'proprio_vinagre_de_maca': {'nome': 'Vinagre de maçã em jejum',
                             'categoria': 'primaria',
                             'aprovado': 'nao',
                             'tagline': 'O vinagre baixa um pouco o pico de glicose depois de uma refeição; '
                                        'o ensaio que prometia grande perda de peso foi retratado em 2025, e '
                                        'parte da saciedade vem de náusea.',
                             'resumo': 'O vinagre de maçã é ácido acético diluído. Tomado junto com uma '
                                       'refeição de carboidrato, ele reduz o pico de glicose e de insulina, '
                                       'segundo uma meta-análise de ensaios; em diabéticos tipo 2, várias '
                                       'meta-análises acham glicemia de jejum menor. Em peso, o efeito é '
                                       'pequeno: uma meta-análise de 2021 não achou mudança no IMC, e a de '
                                       '2025, que achou queda, incluiu um ensaio libanês retratado em 2025. '
                                       'A sensação de fome menor foi atribuída, num estudo, sobretudo à '
                                       'náusea. Nenhum estudo humano mediu "insulina ultrassensível" que '
                                       'mande nutrientes para o músculo, nem ganho de músculo. O vinagre '
                                       'também atrasa o esvaziamento do estômago, o que pode atrapalhar quem '
                                       'tem gastroparesia diabética.',
                             'alerta': 'Vinagre é ácido. Há relato de erosão do esmalte dos dentes com um '
                                       'copo de vinagre de maçã por dia, de lesão no esôfago com comprimido '
                                       'de vinagre de maçã, de potássio baixo com uso de grandes quantidades '
                                       'por anos e um relato de dano ao fígado. Em pessoas com diabetes tipo '
                                       '1 e gastroparesia, 30 mL por dia deixaram o esvaziamento do estômago '
                                       'ainda mais lento. Quem usa insulina ou remédio para diabetes pode '
                                       'ter a glicose alterada; isso é inferência minha, e não achei estudo '
                                       'que tenha medido a combinação.'},
 'proprio_vitamina_b6_com_mucuna': {'nome': 'Vitamina B6 (piridoxina), adjuvante da mucuna',
                                    'categoria': 'primaria',
                                    'aprovado': 'nao',
                                    'tagline': 'A B6 não protege a L-dopa da mucuna: acelera a perda dela. E '
                                               'o máximo diário em suplemento no Brasil, 98,60 mg, é mais de '
                                               'oito vezes o limite seguro fixado na Europa em 2023.',
                                    'resumo': 'A vitamina B6 aparece num vídeo como adjuvante da mucuna, '
                                              'para "proteger os receptores cerebrais". A literatura diz o '
                                              'contrário: sem carbidopa, a B6 acelera a destruição da L-dopa '
                                              'fora do cérebro e, num estudo de 1975, inibiu a subida do '
                                              'hormônio do crescimento. A B6 em excesso causa neuropatia '
                                              'sensitiva: a autoridade europeia baixou em 2023 o limite '
                                              'seguro para 12 mg por dia, enquanto o suplemento brasileiro '
                                              'pode recomendar até 98,60 mg. As promessas comuns de que a B6 '
                                              'baixa a prolactina e sobe a testosterona não se confirmaram '
                                              'em pessoas.',
                                    'alerta': 'Em quem toma mucuna ou levodopa sem carbidopa, a vitamina B6 '
                                              'reduz o efeito da L-dopa. Em excesso, a B6 lesa os nervos '
                                              'sensitivos, com formigamento e dormência nas mãos e nos pés; '
                                              'a autoridade europeia fixou o limite seguro em 12 mg por dia '
                                              'para adultos, e há séries de casos com média de 117 mg por '
                                              'dia, tomados por anos. O máximo permitido em suplemento no '
                                              'Brasil é 98,60 mg por dia. Somar vários produtos com B6 é o '
                                              'caminho mais fácil para passar do limite.'},
 'proprio_vitamina_d_e_sol': {'nome': 'Vitamina D e exposição ao sol (testosterona)',
                              'categoria': 'primaria',
                              'aprovado': 'nao',
                              'tagline': 'O "+25,2% de testosterona" vem de 54 homens analisados em 2011; o '
                                         'mesmo grupo de Graz testou de novo, com placebo, e não achou '
                                         'efeito.',
                              'resumo': 'A vitamina D é necessária ao osso e o testículo tem receptor para '
                                        'ela. Homens com vitamina D baixa costumam ter testosterona um pouco '
                                        'mais baixa, mas os dois andam juntos como marcadores de saúde ruim. '
                                        'O estudo de Graz de 2011 citado nos vídeos existe: 54 homens em '
                                        'dieta para emagrecer, 3.332 UI por dia por um ano, testosterona de '
                                        '10,7 para 13,4 nmol/L no grupo tratado. Depois, o mesmo grupo fez '
                                        'dois ensaios com placebo e espectrometria de massa, em homens com '
                                        'testosterona normal e baixa, e não achou efeito. Duas meta-análises '
                                        'de ensaios randomizados, de 2019 e 2026, também não acharam. No '
                                        'Brasil, suplemento pode ter no máximo 2.000 UI por dia para '
                                        'adultos.',
                              'alerta': 'Os 5.000 UI por dia que circulam passam do máximo permitido em '
                                        'suplemento no Brasil para adultos (50 µg, ou 2.000 UI) e do limite '
                                        'superior de ingestão do Institute of Medicine (4.000 UI). Excesso '
                                        'de vitamina D causa cálcio alto no sangue, com vômito, desidratação '
                                        'e confusão; quem tem doença granulomatosa ou certos linfomas pode '
                                        'ter cálcio alto mesmo com dose comum. O sol "sem protetor entre 10h '
                                        'e 15h" contraria a orientação do INCA, que manda evitar exposição '
                                        'prolongada entre 10h e 16h.'},
 'proprio_whey_caseiro_de_soja': {'nome': '"Whey caseiro" de proteína isolada de soja',
                                  'categoria': 'primaria',
                                  'aprovado': 'parcial',
                                  'tagline': 'A receita entrega mesmo cerca de 25 g de proteína por dose, '
                                             'mas não é whey: é soja. Para músculo, a diferença é pequena '
                                             'quando a proteína total do dia é suficiente, e a soja não '
                                             'baixou a testosterona nas meta-análises.',
                                  'resumo': 'A receita que circula mistura proteína isolada de soja com um '
                                            'pouco de leite em pó, aveia e suco em pó. Pela tabela americana '
                                            'de composição, 30 g dão cerca de 24,6 g de proteína, perto dos '
                                            '25 g prometidos, e o perfil de aminoácidos do isolado de soja '
                                            'atende à proteína de referência da norma brasileira. Não é '
                                            'whey, e não é verdade que a única diferença seja o marketing: a '
                                            'soja estimula menos a síntese de músculo logo após o treino. '
                                            'Mas em semanas de treino, a maior parte das meta-análises não '
                                            'acha diferença de ganho entre soja e whey, e duas meta-análises '
                                            'com 41 estudos não acharam efeito da soja na testosterona de '
                                            'homens.',
                                  'alerta': 'A receita tem soja e leite: quem tem alergia a um dos dois não '
                                            'pode usá-la. Os casos publicados de mama aumentada e '
                                            'testosterona baixa por soja envolveram litros de leite de soja '
                                            'por dia, muito acima de uma dose de proteína. Uma mistura '
                                            'caseira não passa por nenhum controle de composição; o teor de '
                                            'proteína depende do rótulo do isolado comprado.'},
 'proprio_zerar_acucar_30_dias': {'nome': 'Zerar o açúcar por 30 dias (a cronologia dos vídeos)',
                                  'categoria': 'primaria',
                                  'aprovado': 'nao',
                                  'tagline': 'Três dias sem refrigerante deram fissura e dor de cabeça em 25 '
                                             'adolescentes; mas o paladar só mudou no 2º e 3º mês num '
                                             'ensaio, e em outro, de 6 meses, não mudou.',
                                  'resumo': 'A cronologia de 30 dias sem açúcar que circula em vídeos '
                                            'mistura coisas medidas com coisas inventadas. Cortar bebida '
                                            'açucarada por 3 dias aumentou a fissura e baixou o bem-estar de '
                                            '25 adolescentes. O glicogênio guarda 3 a 4 partes de água, mas '
                                            'cortar só o açúcar não esvazia o glicogênio, e o pâncreas não '
                                            '"desliga". Reduzir açúcar baixou o peso em 0,80 kg em '
                                            'meta-análise, pela queda de calorias. O paladar passou a sentir '
                                            'mais o doce no 2º e 3º mês num ensaio, sem gostar menos; outro, '
                                            'de 6 meses, não achou mudança. Nenhum estudo testou "zerar" '
                                            'açúcar e medir testosterona.',
                                  'alerta': 'Esta página trata de alimentação, não de suplemento. Reduzir '
                                            'açúcar adicionado é recomendação da OMS e das diretrizes '
                                            'alimentares, mas a cronologia de 30 dias dos vídeos não foi '
                                            'testada. Quem usa insulina ou remédio que baixa a glicose deve '
                                            'combinar com o médico qualquer mudança grande na dieta. '
                                            'Fissura, dor de cabeça e cansaço que não passam em poucos dias '
                                            'pedem avaliação, não insistência.'},
 'proprio_zinco': {'nome': 'Zinco (inclui ostra e alimentos ricos em zinco)',
                   'categoria': 'primaria',
                   'aprovado': 'nao',
                   'tagline': 'O estudo de 1996 existe, mas a testosterona subiu em 9 idosos com falta de '
                              'zinco e sem grupo placebo; em homens sem deficiência, os ensaios não acham '
                              'efeito.',
                   'resumo': 'O zinco é essencial e a falta grave dele baixa a testosterona: em 4 jovens com '
                             'dieta restrita por 20 semanas, ela caiu de 39,9 para 10,6 nmol/L. O mesmo '
                             'artigo de 1996 viu a testosterona subir de 8,3 para 16 nmol/L em 9 idosos com '
                             'deficiência marginal, sem grupo placebo. Em homens que já comem zinco '
                             'suficiente, um suplemento de zinco com magnésio não mudou a testosterona, e o '
                             'maior ensaio de zinco em homens que localizei, com 2.370 participantes, não '
                             'melhorou sêmen nem nascimentos. A perda por ejaculação medida em estudo é de '
                             'cerca de 0,4 mg, não 1,4 mg. No Brasil, o máximo em suplemento é 29,59 mg por '
                             'dia para adultos.',
                   'alerta': 'Zinco em excesso por tempo prolongado derruba o cobre do corpo e pode causar '
                             'anemia, queda de glóbulos brancos e dano neurológico. O limite superior '
                             'americano é de 40 mg por dia somando comida e suplemento; o europeu, de 25 mg. '
                             'No Brasil, o máximo em suplemento é 29,59 mg por dia para adultos. O zinco '
                             'reduz a absorção da tetraciclina, e suplemento de ferro reduz a do zinco. '
                             'Náusea e dor de estômago são os efeitos mais comuns.'}})
