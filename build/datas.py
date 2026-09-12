# -*- coding: utf-8 -*-
"""As datas do site, num lugar so.

Existe porque os modulos de conteudo (proprios*.py, compostos*.py) nao podem
importar de gerar.py: gerar.py ja importa eles, e daria import circular.

As duas sao FATOS HISTORICOS, nao a data de hoje.

NUNCA derivar nenhuma delas do relogio (datetime.now, date.today e afins).
O gerador roda de novo a cada edicao de texto; se a data vier do relogio, o
site passa a afirmar, a cada rebuild, que foi conferido hoje -- sem que
ninguem tenha conferido nada. Data velha e correta e melhor que data fresca
e falsa.

Trocar DATA_FONTE so ao raspar a fonte secundaria de novo.
Trocar DATA_APURACAO so ao refazer a apuracao em fonte primaria. E ao trocar,
trocar de verdade: refazer as consultas, nao so editar a string.

Por que existe uma terceira data: DATA_APURACAO cobre as paginas apuradas na
varredura de 4 de setembro. A pagina da mazdutida foi levantada depois, num
outro dia, e carimba-la com 4 de setembro seria afirmar uma conferencia que
naquele dia nao aconteceu -- o mesmo erro que a trava de datas existe para
impedir. Pagina apurada em outro dia ganha a sua propria data. Se uma varredura
futura refizer TUDO no mesmo dia, estas constantes voltam a ser uma so.
"""

DATA_FONTE = "3 de setembro de 2026"      # acesso a peptidedosingprotocols.com
DATA_APURACAO = "4 de setembro de 2026"   # PubMed, ClinicalTrials.gov, ANVISA, WADA
DATA_MAZDUTIDA = "5 de setembro de 2026"  # PubMed, ClinicalTrials.gov, openFDA, ANVISA
DATA_MABS = "12 de setembro de 2026"      # PubMed, ClinicalTrials.gov, openFDA, INN/OMS
DATA_EXOSSOMOS = "12 de setembro de 2026"  # PubMed, ClinicalTrials.gov, openFDA, ANVISA, FDA, SBD
DATA_NOVAS_CLASSES = "12 de setembro de 2026"  # PubMed, ClinicalTrials.gov, dado aberto da ANVISA
